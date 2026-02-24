# External Integrations

**Analysis Date:** 2026-02-24

## APIs & External Services

**AI/LLM:**

- OpenRouter - LLM gateway for CrewAI code review
  - SDK/Client: litellm >=1.0.0 (via `crewai` framework)
  - Auth: `OPENROUTER_API_KEY` env var (GitHub Secret in CI, `.env` locally)
  - Base URL: `https://openrouter.ai/api/v1`
  - Default model: `openrouter/xiaomi/mimo-v2-flash` (128k context, free)
  - Fallback model: `openrouter/xiaomi/mimo-v2` (1M context, free)
  - Configuration: `.crewai/crew.py` lines 196–206
  - Rate limit: 10 req/min (set in CrewAI crew config)
  - Cost tracking: LiteLLM success/failure callbacks in `.crewai/crew.py`

**Authentication:**

- Google OAuth 2.0 - User authentication for startup-blueprint app
  - SDK/Client: Direct fetch to Google OAuth endpoints (no SDK)
  - Auth URL: `https://accounts.google.com/o/oauth2/v2/auth`
  - Token URL: `https://oauth2.googleapis.com/token`
  - UserInfo URL: `https://www.googleapis.com/oauth2/v2/userinfo`
  - Scopes: `openid email profile`
  - Env vars: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`
  - Implementation: `apps/startup-blueprint/src/workers/auth-worker.ts`

**Agricultural Data Sources (agri-data-toolkit):**

- USDA Crop Sequence Boundaries via Source Cooperative - Field boundary polygons
  - Client: DuckDB with spatial + httpfs extensions (cloud-native GeoParquet querying)
  - URL: `https://data.source.coop/fiboa/us-usda-cropland/us_usda_cropland.parquet`
  - Auth: None (public data, no API key)
  - Implementation: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/field_boundaries.py`

- NASA POWER API - Daily meteorological time series (planned)
  - Parameters: T2M_MIN, T2M_MAX, PRECTOTCORR, solar radiation, humidity, wind
  - Configuration: `packages/agri-data-toolkit/config/default_config.yaml` (weather section)
  - Status: Configured but downloader not yet implemented

- NOAA Climate Data - Weather station observations (planned, optional)
  - Configuration: `packages/agri-data-toolkit/config/default_config.yaml` (noaa section, `enabled: false`)
  - Status: Not implemented

- Sentinel-2 Satellite Imagery (planned)
  - Client: sentinelsat ^1.2.0
  - Configuration: `packages/agri-data-toolkit/config/default_config.yaml` (imagery.sentinel2 section)
  - Status: Dependency declared, downloader not yet implemented

- Landsat Satellite Imagery (planned)
  - Configuration: `packages/agri-data-toolkit/config/default_config.yaml` (imagery.landsat section)
  - Status: Configured but downloader not yet implemented

- USDA Cropland Data Layer (planned)
  - Configuration: `packages/agri-data-toolkit/config/default_config.yaml` (cropland section)
  - Status: Not implemented

**GitHub API:**

- GitHub REST API - PR analysis for CrewAI code review
  - SDK/Client: PyGithub >=2.1.1
  - Auth: `GITHUB_TOKEN` (auto-provided by GitHub Actions; `ghp_*` token for local)
  - Implementation: `.crewai/tools/github_tools.py`
  - Used for: Reading commit diffs, PR metadata, file contents, posting comments

## Data Storage

**Databases:**

- Cloudflare D1 (SQLite at the edge)
  - Binding: `DB` in `wrangler.toml`
  - Database name: `startup_blueprint_db`
  - Tables: `users`, `activity`, `contacts`
  - Client: Direct D1 binding API (Cloudflare Workers native)
  - Usage: `apps/startup-blueprint/src/workers/api-worker.ts`, `apps/startup-blueprint/src/workers/auth-worker.ts`
  - Queries: Inline SQL via `env.DB.prepare()` with parameterized bindings

- DuckDB (in-process analytical database)
  - Used in: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/field_boundaries.py`
  - Extensions: `spatial`, `httpfs` (for remote GeoParquet querying)
  - Storage: In-memory (no persistent database file)
  - Purpose: Cloud-native querying of GeoParquet files on Source Cooperative

**File Storage:**

- Cloudflare R2 - Object storage for user uploads
  - Binding: `STORAGE` in `wrangler.toml`
  - Bucket name: `startup-blueprint-assets`
  - Key pattern: `{user-id}/{timestamp}-{filename}`
  - Usage: `apps/startup-blueprint/src/workers/api-worker.ts` (handleUploadRequest, handleGetFiles)

- Local filesystem - Agricultural data storage
  - Paths configured in `packages/agri-data-toolkit/config/default_config.yaml`
  - Raw data: `data/raw/`
  - Processed data: `data/processed/`
  - Metadata: `data/metadata/`
  - Export formats: GeoJSON, Shapefile, CSV

**Caching:**

- Cloudflare KV - Session management
  - Binding: `SESSION_STORE` in `wrangler.toml`
  - Session keys: `session:{token}` → `{user-id}` (24hr TTL)
  - Rate limit keys: `ratelimit:{userId}:{minute}` (60s TTL, 10 req/min)
  - Usage: `apps/startup-blueprint/src/workers/api-worker.ts`, `apps/startup-blueprint/src/workers/auth-worker.ts`

## Authentication & Identity

**Auth Provider:**

- Google OAuth 2.0 - Primary authentication for startup-blueprint
  - Implementation: `apps/startup-blueprint/src/workers/auth-worker.ts`
  - Flow: Authorization Code Grant
  - Session: UUID token stored in HttpOnly cookie + Cloudflare KV
  - User data stored in D1 `users` table (id, email, name, picture_url)
  - Session expiry: 24 hours (86400 seconds TTL)
  - CSRF protection: `state` parameter with `crypto.randomUUID()`
  - Cookie: `session={token}; HttpOnly; Secure; SameSite=Lax; Max-Age=86400; Path=/`

## Monitoring & Observability

**Error Tracking:**

- None (no Sentry, DataDog, etc.)
- Errors logged to console in Workers (`console.error`)
- CrewAI logs to stdout via Python `logging` module

**Logs:**

- agri-data-toolkit: loguru with console (colorized) + optional file handler with rotation
  - Configuration: `packages/agri-data-toolkit/src/agri_toolkit/core/logger.py`
  - File rotation: 10 MB, retention: 1 week, compressed with zip
- CrewAI: Python `logging` module to stdout
  - Configuration: `logging.basicConfig()` in `.crewai/main.py`
- Cloudflare Workers: `console.error()` / `console.log()` (Cloudflare dashboard logs)
- CI: GitHub Actions step summaries (`$GITHUB_STEP_SUMMARY`)

**Cost Tracking:**

- Custom cost tracker for LLM API calls
  - Implementation: `.crewai/tools/cost_tracker.py`
  - Tracks: model, tokens_in, tokens_out, cost, duration, generation_id
  - Output: Markdown cost breakdown table appended to review summaries
  - Callbacks registered in `.crewai/crew.py` via `litellm.success_callback`

## CI/CD & Deployment

**Hosting:**

- Cloudflare Pages - Static site hosting (website + startup-blueprint pages)
  - Production domain: `{workspace}.pages.dev`
  - Preview domain: `preview-startup-blueprint.SuperiorByteWorks.com`
  - Custom domain management: `scripts/cloudflare/manage-preview-domain.sh`

- Cloudflare Workers - Serverless API
  - API worker: `apps/startup-blueprint/src/workers/api-worker.ts`
  - Auth worker: `apps/startup-blueprint/src/workers/auth-worker.ts`

**CI Pipeline:**

- GitHub Actions - 4-phase CI pipeline
  - Entry point: `.github/workflows/ci.yml`
  - Phase 1: Validate (environment + format/lint in parallel)
  - Phase 2: Test/Build (docs links, CrewAI tests, website build, agri-toolkit tests + build)
  - Phase 3: Deploy (preview on PR with label, production on merge to main)
  - Phase 4: AI Review (CrewAI code review, runs last)
  - Triggers: PR, push to main, version tags (`v*`), manual
  - Concurrency: Cancel in-progress on non-main branches

- Reusable workflows: 11 reusable YAML files in `.github/workflows/`
  - `validate-environment-reusable.yml` - Labels, credentials, preview conflicts
  - `format-lint-reusable.yml` - Ruff format/lint with auto-commit
  - `link-check-reusable.yml` - Documentation link validation
  - `test-crewai-reusable.yml` - CrewAI Python tests
  - `website-test-build-reusable.yml` - Website build
  - `agri-test-reusable.yml` - Agri toolkit pytest (Python 3.13 matrix)
  - `agri-build-reusable.yml` - Build wheel + sdist
  - `preview-deploy-reusable.yml` - Cloudflare Pages preview deploy
  - `production-deploy-reusable.yml` - Cloudflare Pages production deploy
  - `publish-pypi-reusable.yml` - PyPI package publishing on version tags
  - `crewai-review-reusable.yml` - AI code review

- Local CI: `scripts/ci-local.sh`
  - Mirrors GitHub Actions pipeline locally
  - Flags: `--review`, `--full-review`, `--complete-full-review`, `--deploy`, `--step <name>`
  - Run lock: `.ci-local.lock` prevents concurrent runs
  - Specialist crews available: security, legal, finance, docs, agentic, marketing, science, government, strategy

**Package Publishing:**

- PyPI - agri-data-toolkit package
  - Trigger: Version tag push (`v*`)
  - Workflow: `.github/workflows/publish-pypi-reusable.yml`
  - Environment: `pypi` (GitHub environment protection)
  - Artifacts: Wheel + sdist from `agri-build-reusable.yml`

- Template Repository Sync
  - Target: `SuperiorByteWorks-LLC/py-agri-data-toolkit`
  - Trigger: Version tag push (`v*`)
  - Syncs filtered subset (toolkit package + essential scripts)

## Environment Configuration

**Required env vars (CI):**

- `OPENROUTER_API_KEY` - LLM API access for CrewAI reviews
- `CLOUDFLARE_API_TOKEN` - Cloudflare API access for deploys
- `CLOUDFLARE_ACCOUNT_ID` - Cloudflare account identifier
- `GOOGLE_CLIENT_ID` - Google OAuth client ID (Workers secrets)
- `GOOGLE_CLIENT_SECRET` - Google OAuth client secret (Workers secrets)
- `GITHUB_TOKEN` - Auto-provided by GitHub Actions

**Required env vars (local development):**

- `OPENROUTER_API_KEY` - For `--review` flag in `scripts/ci-local.sh`
- `CLOUDFLARE_API_TOKEN` - For `--deploy` flag (optional)
- `CLOUDFLARE_ACCOUNT_ID` - For `--deploy` flag (optional)

**Optional env vars:**

- `MODEL_DEFAULT` - Override default LLM model (default: `openrouter/xiaomi/mimo-v2-flash`)
- `MODEL_FALLBACK` - Override fallback LLM model (default: `openrouter/xiaomi/mimo-v2`)
- `CREWAI_TELEMETRY_OPT_OUT` - Disable CrewAI telemetry
- `CREWAI_LOG_LEVEL` - CrewAI log verbosity
- `CREWAI_REVIEW_TIMEOUT_SECONDS` - Review timeout (default: 90s quick, 240s full)

**Secrets location:**

- GitHub Secrets (encrypted) for CI
- `.env` file (gitignored) for local development
- `.crewai/.env.example` documents required vars with placeholder values
- Wrangler secrets for Cloudflare Workers bindings

## Webhooks & Callbacks

**Incoming:**

- GitHub Actions webhook triggers:
  - `pull_request` events → CI pipeline + CrewAI review
  - `push` to `main` → Production deployment
  - `push` of `v*` tags → PyPI publish + template sync
  - `workflow_dispatch` → Manual CI trigger

**Outgoing:**

- GitHub PR comments (via `actions/github-script@v7`)
  - Preview deployment URLs posted to PRs
  - Production deployment notifications on merged PRs
- GitHub Actions step summaries (CrewAI review results)
- Cloudflare API calls (Pages deploy, D1/R2/KV management)
- Google OAuth token exchange (`https://oauth2.googleapis.com/token`)
- Google UserInfo fetch (`https://www.googleapis.com/oauth2/v2/userinfo`)
- Source Cooperative HTTP range requests (DuckDB httpfs for GeoParquet)

---

_Integration audit: 2026-02-24_

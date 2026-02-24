# Architecture

**Analysis Date:** 2026-02-24

## Pattern Overview

**Overall:** Polyglot monorepo with pnpm workspaces (JS/TS) and Poetry (Python), orchestrated by Turborepo.

**Key Characteristics:**

- Two independent application domains sharing CI/CD infrastructure: a Python agricultural data toolkit and a TypeScript Cloudflare web application
- YAML-driven configuration for the Python toolkit; wrangler.toml + Cloudflare bindings for the TS app
- Template method pattern in the Python data pipeline layer (abstract base downloader → concrete implementations)
- Edge-first serverless architecture for the web app (Cloudflare Workers + Pages + D1 + R2 + KV)
- AI-assisted development loop via CrewAI review agents integrated into both local and CI workflows

## Layers

**Python Toolkit — Core (`packages/agri-data-toolkit/src/agri_toolkit/core/`):**

- Purpose: Shared infrastructure for all toolkit modules — configuration loading and logging
- Location: `packages/agri-data-toolkit/src/agri_toolkit/core/`
- Contains: `config.py` (YAML config manager with dot-notation access), `logger.py` (loguru setup)
- Depends on: `PyYAML`, `loguru`
- Used by: All other toolkit layers (downloaders, processors, exporters, utils)

**Python Toolkit — Downloaders (`packages/agri-data-toolkit/src/agri_toolkit/downloaders/`):**

- Purpose: Acquire raw agricultural data from external sources
- Location: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/`
- Contains: `base.py` (abstract `BaseDownloader`), `field_boundaries.py` (`FieldBoundaryDownloader`)
- Depends on: Core layer, `duckdb`, `geopandas`, `shapely`
- Used by: Scripts, tests, examples, future processors

**Python Toolkit — Processors (`packages/agri-data-toolkit/src/agri_toolkit/processors/`):**

- Purpose: Transform and integrate raw data (spatial joins, CRS transforms, attribute enrichment)
- Location: `packages/agri-data-toolkit/src/agri_toolkit/processors/`
- Contains: Empty `__init__.py` — stub for future development
- Depends on: Core layer (planned)
- Used by: Future scripts and exporters

**Python Toolkit — Exporters (`packages/agri-data-toolkit/src/agri_toolkit/exporters/`):**

- Purpose: Produce analysis-ready output files in multiple formats
- Location: `packages/agri-data-toolkit/src/agri_toolkit/exporters/`
- Contains: Empty `__init__.py` — stub for future development
- Depends on: Core layer (planned)
- Used by: Future scripts

**Python Toolkit — Utils (`packages/agri-data-toolkit/src/agri_toolkit/utils/`):**

- Purpose: Shared utility functions across the toolkit
- Location: `packages/agri-data-toolkit/src/agri_toolkit/utils/`
- Contains: Empty `__init__.py` — stub for future development
- Depends on: None (planned)
- Used by: All other layers (planned)

**Web App — Static Pages (`apps/startup-blueprint/src/pages/`):**

- Purpose: User-facing HTML pages served via Cloudflare Pages
- Location: `apps/startup-blueprint/src/pages/`
- Contains: `index.html` (landing page), `login.html` (OAuth login), `dashboard.html` (user dashboard)
- Depends on: Nothing (static HTML + Tailwind CSS)
- Used by: Cloudflare Pages hosting, linked to Workers for dynamic routes

**Web App — Workers (`apps/startup-blueprint/src/workers/`):**

- Purpose: Serverless API handlers deployed as Cloudflare Workers
- Location: `apps/startup-blueprint/src/workers/`
- Contains: `api-worker.ts` (REST API for D1/R2/KV operations), `auth-worker.ts` (Google OAuth flow)
- Depends on: Cloudflare runtime bindings (`D1Database`, `KVNamespace`, `R2Bucket`)
- Used by: Frontend pages via fetch calls

**CrewAI Review System (`.crewai/`):**

- Purpose: AI-powered code review agents for PRs
- Location: `.crewai/`
- Contains: `main.py` (entry point), `crew.py`, `crews/` (agent definitions), `tools/`, `utils/`, `memory/`, `config/`
- Depends on: Python, OpenRouter API
- Used by: CI pipeline (Phase 4), local `./scripts/ci-local.sh --review`

**CI/CD Orchestration (`.github/workflows/`):**

- Purpose: 4-phase CI pipeline — Validate → Test/Build → Deploy → CrewAI Review
- Location: `.github/workflows/ci.yml` (orchestrator) + reusable workflow files
- Contains: 15+ workflow YAML files organized by concern
- Depends on: GitHub Actions, Cloudflare, Poetry, pnpm
- Used by: All PRs and pushes to main

## Data Flow

**Agricultural Data Pipeline (Python Toolkit):**

1. User instantiates a downloader (e.g., `FieldBoundaryDownloader(config=Config())`)
2. `Config` loads YAML from `packages/agri-data-toolkit/config/default_config.yaml`, providing paths and parameters
3. `BaseDownloader.__init__()` creates `data/raw/` and `data/processed/` directories
4. `FieldBoundaryDownloader.download()` validates inputs, builds a DuckDB SQL query with region/crop filters
5. DuckDB executes cloud-native GeoParquet query against Source Cooperative (HTTP range requests — no full download)
6. Result DataFrame → WKB geometry parsing → GeoDataFrame creation (EPSG:5070) → area calculation → reprojection to EPSG:4326
7. `validate()` checks non-empty data, required columns, valid geometries, CRS defined
8. `_save_fields()` exports to GeoJSON or Shapefile at `data/raw/field_boundaries/`
9. Returns `GeoDataFrame` to caller

**Web App Request Flow (Startup Blueprint):**

1. Browser hits Cloudflare Pages for static HTML (`index.html`, `login.html`, `dashboard.html`)
2. Auth flow: `/auth/google` → Google OAuth → `/auth/callback` → `auth-worker.ts` exchanges code for token, upserts user in D1, creates session in KV
3. API calls from dashboard hit `api-worker.ts` (routes: `/api/contact`, `/api/user`, `/api/activity`, `/api/upload`, `/api/files`, `/api/logout`)
4. Session validation: cookie → KV lookup → user ID
5. Rate limiting: KV-based counter per user per minute (10 req/min)
6. Data operations: D1 for structured data (users, activity, contacts), R2 for file storage

**State Management:**

- Python toolkit: Stateless per-invocation; config loaded from YAML files; data persisted to filesystem (`data/raw/`, `data/processed/`)
- Web app: Session tokens in Cloudflare KV (24h TTL); user data in D1 SQLite; file storage in R2

**CI/CD Pipeline Flow:**

1. PR opened → `ci.yml` orchestrator triggers Phase 1 (validate-environment + core-ci in parallel)
2. `validate` gate passes both jobs → Phase 2: test-docs-links, test-crewai, test-website, test-agri-toolkit, build-agri-toolkit (parallel, self-detecting file changes)
3. `test-build` gate passes all Phase 2 jobs → Phase 3: deploy-preview (label-triggered on PR), deploy-production (merge to main), publish-pypi (on tag), sync-template-repo (on tag)
4. `deploy` gate → Phase 4: CrewAI review (AI code review on non-draft PRs)

## Key Abstractions

**`Config` (YAML Configuration Manager):**

- Purpose: Centralized access to all toolkit settings via dot-notation keys
- Location: `packages/agri-data-toolkit/src/agri_toolkit/core/config.py`
- Pattern: Loads YAML, provides `get(key, default)` with nested key support (e.g., `"paths.raw"`)
- Convenience properties: `data_root`, `raw_data_path`, `processed_data_path`
- Typed accessors: `get_field_config()`, `get_download_config()`, `get_paths()`

**`BaseDownloader` (Abstract Downloader):**

- Purpose: Template method base for all data source downloaders
- Location: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/base.py`
- Pattern: ABC with abstract `download(**kwargs) -> Any`, concrete `validate(data)`, `get_output_path(filename, subdirectory)`
- Convention: Subclasses implement `download()`, optionally override `validate()`
- Auto-creates `raw` and `processed` data directories on initialization

**`FieldBoundaryDownloader` (Concrete Downloader):**

- Purpose: Downloads USDA Crop Sequence Boundaries via DuckDB cloud-native GeoParquet queries
- Location: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/field_boundaries.py`
- Pattern: Inherits `BaseDownloader`; uses class-level constants for region/crop/URL mappings
- Accepts `data_source_url` override for testing (dependency injection)
- Returns `gpd.GeoDataFrame` with standardized column schema

**Cloudflare `Env` Interface (Worker Bindings):**

- Purpose: Type-safe access to Cloudflare platform services
- Location: `apps/startup-blueprint/src/workers/api-worker.ts`, `apps/startup-blueprint/src/workers/auth-worker.ts`
- Pattern: TypeScript interface defining `SESSION_STORE: KVNamespace`, `DB: D1Database`, `STORAGE: R2Bucket`, plus auth secrets
- Every worker handler function receives `(request: Request, env: Env)`

## Entry Points

**Python Toolkit — Package Import:**

- Location: `packages/agri-data-toolkit/src/agri_toolkit/__init__.py`
- Triggers: `from agri_toolkit.downloaders.field_boundaries import FieldBoundaryDownloader`
- Responsibilities: Exposes version, author, license metadata

**Python Toolkit — CLI Scripts:**

- Location: `packages/agri-data-toolkit/scripts/` (e.g., `generate_sample_field_boundaries.py`, `generate_test_map.py`)
- Triggers: `python scripts/generate_sample_field_boundaries.py`
- Responsibilities: One-off data generation, test fixture creation

**Web App — API Worker:**

- Location: `apps/startup-blueprint/src/workers/api-worker.ts`
- Triggers: HTTP requests to `/api/*` routes via Cloudflare Workers
- Responsibilities: CRUD operations on D1 (users, contacts, activity), R2 file management, session/rate-limit checks via KV

**Web App — Auth Worker:**

- Location: `apps/startup-blueprint/src/workers/auth-worker.ts`
- Triggers: HTTP requests to `/auth/google` and `/auth/callback`
- Responsibilities: Google OAuth redirect, token exchange, user upsert in D1, session creation in KV

**Web App — Static Pages:**

- Location: `apps/startup-blueprint/src/pages/index.html`
- Triggers: Browser navigation to root URL
- Responsibilities: Landing page, email capture form

**CrewAI Review:**

- Location: `.crewai/main.py`
- Triggers: CI Phase 4 (`crewai-review-reusable.yml`) or `./scripts/ci-local.sh --review`
- Responsibilities: Analyze diff + CI logs, route to specialist review agents

**CI Pipeline:**

- Location: `.github/workflows/ci.yml`
- Triggers: Push to main, PR events, tag pushes, manual dispatch
- Responsibilities: Orchestrate 4-phase pipeline via reusable workflows

**Local CI:**

- Location: `scripts/ci-local.sh`
- Triggers: Manual developer invocation
- Responsibilities: Mirror GitHub Actions pipeline locally (format, lint, test, build, optional review/deploy)

## Error Handling

**Strategy:** Layer-specific exception handling with logging at each boundary.

**Patterns:**

- Python toolkit downloaders: Catch broad exceptions in `_query_source_cooperative()`, log via loguru, re-raise as `RuntimeError` with cause chain (`raise RuntimeError(...) from e`)
- Python toolkit validation: Return `bool` from `validate()` methods; callers check and raise `RuntimeError` on failure
- Input validation: Raise `ValueError` early for invalid parameters (count < 1, invalid regions/crops)
- Cloudflare Workers: Top-level try/catch in `fetch()` handler returns `500 Internal Server Error`; auth/session failures return `401 Unauthorized`; rate limit violations return `429`

## Cross-Cutting Concerns

**Logging:**

- Python toolkit: `loguru` via `packages/agri-data-toolkit/src/agri_toolkit/core/logger.py`. Call `setup_logger()` for file + console output. All downloader methods log progress at INFO level, debug at DEBUG level.
- Cloudflare Workers: `console.error()` for error logging (Cloudflare runtime)
- CI: GitHub Actions step summaries with markdown formatting

**Validation:**

- Python toolkit: `BaseDownloader.validate()` (overridden per downloader); field boundaries check: non-empty, required columns, valid geometries, CRS defined
- CI: Multi-phase validation — environment secrets, code formatting (Ruff), linting, type checking, link checking
- Config: `validation` section in `default_config.yaml` with configurable checks (completeness, spatial_validity, temporal_coverage, value_ranges, crs_consistency)

**Authentication:**

- Web app: Google OAuth 2.0 via `auth-worker.ts`; session tokens stored in Cloudflare KV with 24h TTL; cookie-based session identification (`HttpOnly; Secure; SameSite=Lax`)
- Rate limiting: KV-based counter, 10 requests per user per minute

**Configuration:**

- Python toolkit: YAML-driven via `Config` class loading `config/default_config.yaml`; supports custom config paths and dot-notation key access
- Web app: `wrangler.toml` for Cloudflare bindings; environment variables for secrets (Google OAuth credentials)
- CI: Reusable workflows accept `commit_sha` input; secrets passed via `secrets: inherit`

---

_Architecture analysis: 2026-02-24_

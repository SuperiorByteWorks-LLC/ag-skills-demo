# Technology Stack

**Analysis Date:** 2026-02-24

## Languages

**Primary:**

- TypeScript 5.3.3 - Cloudflare Workers (`apps/startup-blueprint/src/workers/`), root linting/typecheck config
- Python 3.12+ (toolkit), 3.10+ (CrewAI) - Two separate Python ecosystems with different version targets

**Secondary:**

- HTML/CSS - Static pages (`apps/startup-blueprint/src/pages/`, `website/public/`)
- YAML - Configuration throughout (`config/default_config.yaml`, `.github/workflows/`, `.crewai/config/`)
- SQL - D1 schema and inline queries (`apps/startup-blueprint/src/workers/api-worker.ts`)
- Bash - CI scripts (`scripts/ci-local.sh`, `scripts/cloudflare/`)

## Runtime

**Environment:**

- Node.js >=18.0.0 (CI uses Node 20)
- Python 3.12 (agri-data-toolkit via Poetry, targets `^3.12`)
- Python 3.10–3.13 (CrewAI subsystem, root `pyproject.toml`)
- Cloudflare Workers runtime (V8 isolates, compatibility_date 2026-01-23)

**Package Manager:**

- pnpm >=8.0.0 (pinned `pnpm@8.15.0` in `package.json` `packageManager` field)
- Lockfile: `pnpm-lock.yaml` present
- Poetry (agri-data-toolkit `packages/agri-data-toolkit/pyproject.toml`, build backend `poetry.core.masonry.api`)
- pip/setuptools (CrewAI subsystem `pyproject.toml`, build backend `setuptools.build_meta`)
- UV recommended for CrewAI local dev (per `.crewai/README.md`)

## Frameworks

**Core:**

- Cloudflare Workers - Serverless API functions (`apps/startup-blueprint/src/workers/`)
- Cloudflare Pages - Static site hosting and preview deployments
- CrewAI >=0.86.0 - Multi-agent AI code review system (`.crewai/`)
- No frontend framework (plain HTML/CSS static pages)

**Testing:**

- Vitest ^1.2.0 - Unit tests for startup-blueprint (`apps/startup-blueprint/package.json`)
- Playwright ^1.40.0 - E2E tests for startup-blueprint (`apps/startup-blueprint/package.json`)
- pytest >=8.0.0 - Python tests for both agri-data-toolkit and CrewAI
- pytest-asyncio - Async test support
- pytest-cov - Coverage reporting
- pytest-mock - Mocking support (agri-data-toolkit only)

**Build/Dev:**

- Turborepo - Monorepo pipeline orchestration (`turbo.json`)
- Wrangler ^3.22.0 - Cloudflare Workers/Pages CLI (`apps/startup-blueprint/package.json`)
- ESLint 8.x + @typescript-eslint - JS/TS linting (`.eslintrc.json`)
- Prettier 3.x - Code formatting (`.prettierrc.json`)
- Black 24.x - Python formatting (pre-commit, both Python subsystems)
- Ruff >=0.6.0 - Python linting (CrewAI subsystem, local CI)
- isort 5.x - Python import sorting (pre-commit, agri-data-toolkit)
- Flake8 7.x - Python linting (pre-commit, agri-data-toolkit)
- mypy >=1.13.0 - Python type checking (agri-data-toolkit: strict; CrewAI: relaxed)
- commitlint - Conventional commit enforcement (`commitlint.config.js`)
- Markdownlint-cli2 - Markdown linting
- Stylelint - CSS linting (`.stylelintrc.json`)
- pre-commit - Git hook management (`.pre-commit-config.yaml`)
- lychee - External link checking (auto-installed by CI)

## Key Dependencies

**Critical (agri-data-toolkit):**

- geopandas ^1.0.0 - Geospatial data handling, core data structure
- duckdb ^1.1.0 - Cloud-native GeoParquet querying with spatial extension
- rasterio ^1.4.0 - Raster data I/O (satellite imagery)
- shapely ^2.0.0 - Geometry processing
- pandas ^2.2.0 - Tabular data processing
- numpy ^2.1.0 - Numerical operations
- pyarrow ^22.0.0 - Parquet file support
- scipy ^1.14.0 - Scientific computing
- aiohttp ^3.10.0 - Async HTTP for data downloads
- requests ^2.32.0 - Synchronous HTTP
- sentinelsat ^1.2.0 - Sentinel satellite imagery API
- loguru ^0.7.0 - Structured logging
- click ^8.1.0 - CLI interface
- PyYAML ^6.0.0 - YAML configuration parsing

**Critical (CrewAI subsystem):**

- crewai >=0.86.0 - Multi-agent orchestration framework
- crewai-tools >=0.12.0 - CrewAI tool extensions
- litellm >=1.0.0 - LLM API abstraction (routes to OpenRouter)
- langchain-openai >=0.2.0 - LangChain OpenAI integration
- PyGithub >=2.1.1 - GitHub API client for PR analysis
- fastapi >=0.115.0 - Required by LiteLLM proxy dependencies
- uvicorn >=0.30.0 - ASGI server (LiteLLM dependency)

**Critical (Cloudflare app):**

- @cloudflare/workers-types ^4.20240117.0 - TypeScript types for Workers API

**Infrastructure:**

- python-dotenv >=1.0.0 - Environment variable loading (both Python subsystems)
- tqdm ^4.67.0 - Progress bars for data downloads
- colorama ^0.4.6 - Terminal color output

**Visualization (optional group):**

- matplotlib ^3.9.0 - Static plots
- seaborn ^0.13.0 - Statistical visualization
- plotly ^5.24.0 - Interactive plots

**Documentation (dev):**

- sphinx ^8.1.0 - API documentation generation
- sphinx-rtd-theme ^3.0.0 - Read the Docs theme
- jupyter ^1.1.0 / jupyterlab ^4.3.0 - Notebook support

## Configuration

**Environment:**

- `.env` files loaded at root level by `scripts/ci-local.sh` and `python-dotenv`
- `.crewai/.env.example` documents required env vars for CrewAI
- GitHub Secrets used in CI: `OPENROUTER_API_KEY`, `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
- Wrangler secrets for Workers: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`
- Agri-data-toolkit uses YAML config: `packages/agri-data-toolkit/config/default_config.yaml`

**Build:**

- `turbo.json` - Turborepo pipeline: build → test → deploy
- `pnpm-workspace.yaml` - Workspaces: `apps/*`, `packages/*`
- `tsconfig.json` (root) - Absent; per-workspace configs in `apps/startup-blueprint/`
- `wrangler.toml` - Cloudflare Workers configuration with D1/R2/KV bindings
- `.pre-commit-config.yaml` - Pre-commit hooks for Black, isort, flake8, general checks

**Linting/Formatting:**

- `.eslintrc.json` - ESLint config with TypeScript plugin and Prettier integration
- `.prettierrc.json` - 80 char width, single quotes, ES5 trailing commas, LF line endings
- `.flake8` - Flake8 config
- `.sqlfluff` - SQL linting
- `.markdownlint.json` - Markdown linting rules
- `.stylelintrc.json` - CSS/SCSS linting
- `.yamllint.yml` - YAML linting

## Platform Requirements

**Development:**

- Linux (Ubuntu LTS 20.04+ recommended), macOS, or Windows with WSL
- Node.js 18+, pnpm 8+
- Python 3.12+ for agri-data-toolkit, Python 3.10+ for CrewAI
- Poetry for agri-data-toolkit dependency management
- 50GB disk for full agricultural datasets; 8GB RAM recommended
- Git, optional: Wrangler CLI for Cloudflare development

**Production:**

- Cloudflare Pages (static hosting, free tier)
- Cloudflare Workers (serverless compute)
- Cloudflare D1 (SQLite edge database)
- Cloudflare R2 (object storage)
- Cloudflare KV (key-value session store)
- GitHub Actions (CI/CD, free tier)
- PyPI (Python package publishing on tagged releases)

---

_Stack analysis: 2026-02-24_

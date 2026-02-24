# Codebase Structure

**Analysis Date:** 2026-02-24

## Directory Layout

```
agri-data-toolkit/
├── apps/                           # pnpm workspace: deployable applications
│   └── startup-blueprint/          # Cloudflare Pages + Workers web app
│       ├── scripts/                # Setup and seed scripts (bash)
│       ├── src/
│       │   ├── pages/              # Static HTML pages (Cloudflare Pages)
│       │   ├── scripts/            # TypeScript utility scripts
│       │   └── workers/            # Cloudflare Workers (TypeScript)
│       ├── package.json            # App dependencies (wrangler, vitest, playwright)
│       ├── tsconfig.json           # TypeScript config (ES2022, strict)
│       ├── tsconfig.pages.json     # Pages-specific TS config
│       ├── wrangler.toml           # Cloudflare bindings (D1, R2, KV)
│       ├── API.md                  # API endpoint documentation
│       └── MIGRATIONS.md           # Database migration docs
├── packages/                       # pnpm workspace: shared packages
│   └── agri-data-toolkit/          # Python agricultural data toolkit
│       ├── config/                 # YAML configuration files
│       ├── docs/                   # Toolkit-specific documentation
│       ├── examples/               # Usage example scripts (stub)
│       ├── notebooks/              # Jupyter notebooks (stub)
│       ├── scripts/                # Data generation and utility scripts
│       ├── src/
│       │   └── agri_toolkit/       # Python package root
│       │       ├── core/           # Config + logging infrastructure
│       │       ├── downloaders/    # Data source downloaders
│       │       ├── exporters/      # Output format exporters (stub)
│       │       ├── processors/     # Data transformation (stub)
│       │       └── utils/          # Shared utilities (stub)
│       ├── tests/                  # Pytest test suite
│       │   └── test_downloaders/   # Downloader-specific tests
│       └── pyproject.toml          # Poetry config, dependencies, tool settings
├── website/                        # Static landing site
│   ├── public/                     # Static files (index.html, styles.css)
│   └── package.json                # Dev server config (serve)
├── .crewai/                        # AI code review agent system
│   ├── config/                     # Agent configuration
│   ├── crews/                      # Agent crew definitions
│   ├── memory/                     # Persistent review memory (JSON)
│   ├── tests/                      # CrewAI test suite
│   ├── tools/                      # Custom agent tools
│   ├── utils/                      # Agent utilities
│   ├── main.py                     # Review entry point
│   ├── crew.py                     # Crew orchestration
│   └── pyproject.toml              # CrewAI Python dependencies
├── docs/                           # Project-wide documentation
│   ├── agentic/                    # AI agent instructions and standards
│   │   ├── adr/                    # Architecture Decision Records
│   │   ├── markdown_templates/     # Templates for PRs, issues, ADRs, kanban
│   │   ├── mermaid_diagrams/       # Diagram examples and references
│   │   └── perplexity/             # Perplexity AI space instructions
│   ├── blueprints/                 # Startup blueprint guide
│   ├── classes/                    # Course materials and assignments
│   │   ├── assignments/            # Student assignments
│   │   └── images/                 # Case study images
│   ├── guides/                     # Step-by-step operational guides (01-07)
│   └── project/                    # Project tracking (file-based)
│       ├── issues/                 # Issue records (markdown)
│       ├── kanban/                 # Sprint boards (markdown)
│       └── pr/                     # Pull request records (markdown)
├── scripts/                        # Repository-wide operational scripts
│   ├── cloudflare/                 # Cloudflare deployment helpers
│   ├── ci-local.sh                 # Local CI runner (mirrors GitHub Actions)
│   ├── validate-credentials.sh     # Environment validation
│   ├── memory.sh                   # CrewAI memory management
│   └── *.py                        # Python utility scripts
├── .github/
│   └── workflows/                  # GitHub Actions CI/CD
│       ├── ci.yml                  # Main orchestrator (4-phase pipeline)
│       ├── agents/                 # Agent workflow configs
│       ├── jobs/                   # Reusable job definitions
│       ├── workspaces/             # Workspace-specific configs
│       └── *-reusable.yml          # 12+ reusable workflow files
├── .tools/                         # Developer tooling
│   └── bin/                        # Tool binaries
├── .planning/                      # GSD planning artifacts
├── package.json                    # Root pnpm workspace config
├── pnpm-workspace.yaml             # Workspace: apps/*, packages/*
├── pnpm-lock.yaml                  # Lock file
├── turbo.json                      # Turborepo pipeline config
├── pyproject.toml                  # Root Python config (not a package)
├── AGENTS.md                       # AI agent entry point and quick reference
├── commitlint.config.js            # Commit message convention enforcement
├── .eslintrc.json                  # ESLint config (root)
├── .prettierrc.json                # Prettier config (root)
├── .prettierignore                 # Prettier ignore patterns
├── .markdownlint.json              # Markdown linting rules
├── .markdownlintignore             # Markdown lint ignore patterns
├── .stylelintrc.json               # CSS linting config
├── .yamllint.yml                   # YAML linting config
├── .flake8                         # Python flake8 config
├── .sqlfluff                       # SQL linting config
├── .pre-commit-config.yaml         # Pre-commit hooks
├── .lycheeignore                   # Link checker ignore patterns
└── .gitignore                      # Git ignore rules
```

## Directory Purposes

**`apps/startup-blueprint/`:**

- Purpose: Cloudflare-hosted web application (Pages for static content, Workers for API)
- Contains: HTML pages, TypeScript worker handlers, bash setup/seed scripts
- Key files: `src/workers/api-worker.ts` (main API), `src/workers/auth-worker.ts` (OAuth), `wrangler.toml` (Cloudflare bindings)

**`packages/agri-data-toolkit/`:**

- Purpose: Installable Python package for agricultural data acquisition and analysis
- Contains: Source code, tests, configuration, documentation, scripts
- Key files: `src/agri_toolkit/downloaders/field_boundaries.py` (primary implemented feature), `config/default_config.yaml` (all settings), `pyproject.toml` (Poetry config + tool settings)

**`packages/agri-data-toolkit/src/agri_toolkit/core/`:**

- Purpose: Foundation layer — configuration management and logging
- Contains: `config.py` (YAML loader with dot-notation access), `logger.py` (loguru setup)
- Key pattern: All other modules import from here; this is the dependency root

**`packages/agri-data-toolkit/src/agri_toolkit/downloaders/`:**

- Purpose: Data source downloaders implementing the `BaseDownloader` abstract class
- Contains: `base.py` (ABC), `field_boundaries.py` (USDA CSB downloader), `README.md` (detailed usage docs)
- Key pattern: Template method — inherit `BaseDownloader`, implement `download()`, optionally override `validate()`

**`packages/agri-data-toolkit/src/agri_toolkit/processors/`:**

- Purpose: Data transformation and integration (spatial joins, enrichment)
- Contains: Empty `__init__.py` — awaiting implementation

**`packages/agri-data-toolkit/src/agri_toolkit/exporters/`:**

- Purpose: Export data in multiple formats (GeoJSON, CSV, Shapefile, GeoParquet)
- Contains: Empty `__init__.py` — awaiting implementation

**`packages/agri-data-toolkit/src/agri_toolkit/utils/`:**

- Purpose: Shared utility functions
- Contains: Empty `__init__.py` — awaiting implementation

**`website/`:**

- Purpose: Static public landing site (separate from the startup-blueprint app)
- Contains: `public/index.html`, `public/styles.css`
- Deployed via Cloudflare Pages through CI pipeline

**`.crewai/`:**

- Purpose: AI code review system using CrewAI framework
- Contains: Agents, tools, memory, configuration for automated PR reviews
- Key files: `main.py` (entry point), `crew.py` (orchestration), `memory/` (persistent JSON rules)

**`docs/agentic/`:**

- Purpose: AI agent operating instructions, style guides, templates, and standards
- Contains: `instructions.md` (primary agent entry), `workflow_guide.md`, style guides, ADRs, templates
- Key pattern: AI agents read these docs to understand how to work in this codebase

**`docs/project/`:**

- Purpose: File-based project tracking (not GitHub UI)
- Contains: `issues/` (issue records), `pr/` (PR records), `kanban/` (sprint boards)
- Key pattern: All tracking is committed to git as markdown files

**`docs/guides/`:**

- Purpose: Step-by-step operational guides for the startup blueprint
- Contains: 7 numbered guides (01-legal through 07-operations) + quickstart

**`scripts/`:**

- Purpose: Developer-facing automation for local CI, credentials, deployment, and memory management
- Contains: `ci-local.sh` (main local CI runner), `cloudflare/` (deploy helpers), `memory.sh` (CrewAI memory CLI)

**`.github/workflows/`:**

- Purpose: GitHub Actions CI/CD — 4-phase pipeline with reusable workflows
- Contains: `ci.yml` (orchestrator), 12+ `*-reusable.yml` files, config subdirectories
- Key pattern: Single orchestrator calls reusable workflows; each workspace self-detects file changes

## Key File Locations

**Entry Points:**

- `packages/agri-data-toolkit/src/agri_toolkit/__init__.py`: Python package entry (version, metadata)
- `apps/startup-blueprint/src/workers/api-worker.ts`: Web app API entry (Cloudflare Worker `fetch` handler)
- `apps/startup-blueprint/src/workers/auth-worker.ts`: Auth entry (Google OAuth flow)
- `apps/startup-blueprint/src/pages/index.html`: Web app UI entry (landing page)
- `.crewai/main.py`: CrewAI review system entry
- `.github/workflows/ci.yml`: CI/CD pipeline entry
- `scripts/ci-local.sh`: Local CI entry

**Configuration:**

- `packages/agri-data-toolkit/config/default_config.yaml`: All toolkit settings (fields, weather, soil, paths, etc.)
- `packages/agri-data-toolkit/pyproject.toml`: Python dependencies, tool config (black, isort, pytest, mypy)
- `apps/startup-blueprint/wrangler.toml`: Cloudflare bindings (D1, R2, KV)
- `apps/startup-blueprint/tsconfig.json`: TypeScript compiler options
- `package.json`: Root pnpm workspace scripts + JS dev dependencies
- `pnpm-workspace.yaml`: Workspace members (`apps/*`, `packages/*`)
- `turbo.json`: Turborepo pipeline (build, dev, test, deploy:preview)
- `commitlint.config.js`: Scoped conventional commit enforcement
- `.eslintrc.json`: ESLint rules (root level)
- `.prettierrc.json`: Prettier formatting rules
- `.flake8`: Python flake8 config
- `.pre-commit-config.yaml`: Git hooks

**Core Logic:**

- `packages/agri-data-toolkit/src/agri_toolkit/core/config.py`: YAML configuration manager
- `packages/agri-data-toolkit/src/agri_toolkit/core/logger.py`: Loguru logging setup
- `packages/agri-data-toolkit/src/agri_toolkit/downloaders/base.py`: Abstract base downloader
- `packages/agri-data-toolkit/src/agri_toolkit/downloaders/field_boundaries.py`: USDA CSB field boundary downloader (primary implemented feature — 471 lines)
- `apps/startup-blueprint/src/workers/api-worker.ts`: REST API handler (201 lines)
- `apps/startup-blueprint/src/workers/auth-worker.ts`: OAuth handler (132 lines)

**Testing:**

- `packages/agri-data-toolkit/tests/conftest.py`: Shared pytest fixtures (temp dirs, sample data loading)
- `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries.py`: Field boundary integration tests
- `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries_unit.py`: Unit tests
- `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries_persistent.py`: Persistent data tests for CI artifacts

**Documentation:**

- `AGENTS.md`: AI agent entry point (read first)
- `docs/agentic/instructions.md`: Primary agent operating instructions
- `docs/agentic/workflow_guide.md`: 14-step development workflow
- `docs/agentic/contribute_standards.md`: Code and commit standards
- `docs/agentic/markdown_style_guide.md`: Markdown formatting rules
- `docs/agentic/mermaid_style_guide.md`: Diagram standards

## Naming Conventions

**Files:**

- Python modules: `snake_case.py` (e.g., `field_boundaries.py`, `config.py`)
- TypeScript workers: `kebab-case.ts` (e.g., `api-worker.ts`, `auth-worker.ts`)
- HTML pages: `lowercase.html` (e.g., `index.html`, `dashboard.html`)
- Config files: `snake_case.yaml` or `kebab-case.json` (e.g., `default_config.yaml`)
- Shell scripts: `kebab-case.sh` (e.g., `ci-local.sh`, `setup-all.sh`)
- Docs guides: `NN-kebab-case.md` (e.g., `01-legal-foundation.md`)
- Project tracking: `type-NNNNNNN-slug.md` (e.g., `pr-00000001-assignment-template.md`)
- CI workflows: `kebab-case-reusable.yml` (e.g., `agri-test-reusable.yml`)

**Directories:**

- Python packages: `snake_case` (e.g., `agri_toolkit`, `test_downloaders`)
- JS/TS app dirs: `kebab-case` (e.g., `startup-blueprint`)
- Top-level: `lowercase` (e.g., `apps`, `packages`, `docs`, `scripts`, `website`)
- Hidden dirs: `.prefix` for tooling (e.g., `.crewai`, `.github`, `.tools`, `.planning`)

**Python Classes:** `PascalCase` (e.g., `BaseDownloader`, `FieldBoundaryDownloader`, `Config`)
**Python Functions/Variables:** `snake_case` (e.g., `get_duckdb_connection`, `data_source_url`)
**TypeScript Functions:** `camelCase` (e.g., `handleContactSubmission`, `getUserIdFromRequest`)
**TypeScript Interfaces:** `PascalCase` (e.g., `Env`, `GoogleUserInfo`)
**Constants:** `UPPER_SNAKE_CASE` in Python (e.g., `SOURCE_COOP_BASE_URL`, `REGION_STATE_FIPS`, `CROP_TYPES`)

## Where to Add New Code

**New Downloader (e.g., soil, weather, satellite):**

- Implementation: `packages/agri-data-toolkit/src/agri_toolkit/downloaders/{source_name}.py`
- Pattern: Inherit from `BaseDownloader` in `base.py`, implement `download(**kwargs)` and `validate(data)`
- Register: Import in `packages/agri-data-toolkit/src/agri_toolkit/downloaders/__init__.py`
- Tests: `packages/agri-data-toolkit/tests/test_downloaders/test_{source_name}.py`
- Config: Add section to `packages/agri-data-toolkit/config/default_config.yaml`

**New Processor (e.g., spatial join, CRS transform):**

- Implementation: `packages/agri-data-toolkit/src/agri_toolkit/processors/{processor_name}.py`
- Pattern: Follow similar abstract base pattern as downloaders (create `base.py` if needed)
- Tests: `packages/agri-data-toolkit/tests/test_processors/test_{processor_name}.py`

**New Exporter (e.g., GeoParquet, CSV):**

- Implementation: `packages/agri-data-toolkit/src/agri_toolkit/exporters/{format_name}.py`
- Tests: `packages/agri-data-toolkit/tests/test_exporters/test_{format_name}.py`

**New Utility Function:**

- Implementation: `packages/agri-data-toolkit/src/agri_toolkit/utils/{utility_group}.py`
- Tests: `packages/agri-data-toolkit/tests/test_utils/test_{utility_group}.py`

**New Web App API Endpoint:**

- Implementation: Add route handler in `apps/startup-blueprint/src/workers/api-worker.ts` (follow existing `if (url.pathname === ...) return await handle...()` pattern)
- Or create new worker file in `apps/startup-blueprint/src/workers/`
- Update: `apps/startup-blueprint/API.md` with endpoint documentation

**New Web App Page:**

- Implementation: `apps/startup-blueprint/src/pages/{page_name}.html`
- Static HTML + Tailwind CSS; link from navigation

**New CI Workflow:**

- Implementation: `.github/workflows/{workspace}-{type}-reusable.yml`
- Register: Add job in `.github/workflows/ci.yml` with appropriate phase and gate dependencies
- Pattern: Self-detect file changes, skip gracefully if no relevant changes

**New Documentation:**

- Guides: `docs/guides/NN-{topic}.md` (follow numbering scheme)
- ADRs: `docs/agentic/adr/adr-NNNN-{title}.md`
- Issues: `docs/project/issues/issue-NNNNNNNN-{slug}.md`
- PRs: `docs/project/pr/pr-NNNNNNNN-{slug}.md`
- Kanban: `docs/project/kanban/{sprint-name}.md`

**New Script:**

- Repository-wide: `scripts/{script-name}.sh` or `scripts/{script-name}.py`
- Toolkit-specific: `packages/agri-data-toolkit/scripts/{script-name}.py`
- Cloudflare helpers: `scripts/cloudflare/{helper-name}.sh`

## Special Directories

**`data/` (within agri-data-toolkit working directory):**

- Purpose: Downloaded and processed agricultural data files
- Generated: Yes (by downloaders and processors at runtime)
- Committed: No (gitignored)

**`.crewai/workspace/`:**

- Purpose: Temporary workspace for CrewAI review artifacts
- Generated: Yes (cleared at each `ci-local.sh` run)
- Committed: No

**`.crewai/memory/`:**

- Purpose: Persistent review memory and suppression rules (JSON)
- Generated: Yes (by `scripts/memory.sh`)
- Committed: Yes (intentionally version-controlled)

**`dist/` (within apps):**

- Purpose: Build output for TypeScript compilation
- Generated: Yes (by `tsc` via `pnpm build`)
- Committed: No (gitignored)

**`.planning/`:**

- Purpose: GSD planning artifacts (codebase analysis, phase plans)
- Generated: Yes (by GSD commands)
- Committed: Varies by project policy

**`.tools/bin/`:**

- Purpose: Local developer tool binaries
- Generated: Varies
- Committed: Varies

**`docs/project/`:**

- Purpose: File-based project tracking (issues, PRs, kanban boards)
- Generated: By humans and AI agents
- Committed: Yes (this is the project's tracking system)

---

_Structure analysis: 2026-02-24_

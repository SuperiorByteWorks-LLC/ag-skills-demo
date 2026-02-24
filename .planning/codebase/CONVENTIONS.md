# Coding Conventions

**Analysis Date:** 2026-02-24

## Naming Patterns

**Files (Python):**

- Use `snake_case.py` for all modules: `field_boundaries.py`, `cost_tracker.py`, `workspace_tool.py`
- Test files: `test_<module>.py` prefix: `test_field_boundaries_unit.py`, `test_cost_tracker.py`
- `__init__.py` in every package directory (even if only a docstring)

**Files (TypeScript):**

- Use `kebab-case.ts`: `api-worker.ts`, `auth-worker.ts`, `agentic-loop.ts`
- Config files: `<tool>.config.<ext>`: `commitlint.config.js`, `turbo.json`

**Files (Configuration):**

- Dot-prefixed JSON: `.eslintrc.json`, `.prettierrc.json`, `.stylelintrc.json`, `.markdownlint.json`
- Dot-prefixed YAML: `.yamllint.yml`, `.pre-commit-config.yaml`

**Functions (Python):**

- `snake_case` for all functions and methods: `download()`, `_query_source_cooperative()`, `get_output_path()`
- Private methods prefixed with underscore: `_get_duckdb_connection()`, `_save_fields()`, `_setup_directories()`
- Test functions: `test_<description>`: `test_download_minimum_fields`, `test_validate_rejects_empty_data`

**Functions (TypeScript):**

- `camelCase` for all functions: `getUserIdFromRequest()`, `handleContactSubmission()`, `checkRateLimit()`
- Handler functions prefixed with `handle`: `handleGetUser()`, `handleLogout()`, `handleUploadRequest()`

**Variables (Python):**

- `snake_case` for all variables: `state_fips`, `crop_codes`, `fields_gdf`
- Constants as `UPPER_SNAKE_CASE`: `SOURCE_COOP_BASE_URL`, `REGION_STATE_FIPS`, `CROP_TYPES`, `MAX_FILE_SIZE`
- Module-level constants at class level or module top

**Variables (TypeScript):**

- `camelCase` for variables: `corsHeaders`, `userId`, `sessionMatch`

**Classes (Python):**

- `PascalCase`: `BaseDownloader`, `FieldBoundaryDownloader`, `Config`, `WorkspaceTool`, `CostTracker`
- Test classes: `Test<ClassName>`: `TestFieldBoundaryDownloaderUnit`, `TestWorkspaceTool`, `TestCostTracker`
- Input schemas: `<ToolName>Input`: `WorkspaceToolInput`
- Dataclasses: `PascalCase`: `APICallMetrics`

**Types (TypeScript):**

- `PascalCase` interfaces: `Env`

## Code Style

**Formatting (Python):**

- **Formatter:** Black
- **Line length:** 100 characters
- **Target version:** `py312` (agri-data-toolkit), `py310`+ (crewai)
- **Config:** `[tool.black]` in each `pyproject.toml`
  - `packages/agri-data-toolkit/pyproject.toml`: `line-length = 100`, `target-version = ['py312']`
  - `pyproject.toml` (root): `line-length = 100`, `target-version = ["py310", "py311", "py312", "py313"]`
  - `.crewai/pyproject.toml`: `line-length = 100`, `target-version = ["py310", "py311", "py312", "py313"]`

**Formatting (TypeScript/JavaScript):**

- **Formatter:** Prettier (v3.1.0+)
- **Config:** `.prettierrc.json`
  - `printWidth`: 80 (default), 120 for `.md` and `.json`
  - `tabWidth`: 2
  - `useTabs`: false
  - `semi`: true (semicolons required)
  - `singleQuote`: true
  - `trailingComma`: "es5"
  - `arrowParens`: "always"
  - `endOfLine`: "lf"
  - `proseWrap`: "always" (default), "preserve" for markdown

**Linting (Python):**

- **agri-data-toolkit:** Flake8 (`.flake8`) + isort + mypy (strict)
  - `max-line-length = 100`
  - `extend-ignore = E203, W503`
  - `per-file-ignores: __init__.py:F401`
- **CrewAI / root:** Ruff
  - `line-length = 100`
  - Rules: `["E", "F", "I", "N", "W", "UP"]` (root), `["E", "F", "W", "I001"]` (.crewai)
  - `ignore = ["E501"]` (line too long, handled by formatter)

**Linting (TypeScript/JavaScript):**

- **Linter:** ESLint (v8) with `@typescript-eslint`
- **Config:** `.eslintrc.json`
  - Extends: `eslint:recommended`, `plugin:@typescript-eslint/recommended`, `plugin:prettier/recommended`
  - Key rules:
    - `no-console`: warn
    - `@typescript-eslint/no-unused-vars`: error (ignore `^_` prefixed args)
    - `@typescript-eslint/no-explicit-any`: warn
  - Ignores: `node_modules/`, `dist/`, `build/`, `.turbo/`, `*.config.js`, `*.config.ts`

**Linting (CSS):**

- **Linter:** Stylelint (v16)
- **Config:** `.stylelintrc.json`
  - Extends: `stylelint-config-standard`, `stylelint-config-prettier`
  - Relaxed rules: `selector-class-pattern: null`, `no-descending-specificity: null`

**Linting (Markdown):**

- **Linter:** markdownlint-cli2
- **Config:** `.markdownlint.json`
  - Disabled rules: MD013 (line length), MD033 (inline HTML), MD040 (fenced code language), MD029 (ordered list numbering), MD036 (emphasis as heading), MD001 (heading increment), MD025 (single H1), MD041 (first line heading)

**Linting (SQL):**

- **Linter:** SQLFluff (`.sqlfluff`)
  - Dialect: PostgreSQL
  - Keywords: UPPERCASE
  - Identifiers: lowercase
  - Functions/types: UPPERCASE
  - Indent: 2 spaces
  - `max_line_length = 200`
  - Explicit aliases required (`min_alias_length = 3`)

**Linting (YAML):**

- **Linter:** yamllint (`.yamllint.yml`)
  - `max_line_length: 200` (warning only)
  - `document-start: disable`
  - Allows `on` as truthy value (for GitHub Actions)

## Import Organization

**Python (agri-data-toolkit):**

- **Tool:** isort (profile: "black", `line_length = 100`, `multi_line_output = 3`, `include_trailing_comma = true`)
- **Order:**
  1. Standard library: `import os`, `from pathlib import Path`, `from typing import Any`
  2. Third-party: `import geopandas as gpd`, `import duckdb`, `from loguru import logger`
  3. Local: `from agri_toolkit.core.config import Config`, `from agri_toolkit.downloaders.base import BaseDownloader`

**Python (CrewAI):**

- **Tool:** Ruff with `I001` rule (isort-compatible)
- **Order:**
  1. Standard library: `import json`, `import os`, `import logging`
  2. Third-party: `import pytest`, `from crewai.tools import BaseTool`, `from pydantic import BaseModel`
  3. Local: `from tools.workspace_tool import WorkspaceTool`, `from tools.cost_tracker import get_tracker`

**TypeScript:**

- No import sorting tool enforced
- Observed pattern: type imports first, then external, then relative
- No path aliases configured

## Error Handling

**Python (agri-data-toolkit):**

- Raise `ValueError` for invalid arguments with descriptive `match`-friendly messages:
  ```python
  raise ValueError("count must be at least 1")
  raise ValueError(f"Invalid regions: {invalid_regions}. Valid options: {list(self.REGION_STATE_FIPS.keys())}")
  ```
- Raise `RuntimeError` for operational/download failures:
  ```python
  raise RuntimeError(f"Data download failed: {e}") from e
  ```
- Chain exceptions with `from e` when wrapping:
  ```python
  except Exception as e:
      self.logger.error("Failed to query Source Cooperative: %s", e)
      raise RuntimeError(f"Data download failed: {e}") from e
  ```
- Use `FileNotFoundError` for missing files/configs:
  ```python
  raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
  ```

**Python (CrewAI):**

- Return error strings from tool methods instead of raising:
  ```python
  return f"Error: Could not stringify JSON - {e}"
  ```
- Catch broad `Exception` in tool operations, log and return fallback:
  ```python
  except Exception as e:
      logger.error(f"❌ Error reading {filepath}: {e}")
      return ""
  ```
- Use `raise ValueError(...)` for truly invalid operations:
  ```python
  raise ValueError(f"Unknown operation: {operation}")
  ```

**TypeScript:**

- Return HTTP `Response` objects with status codes for errors:
  ```typescript
  return new Response('Unauthorized', { status: 401 });
  return new Response('Rate limit exceeded', { status: 429 });
  ```
- Top-level try/catch in worker entry point with `console.error` + 500 response:
  ```typescript
  } catch (error) {
    console.error('API error:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
  ```

## Logging

**Python (agri-data-toolkit):**

- **Framework:** Loguru (`from loguru import logger`)
- **Setup:** `packages/agri-data-toolkit/src/agri_toolkit/core/logger.py`
- **Pattern:** Module-level logger via `get_logger()`:
  ```python
  from agri_toolkit.core.logger import get_logger
  logger = get_logger()
  ```
- **Usage:** `logger.info(...)`, `logger.debug(...)`, `logger.error(...)`, `logger.warning(...)`
- **Format strings:** Use `%s` style (not f-strings) for Loguru:
  ```python
  self.logger.info("Starting field boundary download: %d fields from Source Cooperative", count)
  self.logger.error("Missing required columns: %s", missing_columns)
  ```

**Python (CrewAI):**

- **Framework:** stdlib `logging`
- **Pattern:** Module-level logger:
  ```python
  import logging
  logger = logging.getLogger(__name__)
  ```
- **Usage:** f-strings with emoji prefixes for visual scanning:
  ```python
  logger.info(f"📁 WorkspaceTool initialized: {self.workspace_dir}")
  logger.warning(f"⚠️ Large file truncated: {filepath}")
  logger.error(f"❌ Error writing to {filepath}: {e}")
  ```

**TypeScript:**

- **Framework:** `console` (with `eslint-disable-next-line no-console` annotation):
  ```typescript
  // eslint-disable-next-line no-console
  console.error('API error:', error);
  ```

## Comments

**When to Comment:**

- Module-level docstrings required on all Python files (one-line description minimum)
- Class docstrings required explaining purpose, usage patterns, and data sources
- Method docstrings in Google style with `Args:`, `Returns:`, `Raises:` sections
- Inline comments for non-obvious business logic (e.g., USDA data format quirks, DuckDB behavior)
- `# noqa: ARG002` for intentionally unused function parameters

**Docstring Style (Python):**

```python
def download(self, **kwargs: Any) -> gpd.GeoDataFrame:
    """Download field boundaries from Source Cooperative.

    This method queries the USDA Crop Sequence Boundaries dataset...

    Args:
        **kwargs: Keyword arguments:
            count (int): Number of fields to download (default: 200).
            regions (Optional[List[str]]): Regions to sample from.

    Returns:
        GeoDataFrame containing field boundaries with attributes:
            - field_id: Unique identifier
            - region: Region name

    Raises:
        ValueError: If count < 1, regions is empty, or invalid parameters.
        RuntimeError: If data download fails.

    Example:
        >>> downloader = FieldBoundaryDownloader()
        >>> fields = downloader.download(count=10, regions=['corn_belt'])
    """
```

**JSDoc (TypeScript):**

- File-level `/** */` block comments for workers:
  ```typescript
  /**
   * API Worker
   * Handles API endpoints for D1, R2, and user management
   */
  ```
- No per-function JSDoc observed; inline comments used instead

## Function Design

**Size:** Functions generally under 50 lines. Largest methods (~80 lines) are `_query_source_cooperative` and `download`, which perform multi-step data processing.

**Parameters (Python):**

- Use `**kwargs` with typed extraction for flexible API surface:
  ```python
  def download(self, **kwargs: Any) -> gpd.GeoDataFrame:
      count: int = kwargs.get("count", 200)
      regions: list[str] | None = kwargs.get("regions", None)
  ```
- Use `str | None = None` union syntax (Python 3.10+ style)
- Use `Path` objects for file paths, not strings

**Return Values (Python):**

- Return typed objects: `gpd.GeoDataFrame`, `Path`, `bool`, `dict`
- Use explicit type annotations on all public methods
- Return `""` or `{}` as empty fallbacks in tool methods (never `None` when string expected)

**Parameters (TypeScript):**

- Destructure request body with type assertion:
  ```typescript
  const { email } = (await request.json()) as { email: string };
  ```
- Pass `env: Env` typed bindings for Cloudflare Workers

## Module Design

**Exports (Python):**

- Use `__all__` in top-level `__init__.py` for explicit public API
- Single-line docstrings in subpackage `__init__.py` files:
  ```python
  """Data downloaders for various agricultural data sources."""
  ```
- Classes exported from their own module files (one class per file pattern)

**Exports (TypeScript):**

- `export default { fetch }` pattern for Cloudflare Workers
- Module-scoped async functions (not exported)

**Barrel Files:**

- Not used in Python (import directly from module path)
- Not used in TypeScript

## Commit Messages

**Tool:** commitlint with `@commitlint/config-conventional`
**Config:** `commitlint.config.js`
**Format:** `type(scope): description`

**Allowed types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`, `build`, `revert`

**Rules:**

- `scope-case`: kebab-case
- `subject-empty`: never (subject required)
- `subject-full-stop`: never ends with `.`
- `header-max-length`: 100 characters
- `body-leading-blank`: required
- `body-max-line-length`: unlimited (disabled)
- `footer-leading-blank`: required

## Type Checking

**Python (agri-data-toolkit):**

- **Tool:** mypy (strict mode)
- **Config:** `packages/agri-data-toolkit/pyproject.toml`
  - `python_version = "3.12"`
  - `warn_return_any = true`
  - `warn_unused_configs = true`
  - `disallow_untyped_defs = true`

**Python (CrewAI):**

- **Tool:** mypy (relaxed)
- **Config:** `.crewai/pyproject.toml`
  - `python_version = "3.10"`
  - `disallow_untyped_defs = false` (relaxed for CrewAI tool integration)

**TypeScript:**

- **Config:** `apps/startup-blueprint/tsconfig.json`
  - `strict: true`
  - `target: "ES2022"`, `module: "ES2022"`
  - Types: `@cloudflare/workers-types`

## Pre-commit Hooks

**Config:** `.pre-commit-config.yaml`
**Hooks (in order):**

1. Black (v24.10.0) — Python formatting
2. isort (v5.13.2) — Import sorting (`--profile black`)
3. Flake8 (v7.1.1) — Python linting (`--max-line-length=100`, `--extend-ignore=E203,W503`)
4. General checks (pre-commit-hooks v5.0.0):
   - `trailing-whitespace`
   - `end-of-file-fixer`
   - `check-yaml`
   - `check-added-large-files` (max 1000KB)
   - `check-merge-conflict`
   - `check-toml`

## Local CI

**Script:** `scripts/ci-local.sh`
**Phases:**

1. Format & Lint (Prettier, ESLint, Markdownlint, Stylelint, Ruff, Commitlint, TypeScript)
2. Tests & Builds (Link Check, CrewAI Tests, Website Build)
3. Deploy (optional, `--deploy` flag)
4. AI Code Review (optional, `--review` flag)

**Run before every commit:** `./scripts/ci-local.sh`
**Run with review:** `./scripts/ci-local.sh --review`
**Single step:** `./scripts/ci-local.sh --step test-crewai`

---

_Convention analysis: 2026-02-24_

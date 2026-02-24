# Testing Patterns

**Analysis Date:** 2026-02-24

## Test Framework

**Runner (Python — both workspaces):**

- pytest (v8.3.0+ for agri-data-toolkit, v8.0.0+ for crewai)
- Config: `[tool.pytest.ini_options]` in respective `pyproject.toml` files

**Runner (TypeScript — startup-blueprint):**

- Vitest (v1.2.0+) for unit tests
- Playwright (v1.40.0+) for E2E tests
- Config: `apps/startup-blueprint/package.json` (scripts only — no vitest/playwright config files found)
- **Note:** No TypeScript test files exist yet. Test infrastructure is declared but unused.

**Assertion Library:**

- Python: pytest built-in `assert` statements (no `unittest.TestCase`)
- Python: `pytest.raises` for exception testing with `match=` for message validation

**Run Commands:**

```bash
# agri-data-toolkit — all tests
cd packages/agri-data-toolkit && poetry run pytest tests/ -v

# agri-data-toolkit — unit tests only
cd packages/agri-data-toolkit && poetry run pytest tests/ -v -m unit

# agri-data-toolkit — integration tests only
cd packages/agri-data-toolkit && poetry run pytest tests/ -v -m integration

# agri-data-toolkit — persistent tests (CI/CD artifact generation)
cd packages/agri-data-toolkit && poetry run pytest tests/ -v -m persistent

# agri-data-toolkit — skip slow tests
cd packages/agri-data-toolkit && poetry run pytest tests/ -v -m "not slow"

# agri-data-toolkit — coverage
cd packages/agri-data-toolkit && poetry run pytest tests/ --cov=src/agri_toolkit --cov-report=html --cov-report=term

# crewai — all tests
pytest .crewai/tests/ -v --tb=short

# crewai — specific test file
pytest .crewai/tests/test_cost_tracker.py -v

# crewai — coverage
pytest .crewai/tests/ -v --cov=.crewai --cov-report=term-missing

# local CI (runs crewai tests as part of Phase 2)
./scripts/ci-local.sh --step test-crewai

# startup-blueprint (declared but no tests exist)
cd apps/startup-blueprint && pnpm test        # vitest
cd apps/startup-blueprint && pnpm test:e2e    # playwright
```

## Test File Organization

**Location:** Separate `tests/` directories (not co-located)

**agri-data-toolkit:**

```
packages/agri-data-toolkit/
├── src/agri_toolkit/          # Source code
│   ├── core/
│   ├── downloaders/
│   ├── exporters/
│   ├── processors/
│   └── utils/
└── tests/                     # All tests live here
    ├── __init__.py
    ├── conftest.py            # Shared fixtures (session-scoped)
    ├── data/                  # Test data fixtures (e.g., sample_field_boundaries.parquet)
    └── test_downloaders/      # Mirrors src module structure
        ├── __init__.py
        ├── test_field_boundaries.py           # Integration tests
        ├── test_field_boundaries_unit.py      # Unit tests (local fixtures)
        └── test_field_boundaries_persistent.py # CI/CD artifact generation
```

**CrewAI:**

```
.crewai/
├── tools/                     # Source code (tools, crews, utils)
├── crews/
├── utils/
└── tests/                     # All tests here
    ├── __init__.py
    ├── conftest.py            # Shared fixtures
    ├── test_workspace_tool.py
    ├── test_cost_tracker.py
    ├── test_github_tools.py
    ├── test_ci_output_parser_tool.py
    └── test_pr_metadata_tool.py
```

**Naming:**

- Test files: `test_<module_name>.py` or `test_<module_name>_<variant>.py`
- Test classes: `Test<ClassName>` or `Test<ClassName><Variant>`
- Test functions: `test_<behavior_description>`

## Test Structure

**Suite Organization (agri-data-toolkit):**

```python
# packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries_unit.py

class TestFieldBoundaryDownloaderUnit:
    """Unit tests for FieldBoundaryDownloader using local fixtures."""

    @pytest.fixture
    def downloader_with_sample_data(self, tmp_path, sample_field_boundaries_parquet):
        """Create downloader instance configured to use sample data."""
        config = Config()
        config._config["paths"]["raw"] = str(tmp_path / "raw")
        config._config["paths"]["processed"] = str(tmp_path / "processed")
        return FieldBoundaryDownloader(
            config=config, data_source_url=str(sample_field_boundaries_parquet)
        )

    @pytest.mark.unit
    def test_download_with_sample_data(self, downloader_with_sample_data):
        """Test downloading from sample data fixture."""
        fields = downloader_with_sample_data.download(count=5)
        assert len(fields) <= 5
        assert len(fields) > 0
        assert isinstance(fields, gpd.GeoDataFrame)
```

**Suite Organization (CrewAI):**

```python
# .crewai/tests/test_workspace_tool.py

# Test constants centralized at module top
TEST_FILENAME = "test.txt"
TEST_CONTENT = "Hello"
TEST_CONTENT_FULL = "Hello World"

class TestWorkspaceTool:
    """Test suite for WorkspaceTool."""

    def test_init_creates_workspace(self):
        """Test that workspace directory is created on init."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tool = WorkspaceTool(workspace_dir=tmpdir)
            assert tool is not None
            assert os.path.exists(tmpdir)

    def test_write_file(self):
        """Test writing a file to workspace."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tool = WorkspaceTool(workspace_dir=tmpdir)
            _result = tool._run(operation="write", filename=TEST_FILENAME, content=TEST_CONTENT)
            assert os.path.exists(os.path.join(tmpdir, TEST_FILENAME))
```

**Patterns:**

- **Setup:** Class-level or method-level `@pytest.fixture` (not `setUp`/`tearDown`)
- **Teardown:** Automatic via `tmp_path`, `tempfile.TemporaryDirectory`, or session-scoped `shutil.rmtree`
- **Assertion:** Plain `assert` with descriptive messages:
  ```python
  assert len(fields) == 2, f"Expected 2 fields, got {len(fields)}"
  assert col in fields.columns, f"Missing required column: {col}"
  ```
- **Exception testing:**
  ```python
  with pytest.raises(ValueError, match="count must be at least 1"):
      downloader.download(count=0)
  ```

## Test Categories (Markers)

**agri-data-toolkit markers** (defined in `packages/agri-data-toolkit/pyproject.toml`):

| Marker                     | Purpose                                              | When to Use                            |
| -------------------------- | ---------------------------------------------------- | -------------------------------------- |
| `@pytest.mark.unit`        | Unit tests using local fixtures                      | Tests that use sample data, no network |
| `@pytest.mark.integration` | Integration tests hitting live endpoints             | Tests that call Source Cooperative API |
| `@pytest.mark.slow`        | Tests that take longer than 5 seconds                | Large downloads, heavy processing      |
| `@pytest.mark.persistent`  | Tests generating persistent data for CI/CD artifacts | CI/CD visualization data               |

**Usage examples:**

```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Skip slow tests
pytest -m "not slow"

# Run persistent tests for CI artifact generation
pytest -m persistent
```

## Fixtures

**agri-data-toolkit shared fixtures** (`packages/agri-data-toolkit/tests/conftest.py`):

```python
@pytest.fixture(scope="session")
def test_data_dir():
    """Create a temporary directory for test data."""
    temp_dir = tempfile.mkdtemp(prefix="agri_toolkit_test_")
    yield Path(temp_dir)
    shutil.rmtree(temp_dir, ignore_errors=True)

@pytest.fixture(scope="function")
def clean_test_dir(tmp_path):
    """Provide a clean temporary directory for each test."""
    yield tmp_path

@pytest.fixture(scope="session")
def sample_field_boundaries_parquet():
    """Load sample field boundaries data for testing.
    Skips if sample data file not found.
    """
    sample_path = Path(__file__).parent / "data" / "sample_field_boundaries.parquet"
    if not sample_path.exists():
        pytest.skip("Sample data not found...")
    return sample_path

@pytest.fixture
def sample_field_boundaries_gdf(sample_field_boundaries_parquet):
    """Load sample field boundaries as GeoDataFrame."""
    return gpd.read_parquet(sample_field_boundaries_parquet)
```

**CrewAI shared fixtures** (`.crewai/tests/conftest.py`):

```python
@pytest.fixture
def temp_workspace():
    """Create a temporary workspace directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing."""
    env_vars = {
        "PR_NUMBER": "123",
        "COMMIT_SHA": "abc123def456",
        "GITHUB_REPOSITORY": "test-owner/test-repo",
        "CORE_CI_RESULT": "success",
        "GITHUB_TOKEN": "fake_token_12345",
        "OPENROUTER_API_KEY": "fake_openrouter_key",
    }
    with patch.dict(os.environ, env_vars, clear=False):
        yield env_vars

@pytest.fixture
def mock_github_api():
    """Mock GitHub API responses."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = { ... }
    with patch("requests.get", return_value=mock_response):
        yield mock_response

@pytest.fixture
def sample_diff():
    """Sample git diff output."""
    return { "sha": "abc123def456", "files": [...], "stats": {...} }

@pytest.fixture
def sample_commits():
    """Sample commit history."""
    return [{"sha": "abc123", "commit": {"message": "feat: add new feature", ...}}, ...]

@pytest.fixture
def sample_pr_metadata():
    """Sample PR metadata."""
    return {"commit_sha": "abc123def456", "repository": "test-owner/test-repo", ...}

@pytest.fixture
def sample_ci_output():
    """Sample CI output."""
    return {"status": "success", "jobs": [...]}
```

## Mocking

**Framework:** `unittest.mock` (stdlib) + `pytest-mock` (agri-data-toolkit)

**Patterns:**

**Environment variable mocking (CrewAI — most common pattern):**

```python
from unittest.mock import patch

def test_read_from_environment(self):
    """Test reading PR metadata from environment variables."""
    os.environ["PR_NUMBER"] = "123"
    os.environ["COMMIT_SHA"] = "abc123def456"
    os.environ["GITHUB_REPOSITORY"] = "test-owner/test-repo"
    tool = PRMetadataTool()
    result = tool._run()
    assert isinstance(result, dict)
```

**API response mocking (CrewAI):**

```python
from unittest.mock import Mock, patch

def test_fetch_labels_from_api(self):
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"labels": [{"name": "crewai:full-review"}]}
        mock_get.return_value = mock_response

        tool = PRMetadataTool()
        result = tool._run()
        assert "labels" in result
```

**Data source URL injection (agri-data-toolkit — preferred over mocking):**

```python
# Instead of mocking HTTP calls, inject a local file URL
downloader = FieldBoundaryDownloader(
    config=config,
    data_source_url=str(sample_field_boundaries_parquet)  # Local file instead of remote
)
```

**What to Mock:**

- External API calls (`requests.get`, GitHub API)
- Environment variables (`os.environ`)
- Time-sensitive operations

**What NOT to Mock:**

- Core business logic (test with real data via local fixtures)
- DuckDB query execution (use local parquet files instead)
- File I/O (use `tmp_path` / `tempfile.TemporaryDirectory` for real filesystem operations)
- GeoDataFrame operations (test with actual geometries)

## Fixtures and Factories

**Test Data (agri-data-toolkit):**

- Sample data stored as Parquet files in `packages/agri-data-toolkit/tests/data/`
- Generated via: `python scripts/generate_sample_field_boundaries.py`
- Session-scoped fixture loads once, shared across all tests
- Tests use `pytest.skip()` if sample data not available

**Test Data (CrewAI):**

- Inline test constants at module top:
  ```python
  TEST_FILENAME = "test.txt"
  TEST_CONTENT = "Hello"
  TEST_CONTENT_FULL = "Hello World"
  ```
- Fixture-based sample data (dicts) in `conftest.py` for diffs, commits, PR metadata
- No external data files — all test data is inline

**Location:**

- agri-data-toolkit fixtures: `packages/agri-data-toolkit/tests/conftest.py`
- agri-data-toolkit sample data: `packages/agri-data-toolkit/tests/data/`
- CrewAI fixtures: `.crewai/tests/conftest.py`
- CrewAI test constants: Inline in each test file

## Coverage

**Requirements:**

- agri-data-toolkit: Coverage reports generated but no minimum threshold enforced
- CrewAI: Coverage reports generated but no minimum threshold enforced

**Configuration:**

- agri-data-toolkit: `addopts = "-v --cov=src/agri_toolkit --cov-report=html --cov-report=term"`
- CrewAI (root): `addopts = "-v --cov=.crewai --cov-report=term-missing"`

**View Coverage:**

```bash
# agri-data-toolkit — HTML report
cd packages/agri-data-toolkit && poetry run pytest tests/ --cov=src/agri_toolkit --cov-report=html
# Opens: htmlcov/index.html

# agri-data-toolkit — terminal report
cd packages/agri-data-toolkit && poetry run pytest tests/ --cov=src/agri_toolkit --cov-report=term

# crewai — terminal report with missing lines
pytest .crewai/tests/ -v --cov=.crewai --cov-report=term-missing
```

## Test Types

**Unit Tests (agri-data-toolkit):**

- File: `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries_unit.py`
- Marked with `@pytest.mark.unit`
- Use local sample Parquet data via `data_source_url` injection
- Test: argument validation, data structure, CRS, geometry validity
- No network calls

**Integration Tests (agri-data-toolkit):**

- File: `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries.py`
- Marked with `@pytest.mark.integration` (only `test_download_real_data_structure`)
- Use local sample data for most tests (via `data_source_url` injection in fixture)
- One test (`test_download_real_data_structure`) hits live Source Cooperative API
- Download minimal data (2-5 fields) to minimize API load

**Persistent Tests (agri-data-toolkit):**

- File: `packages/agri-data-toolkit/tests/test_downloaders/test_field_boundaries_persistent.py`
- Marked with `@pytest.mark.persistent` + `@pytest.mark.integration`
- Write output to actual workspace paths (not `tmp_path`)
- Generate GeoJSON/Shapefile artifacts for CI/CD visualization workflows
- Print summary output for CI visibility

**Unit Tests (CrewAI):**

- Files: `.crewai/tests/test_*.py`
- No pytest markers used
- Test tool initialization, operation dispatch, data format
- Mock external dependencies (GitHub API, environment vars)
- Each test class covers one tool class

**E2E Tests:**

- **Declared** in `apps/startup-blueprint/package.json` (`@playwright/test`)
- **No test files exist** — infrastructure only

## Common Patterns

**Testing with temporary directories:**

```python
# agri-data-toolkit pattern: pytest tmp_path
def test_download_saves_to_file(self, downloader, tmp_path):
    downloader.download(count=2, regions=["corn_belt"], output_format="geojson")
    expected_path = tmp_path / "raw" / "field_boundaries" / "fields.geojson"
    assert expected_path.exists()

# CrewAI pattern: tempfile.TemporaryDirectory context manager
def test_write_file(self):
    with tempfile.TemporaryDirectory() as tmpdir:
        tool = WorkspaceTool(workspace_dir=tmpdir)
        _result = tool._run(operation="write", filename="test.txt", content="Hello")
        assert os.path.exists(os.path.join(tmpdir, "test.txt"))
```

**Testing error conditions:**

```python
# ValueError with match
with pytest.raises(ValueError, match="count must be at least 1"):
    downloader.download(count=0)

with pytest.raises(ValueError, match="Invalid regions"):
    downloader.download(count=2, regions=["invalid_region"])

# Generic exception
with pytest.raises(ValueError):
    tool._run(operation="invalid_op", filename="test.txt")
```

**Testing validation methods:**

```python
# Valid data passes
assert downloader.validate(fields) is True

# Empty data fails
empty_gdf = gpd.GeoDataFrame()
assert downloader.validate(empty_gdf) is False

# Missing columns fails
gdf = gpd.GeoDataFrame(
    {"field_id": ["TEST_001"], "geometry": [Polygon([(0,0),(1,0),(1,1),(0,1),(0,0)])]},
    crs="EPSG:4326",
)
assert downloader.validate(gdf) is False
```

**Testing singletons/reset patterns:**

```python
# CostTracker singleton
def test_singleton_instance(self):
    tracker1 = get_tracker()
    tracker2 = get_tracker()
    assert tracker1 is tracker2

def test_reset(self):
    reset_tracker()  # Start fresh
    tracker = get_tracker()
    tracker.log_api_call("gpt-4", 100, 50, 0.01, 1.0)
    reset_tracker()
    tracker = get_tracker()
    summary = tracker.get_summary()
    assert summary["total_calls"] == 0
```

**Unused return value convention:**

```python
# Prefix with underscore when return value intentionally not asserted
_result = tool._run(operation="write", filename=TEST_FILENAME, content=TEST_CONTENT)
# Note: _result intentionally unused, testing file creation only
```

**Data round-trip testing:**

```python
# Write then read back
downloader.download(count=2, regions=["corn_belt"], output_format="geojson")
expected_path = tmp_path / "raw" / "field_boundaries" / "fields.geojson"
loaded_fields = gpd.read_file(expected_path)
assert len(loaded_fields) == 2
```

## Test Philosophy

**agri-data-toolkit:**

- Download minimal data (2-5 fields) per test to minimize external API load
- Keep CI/CD execution under 2 minutes total
- Use local sample Parquet files for unit tests (no network dependency)
- Validate real data structure from actual Source Cooperative data
- Test both happy paths and error conditions with descriptive messages
- `pytest.skip()` when sample data not available (graceful degradation)

**CrewAI:**

- Test tool interfaces (initialization, operation dispatch, data format)
- Mock external services (GitHub API, environment variables)
- Centralize test constants at module top for maintenance
- Use `tempfile.TemporaryDirectory` for isolated filesystem tests
- Test error handling paths (missing env vars, API failures, invalid operations)

## CI Test Execution

**Local CI (`scripts/ci-local.sh`):**

- Phase 2 runs CrewAI tests: `pytest .crewai/tests/ -v --tb=short`
- Falls back to `python3 -m pytest` if `pytest` not on PATH
- Results tracked in step results table

**GitHub Actions:**

- agri-data-toolkit tests run via `poetry run pytest`
- CrewAI tests run via `pytest` or `python3 -m pytest`
- Test results reported in CI job summaries
- Persistent tests generate artifacts for visualization

---

_Testing analysis: 2026-02-24_

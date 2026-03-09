# Corn RM + Soybean MG by FIPS and geoadmin pipeline

## 🎯 TL;DR

> **Quick Summary**: Build a repo-native annual maturity-by-FIPS pipeline that adds shared geoadmin data, assigns fields to counties/FIPS, derives county-level weather and GDD outputs from existing field workflows, and publishes heuristic corn RM plus soybean MG products with static maps and explicit caveats.
>
> **Deliverables**:
>
> - Canonical `data/shared/geoadmin/` admin polygon and FIPS lookup artifacts
> - Canonical `data/shared/weather/...` county/FIPS weather transforms where needed for maturity calculations
> - Canonical `data/shared/corn_maturity/` and `data/shared/soybean_maturity/` annual outputs
> - Repo-native skills and `data/scripts/...` orchestration wired into existing manifest/path conventions
>
> **Estimated Effort**: Large
> **Parallel Execution**: YES - 4 waves
> **Critical Path**: canonical geoadmin -> field-to-FIPS mapping -> county weather/GDD -> corn RM + soybean MG -> annual orchestration + maps

---

## 📚 Context

### Original Request

Plan a county/FIPS maturity pipeline that fits this repository, integrates geoadmin data, calculates annual corn RM and soybean MG outputs, and works with the repo's existing skills system rather than a separate package architecture.

### Interview Summary

**Key discussions**:

- The pipeline should generally run once per year after it is working.
- Execution should commit and push often during implementation.
- Corn RM and soybean MG outputs should be heuristic agronomic planning layers, not recommendation-grade systems.
- The implementation must integrate with this repo's existing skills system, canonical script layout, shared data layout, and manifest/path conventions.

**Research findings**:

- Existing weather ingestion is field-centric in `data/scripts/ingest/download_weather.py`, so v1 county outputs should derive from field-level weather/GDD or shared transformed weather artifacts, not invent a fully separate weather source of truth.
- Existing canonical paths and reporting scaffolding live in `data/scripts/lib/paths.py` and `data/scripts/reporting_bootstrap.py`.
- Existing manifest/staleness patterns live in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py`.
- Existing reporting/map patterns live in `data/scripts/reporting/generate_ssurgo_maps.py`, `.opencode/skills/ssurgo-soil/src/ssurgo_workflows.py`, `data/scripts/reporting/generate_aggregate_poster.py`, and `data/scripts/reporting/generate_farm_html.py`.
- Natural Earth is appropriate for global admin layers, while US Census TIGER/Line is the authoritative public-domain source for US states and counties/FIPS.
- The `1 RM day ~= 22 GDD` rule is supported in extension literature only as a heuristic with caveats around seed-company baselines, planting-date compression, and regional variability.

### Metis Review

**Identified gaps** (addressed):

- The handoff's `src/skills/maturity_calc/...` structure is rejected in favor of repo-native `.opencode/skills/...` plus `data/scripts/...` integration.
- Trigger ambiguity resolved by defaulting v1 to manual annual invocation, not scheduling infrastructure.
- Output ambiguity resolved by defaulting v1 to canonical shared `parquet` tables plus rendered `png/html` maps.
- Partial failure ambiguity resolved by defaulting to explicit null/flagged county outputs and logged exceptions, not silent interpolation.
- Product ambiguity resolved in favor of explicitly caveated heuristic products for both corn RM and soybean MG.

---

## 🎯 Work Objectives

### Core Objective

Create a single, canonical annual maturity-by-FIPS workflow that integrates into this repo's skills system, adds reusable geoadmin datasets, maps fields to counties/FIPS with transparent heuristics, derives county-level weather/GDD inputs, computes heuristic corn RM and soybean MG outputs, and renders county-level reporting artifacts.

### Concrete Deliverables

- `data/shared/geoadmin/` country, state, county, and FIPS lookup artifacts pinned to source vintage
- `data/shared/weather/{source}/{year}/` county/FIPS transform artifacts needed by maturity calculations
- `data/shared/corn_maturity/` annual GDD-by-FIPS, RM-by-FIPS, band metadata, and caveat outputs
- `data/shared/soybean_maturity/` annual MG-by-FIPS, zoner metadata, and caveat outputs
- Versioned field-to-FIPS mapping plus ambiguity-report artifacts
- Repo-native skills under `.opencode/skills/` and annual orchestration scripts under `data/scripts/`
- Static county-level map outputs and optional HTML summary outputs following existing reporting conventions

### Definition of Done

- [ ] A fresh annual run can populate geoadmin data, field-to-FIPS mapping, county weather/GDD outputs, corn RM outputs, soybean MG outputs, and rendered maps using canonical paths only
- [ ] Re-running without source changes is idempotent and skips unchanged work via manifests
- [ ] Corn RM and soybean MG outputs are marked heuristic and include assumptions/caveats metadata
- [ ] Ambiguous or unsupported field/county assignments are surfaced explicitly, not silently hidden
- [ ] The implementation integrates into `.opencode/skills/...` and `data/scripts/...` instead of a parallel package layout

### Must Have

- Shared geoadmin data pinned to source vintage and stored canonically
- County/FIPS assignment logic with explicit ambiguity detection
- County weather/GDD transforms compatible with the existing weather data model
- Configurable heuristic corn RM conversion parameters
- Configurable heuristic soybean MG lookup or zoner parameters
- Frequent commit/push checkpoints during implementation

### Must NOT Have

- No recommendation-grade agronomic claims in v1
- No real-time or sub-annual refresh infrastructure in v1
- No direct county weather ingestion path as a new source of truth in v1
- No silent interpolation for counties with missing/insufficient field data
- No expansion to ZIP, tract, or broader geocoding systems
- No CrewAI-specific standalone package architecture that bypasses this repo's current skills system

---

## 🔍 Verification Strategy

> **ZERO HUMAN INTERVENTION** — all verification must be agent-executed.

### Test Decision

- **Infrastructure exists**: YES
- **Automated tests**: Tests-after
- **Framework**: `pytest`
- **Agent-executed QA**: Mandatory for spatial joins, annual batch outputs, and rendered maps

### QA Policy

Every task must include executable QA that validates data products, manifests, and rendered outputs. Evidence should be saved under `.sisyphus/evidence/` during execution.

- **Data pipeline**: Use Bash with `python` commands to generate outputs, inspect schemas, and confirm manifest freshness/skips
- **Geospatial outputs**: Use Bash with small verification scripts to assert CRS, FIPS keys, row counts, and ambiguity flags
- **Rendered reports**: Use Bash or `look_at` to confirm map/image generation and visible heuristic disclaimers

---

## ⚙️ Execution Strategy

### Parallel Execution Waves

```text
Wave 1 (repo-native foundation):
- Task 1 geoadmin source contract and canonical repo integration model
- Task 2 shared geoadmin downloader/standardizer skill + script wiring
- Task 3 shared path helpers, schemas, and manifest constants for maturity outputs

Wave 2 (county mapping + climate transforms):
- Task 4 field-to-FIPS assignment and ambiguity detection
- Task 5 county weather/FIPS transform layer under canonical shared weather paths
- Task 6 county GDD-by-FIPS computation layer

Wave 3 (crop maturity products):
- Task 7 corn RM heuristic config and annual outputs
- Task 8 soybean MG heuristic config and annual outputs
- Task 9 county choropleth/static map rendering for maturity outputs

Wave 4 (orchestration + validation):
- Task 10 annual orchestration entrypoint and step-manifest wiring
- Task 11 automated tests and fixture coverage
- Task 12 docs/tracking/operator guidance and commit cadence documentation

Wave FINAL:
- F1 plan compliance audit
- F2 code quality review
- F3 real QA replay
- F4 scope fidelity check
```

### Dependency Matrix

- **1**: none -> 2, 3, 12
- **2**: 1 -> 4, 9, 10
- **3**: 1 -> 4, 5, 6, 7, 8, 10, 11
- **4**: 2, 3 -> 5, 6, 7, 8, 10, 11
- **5**: 3, 4 -> 6, 7, 8, 9, 10, 11
- **6**: 3, 4, 5 -> 7, 8, 9, 10, 11
- **7**: 3, 4, 5, 6 -> 9, 10, 11
- **8**: 3, 4, 5, 6 -> 9, 10, 11
- **9**: 2, 5, 6, 7, 8 -> 10, 12
- **10**: 2, 3, 4, 5, 6, 7, 8, 9 -> 11, 12, FINAL
- **11**: 3, 4, 5, 6, 7, 8, 10 -> FINAL
- **12**: 1, 9, 10 -> FINAL

### Agent Dispatch Summary

- **1**: 3 tasks — T1 `writing`, T2 `quick`, T3 `quick`
- **2**: 3 tasks — T4 `unspecified-high`, T5 `quick`, T6 `quick`
- **3**: 3 tasks — T7 `deep`, T8 `deep`, T9 `visual-engineering`
- **4**: 3 tasks — T10 `unspecified-high`, T11 `deep`, T12 `writing`
- **FINAL**: 4 tasks — F1 `oracle`, F2 `unspecified-high`, F3 `unspecified-high`, F4 `deep`

---

## ✍️ TODOs

- [ ] 1. Define the repo-native maturity architecture contract

  **What to do**:
  - Define canonical locations for geoadmin, corn maturity, soybean maturity, and annual weather/FIPS transform artifacts under `data/shared/`
  - Define where new implementation belongs in `.opencode/skills/` and `data/scripts/`
  - Define step names, manifest ownership, and annual run entrypoints so the handoff cannot drift into a parallel package model

  **Must NOT do**:
  - Introduce `src/skills/maturity_calc` or any standalone architecture that bypasses repo-native skills conventions
  - Introduce scheduling infrastructure in v1

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: architecture contract and repo integration guidance are the main outputs
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `frontend-ui-ux`: no UI design work in this task

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 2, 3, 12
  - **Blocked By**: None

  **References**:
  - `data/scripts/lib/paths.py` - existing canonical path helper conventions to extend rather than replace
  - `data/scripts/reporting_bootstrap.py` - existing scaffold/bootstrap pattern for canonical data trees
  - `.opencode/skills/farm-intelligence-reporting/src/pipeline.py` - existing manifest and stale-step orchestration pattern
  - `docs/project/pr/pr-00000003-build-farm-intelligence-reporting.md` - current repo-native reporting architecture and conventions already documented in-project

  **Acceptance Criteria**:
  - [ ] Canonical target locations for geoadmin, corn maturity, soybean maturity, and transformed county weather outputs are specified in code/docs
  - [ ] New skills/scripts are placed in repo-native locations only

  **QA Scenarios**:

  ```text
  Scenario: Architecture contract points only to repo-native integration points
    Tool: Bash (python)
    Preconditions: Updated plan/code/docs exist
    Steps:
      1. Search for `src/skills/maturity_calc` and standalone package references in touched files
      2. Search for `.opencode/skills/` and `data/scripts/` references in the new maturity planning/implementation docs
      3. Assert only repo-native integration points remain
    Expected Result: No standalone package path remains; repo-native skill/script locations are referenced
    Evidence: .sisyphus/evidence/task-1-repo-native-contract.txt

  Scenario: Annual invocation is documented instead of scheduler infrastructure
    Tool: Bash (python)
    Preconditions: Updated docs/scripts available
    Steps:
      1. Inspect touched files for cron/scheduler/background service additions
      2. Verify annual manual invocation commands are present
    Expected Result: No scheduler dependency is introduced; annual invocation remains explicit
    Evidence: .sisyphus/evidence/task-1-annual-invocation.txt
  ```

  **Commit**: YES
  - Message: `docs(maturity): define repo-native annual pipeline contract`

- [ ] 2. Build shared geoadmin download and standardization integration

  **What to do**:
  - Add repo-native skill/script support for downloading or standardizing Natural Earth and TIGER/Line admin layers
  - Produce canonical `data/shared/geoadmin/` artifacts and FIPS lookup tables pinned to source vintage
  - Include metadata files recording source URLs, vintage, and licensing/public-domain assumptions

  **Must NOT do**:
  - Mix admin source files into grower/farm-specific directories
  - Fetch county boundaries from unofficial/non-authoritative sources when TIGER/Line is available

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: data-source wiring and canonical output scaffolding are implementation-heavy but localized
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 4, 9, 10
  - **Blocked By**: 1

  **References**:
  - `data/scripts/lib/paths.py` - extend with shared geoadmin path helpers
  - `data/scripts/migrate_legacy_data.py` - example of canonical data-migration discipline
  - `https://www.naturalearthdata.com/downloads/10m-cultural-vectors/` - authoritative global country source for Level 0 layers
  - `https://www2.census.gov/geo/tiger/` - authoritative annual TIGER/Line source for states/counties/FIPS

  **Acceptance Criteria**:
  - [ ] `data/shared/geoadmin/` contains version-pinned state/county lookup artifacts and metadata
  - [ ] County artifacts contain usable FIPS keys (`STATEFP`, `COUNTYFP`, `GEOID` or normalized equivalents)

  **QA Scenarios**:

  ```text
  Scenario: Geoadmin artifacts are created in canonical shared paths
    Tool: Bash (python)
    Preconditions: Geoadmin build step completed
    Steps:
      1. List files under `data/shared/geoadmin/`
      2. Assert expected county/state outputs and metadata files exist
      3. Open one county artifact and verify FIPS columns are present
    Expected Result: Canonical shared geoadmin outputs exist with FIPS columns and source metadata
    Evidence: .sisyphus/evidence/task-2-geoadmin-layout.txt

  Scenario: Source vintage is pinned and reproducible
    Tool: Bash (python)
    Preconditions: Metadata file exists
    Steps:
      1. Read geoadmin metadata
      2. Assert source URL, vintage year, and license/public-domain note are present
    Expected Result: Geoadmin source provenance is explicit
    Evidence: .sisyphus/evidence/task-2-geoadmin-metadata.txt
  ```

  **Commit**: YES
  - Message: `feat(geoadmin): add canonical admin boundary assets`

- [ ] 3. Extend path helpers, schemas, and manifest constants for maturity outputs

  **What to do**:
  - Add canonical helpers for `data/shared/geoadmin/`, `data/shared/corn_maturity/`, `data/shared/soybean_maturity/`, and any county/FIPS weather transform outputs
  - Define or document schema expectations for field-FIPS mapping, county GDD, corn RM, and soybean MG artifacts
  - Add manifest step constants for annual geoadmin, mapping, transform, maturity, and reporting stages

  **Must NOT do**:
  - Hardcode ad hoc output paths inside multiple scripts
  - Leave maturity artifact naming inconsistent across crops

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: highly localized path/schema/manifest extension work
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: 4, 5, 6, 7, 8, 10, 11
  - **Blocked By**: 1

  **References**:
  - `data/scripts/lib/paths.py` - core canonical path helper source of truth
  - `.opencode/skills/farm-intelligence-reporting/src/pipeline.py` - step manifest and stale-checking conventions
  - `data/reporting/manifests/` - existing manifest outputs to mirror semantically

  **Acceptance Criteria**:
  - [ ] Maturity/geoadmin outputs can be addressed through helpers instead of raw path literals
  - [ ] Manifest step names exist for every annual stage

  **QA Scenarios**:

  ```text
  Scenario: Path helpers resolve all maturity output roots
    Tool: Bash (python)
    Preconditions: Helper functions added
    Steps:
      1. Run a small Python probe importing the helper module
      2. Print resolved geoadmin, corn maturity, soybean maturity, and county weather transform paths
      3. Assert all resolve under `data/shared/`
    Expected Result: All maturity/geoadmin roots resolve canonically
    Evidence: .sisyphus/evidence/task-3-path-helpers.txt

  Scenario: Manifest constants cover annual maturity stages
    Tool: Bash (python)
    Preconditions: Manifest constants defined
    Steps:
      1. Import manifest constants
      2. Assert constants exist for geoadmin, field-fips mapping, county weather transform, GDD, corn RM, soybean MG, and map rendering
    Expected Result: Annual maturity stages are fully addressable by manifest name
    Evidence: .sisyphus/evidence/task-3-manifest-constants.txt
  ```

  **Commit**: YES
  - Message: `refactor(maturity): add canonical paths and manifest constants`

- [ ] 4. Implement field-to-FIPS assignment and ambiguity detection

  **What to do**:
  - Build field centroid or equivalent default assignment against county polygons
  - Emit a versioned field-to-FIPS mapping artifact and a separate ambiguity report for fields near or across county boundaries
  - Persist enough metadata to invalidate downstream county outputs if assignment logic changes

  **Must NOT do**:
  - Silently assign multi-county fields without surfacing ambiguity
  - Run repeated spatial joins at query time instead of persisting a reusable mapping artifact

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: geospatial join logic and ambiguity handling are the highest-risk data-bridge task
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 5, 6, 7, 8, 10, 11
  - **Blocked By**: 2, 3

  **References**:
  - `data/scripts/ingest/download_weather.py` - existing centroid extraction pattern used in current field-centric weather ingestion
  - `data/scripts/reporting/generate_farm_html.py` - current centroid/projection handling patterns
  - `data/growers/iowa-demo-grower/farms/iowa-demo-farm/boundary/field_boundaries.geojson` - example field boundary dataset shape
  - `https://www2.census.gov/geo/tiger/` - authoritative county geometry source used for FIPS assignment

  **Acceptance Criteria**:
  - [ ] A reusable field-to-FIPS mapping artifact is generated
  - [ ] Ambiguous assignments are emitted to a separate report with enough detail to inspect edge cases

  **QA Scenarios**:

  ```text
  Scenario: Field-to-FIPS mapping is generated for known demo fields
    Tool: Bash (python)
    Preconditions: Assignment step completed
    Steps:
      1. Run the mapping script for demo fields
      2. Load the output artifact
      3. Assert each field has a county GEOID/FIPS or an explicit flagged status
    Expected Result: Every field is either mapped or explicitly flagged
    Evidence: .sisyphus/evidence/task-4-field-fips-mapping.txt

  Scenario: Ambiguity report captures boundary edge cases
    Tool: Bash (python)
    Preconditions: Ambiguity report generated
    Steps:
      1. Read the ambiguity artifact
      2. Assert required columns exist (field id, assigned FIPS, ambiguity reason, confidence/flag columns)
    Expected Result: Ambiguous county assignments are inspectable and explicit
    Evidence: .sisyphus/evidence/task-4-ambiguity-report.txt
  ```

  **Commit**: YES
  - Message: `feat(maturity): add field to county fips mapping`

- [ ] 5. Build county weather/FIPS transform artifacts under canonical shared weather paths

  **What to do**:
  - Transform existing weather data into annual county/FIPS-aligned weather tables under `data/shared/weather/{source}/{year}/`
  - Make the transform explicitly downstream of persisted field-to-FIPS mapping
  - Preserve source-year provenance and null handling for counties with missing field coverage

  **Must NOT do**:
  - Replace the existing field-level weather source of truth
  - Invent synthetic county weather for counties with zero field coverage

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: deterministic transform work once mapping is established
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 6, 7, 8, 9, 10, 11
  - **Blocked By**: 3, 4

  **References**:
  - `data/scripts/ingest/download_weather.py` - source schema and weather parameter set
  - `data/scripts/lib/paths.py` - canonical weather path conventions to extend
  - `tests/farm_intelligence/test_pipeline.py` - existing pipeline verification style to mimic

  **Acceptance Criteria**:
  - [ ] County/FIPS weather artifacts are generated under canonical shared weather paths
  - [ ] Counties with no field coverage are represented explicitly as null/absent, not interpolated

  **QA Scenarios**:

  ```text
  Scenario: County weather transforms land in canonical shared weather paths
    Tool: Bash (python)
    Preconditions: Weather transform step completed
    Steps:
      1. Run the transform for one source/year
      2. List outputs under `data/shared/weather/`
      3. Assert county/FIPS keyed artifacts exist and contain year/source columns
    Expected Result: Shared weather outputs are canonical and source/year keyed
    Evidence: .sisyphus/evidence/task-5-county-weather-layout.txt

  Scenario: No-coverage counties are not fabricated
    Tool: Bash (python)
    Preconditions: County weather artifact exists
    Steps:
      1. Inspect artifact rows for counties without mapped fields
      2. Assert they are null/flagged/absent according to the documented rule
    Expected Result: No synthetic county weather is introduced
    Evidence: .sisyphus/evidence/task-5-null-county-policy.txt
  ```

  **Commit**: YES
  - Message: `feat(weather): add county fips transform outputs`

- [ ] 6. Compute county GDD-by-FIPS annual outputs

  **What to do**:
  - Implement annual GDD derivation from county weather transforms using documented corn-relevant base/ceiling assumptions
  - Emit annual GDD-by-FIPS tables with provenance and configuration metadata
  - Keep the computation separate from RM and MG logic so maturity heuristics remain modular

  **Must NOT do**:
  - Hardcode crop maturity assumptions into generic weather transforms
  - Hide source-year or parameter provenance

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: deterministic numeric transformation with clear inputs/outputs
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: 7, 8, 9, 10, 11
  - **Blocked By**: 3, 4, 5

  **References**:
  - `.opencode/skills/nasa-power-weather/src/weather_reporting.py` - existing GDD/weather-summary logic to align with where appropriate
  - `https://ohioline.osu.edu/factsheet/agf-101` - standard 86/50 GDD method reference for corn planning assumptions
  - `https://www.agry.purdue.edu/ext/corn/news/timeless/hybridmaturity.html` - Purdue maturity/GDD context for corn RM heuristic documentation

  **Acceptance Criteria**:
  - [ ] Annual GDD-by-FIPS output exists with parameter metadata
  - [ ] GDD logic is isolated from downstream RM/MG layers

  **QA Scenarios**:

  ```text
  Scenario: Annual GDD-by-FIPS output is generated with provenance
    Tool: Bash (python)
    Preconditions: GDD computation step completed
    Steps:
      1. Run the GDD step for one year
      2. Inspect the output schema
      3. Assert FIPS, year, GDD totals, and parameter metadata columns exist
    Expected Result: Annual GDD output is complete and self-describing
    Evidence: .sisyphus/evidence/task-6-gdd-output.txt

  Scenario: GDD step is modular and independent of RM/MG outputs
    Tool: Bash (python)
    Preconditions: GDD step and downstream steps exist
    Steps:
      1. Run only the GDD step
      2. Assert GDD outputs are created without requiring RM or MG generation
    Expected Result: GDD is a standalone reusable annual artifact
    Evidence: .sisyphus/evidence/task-6-gdd-modularity.txt
  ```

  **Commit**: YES
  - Message: `feat(maturity): add annual gdd by fips outputs`

- [ ] 7. Add heuristic corn RM conversion outputs

  **What to do**:
  - Implement configurable corn RM conversion from GDD-by-FIPS outputs
  - Emit RM-by-FIPS tables, bands, metadata, and caveat text under `data/shared/corn_maturity/`
  - Document the specific heuristic assumptions used, including the status of the `22 GDD per RM day` rule

  **Must NOT do**:
  - Present RM outputs as recommendation-grade hybrid guidance
  - Assume cross-company comparability without caveats

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: agronomy heuristics and caveat encoding are the main complexity here
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3
  - **Blocks**: 9, 10, 11
  - **Blocked By**: 3, 4, 5, 6

  **References**:
  - `https://www.agry.purdue.edu/ext/corn/news/timeless/hybridmaturity.html` - Purdue reference for RM-to-GDD heuristic framing
  - `https://extension.umn.edu/corn-hybrid-selection/selecting-corn-hybrids-grain-production` - northern Corn Belt caveats and maturity context
  - `data/shared/corn_maturity/` - canonical target root for annual RM outputs

  **Acceptance Criteria**:
  - [ ] Annual RM-by-FIPS outputs exist under canonical corn maturity paths
  - [ ] Output metadata explicitly marks RM as heuristic and records parameter assumptions

  **QA Scenarios**:

  ```text
  Scenario: Corn RM outputs are produced with heuristic caveats
    Tool: Bash (python)
    Preconditions: Corn RM step completed
    Steps:
      1. Inspect the annual RM artifact and metadata
      2. Assert FIPS, year, RM or RM band columns, and caveat fields exist
    Expected Result: Corn RM outputs are present and explicitly caveated
    Evidence: .sisyphus/evidence/task-7-corn-rm-output.txt

  Scenario: Corn RM output does not claim recommendation-grade certainty
    Tool: Bash (python)
    Preconditions: Output metadata and any rendered labels exist
    Steps:
      1. Search output metadata/render labels for certainty or recommendation language
      2. Assert heuristic/disclaimer language is present instead
    Expected Result: Corn RM remains a planning heuristic product
    Evidence: .sisyphus/evidence/task-7-corn-rm-caveat.txt
  ```

  **Commit**: YES
  - Message: `feat(corn-maturity): add heuristic rm by fips outputs`

- [ ] 8. Add heuristic soybean MG outputs

  **What to do**:
  - Implement configurable soybean MG derivation compatible with county/FIPS outputs and repo-native paths
  - Emit MG-by-FIPS tables, bands or zone ranges, metadata, and caveat text under `data/shared/soybean_maturity/`
  - Keep soybean logic separate from corn RM logic while sharing common FIPS/geoadmin/weather inputs where appropriate

  **Must NOT do**:
  - Force soybean MG into corn RM formulas or directory structures
  - Present soybean MG as a recommendation-grade planting prescription

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: soybean maturity logic is related but distinct and needs its own heuristic boundary definitions
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3
  - **Blocks**: 9, 10, 11
  - **Blocked By**: 3, 4, 5, 6

  **References**:
  - `data/shared/soybean_maturity/` - canonical target root for annual soybean outputs
  - `https://www.no-tillfarmer.com/articles/6198-delineating-optimal-soybean-maturity-groups-across-the-us` - planning reference for MG zoning context
  - `https://www.canr.msu.edu/news/what_is_the_relationship_between_soybean_maturity_group_and_yield` - planning context for soybean MG/yield caveats

  **Acceptance Criteria**:
  - [ ] Annual MG-by-FIPS outputs exist under canonical soybean maturity paths
  - [ ] Soybean outputs explicitly record lookup/zoner assumptions and caveat text

  **QA Scenarios**:

  ```text
  Scenario: Soybean MG outputs are produced with metadata
    Tool: Bash (python)
    Preconditions: Soybean MG step completed
    Steps:
      1. Inspect the annual MG artifact and metadata
      2. Assert FIPS, year, MG range/zone columns, and caveat fields exist
    Expected Result: Soybean MG outputs are complete and self-describing
    Evidence: .sisyphus/evidence/task-8-soybean-mg-output.txt

  Scenario: Soybean MG logic is separated from corn RM outputs
    Tool: Bash (python)
    Preconditions: Both crop outputs exist
    Steps:
      1. Verify soybean outputs land under `data/shared/soybean_maturity/`
      2. Verify corn outputs land under `data/shared/corn_maturity/`
    Expected Result: Crop-specific products stay separated while sharing upstream inputs
    Evidence: .sisyphus/evidence/task-8-crop-separation.txt
  ```

  **Commit**: YES
  - Message: `feat(soybean-maturity): add heuristic mg by fips outputs`

- [ ] 9. Render county-level maturity maps and static report assets

  **What to do**:
  - Reuse existing choropleth/reporting patterns to render static county maps for corn RM and soybean MG outputs
  - Produce canonical rendered assets and optional HTML summaries with visible heuristic caveats
  - Keep map generation downstream of the canonical annual maturity tables

  **Must NOT do**:
  - Make interactive-map infrastructure a prerequisite for v1
  - Hide caveats or source-vintage details from rendered outputs

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
    - Reason: output rendering and map readability are the main task concerns
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3
  - **Blocks**: 10, 12
  - **Blocked By**: 2, 5, 6, 7, 8

  **References**:
  - `data/scripts/reporting/generate_ssurgo_maps.py` - closest static choropleth rendering pattern already in repo
  - `.opencode/skills/ssurgo-soil/src/ssurgo_workflows.py` - reusable choropleth/basemap helper patterns
  - `data/scripts/reporting/generate_farm_html.py` - self-contained HTML output pattern with embedded images

  **Acceptance Criteria**:
  - [ ] Corn RM and soybean MG county map assets are rendered from canonical outputs
  - [ ] Rendered assets include visible heuristic/source caveats

  **QA Scenarios**:

  ```text
  Scenario: County maturity map assets are rendered for both crops
    Tool: Bash (python)
    Preconditions: Rendering step completed
    Steps:
      1. Run maturity map rendering
      2. Assert corn RM and soybean MG map files exist
      3. Verify output filenames and directories are canonical
    Expected Result: Static map outputs exist for both crop maturity products
    Evidence: .sisyphus/evidence/task-9-map-assets.txt

  Scenario: Rendered assets show heuristic caveats
    Tool: look_at
    Preconditions: At least one rendered PNG or HTML exists
    Steps:
      1. Inspect one corn RM render and one soybean MG render
      2. Confirm caveat/source-vintage text is visible
    Expected Result: Rendered outputs do not hide heuristic framing
    Evidence: .sisyphus/evidence/task-9-map-caveats.txt
  ```

  **Commit**: YES
  - Message: `feat(reporting): render county maturity maps`

- [ ] 10. Wire annual orchestration into repo-native scripts and skills

  **What to do**:
  - Add an annual entrypoint under `data/scripts/` that orchestrates geoadmin, mapping, transform, GDD, crop maturity, and map-render steps
  - Wire the flow into repo-native skills where appropriate instead of a separate package runtime
  - Use manifest tracking to support annual idempotent reruns and partial-step freshness decisions

  **Must NOT do**:
  - Hide orchestration inside undocumented ad hoc commands
  - Make county outputs dependent on manual file copying between steps

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: orchestrating multiple repo-native stages and manifests is the key integration task
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4
  - **Blocks**: 11, 12, FINAL
  - **Blocked By**: 2, 3, 4, 5, 6, 7, 8, 9

  **References**:
  - `data/scripts/run_farm_pipeline.py` - existing multi-step pipeline orchestration pattern
  - `.opencode/skills/farm-intelligence-reporting/src/pipeline.py` - manifest staleness and step registration model
  - `data/growers/iowa-demo-grower/manifests/pipeline_schedule.json` - example manifest scheduling/state artifact already used in repo

  **Acceptance Criteria**:
  - [ ] A single annual maturity entrypoint can run the full maturity-by-FIPS workflow
  - [ ] Re-running without changes skips unchanged steps via manifests

  **QA Scenarios**:

  ```text
  Scenario: Annual maturity pipeline runs end-to-end
    Tool: Bash
    Preconditions: All upstream tasks completed
    Steps:
      1. Run `python data/scripts/run_maturity_by_fips.py --year 2025`
      2. Assert geoadmin, mapping, transform, GDD, corn RM, soybean MG, and map steps complete
    Expected Result: Full annual pipeline completes successfully
    Evidence: .sisyphus/evidence/task-10-annual-run.txt

  Scenario: Annual maturity pipeline is idempotent
    Tool: Bash
    Preconditions: First full run completed
    Steps:
      1. Run the same command again
      2. Assert manifest-aware skip/current behavior is reported for unchanged steps
    Expected Result: Unchanged steps are skipped without recomputation
    Evidence: .sisyphus/evidence/task-10-idempotent-rerun.txt
  ```

  **Commit**: YES
  - Message: `feat(pipeline): add annual maturity by fips orchestrator`

- [ ] 11. Add automated tests and fixture coverage for maturity-by-FIPS logic

  **What to do**:
  - Add targeted tests for path helpers, field-to-FIPS mapping, ambiguity detection, county weather transforms, GDD calculation, corn RM outputs, and soybean MG outputs
  - Add fixture data or small deterministic samples so annual maturity logic is testable without a full national run
  - Keep tests aligned with the existing `pytest`-based farm intelligence suite

  **Must NOT do**:
  - Depend entirely on manual map inspection
  - Require national-scale data downloads to run the test suite

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: coverage must validate geospatial/data assumptions without brittle integration tests only
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4
  - **Blocks**: FINAL
  - **Blocked By**: 3, 4, 5, 6, 7, 8, 10

  **References**:
  - `tests/farm_intelligence/test_pipeline.py` - existing test style and fixture expectations in repo
  - `data/scripts/run_farm_pipeline.py` - current integration surface worth testing analogously

  **Acceptance Criteria**:
  - [ ] `pytest` coverage exists for core maturity-by-FIPS logic
  - [ ] Tests can run from deterministic fixtures without national-scale downloads

  **QA Scenarios**:

  ```text
  Scenario: Maturity test suite passes
    Tool: Bash
    Preconditions: Tests added
    Steps:
      1. Run `python -m pytest tests/farm_intelligence/test_pipeline.py`
      2. Run any new maturity-focused test module(s)
    Expected Result: Existing and new targeted tests pass
    Evidence: .sisyphus/evidence/task-11-pytest.txt

  Scenario: Fixture-backed tests do not require full geoadmin downloads
    Tool: Bash
    Preconditions: Tests and fixtures exist
    Steps:
      1. Run the targeted maturity tests in a clean environment
      2. Assert tests use local fixtures and complete without national download steps
    Expected Result: Test suite remains fast and deterministic
    Evidence: .sisyphus/evidence/task-11-fixtures.txt
  ```

  **Commit**: YES
  - Message: `test(maturity): cover county fips pipeline logic`

- [ ] 12. Update tracking docs and operator guidance for annual maturity runs

  **What to do**:
  - Update PR/issue/kanban records as the work progresses
  - Add operator guidance for annual invocation, commit/push cadence, source vintage expectations, and heuristic caveats
  - Document repo-native integration points so future contributors do not recreate the rejected standalone package layout

  **Must NOT do**:
  - Leave annual run semantics implicit
  - Document maturity outputs as recommendation-grade guidance

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: documentation and operator guidance are the main outputs
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4
  - **Blocks**: FINAL
  - **Blocked By**: 1, 9, 10

  **References**:
  - `docs/project/pr/pr-00000003-build-farm-intelligence-reporting.md` - current source-of-truth tracking format
  - `docs/project/issues/issue-00000006-build-farm-intelligence-reporting.md` - issue tracking conventions in repo
  - `docs/project/kanban/project-farm-intelligence-reporting.md` - kanban/source-of-truth workflow expectations
  - `AGENTS.md` - repo requirements for PR/issue/kanban updates and local CI expectations

  **Acceptance Criteria**:
  - [ ] PR/issue/kanban documents reflect the maturity pipeline work and annual operating model
  - [ ] Operator guidance explicitly describes annual invocation, heuristic caveats, and frequent commit/push expectations

  **QA Scenarios**:

  ```text
  Scenario: Tracking docs are updated consistently
    Tool: Bash (python)
    Preconditions: Docs updated
    Steps:
      1. Read the PR, issue, and kanban files
      2. Assert all mention annual maturity-by-FIPS scope and current status
    Expected Result: Repo source-of-truth records are aligned
    Evidence: .sisyphus/evidence/task-12-tracking-docs.txt

  Scenario: Operator guidance includes caveats and annual invocation
    Tool: Bash (python)
    Preconditions: Guidance doc exists
    Steps:
      1. Search updated docs for `heuristic`, `annual`, and `commit` guidance
      2. Assert all are present
    Expected Result: Operator guidance is explicit and complete
    Evidence: .sisyphus/evidence/task-12-operator-guidance.txt
  ```

  **Commit**: YES
  - Message: `docs(maturity): add annual run guidance and tracking`

---

## 📋 Final Verification Wave

- [ ] F1. **Plan Compliance Audit** — `oracle`
      Read the plan end-to-end. Verify canonical outputs exist under `data/shared/geoadmin/`, `data/shared/weather/...`, `data/shared/corn_maturity/`, and `data/shared/soybean_maturity/`; verify repo-native integration exists under `.opencode/skills/` and `data/scripts/`; reject any drift into standalone package structure or recommendation-grade language.

- [ ] F2. **Code Quality Review** — `unspecified-high`
      Run relevant lint/tests for touched files. Confirm no silent interpolation, no ad hoc path literals bypassing helpers, and no scheduler infrastructure slipped into v1.

- [ ] F3. **Real QA Replay** — `unspecified-high`
      Execute the annual maturity flow from clean state, then rerun it to confirm manifest-aware skip behavior, county null handling, crop output separation, and rendered maturity asset generation.

- [ ] F4. **Scope Fidelity Check** — `deep`
      Compare actual implementation against this plan. Reject any drift into recommendation-grade outputs, direct county weather source replacement, ZIP/tract geoadmin expansion, or non-repo-native skill architecture.

---

## 📦 Commit Strategy

- Commit after each Wave 1 task to lock architecture, geoadmin, and path/schema foundations early
- Commit after each Wave 2 task to keep mapping and climate transforms auditable
- Commit separately for corn RM, soybean MG, and map/report rendering in Wave 3
- Push after each green checkpoint to satisfy the requested frequent sync cadence
- Use scoped conventional commits with multi-line bodies describing why, key files, and behavior changes

---

## ✅ Success Criteria

### Verification Commands

```bash
python -m pytest tests/farm_intelligence/test_pipeline.py
# Expected: existing suite passes and new maturity/geoadmin tests pass

python data/scripts/run_maturity_by_fips.py --year 2025
# Expected: canonical geoadmin, mapping, county weather/GDD, corn RM, soybean MG, and map outputs created

python data/scripts/run_maturity_by_fips.py --year 2025
# Expected: manifest-aware skip behavior for unchanged steps
```

### Final Checklist

- [ ] Shared geoadmin data is present and version-pinned
- [ ] Field-to-FIPS mapping exists with ambiguity flags
- [ ] County weather/GDD outputs exist in canonical shared paths
- [ ] Corn RM outputs exist in `data/shared/corn_maturity/` with heuristic caveats and metadata
- [ ] Soybean MG outputs exist in `data/shared/soybean_maturity/` with heuristic caveats and metadata
- [ ] Annual rerun is idempotent
- [ ] Implementation integrates with `.opencode/skills/` and `data/scripts/` rather than a parallel package layout
- [ ] Frequent commit/push checkpoints are defined and followed during execution

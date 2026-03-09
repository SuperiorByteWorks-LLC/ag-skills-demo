# Work Plan: Cached field cards and NDVI reporting refresh

_Planning record for upgrading field reporting so expensive SSURGO and NDVI assets are cached and cheap poster/HTML/Markdown assembly can rerun independently._

---

## 📋 TL;DR

> **Quick summary**: Repair the reporting pipeline so canonical `data/growers/...` outputs become the only active source of truth, raw seasonal satellite TIFFs are preserved first, and NDVI reporting shifts from single best-scene yearly snapshots to crop-conditioned seasonal rollups.
>
> **Deliverables**:
>
> - Canonical-only grower/farm/field report outputs and logs with no active `data/EDA` dependency
> - Raw clipped Sentinel-2 and Landsat TIFF inventories across each growing season
> - Yearly NDVI composites grouped into reusable `corn`, `soybean`, and current-season cumulative cards
> - SSURGO, CDL, poster, HTML, and Markdown steps aligned to the same cache/rebuild contract
> - Incremental dependency-based rebuilds plus explicit full refresh
>
> **Estimated effort**: Large
> **Parallel execution**: YES - 4 implementation waves plus final verification
> **Critical path**: canonical path contract -> seasonal scene inventory -> yearly crop-conditioned NDVI composites -> canonical report assembly -> refresh orchestration -> final verification

---

## 📚 Context

### Original request

The user wants field reporting to stop recomputing expensive products on every run. SSURGO cards and satellite NDVI cards should be reusable assets. Final poster, HTML, and Markdown assembly should be cheap. The field report should replace the current CDL composition slot with stronger NDVI content and a text-based crop rotation forecast.

### Interview summary

**Confirmed requirements**:

- Add Sentinel-2 and Landsat NDVI imagery/products into field reporting
- Download and retain raw clipped TIFFs first, across each growing season for each target year
- Remove the CDL crop composition by year card from field cards
- Keep crop rotation information in the first card and add heuristic predictions for next year and the following year
- Replace best-scene-only NDVI with growing-season/yearly rollups and crop-conditioned output cards
- Place NDVI under the GDD card where the cropland card currently sits, using the right-side image slots
- Use reusable card-sized PNG assets for expensive outputs
- Rebuild expensive cards only when source manifests or card specs change, unless a user explicitly requests a full refresh
- Target 5 years of cropland, weather, and NDVI history where imagery/data are available
- Fix structure drift so canonical `data/growers/...` is the active reporting root
- Move manifests/logs closer to canonical grower/farm/field outputs instead of `data/reporting/manifests/`
- Treat `shared/cdl/rasters/` as canonical for moved CDL TIFFs and align the remaining CDL/reporting steps around that tree
- Fix remaining path drift so active reporting no longer depends on legacy `data/EDA/` or old `data/cdl/` paths

**Defaults applied**:

- Use a rolling 5-year window by default
- Prefer Sentinel-2 over Landsat when both qualify for the same seasonal slot, while still allowing Landsat to fill gaps in the 5-year history
- Use a simple rotation heuristic for the two-year crop forecast rather than a formal predictive model
- Store reusable card assets inside canonical per-field derived outputs so assembly can consume them directly
- Use three final NDVI field slots by default: `corn average NDVI`, `soybean average NDVI`, and `current-season cumulative NDVI`; if a crop class is absent, render a clear unavailable-state asset instead of reviving the old best-scene layout
- Treat `data/EDA/` as legacy only and remove it from active orchestration rather than maintaining an ongoing mirror

### Research findings

- Existing manifest/stale-check logic already lives in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py`, but active reporting scripts still point to `data/reporting/manifests/`
- Existing canonical path helpers already live in `data/scripts/lib/paths.py`, but reporting scripts do not use them consistently
- `data/scripts/run_farm_pipeline.py` currently syncs from legacy `data/EDA/...` outputs back into `data/growers/...`, which preserves structure drift instead of eliminating it
- `data/scripts/ingest/download_satellite_imagery.py` currently downloads one best scene per year via `search_best_feature(...)`; this must expand to dense within-season scene inventories
- `data/scripts/reporting/generate_ndvi_cards.py` currently builds `ndvi_multi_year`, `ndvi_recent`, and `ndvi_accumulated` assets from available NDVI TIFFs, but it does not build yearly seasonal composites or crop-conditioned rollups
- `data/scripts/ingest/download_cdl.py` and current report builders still depend on old `data/cdl/...` paths even though the CDL TIFFs were manually moved to `shared/cdl/rasters/`
- Existing reporting/panel patterns live in `.opencode/skills/farm-intelligence-reporting/src/reporting.py`
- Existing Sentinel-2 NDVI helper/reporting code lives in `.opencode/skills/sentinel2-imagery/src/sentinel_reporting.py`
- Existing Landsat NDVI helper/reporting code lives in `.opencode/skills/landsat-imagery/src/landsat_reporting.py`
- Existing SSURGO card skill exists in `.opencode/skills/ssurgo-poster-cards/`
- User-provided visual/process references live outside this repo:
  - `/home/clay/dev/agri-data-toolkit-worktrees/class-7/docs/classes/examples/class7-satellite-and-drone-intelligence/07-complete-workflow/scripts/07_class7_pipeline.py`
  - `/home/clay/dev/agri-data-toolkit-worktrees/class-7/docs/classes/examples/class7-satellite-and-drone-intelligence/07-complete-workflow/scripts/07_complete_pipeline.py`
  - `/home/clay/dev/agri-data-toolkit-worktrees/class-7/docs/classes/examples/class7-satellite-and-drone-intelligence/07-complete-workflow/scripts/08_make_visualization_grid.py`

### Planning review

**Gaps addressed in this plan**:

- Explicitly define cache/regeneration behavior instead of leaving it implicit
- Lock NDVI scope to NDVI only, not extra vegetation indices
- Lock crop prediction to a heuristic based on recent crop history
- Add negative acceptance criteria for CDL composition card removal
- Add handling for partial imagery history, no-scene years, and full-refresh behavior
- Add explicit repair work for path/manifest drift and legacy `data/EDA` removal
- Add explicit yearly crop join and crop-conditioned NDVI rollup requirements

---

## 🎯 Work objectives

### Core objective

Create a canonical reporting workflow where expensive field-level analytical cards are cached as reusable assets under `data/growers/...`, raw growing-season satellite TIFFs are preserved for reuse, and downstream report assembly can rerun quickly without reviving legacy path drift.

### Concrete deliverables

- Per-field cached SSURGO card assets inside canonical derived outputs
- Per-field raw seasonal satellite TIFF inventories plus yearly NDVI composite rasters
- Per-field cached NDVI card assets for `corn average`, `soybean average`, and `current-season cumulative` views
- Updated field poster/HTML/Markdown assembly that consumes canonical cached card assets directly
- Updated crop-rotation summary with heuristic next-year and following-year text
- Removal of the old CDL composition card from field cards
- Canonical manifest/log relocation under grower/farm/field outputs
- Shared CDL path cleanup around `shared/cdl/rasters/` and aligned derived outputs
- Incremental dependency-aware rebuild behavior plus explicit full refresh

### Definition of done

- [ ] Expensive SSURGO and NDVI cards are independently cacheable and reusable
- [ ] Poster/HTML/Markdown assembly can rerun without recomputing unchanged expensive cards
- [ ] The field report layout replaces the CDL composition panel with NDVI content
- [ ] Crop rotation card includes two-year heuristic forecast text
- [ ] The field report layout uses crop-conditioned NDVI cards instead of best-scene yearly panels
- [ ] Active report generation no longer depends on `data/EDA/` or `data/reporting/manifests/`
- [ ] Incremental run skips unchanged card assets and full refresh forces regeneration

### Must have

- 5-year target window for cropland, weather, and NDVI inputs
- Clear dependency tracking for each expensive card asset
- Canonical outputs remain under `data/growers/...`
- Canonical manifests/logs live under grower/farm/field outputs
- Raw clipped TIFFs are retained for each accepted in-season scene
- Active shared CDL inputs live in canonical shared paths instead of old ad hoc roots
- Agent-executable verification only

### Must not have

- No new ML prediction model
- No additional vegetation indices beyond NDVI in this scope
- No mandatory recomputation of all expensive cards during cheap assembly runs
- No human-only visual verification criteria
- No active `data/EDA/` output root for the reporting pipeline
- No active `data/reporting/manifests/` dependency for reporting steps

---

## 📊 Verification strategy

> **Zero human intervention** — all verification must be executable by the implementation agent.

### Test decision

- **Infrastructure exists**: YES
- **Automated tests**: Tests-after
- **Framework**: existing project test/build commands plus targeted script execution

### QA policy

Every task below includes executable QA scenarios. Evidence should be saved under `.sisyphus/evidence/` during execution.

- **Frontend/report visuals**: Use generated PNG/HTML artifacts plus script-level assertions
- **Pipeline/CLI**: Use Bash commands with concrete expected files and manifest states
- **Library/module behavior**: Use Python entrypoints/import checks where appropriate

---

## ⚙️ Execution strategy

### Parallel execution waves

```text
Wave 1 (foundations)
1. Lock canonical path, manifest, and log contract
2. Align CDL ingestion and crop-history inputs to the canonical shared tree

Wave 2 (imagery + rollup production)
3. Expand satellite ingest to dense growing-season inventories
4. Build yearly NDVI composites and year-to-crop joins
5. Render canonical NDVI cards for corn, soybean, and current-season cumulative views

Wave 3 (other cached assets + layout)
6. Align SSURGO and crop-summary assets to the same canonical cache contract
7. Refactor poster, farm poster, HTML, and Markdown assembly to canonical-only inputs

Wave 4 (orchestration + cleanup)
8. Finish orchestration, cleanup, and verification for incremental vs full refresh

Wave FINAL (verification)
F1. Plan compliance audit
F2. Code quality + test/build review
F3. Report artifact QA
F4. Scope fidelity audit
```

### Dependency matrix

- **1**: none -> 3, 5, 6, 7, 8
- **2**: none -> 4, 6, 7, 8
- **3**: 1 -> 4, 5, 8
- **4**: 2, 3 -> 5, 8
- **5**: 1, 3, 4 -> 7, 8
- **6**: 1, 2 -> 7, 8
- **7**: 1, 2, 5, 6 -> 8, F1-F4
- **8**: 1, 2, 3, 4, 5, 6, 7 -> F1-F4

### Agent dispatch summary

- **Wave 1**: T1 `deep`, T2 `deep`
- **Wave 2**: T3 `deep`, T4 `deep`, T5 `visual-engineering`
- **Wave 3**: T6 `unspecified-high`, T7 `writing`
- **Wave 4**: T8 `deep`
- **Final**: F1 `oracle`, F2 `unspecified-high`, F3 `unspecified-high`, F4 `deep`

---

## ✍️ TODOs

- [x] 1. Lock the canonical path, manifest, and log contract

  **What to do**:
  - Make `data/growers/...` the only active report/output root
  - Move active manifests/logs out of `data/reporting/manifests/` into canonical grower/farm/field locations
  - Define the canonical path contract for field assets, farm assets, shared CDL assets, and per-step logs

  **Must NOT do**:
  - Keep `data/EDA/` as an active reporting root
  - Leave mixed legacy/canonical manifest references in the final pipeline contract

  **References**:
  - `data/scripts/lib/paths.py` - canonical path helper surface to expand and standardize
  - `data/scripts/run_farm_pipeline.py` - current bridge/orchestrator still preserving drift
  - `data/scripts/reporting_bootstrap.py` - canonical grower/farm/field scaffolding

  **Acceptance criteria**:
  - [ ] A canonical location exists for field-level assets, farm-level reports, shared CDL outputs, and step manifests/logs
  - [ ] `data/reporting/manifests/` is no longer required by active reporting steps
  - [ ] The contract distinguishes active canonical outputs from any optional legacy compatibility artifacts

  **QA scenarios**:

  ```text
  Scenario: path helpers resolve only canonical reporting roots
    Tool: Bash
    Steps:
      1. Import the path helper module and print the field, farm, shared CDL, and manifest/log locations for a sample grower/farm/field
      2. Assert every emitted path lives under `data/growers/...` or the canonical shared CDL tree
    Expected Result: no active reporting path points at `data/EDA/` or `data/reporting/manifests/`
    Evidence: .sisyphus/evidence/task-1-path-contract.txt

  Scenario: manifest contract is canonical-only
    Tool: Bash
    Steps:
      1. Build a sample step manifest after the refactor
      2. Assert all recorded input/output paths use canonical roots
    Expected Result: mixed legacy/canonical path recording is gone
    Evidence: .sisyphus/evidence/task-1-manifest-contract.txt
  ```

- [x] 2. Align CDL ingestion and crop-history inputs to the canonical shared tree

  **What to do**:
  - Treat `shared/cdl/rasters/` as canonical for the moved CDL TIFFs
  - Move active CDL CSV/summary/manifests under the canonical shared CDL tree
  - Update crop-history consumers to read from canonical shared CDL outputs only

  **Must NOT do**:
  - Keep active reporting coupled to old `data/cdl/...` paths

  **References**:
  - `data/scripts/ingest/download_cdl.py` - current ingest still writes to the old root
  - `scripts/rebuild_data_folder.py` - rebuild logic with legacy CDL aliases
  - `.opencode/skills/cdl-cropland/src/cdl_reporting.py` - crop-history and rotation summary behavior

  **Acceptance criteria**:
  - [ ] Active CDL raster, CSV, and summary outputs resolve from the canonical shared CDL tree
  - [ ] Crop-history joins still produce 5-year deterministic summaries
  - [ ] No active reporting script requires `data/cdl/...` after the migration

  **QA scenarios**:

  ```text
  Scenario: crop history resolves from canonical shared CDL assets
    Tool: Bash
    Steps:
      1. Run the CDL ingest/summary step against the canonical shared tree
      2. Assert yearly CDL outputs and crop rotation summaries are written/read from canonical locations
    Expected Result: crop history is available without reading the old root
    Evidence: .sisyphus/evidence/task-2-cdl-canonical.txt

  Scenario: legacy CDL paths are not required
    Tool: Bash
    Steps:
      1. Run the reporting pipeline with only canonical shared CDL assets present
      2. Assert the pipeline still builds crop-history outputs successfully
    Expected Result: no runtime dependency remains on `data/cdl/...`
    Evidence: .sisyphus/evidence/task-2-cdl-no-legacy.txt
  ```

- [x] 3. Expand satellite ingest from best-scene yearly picks to dense growing-season inventories

  **What to do**:
  - Replace the single `search_best_feature(...)` yearly pattern with per-year growing-season scene inventories
  - Retain raw clipped TIFFs for every accepted scene before derived NDVI products are built
  - Record accepted scenes, rejected gaps, and yearly coverage in canonical field satellite manifests/logs

  **Must NOT do**:
  - Collapse back to one best scene per year
  - Drop raw TIFF retention after composite generation

  **References**:
  - `data/scripts/lib/satellite_imagery.py` - current single-feature selection and NDVI helpers
  - `data/scripts/ingest/download_satellite_imagery.py` - current best-scene-per-year ingest implementation
  - `/home/clay/dev/agri-data-toolkit-worktrees/class-7/docs/classes/examples/class7-satellite-and-drone-intelligence/common/real_imagery.py` - raw clipping/signing reference
  - `/home/clay/dev/agri-data-toolkit-worktrees/class-7/docs/classes/examples/class7-satellite-and-drone-intelligence/07-complete-workflow/scripts/08_make_visualization_grid.py` - dense in-season time-series reference

  **Acceptance criteria**:
  - [ ] Each imagery year can store multiple accepted in-season scenes per sensor
  - [ ] Raw clipped TIFFs are retained for every accepted scene
  - [ ] Missing-scene years are logged explicitly instead of failing silently

  **QA scenarios**:

  ```text
  Scenario: growing-season ingest stores multiple scenes for one year
    Tool: Bash
    Steps:
      1. Run satellite ingest for a sample field/year with multiple available Sentinel-2 scenes
      2. Assert the field manifest records more than one scene for that year
      3. Assert raw clipped TIFFs exist for every accepted scene
    Expected Result: yearly ingest is inventory-based, not best-scene-only
    Evidence: .sisyphus/evidence/task-3-scene-inventory.txt

  Scenario: sparse year degrades gracefully
    Tool: Bash
    Steps:
      1. Run ingest for a year with poor availability or cloud-filtered dropouts
      2. Assert the manifest records the gap and keeps the broader field pipeline usable
    Expected Result: explicit sparse/missing coverage metadata without aborting the run
    Evidence: .sisyphus/evidence/task-3-sparse-year.txt
  ```

- [x] 4. Build yearly NDVI composites and year-to-crop joins

  **What to do**:
  - Generate yearly NDVI composite rasters from accepted in-season scenes
  - Join each yearly composite to the dominant crop history for that field-year
  - Produce reusable crop-conditioned rollup inputs for `corn` and `soybean`

  **Must NOT do**:
  - Introduce new vegetation indices
  - Skip year-to-crop attribution in the final rollup pipeline

  **References**:
  - `data/scripts/reporting/generate_ndvi_cards.py` - current aggregation assumptions to replace
  - `.opencode/skills/cdl-cropland/src/cdl_reporting.py` - year/crop composition and rotation summaries
  - `shared/cdl/rasters/` - canonical raw CDL raster root already moved by the user

  **Acceptance criteria**:
  - [ ] A yearly NDVI composite exists for each field-year with sufficient accepted scenes
  - [ ] Each yearly composite is tagged or joinable to the field-year crop class
  - [ ] Crop-conditioned rollup inputs can separate corn years from soybean years

  **QA scenarios**:

  ```text
  Scenario: yearly NDVI composite is built from multiple scenes
    Tool: Bash
    Steps:
      1. Generate yearly NDVI products for a field-year with multiple accepted scenes
      2. Assert a yearly composite raster and summary metadata are written
    Expected Result: yearly NDVI is composite-based rather than a direct copy of one scene
    Evidence: .sisyphus/evidence/task-4-yearly-composite.txt

  Scenario: crop join classifies yearly composites
    Tool: Bash
    Steps:
      1. Join yearly NDVI outputs to crop history for a sample field
      2. Assert yearly composites are grouped into `corn` or `soybean` rollup buckets when history exists
    Expected Result: crop-conditioned grouping is deterministic and auditable
    Evidence: .sisyphus/evidence/task-4-crop-join.txt
  ```

- [x] 5. Render canonical NDVI cards for corn, soybean, and current-season cumulative views

  **What to do**:
  - Replace the old `multi_year`, `recent`, and `accumulated` field-card contract with reusable `corn average`, `soybean average`, and `current-season cumulative` cards
  - Render a clear unavailable-state card when a crop class lacks usable years
  - Store card images and manifests in canonical field derived outputs and logs

  **Must NOT do**:
  - Reintroduce best-scene yearly bars as the main field-card outputs
  - Write active NDVI cards outside canonical field roots

  **References**:
  - `data/scripts/reporting/generate_ndvi_cards.py` - main NDVI card renderer to redesign
  - `data/scripts/reporting/generate_field_posters.py` - current consumer of cached NDVI cards
  - `data/scripts/reporting/generate_farm_html.py` - current HTML card embedding logic
  - `data/scripts/reporting/generate_farm_markdown.py` - current Markdown card linking logic

  **Acceptance criteria**:
  - [ ] Three canonical NDVI field-card assets exist: `corn`, `soybean`, `current-season cumulative`
  - [ ] Crop-missing cases render explicit fallback cards and metadata
  - [ ] Incremental runs reuse unchanged NDVI cards through canonical manifests/logs

  **QA scenarios**:

  ```text
  Scenario: all three NDVI card slots render canonically
    Tool: Bash
    Steps:
      1. Run NDVI card generation for a field with both corn and soybean history plus current-season observations
      2. Assert the three canonical card assets are present under the field derived feature tree
    Expected Result: the final card contract matches the refreshed plan
    Evidence: .sisyphus/evidence/task-5-ndvi-cards.txt

  Scenario: missing crop class produces a fallback asset
    Tool: Bash
    Steps:
      1. Run card generation for a field with only one qualifying crop class in the 5-year window
      2. Assert the missing class card renders an explicit unavailable state and logs why
    Expected Result: layout remains stable without misleading empty output
    Evidence: .sisyphus/evidence/task-5-ndvi-fallback.txt
  ```

- [ ] 6. Align SSURGO and crop-summary assets to the same canonical cache contract

  **What to do**:
  - Bring SSURGO cards and soil maps under the same canonical asset + log contract
  - Keep crop rotation history and heuristic next-two-year outlook in the first card
  - Remove the old CDL composition card from active report layouts and outputs

  **Must NOT do**:
  - Regress existing SSURGO visual quality
  - Remove crop history text while removing the obsolete CDL card

  **References**:
  - `data/scripts/reporting/generate_ssurgo_cards.py` - existing soil card generator needing cache alignment
  - `data/scripts/reporting/generate_ssurgo_maps.py` - existing soil map generation paths
  - `data/scripts/reporting/generate_field_posters.py` - first-card content and old CDL slot usage

  **Acceptance criteria**:
  - [ ] SSURGO cards and maps are cacheable canonically and independently of report assembly
  - [ ] Crop rotation history plus heuristic outlook remain visible in the first card
  - [ ] The old CDL composition card is absent from active report outputs

  **QA scenarios**:

  ```text
  Scenario: SSURGO assets reuse canonically
    Tool: Bash
    Steps:
      1. Run SSURGO asset generation twice with unchanged inputs
      2. Assert the second run reuses existing canonical assets and logs
    Expected Result: SSURGO participates in the same cheap-reassembly model
    Evidence: .sisyphus/evidence/task-6-ssurgo-reuse.txt

  Scenario: field summary keeps crop outlook and drops old CDL card
    Tool: Bash
    Steps:
      1. Build a field report after the layout/content refactor
      2. Assert the first card contains crop rotation history and heuristic outlook text
      3. Assert no obsolete CDL composition panel is rendered
    Expected Result: the field summary reflects the requested content swap
    Evidence: .sisyphus/evidence/task-6-crop-summary.txt
  ```

- [ ] 7. Refactor poster, farm poster, HTML, and Markdown assembly to canonical-only inputs

  **What to do**:
  - Make field poster, farm poster, HTML, and Markdown assembly read directly from canonical cached assets
  - Remove the active `data/EDA/...` write/read cycle and the sync bridge back into `data/growers/...`
  - Keep report assembly cheap once expensive assets are up to date

  **Must NOT do**:
  - Preserve the old bridge as the primary execution path
  - Fork inconsistent asset locations across poster vs HTML vs Markdown

  **References**:
  - `data/scripts/reporting/generate_field_posters.py`
  - `data/scripts/reporting/generate_aggregate_poster.py`
  - `data/scripts/reporting/generate_farm_html.py`
  - `data/scripts/reporting/generate_farm_markdown.py`
  - `data/scripts/run_farm_pipeline.py` - current sync bridge to remove after canonicalization

  **Acceptance criteria**:
  - [ ] Final report builders read from canonical cached assets only
  - [ ] No active assembly step writes its primary output to `data/EDA/...`
  - [ ] Re-running assembly without upstream changes avoids expensive recomputation

  **QA scenarios**:

  ```text
  Scenario: assembly runs canonically without the legacy bridge
    Tool: Bash
    Steps:
      1. Run field/farm poster plus HTML/Markdown assembly after canonical refactor
      2. Assert outputs are written into canonical grower/farm locations
      3. Assert the run does not depend on `data/EDA/...` inputs
    Expected Result: canonical-only assembly succeeds end to end
    Evidence: .sisyphus/evidence/task-7-canonical-assembly.txt

  Scenario: unchanged expensive assets keep assembly cheap
    Tool: Bash
    Steps:
      1. Re-run report assembly with unchanged SSURGO/NDVI assets
      2. Assert assembly refreshes only downstream outputs and skips upstream expensive renders
    Expected Result: the cheap-reassembly contract holds
    Evidence: .sisyphus/evidence/task-7-cheap-rerun.txt
  ```

- [ ] 8. Finish orchestration, cleanup, and verification for incremental vs full refresh

  **What to do**:
  - Update `run_farm_pipeline.py` so users can request incremental updates or full refresh without reasoning about internal dependency order
  - Remove or quarantine the remaining legacy EDA/report assumptions from active execution paths
  - Add tests and verification coverage for canonical paths, seasonal NDVI inventories, crop-conditioned card outputs, and missing-data behavior

  **Must NOT do**:
  - Leave the new pipeline dependent on manual cleanup or one-off migration steps
  - Hide missing-data states behind silent failures

  **References**:
  - `data/scripts/run_farm_pipeline.py` - top-level orchestration and current sync bridge
  - `tests/farm_intelligence/test_pipeline.py` - targeted regression coverage
  - `docs/project/pr/pr-00000003-build-farm-intelligence-reporting.md`
  - `docs/project/issues/issue-00000006-build-farm-intelligence-reporting.md`
  - `docs/project/kanban/project-farm-intelligence-reporting.md`

  **Acceptance criteria**:
  - [ ] Incremental runs skip unchanged expensive assets while rebuilding required downstream outputs
  - [ ] Full refresh forces end-to-end expensive regeneration and then canonical assembly
  - [ ] Tests and project tracking records reflect the canonical-only structure and new NDVI contract

  **QA scenarios**:

  ```text
  Scenario: incremental mode is dependency-correct
    Tool: Bash
    Steps:
      1. Run the canonical pipeline in default incremental mode with current manifests/logs present
      2. Assert unchanged expensive assets are skipped while changed downstream outputs rebuild
    Expected Result: incremental refresh is fast and correct
    Evidence: .sisyphus/evidence/task-8-incremental.txt

  Scenario: full refresh rebuilds everything deterministically
    Tool: Bash
    Steps:
      1. Run the canonical pipeline with the full-refresh flag
      2. Assert seasonal ingest, yearly composites, NDVI cards, SSURGO assets, and final report outputs all rebuild
    Expected Result: force mode bypasses reuse cleanly and then restores canonical outputs/logs
    Evidence: .sisyphus/evidence/task-8-full-refresh.txt
  ```

---

## 🔍 Final verification wave

- [ ] F1. **Plan compliance audit** — `oracle`
  - Verify every must-have item exists in delivered outputs and every must-not-have item is absent
  - Verify evidence files exist for all task scenarios

- [ ] F2. **Code quality review** — `unspecified-high`
  - Run available build/test/lint commands and inspect changed files for dead code, brittle branching, and skipped cache logic

- [ ] F3. **Report artifact QA** — `unspecified-high`
  - Run the field reporting pipeline on a representative farm and verify cached-card reuse, refreshed outputs, and no-scene degradation paths

- [ ] F4. **Scope fidelity audit** — `deep`
  - Compare the implementation diff against this plan and reject any scope creep such as extra vegetation indices or model-based prediction

---

## 📦 Commit strategy

- Prefer one cohesive implementation sequence with atomic commits around:
  - manifest/cache contract
  - NDVI + SSURGO asset generation
  - report assembly updates
  - orchestration + verification

---

## ✅ Success criteria

### Verification commands

```bash
python data/scripts/run_farm_pipeline.py --help
python data/scripts/run_farm_pipeline.py
python data/scripts/run_farm_pipeline.py --force
```

### Final checklist

- [ ] Cached expensive card assets exist in canonical field outputs
- [ ] Poster/HTML/Markdown assembly reuses unchanged cached assets
- [ ] NDVI replaces the old CDL composition slot in the field report
- [ ] Final NDVI field cards expose `corn`, `soybean`, and `current-season cumulative` outputs
- [ ] Crop rotation card includes two-year heuristic forecast text
- [ ] 5-year cropland, weather, and NDVI target behavior is implemented and documented
- [ ] Active reporting no longer depends on `data/EDA/`, `data/reporting/manifests/`, or old `data/cdl/` paths
- [ ] Incremental and full-refresh modes both work deterministically

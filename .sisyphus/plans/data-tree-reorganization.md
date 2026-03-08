# Work Plan: Reorganize data tree into scripts/shared/growers

## TL;DR

Reorganize `data/` into a deterministic, scalable hierarchy built around `data/scripts/`, `data/shared/`, and `data/growers/`, then hard-cut all pipeline and script path usage to the new structure using canonical demo slugs `iowa-demo-grower` and `iowa-demo-farm`.

**Deliverables:**

- `data/scripts/` reorganized into `ingest/`, `eda/`, `reporting/`, and `lib/`
- `data/shared/` created for canonical reusable assets such as CDL, reference data, and shared manifests
- `data/growers/iowa-demo-grower/farms/iowa-demo-farm/` created as the canonical farm tree
- Current field, soil, weather, cache, report, and manifest assets relocated into canonical field/farm/shared locations
- `data/scripts/lib/paths.py`, `data/scripts/lib/manifest.py`, and `data/scripts/lib/naming.py`
- `farm.json`, `field.json`, and dataset `metadata.json` / `manifest.json` files added where required
- `data/scripts/run_farm_pipeline.py` updated to operate entirely against the new structure
- `data/README.md` rewritten to match the actual post-migration tree

---

## Context

The current `data/` area has grown beyond the original minimal `sql/` layout and now contains a mixed flat structure with raw inputs, cached API downloads, derived EDA outputs, reporting artifacts, manifests, and executable scripts. The user wants a production-shaped structure that supports one grower / one farm / many fields now, and many growers / many farms / many fields later.

The current repo state that must be migrated includes:

- `data/EDA/` with `field_cards/`, `soil_cards/`, `soil_maps/`, and `iowa_farm_report.*`
- `data/cdl/` with canonical CDL rasters and derived CSV summaries
- `data/field-boundaries/` with the Iowa field boundary source
- `data/reporting/manifests/` with per-step manifests
- `data/soil/` with `iowa_full_ssurgo.csv`, `iowa_ssurgo_summary.csv`, and `cache/*.geojson`
- `data/weather/` with field weather exports
- `data/scripts/` with flat numbered ingest/EDA/reporting scripts plus bootstrap and pipeline entrypoints

The user explicitly selected:

- Demo slugs: `iowa-demo-grower` / `iowa-demo-farm`
- Migration style: **hard cutover immediately**

The plan must preserve the working SSURGO integrations that already exist, including cached USDA SDA polygon downloads and field poster rendering that now uses multiple soil polygons.

---

## Work Objectives

### Core Objective

Replace the ad hoc flat `data/` tree with a canonical hierarchy that cleanly separates executable code, shared datasets, and grower/farm/field-scoped data while keeping the pipeline reproducible and deterministic.

### Concrete Deliverables

1. New top-level `data/` structure with only `scripts/`, `shared/`, and `growers/` as active data concerns
2. Canonical grower/farm/field tree under `data/growers/iowa-demo-grower/farms/iowa-demo-farm/fields/`
3. Canonical shared asset tree under `data/shared/` for CDL, reference data, and shared manifests
4. Centralized path helpers and naming helpers under `data/scripts/lib/`
5. Script reorganization from flat numbered files into `ingest/`, `eda/`, and `reporting/`
6. Metadata and manifest coverage for farm, field, and dataset folders
7. Updated pipeline and reporting scripts that no longer depend on legacy top-level paths
8. Updated `data/README.md` that accurately documents the final structure

### Definition of Done

- [ ] `data/` uses the new top-level structure with `scripts/`, `shared/`, and `growers/`
- [ ] Current field, soil, weather, CDL, cache, manifest, and derived report assets are relocated into canonical locations
- [ ] Every field has a `field.json`
- [ ] The farm has a `farm.json`
- [ ] Dataset folders have `metadata.json` or `manifest.json` where appropriate
- [ ] `data/scripts/lib/paths.py` exists and is used by moved scripts
- [ ] `data/scripts/run_farm_pipeline.py` works against the new structure without fallback to old paths
- [ ] No active script still depends on the old top-level data folders
- [ ] `data/README.md` matches the final structure exactly

---

## Execution Strategy

### Target architecture

```text
data/
├── README.md
├── scripts/
│   ├── ingest/
│   ├── eda/
│   ├── reporting/
│   ├── lib/
│   ├── reporting_bootstrap.py
│   └── run_farm_pipeline.py
├── shared/
│   ├── cdl/
│   ├── reference/
│   └── manifests/
└── growers/
    └── iowa-demo-grower/
        └── farms/
            └── iowa-demo-farm/
                ├── farm.json
                └── fields/
                    └── <field_slug>/
                        ├── field.json
                        ├── boundary/
                        ├── soil/
                        ├── weather/
                        ├── satellite/
                        ├── derived/
                        └── logs/
```

### Non-negotiable design rules

- Shared reusable assets live once under `data/shared/`
- Field-specific raw assets live under each field directory
- Raw and derived outputs stay separated
- Stable slug-based paths only; no display-name directory names
- Dataset folders must carry machine-readable metadata or manifests
- Hard cutover means no compatibility wrappers and no dual-write behavior after migration
- Canonical path construction must come from shared helper modules, not per-script relative path logic

### Migration waves

**Wave 1 — Scaffold and helpers**

- Create new directory tree
- Create helper modules in `data/scripts/lib/`
- Create farm/field identity JSON files and metadata skeletons

**Wave 2 — Data migration**

- Move shared datasets and manifests into `data/shared/`
- Move field-scoped boundary, soil, weather, cache, and derived assets into grower/farm/field directories

**Wave 3 — Script migration**

- Move scripts into `ingest/`, `eda/`, and `reporting/`
- Refactor imports and path usage to central helpers

**Wave 4 — Pipeline cutover**

- Update `run_farm_pipeline.py`
- Update all reporting scripts and ingest scripts
- Remove remaining old-path assumptions

**Wave 5 — Documentation and verification**

- Rewrite `data/README.md`
- Run migration verification and pipeline verification

---

## TODOs

- [ ] 1. Create canonical `data/` scaffold

  **What to do:**
  Create the new directory structure under `data/` using the agreed hierarchy:
  - `data/scripts/ingest/`
  - `data/scripts/eda/`
  - `data/scripts/reporting/`
  - `data/scripts/lib/`
  - `data/shared/cdl/metadata/`
  - `data/shared/cdl/rasters/`
  - `data/shared/cdl/manifests/`
  - `data/shared/reference/schemas/`
  - `data/shared/reference/crop_codes/`
  - `data/shared/reference/units/`
  - `data/shared/manifests/`
  - `data/growers/iowa-demo-grower/farms/iowa-demo-farm/`
  - `data/growers/iowa-demo-grower/farms/iowa-demo-farm/fields/<field_slug>/...`

  **Must NOT do:**
  - Leave old top-level dataset folders as active homes after migration
  - Introduce new top-level dataset categories outside `scripts/`, `shared/`, and `growers/`

  **Acceptance Criteria:**
  - [ ] New scaffold exists
  - [ ] Farm-level and field-level folders exist for the demo hierarchy
  - [ ] Directory naming is lowercase kebab-case

  **Commit:** NO (group with full migration verification)

- [ ] 2. Create path, naming, and manifest helper modules

  **What to do:**
  Create:
  - `data/scripts/lib/paths.py`
  - `data/scripts/lib/manifest.py`
  - `data/scripts/lib/naming.py`

  `paths.py` must provide canonical functions for grower, farm, field, boundary, soil, weather, satellite, derived, logs, and shared dataset paths. `naming.py` must centralize slug and filename conventions. `manifest.py` must centralize metadata/manifest loading and writing patterns.

  **Must NOT do:**
  - Leave scripts building canonical paths via repeated string concatenation
  - Duplicate path logic across multiple scripts

  **Acceptance Criteria:**
  - [ ] Helper modules exist
  - [ ] Helper API covers all dataset locations needed by current pipeline scripts
  - [ ] New scripts can import canonical path builders without `../../` traversal logic

  **Commit:** NO

- [ ] 3. Add farm and field identity records

  **What to do:**
  Create `farm.json` and one `field.json` per migrated field under the new grower/farm tree. Use:
  - `grower_slug = iowa-demo-grower`
  - `farm_slug = iowa-demo-farm`

  Each field record must include canonical references to its boundary, soil, weather, satellite, and derived/report locations.

  **Must NOT do:**
  - Use display names as folder names
  - Omit canonical file references from field metadata

  **Acceptance Criteria:**
  - [ ] One `farm.json` exists at farm level
  - [ ] Every field directory contains a `field.json`
  - [ ] Metadata values use stable slugs and relative file references

  **Commit:** NO

- [ ] 4. Migrate shared datasets into `data/shared/`

  **What to do:**
  Move reusable assets into canonical shared locations, including:
  - CDL rasters from `data/cdl/*.tif` → `data/shared/cdl/rasters/`
  - CDL manifests/metadata and reusable CDL summaries into `data/shared/cdl/` and `data/shared/manifests/`
  - Reference mappings / schemas as applicable into `data/shared/reference/`

  Decide what current CSV products are canonical shared sources versus field- or farm-derived outputs, and place them accordingly.

  **Must NOT do:**
  - Duplicate canonical CDL sources into each field folder
  - Misclassify derived CSV outputs as raw shared source data

  **Acceptance Criteria:**
  - [ ] Canonical shared CDL assets live under `data/shared/cdl/`
  - [ ] Shared metadata/manifests exist
  - [ ] No script still treats old `data/cdl/` as canonical

  **Commit:** NO

- [ ] 5. Migrate field-scoped raw datasets into grower/farm/field directories

  **What to do:**
  For each current field, move or rewrite canonical locations for:
  - boundary GeoJSON
  - SSURGO soil summary/full exports and raw polygon GeoJSON cache
  - weather CSVs
  - future satellite placeholders / manifests

  Store raw source-of-truth field assets under:
  - `boundary/field_boundary.geojson`
  - `soil/ssurgo_soil_types.geojson` and related metadata/raw tables
  - `weather/daily_weather.csv`
  - `satellite/...`

  Preserve the one-time-per-field SSURGO polygon cache behavior, but relocate it into field `soil/` rather than the old shared cache folder.

  **Must NOT do:**
  - Mix derived report outputs into raw source folders
  - Keep active field source data in legacy `data/field-boundaries/`, `data/soil/`, or `data/weather/`

  **Acceptance Criteria:**
  - [ ] Every field has boundary, soil, and weather directories
  - [ ] Cached SSURGO polygon GeoJSON is field-scoped
  - [ ] Metadata exists for dataset folders that hold real data

  **Commit:** NO

- [ ] 6. Migrate derived outputs and logs into canonical farm/field derived areas

  **What to do:**
  Re-home current derived/report outputs from `data/EDA/` and run records from `data/reporting/manifests/` into the new farm/field tree.

  At minimum, map:
  - field posters
  - soil cards
  - soil maps
  - farm HTML / markdown / poster outputs
  - pipeline manifests and run logs

  into `derived/`, `reports/`, `summaries/`, `tables/`, `features/`, and `logs/` as appropriate.

  **Must NOT do:**
  - Leave `data/EDA/` as the canonical home after cutover
  - Keep manifests detached from the migrated data model

  **Acceptance Criteria:**
  - [ ] Field-level derived outputs live with their field or farm scope
  - [ ] Farm-level outputs have a canonical home
  - [ ] Run logs or manifests are stored in deterministic locations

  **Commit:** NO

- [ ] 7. Reorganize script files by function

  **What to do:**
  Move scripts according to the approved mapping:
  - `01_download_fields.py` → `data/scripts/ingest/download_fields.py`
  - `02_download_soil.py` → `data/scripts/ingest/download_soil.py`
  - `03_download_weather.py` → `data/scripts/ingest/download_weather.py`
  - `04_download_cdl.py` → `data/scripts/ingest/download_cdl.py`
  - `05_eda_overview.py` → `data/scripts/eda/eda_overview.py`
  - `06_eda_time_series.py` → `data/scripts/eda/eda_time_series.py`
  - `07_eda_distributions.py` → `data/scripts/eda/eda_distributions.py`
  - `08_eda_correlations.py` → `data/scripts/eda/eda_correlations.py`
  - `09_eda_field_cards.py` → `data/scripts/eda/eda_field_cards.py`
  - `10_eda_summary_dashboard.py` → `data/scripts/eda/eda_summary_dashboard.py`
  - `11_generate_field_posters.py` → `data/scripts/reporting/generate_field_posters.py`
  - `12_generate_aggregate_poster.py` → `data/scripts/reporting/generate_aggregate_poster.py`
  - `13_generate_farm_html.py` → `data/scripts/reporting/generate_farm_html.py`
  - `14_generate_farm_markdown.py` → `data/scripts/reporting/generate_farm_markdown.py`
  - `15_generate_ssurgo_cards.py` → `data/scripts/reporting/generate_ssurgo_cards.py`
  - `16_generate_ssurgo_maps.py` → `data/scripts/reporting/generate_ssurgo_maps.py`

  Keep `data/scripts/run_farm_pipeline.py` at top level.

  **Must NOT do:**
  - Leave the old numbered filenames in active use
  - Scatter helper logic back into reporting scripts once moved

  **Acceptance Criteria:**
  - [ ] Scripts exist in the new subfolders
  - [ ] Imports are updated to the new locations
  - [ ] No active script path points to the old flat filenames

  **Commit:** NO

- [ ] 8. Refactor all scripts to use canonical helpers and new data locations

  **What to do:**
  Update all ingest, EDA, reporting, and pipeline scripts to:
  - import path helpers from `data/scripts/lib/paths.py`
  - use new grower/farm/field/shared locations
  - stop referencing old legacy top-level locations such as `data/soil/`, `data/weather/`, `data/cdl/`, `data/EDA/`, and `data/reporting/manifests/`

  This includes current working SSURGO integrations, cache handling, field posters, farm poster, HTML, markdown, soil cards, and soil maps.

  **Must NOT do:**
  - Leave any hard-coded legacy `data/...` paths in active scripts after cutover
  - Break the existing one-time SSURGO polygon cache/download workflow

  **Acceptance Criteria:**
  - [ ] Path helper usage is adopted across the moved scripts
  - [ ] Legacy path grep for active scripts is clean or only present in migration notes/tests
  - [ ] Scripts still implement their existing responsibilities

  **Commit:** NO

- [ ] 9. Update pipeline entrypoint and manifests for hard cutover

  **What to do:**
  Refactor `data/scripts/run_farm_pipeline.py` to operate on the new structure and canonical helpers. Ensure it locates field/farm assets via metadata and helper functions rather than fixed Iowa one-off paths. Update manifest handling to use new canonical manifest locations.

  **Must NOT do:**
  - Leave `run_farm_pipeline.py` coupled to legacy folder names
  - Break idempotent skip/stale detection behavior

  **Acceptance Criteria:**
  - [ ] Pipeline runs from the new structure
  - [ ] Per-step manifests/logs are written in canonical locations
  - [ ] Hard cutover means no fallback to legacy input paths

  **Commit:** NO

- [ ] 10. Rewrite `data/README.md` to match the new structure

  **What to do:**
  Replace the current minimal `data/README.md` with a full repo-specific guide that documents:
  - the three top-level concerns
  - shared vs field-scoped data
  - raw vs derived separation
  - the canonical demo grower/farm example
  - metadata requirements
  - script organization
  - a Mermaid diagram showing the new hierarchy or flow of shared/farm/field assets

  Follow the repository markdown and Mermaid style guides exactly.

  **Must NOT do:**
  - Leave README describing only `sql/`
  - Add uncited external claims
  - Use Mermaid inline styles or omit `accTitle` / `accDescr`

  **Acceptance Criteria:**
  - [ ] `data/README.md` matches the migrated tree
  - [ ] Includes at least one valid Mermaid diagram with accessibility metadata
  - [ ] Explains naming rules and metadata expectations

  **Commit:** NO

- [ ] 11. Verify hard cutover migration end to end

  **What to do:**
  Run verification for:
  - file presence in canonical locations
  - metadata coverage
  - absence of active hard-coded legacy paths
  - pipeline execution from the new structure
  - existence of migrated outputs in the new farm/field derived locations

  **Acceptance Criteria:**
  - [ ] Canonical tree exists and old top-level data homes are no longer active dependencies
  - [ ] Pipeline succeeds using the new structure
  - [ ] README and code agree on actual paths
  - [ ] SSURGO cards, maps, field posters, and farm reports still generate in their new locations

  **Evidence:** command output and directory listings from the new structure

  **Commit:** YES — group as final migration commit after verification

---

## Success Criteria

### Verification Commands

```bash
# Verify new top-level structure
ls -la data/

# Verify script organization
find data/scripts -maxdepth 2 -type f | sort

# Verify metadata coverage
find data/growers/iowa-demo-grower -name "farm.json" -o -name "field.json" -o -name "metadata.json" -o -name "manifest.json" | sort

# Verify no active legacy path assumptions remain
grep -R "data/field-boundaries\|data/soil\|data/weather\|data/cdl\|data/EDA\|data/reporting/manifests" data/scripts --include="*.py"

# Verify pipeline works after cutover
python data/scripts/run_farm_pipeline.py
```

### Final Checklist

- [ ] `data/` uses the new three-part top-level structure
- [ ] Shared datasets live under `data/shared/`
- [ ] Field-scoped raw data lives under `data/growers/iowa-demo-grower/farms/iowa-demo-farm/fields/<field_slug>/`
- [ ] Raw and derived outputs are separated
- [ ] Farm and field identity JSON files exist
- [ ] Dataset metadata/manifests exist where required
- [ ] Scripts are reorganized by function
- [ ] Canonical helper modules exist and are used
- [ ] Pipeline works from the new structure
- [ ] `data/README.md` matches reality

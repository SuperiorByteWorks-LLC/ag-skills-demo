# Draft: data tree reorganization migration details

_Repo-specific migration draft for the `data/` hard cutover from the current flat structure to the canonical `scripts/` + `shared/` + `growers/` layout._

---

## 📋 Scope summary

This draft converts the current `data/` tree into a production-shaped structure using:

- `data/scripts/`
- `data/shared/`
- `data/growers/iowa-demo-grower/farms/iowa-demo-farm/`

The implementation must preserve the currently working reporting pipeline, including:

- field posters
- farm poster
- farm HTML report
- farm markdown report
- SSURGO soil profile cards
- SSURGO soil maps
- real USDA SDA polygon caching per field

---

## 🎯 Fixed decisions

| Decision                                    | Value                                           |
| ------------------------------------------- | ----------------------------------------------- |
| **Grower slug**                             | `iowa-demo-grower`                              |
| **Farm slug**                               | `iowa-demo-farm`                                |
| **Migration mode**                          | Hard cutover immediately                        |
| **Canonical shared dataset example**        | CDL                                             |
| **Canonical field SSURGO polygon behavior** | Download once from USDA API and cache per field |
| **Canonical path policy**                   | Use helper modules only                         |

---

## 🏗️ Target tree for first-pass migration

```text
data/
├── README.md
├── scripts/
│   ├── ingest/
│   │   ├── download_fields.py
│   │   ├── download_soil.py
│   │   ├── download_weather.py
│   │   └── download_cdl.py
│   ├── eda/
│   │   ├── eda_overview.py
│   │   ├── eda_time_series.py
│   │   ├── eda_distributions.py
│   │   ├── eda_correlations.py
│   │   ├── eda_field_cards.py
│   │   └── eda_summary_dashboard.py
│   ├── reporting/
│   │   ├── generate_field_posters.py
│   │   ├── generate_aggregate_poster.py
│   │   ├── generate_farm_html.py
│   │   ├── generate_farm_markdown.py
│   │   ├── generate_ssurgo_cards.py
│   │   └── generate_ssurgo_maps.py
│   ├── lib/
│   │   ├── paths.py
│   │   ├── manifest.py
│   │   └── naming.py
│   ├── reporting_bootstrap.py
│   └── run_farm_pipeline.py
├── shared/
│   ├── cdl/
│   │   ├── metadata/
│   │   ├── rasters/
│   │   ├── derived/
│   │   └── manifests/
│   ├── reference/
│   │   ├── schemas/
│   │   ├── crop_codes/
│   │   └── units/
│   └── manifests/
└── growers/
    └── iowa-demo-grower/
        └── farms/
            └── iowa-demo-farm/
                ├── farm.json
                ├── manifests/
                ├── derived/
                │   ├── reports/
                │   ├── summaries/
                │   └── dashboards/
                └── fields/
                    └── <field_slug>/
                        ├── field.json
                        ├── boundary/
                        │   ├── field_boundary.geojson
                        │   └── metadata.json
                        ├── soil/
                        │   ├── ssurgo_soil_types.geojson
                        │   ├── ssurgo_full.csv
                        │   ├── ssurgo_summary.csv
                        │   └── metadata.json
                        ├── weather/
                        │   ├── daily_weather.csv
                        │   └── metadata.json
                        ├── satellite/
                        │   ├── landsat/
                        │   └── sentinel/
                        ├── derived/
                        │   ├── tables/
                        │   ├── features/
                        │   ├── reports/
                        │   └── summaries/
                        └── logs/
                            └── pipeline_runs.jsonl
```

---

## 🔄 Current to target migration map

### Top-level directory migration

| Current location            | Target location                                                                             | Notes                               |
| --------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------- |
| `data/cdl/`                 | `data/shared/cdl/`                                                                          | Canonical shared dataset home       |
| `data/field-boundaries/`    | `data/growers/iowa-demo-grower/farms/iowa-demo-farm/fields/<field_slug>/boundary/`          | Field-scoped raw boundary           |
| `data/soil/`                | `data/growers/.../fields/<field_slug>/soil/` plus limited farm/shared placement             | Split summary/full/cache by scope   |
| `data/weather/`             | `data/growers/.../fields/<field_slug>/weather/`                                             | Field-scoped weather                |
| `data/EDA/`                 | `data/growers/.../fields/<field_slug>/derived/` and farm `derived/`                         | Derived/report outputs only         |
| `data/reporting/manifests/` | `data/growers/iowa-demo-grower/farms/iowa-demo-farm/manifests/` and/or field logs/manifests | Must become canonical manifest home |
| `data/scripts/`             | `data/scripts/{ingest,eda,reporting,lib}`                                                   | Functional grouping                 |

### Script migration map

| Current file                                   | Target file                                           |
| ---------------------------------------------- | ----------------------------------------------------- |
| `data/scripts/01_download_fields.py`           | `data/scripts/ingest/download_fields.py`              |
| `data/scripts/02_download_soil.py`             | `data/scripts/ingest/download_soil.py`                |
| `data/scripts/03_download_weather.py`          | `data/scripts/ingest/download_weather.py`             |
| `data/scripts/04_download_cdl.py`              | `data/scripts/ingest/download_cdl.py`                 |
| `data/scripts/05_eda_overview.py`              | `data/scripts/eda/eda_overview.py`                    |
| `data/scripts/06_eda_time_series.py`           | `data/scripts/eda/eda_time_series.py`                 |
| `data/scripts/07_eda_distributions.py`         | `data/scripts/eda/eda_distributions.py`               |
| `data/scripts/08_eda_correlations.py`          | `data/scripts/eda/eda_correlations.py`                |
| `data/scripts/09_eda_field_cards.py`           | `data/scripts/eda/eda_field_cards.py`                 |
| `data/scripts/10_eda_summary_dashboard.py`     | `data/scripts/eda/eda_summary_dashboard.py`           |
| `data/scripts/11_generate_field_posters.py`    | `data/scripts/reporting/generate_field_posters.py`    |
| `data/scripts/12_generate_aggregate_poster.py` | `data/scripts/reporting/generate_aggregate_poster.py` |
| `data/scripts/13_generate_farm_html.py`        | `data/scripts/reporting/generate_farm_html.py`        |
| `data/scripts/14_generate_farm_markdown.py`    | `data/scripts/reporting/generate_farm_markdown.py`    |
| `data/scripts/15_generate_ssurgo_cards.py`     | `data/scripts/reporting/generate_ssurgo_cards.py`     |
| `data/scripts/16_generate_ssurgo_maps.py`      | `data/scripts/reporting/generate_ssurgo_maps.py`      |
| `data/scripts/reporting_bootstrap.py`          | `data/scripts/reporting_bootstrap.py`                 |
| `data/scripts/run_farm_pipeline.py`            | `data/scripts/run_farm_pipeline.py`                   |

---

## 📦 Dataset mapping details

### Shared CDL assets

#### Current assets

- `data/cdl/CDL_2021_19.tif`
- `data/cdl/CDL_2022_19.tif`
- `data/cdl/CDL_2023_19.tif`
- `data/cdl/CDL_2024_19.tif`
- `data/cdl/iowa_2021_cdl.csv`
- `data/cdl/iowa_2022_cdl.csv`
- `data/cdl/iowa_2023_cdl.csv`
- `data/cdl/iowa_2024_cdl.csv`
- `data/cdl/iowa_cdl_2021_2024.csv`
- `data/cdl/iowa_crop_rotation.csv`

#### Target recommendation

- raw rasters → `data/shared/cdl/rasters/`
- shared derived/statewide or farm-wide reusable CDL tables → `data/shared/cdl/derived/`
- dataset manifests/metadata → `data/shared/cdl/manifests/` and `data/shared/cdl/metadata/`

### Field boundaries

#### Current asset

- `data/field-boundaries/iowa_10_fields.geojson`

#### Target recommendation

- split into one boundary file per field:
  - `data/growers/iowa-demo-grower/farms/iowa-demo-farm/fields/<field_slug>/boundary/field_boundary.geojson`

Also add field-level boundary metadata.

### Soil assets

#### Current assets

- `data/soil/iowa_10_fields_soil.csv`
- `data/soil/iowa_full_ssurgo.csv`
- `data/soil/iowa_ssurgo_summary.csv`
- `data/soil/cache/*.geojson`

#### Target recommendation

Per field:

- raw field polygon cache → `soil/ssurgo_soil_types.geojson`
- field full soil table → `soil/ssurgo_full.csv`
- field summary soil table → `soil/ssurgo_summary.csv`
- `soil/metadata.json`

Potential farm-level aggregated soil tables can also live under farm `derived/summaries/` if needed.

### Weather assets

#### Current assets

- `data/weather/iowa_10_fields_weather.csv`
- `data/weather/iowa_weather_2021_2025.csv`

#### Target recommendation

Per field:

- `weather/daily_weather.csv`
- `weather/metadata.json`

Farm-level rollups belong under farm `derived/summaries/`.

### Current derived/report assets

#### Current assets

- `data/EDA/field_cards/iowa_field_report_01.png` … `10.png`
- `data/EDA/soil_cards/*.png`
- `data/EDA/soil_maps/*.png`
- `data/EDA/iowa_farm_report.html`
- `data/EDA/iowa_farm_report.md`
- `data/EDA/iowa_farm_report.png`

#### Target recommendation

Per field:

- field poster → `derived/reports/field_report.png`
- soil cards → `derived/reports/soil_cards/*.png`
- soil map → `derived/reports/soil_map.png`

Farm-level:

- farm poster → `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/reports/farm_report.png`
- HTML report → `.../derived/reports/farm_report.html`
- markdown report → `.../derived/reports/farm_report.md`
- dashboards / summaries → `.../derived/dashboards/` and `.../derived/summaries/`

### Current manifests

#### Current assets

- `data/reporting/manifests/farm_html_render.json`
- `data/reporting/manifests/farm_markdown.json`
- `data/reporting/manifests/farm_poster_render.json`
- `data/reporting/manifests/field_poster_render_<field_id>.json`

#### Target recommendation

- farm-level manifests → `data/growers/iowa-demo-grower/farms/iowa-demo-farm/manifests/`
- field-level execution traces or run logs → `fields/<field_slug>/logs/pipeline_runs.jsonl`
- dataset-specific manifests should live with the relevant dataset folders where practical

---

## 📚 Field slug strategy

Current field IDs look like:

- `OSM_1428284928`
- `OSM_998713335`
- `OSM_998706549`

Recommended first-pass field slugs:

- `osm-1428284928`
- `osm-998713335`
- `osm-998706549`
- etc.

This preserves stable machine identity while staying lowercase and URL-safe.

---

## ⚙️ Proposed `paths.py` interface

```python
from pathlib import Path

DATA_ROOT = Path(__file__).resolve().parents[2]
GROWERS_ROOT = DATA_ROOT / "growers"
SHARED_ROOT = DATA_ROOT / "shared"


def grower_dir(grower_slug: str) -> Path: ...


def farm_dir(grower_slug: str, farm_slug: str) -> Path: ...


def farm_manifest_dir(grower_slug: str, farm_slug: str) -> Path: ...


def farm_derived_dir(grower_slug: str, farm_slug: str) -> Path: ...


def farm_reports_dir(grower_slug: str, farm_slug: str) -> Path: ...


def field_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_boundary_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_boundary_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_soil_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_soil_polygon_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_soil_full_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_soil_summary_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_weather_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_weather_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_satellite_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_derived_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_reports_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def field_logs_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path: ...


def shared_cdl_dir() -> Path: ...


def shared_cdl_raster_dir() -> Path: ...


def shared_cdl_manifest_dir() -> Path: ...
```

---

## 📝 Required metadata skeletons

### `farm.json`

```json
{
  "grower_slug": "iowa-demo-grower",
  "farm_slug": "iowa-demo-farm",
  "display_name": "Iowa Demo Farm",
  "state": "IA",
  "country": "US",
  "default_crs": "EPSG:4326",
  "notes": "Primary Iowa demo farm"
}
```

### `field.json`

```json
{
  "grower_slug": "iowa-demo-grower",
  "farm_slug": "iowa-demo-farm",
  "field_slug": "osm-1428284928",
  "display_name": "OSM 1428284928",
  "field_id": "OSM_1428284928",
  "boundary_file": "boundary/field_boundary.geojson",
  "soil_file": "soil/ssurgo_soil_types.geojson",
  "weather_file": "weather/daily_weather.csv",
  "satellite_dir": "satellite/",
  "notes": "Canonical field metadata"
}
```

### Dataset `metadata.json`

```json
{
  "dataset_name": "daily_weather",
  "source": "nasa-power",
  "spatial_scope": "field",
  "grower_slug": "iowa-demo-grower",
  "farm_slug": "iowa-demo-farm",
  "field_slug": "osm-1428284928",
  "format": "csv",
  "crs": "EPSG:4326",
  "created_at": "2026-03-08T00:00:00Z",
  "updated_at": "2026-03-08T00:00:00Z",
  "producer_script": "data/scripts/ingest/download_weather.py",
  "notes": "Field-level daily weather time series"
}
```

---

## 🔍 Hard-coded path clusters to eliminate

These path families are actively hard-coded and must be replaced by helper usage:

- `data/field-boundaries/...`
- `data/soil/...`
- `data/weather/...`
- `data/cdl/...`
- `data/EDA/...`
- `data/reporting/manifests/...`

High-priority scripts for path refactor:

- `data/scripts/run_farm_pipeline.py`
- `data/scripts/11_generate_field_posters.py`
- `data/scripts/12_generate_aggregate_poster.py`
- `data/scripts/13_generate_farm_html.py`
- `data/scripts/14_generate_farm_markdown.py`
- `data/scripts/15_generate_ssurgo_cards.py`
- `data/scripts/16_generate_ssurgo_maps.py`
- `data/scripts/01_download_fields.py`
- `data/scripts/02_download_soil.py`
- `data/scripts/03_download_weather.py`
- `data/scripts/04_download_cdl.py`
- plus legacy EDA scripts `05` through `10`

---

## ⚠️ Sequencing risks to control

### Hard cutover risks

1. Move scripts before path helpers exist → import/path breakage
2. Move raw datasets before field metadata exists → pipeline loses discovery context
3. Migrate EDA outputs before deciding farm-vs-field ownership → derived outputs land in inconsistent places
4. Move SSURGO cache without updating field poster and map scripts together → posters lose multi-soil rendering again
5. Rewrite README too early → docs drift while migration is still incomplete

### Safe sequence

1. scaffold
2. helper modules
3. identity metadata
4. migrate raw/shared data
5. migrate derived outputs/manifests
6. move scripts
7. refactor paths/imports
8. pipeline verification
9. README rewrite

---

## ✅ Acceptance additions beyond the base plan

- No active script may reference `data/EDA/` after cutover
- No active script may reference `data/soil/cache/` after cutover; field-scoped soil cache paths must be used instead
- `run_farm_pipeline.py` must derive its canonical field/farm targets from metadata and helper paths, not from Iowa-specific constants alone
- The working USDA SSURGO polygon cache behavior must survive migration
- Field poster generation must still render multiple soil polygons after cutover
- Farm HTML and markdown reports must still link to the migrated outputs in their new locations

---

## 🔗 Implementation note

This draft is repo-specific and should be treated as the canonical migration companion to:

- `.sisyphus/plans/data-tree-reorganization.md`

Use this draft to avoid rediscovering the current tree or re-deriving the move map during implementation.

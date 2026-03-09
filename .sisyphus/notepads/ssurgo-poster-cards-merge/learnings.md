## 2026-03-08T16:18:00Z Task: startup-analysis

- `data/scripts/lib/manifest.py` is only a thin JSON/JSONL helper; the real stale-check and step-manifest logic lives in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py`.
- `data/scripts/run_farm_pipeline.py` currently runs six reporting scripts directly and only syncs legacy `data/EDA` outputs into canonical `data/growers/...` after all scripts finish.
- `data/scripts/reporting/generate_field_posters.py` currently renders CDL crop composition directly into the poster and leaves NDVI slots as placeholders, so Wave 3 will need both layout and content changes.
- `.opencode/skills/farm-intelligence-reporting/src/reporting.py` already defines `cdl_stacked`, `ndvi_summary`, weather, soil, and ranking panel concepts that should stay aligned with any new cached-card contract.

## 2026-03-08 Task: Define cached card asset and dependency-manifest contract

- Canonical cached card assets must live under per-field `data/growers/{grower}/{farm}/fields/{field}/derived/` outputs.
- The manifest contract uses three fingerprint types for invalidation: `input_fingerprints`, `code_fingerprints`, and `config_fingerprint`.
- Cheap assembly operations (poster/HTML/Markdown rendering) should reuse expensive cached assets rather than regenerate them.
- Incremental refresh is default; full refresh via `--force` flag regenerates all assets from upstream sources.
- SSURGO data changes infrequently and should use incremental refresh unless soil survey updates are known.
- NDVI data changes with each new satellite scene; incremental refresh respects configured date ranges in `imagery_start_date` and `imagery_end_date`.
- The stale-check logic in `pipeline.py` compares fingerprints and checks output file existence to determine step freshness.

## 2026-03-08T16:29:00Z Task: background-search-synthesis

- `scripts/rebuild_data_folder.py` is the top-level rebuild CLI, while `data/scripts/run_farm_pipeline.py` is the reporting-focused runner; both will matter once incremental/full-refresh behavior is wired through.
- Existing per-field satellite manifest placeholders already exist at `data/growers/.../satellite/sentinel/manifest.json` and `data/growers/.../satellite/landsat/manifest.json`, but they currently have empty year lists.
- Current remote-sensing config in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py` is not yet aligned with the new ask: weather covers 2021-2025, CDL covers 2021-2024, and imagery is a single 2025 season window.

## 2026-03-08T16:39:00Z Task: wave1-foundations

- `cdl_reporting.summarize_crop_history()` now trims to a rolling 5-year window by default and emits `history_*`, `predicted_next_crop`, `predicted_following_crop`, `rotation_confidence`, and `rotation_outlook` fields.
- `reporting.py` now exposes `rolling_year_window()`, `summarize_year_coverage()`, and `choose_primary_ndvi_source()` so later poster/HTML work can reason about 5-year coverage gaps and Sentinel-vs-Landsat precedence.
- `FieldReportingConfig` now advertises 5-year target tuples for weather, CDL, and imagery (`imagery_years`) even though downstream scripts still need to consume them.

## 2026-03-08T16:55:10Z Task: report-assembly-refresh

- `generate_field_posters.py` now removes the standalone CDL composition panel from the poster grid, adds crop outlook lines to the identity card, and reads cached canonical NDVI assets from `data/growers/.../derived/features/ndvi_*.png` when present.
- `generate_farm_html.py` now replaces the CDL-by-year field section with crop rotation outlook text and an NDVI card gallery sourced from canonical field assets.
- `generate_farm_markdown.py` now includes heuristic crop outlook text and NDVI card links per field, using the field inventory CSV to resolve field slugs.

## 2026-03-08T17:03:20Z Task: cdl-window-updates

- `download_cdl.py` now targets 2021-2025 rather than only 2023-2024 and writes `data/cdl/iowa_cdl_2021_2025_full_composition.csv`.
- Reporting scripts now prefer `data/cdl/iowa_cdl_2021_2025.csv` but gracefully fall back to `data/cdl/iowa_cdl_2021_2024.csv` until the new ingest output exists.
- `scripts/rebuild_data_folder.py` now aliases the rebuild pipeline to the new 2021-2025 CDL aggregate filename.

## 2026-03-08T15:35:00Z Task: ndvi-card-contract-refresh

- `generate_ndvi_cards.py` now renders canonical cached PNG assets named `ndvi_corn.png`, `ndvi_soybean.png`, and `ndvi_current_season_cumulative.png` under each field's `derived/features/` directory.
- Crop-class availability is recorded in `derived/summaries/ndvi_card_summary.json`, which makes fallback reasons auditable without opening the PNGs.
- Current-season cumulative NDVI now prefers one scene per month, with Sentinel chosen ahead of Landsat and cloud cover used as the tie-breaker within a month.
- Downstream poster, HTML, and Markdown assembly now read the new NDVI card names directly from canonical field outputs.

## 2026-03-08T16:18:20Z Task: startup-analysis

- The plan references `.sisyphus/drafts/ssurgo-poster-cards-specs.md` in multiple TODO reference sections, but that draft was deleted after the plan was finalized.
- `run_farm_pipeline.py` exposes `--force`, but individual reporting scripts still implement their own stale-check behavior and output primarily into legacy `data/EDA`, so orchestration and canonical cache behavior are not yet unified.

## 2026-03-08T16:24:10Z Task: background-search-synthesis

- `FieldReportingConfig` currently uses a 5-year weather window, a 4-year CDL window, and a single-season imagery date range, so the current code does not yet match the requested 5-year cropland + NDVI scope.
- Current field poster and HTML generators still render a CDL composition panel and only show NDVI placeholders, so the requested NDVI replacement work remains fully open.

## 2026-03-08T16:55:30Z Task: report-assembly-refresh

- The report assembly now looks for canonical NDVI assets, but there is still no completed NDVI card-generation step producing `ndvi_multi_year.png`, `ndvi_recent.png`, and `ndvi_accumulated.png` in the field `derived/features/` directories.
- The input aliases still point at `data/cdl/iowa_cdl_2021_2024.csv`, so the code now expects a 5-year semantic window but the current demo dataset still contains only 2023-2024 crop composition unless upstream ingest changes.

## 2026-03-08T15:36:00Z Task: verification-followup

- `./scripts/ci-local.sh` still fails for unrelated repo-wide checks outside this NDVI change set: markdownlint reports a duplicate `Data Source` heading in `.opencode/skills/csb-field-sampling/SKILL.md`, and link checking hits TLS `UnknownIssuer` failures on external URLs.

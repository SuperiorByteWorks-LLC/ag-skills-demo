## 2026-03-08T16:20:10Z Task: session-setup

- Using `/home/clay/dev/ag-skills-demo` as the active worktree for this plan because it is already a valid git worktree and no separate worktree was preconfigured in `boulder.json`.
- Wave 1 execution will start with a tracking-doc update task before implementation file changes so PR/issue/kanban stay in sync with repo instructions.

## 2026-03-08 Task: Define cached card asset and dependency-manifest contract

- **Decision**: Canonical reusable card assets must live under per-field `data/growers/{grower_slug}/farms/{farm_slug}/fields/{field_slug}/derived/` outputs.
- **Decision**: Poster, HTML, and Markdown assembly should reuse cached assets rather than regenerate them.
- **Decision**: The real stale-check logic lives in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py`; `data/scripts/lib/manifest.py` is JSON helper code only.
- **Decision**: Manifest invalidation uses three fingerprint fields: `input_fingerprints`, `code_fingerprints`, and `config_fingerprint`.
- **Decision**: Cheap assembly (poster/HTML rendering) is not cached; expensive generation (SSURGO, weather, CDL, satellite) is cached.
- **Decision**: Incremental refresh is default behavior; full refresh via `--force` regenerates all assets.
- **Decision**: SSURGO refresh phase uses incremental unless soil survey updates known; NDVI refresh phase respects configured date ranges.
- **Decision**: No new cache root outside canonical field outputs; all assets route through the grower/farm/field hierarchy.

## 2026-03-08T16:28:30Z Task: tracking-doc-sync

- The active tracking docs now treat the refresh phase as in progress under PR `#3` / Issue `#6` / the farm-intelligence-reporting kanban.
- Canonical cached card assets are documented as per-field `derived/` outputs, including planned NDVI files `ndvi_multi_year.png`, `ndvi_recent.png`, and `ndvi_accumulated.png`.
- The docs now lock the layout direction: remove the standalone CDL composition card, keep crop history in the first card, and add heuristic next-year/following-year crop text there.

## 2026-03-08T16:39:20Z Task: wave1-foundations

- The crop-history heuristic uses recent dominant-crop transitions within a rolling 5-year window; when direct follower history is weak, it falls back to the alternating recent pattern or repeats the current crop with low confidence.
- Sentinel is the preferred primary NDVI source when Sentinel and Landsat tie on cloud cover and target-date distance; Landsat remains available for coverage filling.
- The 5-year target is now encoded at the configuration level for weather, CDL, and imagery, but downstream generation scripts still need to adopt those config values explicitly.

## 2026-03-08T17:03:40Z Task: cdl-window-updates

- Reporting generators now prefer a 2021-2025 CDL aggregate file but retain a fallback reader for the existing 2021-2024 demo artifact so the current repo stays runnable during transition.
- The rebuild path is standardized around `iowa_cdl_2021_2025_full_composition.csv` / `iowa_cdl_2021_2025.csv` to align filenames with the requested 5-year cropland window.

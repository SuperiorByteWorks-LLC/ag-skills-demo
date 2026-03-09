# Context Pack

## Scope
- Tier: quick
- Diff strategy: working-tree-vs-head
- Base ref: HEAD
- Merge base: HEAD

## Recent commits
- e255ad6 docs(maturity): record county weather checkpoint
- f5fd7b4 chore(weather): record county weather outputs
- 1d97d4f feat(weather): add county fips transform script
- 6440bed feat(maturity): add county weather aggregation helpers
- bbae2aa docs(maturity): sync bridge checkpoint records

## Local CI summary markdown
# Local CI Summary

Generated: 2026-03-09T03:24:49Z

## ✅ Validate Environment

- format/lint/typecheck/commitlint steps are tracked in the table below

## ✅ Test & Build

- test-docs-links: completed (see `link-check-report.md`)

## 🚀 Deploy

- deploy-preview: skip
- deploy-production: skip

## 🤖 CrewAI Review

- crewai-review: pending

## 📊 Step table

| Step | Status | Duration |
| --- | --- | --- |
| Prettier Format | pass | 3s |
| ESLint | pass | 1s |
| Markdownlint | fail | 2s |
| Stylelint | pass | 1s |
| Ruff Lint | pass | 0s |
| Ruff Format | pass | 0s |
| Commitlint | warn | 0s |
| TypeScript | skip | 0s |
| Link Check | fail | 4s |
| CrewAI Tests | pass | 3s |
| Website Build | pass | 0s |
| Preview Deploy | skip | 0s |
| Production Deploy | skip | 0s |


## Docs link-check summary markdown
# Docs Link Check Summary

Generated: 2026-03-09T03:24:46Z

⚠️ Link check reported issues.

- Internal checker: fail
- Lychee checker: fail
- Report file: `link-check-report.md`
- Status: fail


## Docs link-check report markdown
# Documentation Link Check Report

Generated: 2026-03-09T03:24:46Z

- Internal markdown checker: fail
- Lychee checker: fail

## Internal markdown checker

# Internal Markdown Link Check

Files scanned: 131
Links checked: 854
Broken links: 118

| Source file | Link target | Error |
| --- | --- | --- |
| `README.md` | `../LICENSE` | missing file |
| `AGENTS.md` | `data/sql/README.md` | missing file |
| `services/README.md` | `../data/sql/` | missing file |
| `apps/README.md` | `../data/sql/` | missing file |
| `src/README.md` | `../data/sql/` | missing file |
| `.opencode/skills/nasa-power-weather/SKILL.md` | `../.skills/field-boundaries/` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_01.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_01_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_01_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_02.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_02_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_02_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_03.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_03_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_03_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_04.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_04_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_04_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_05.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_05_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_05_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_06.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_06_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_06_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_07.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_07_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_07_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_08.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_08_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_08_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_09.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_09_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_09_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/iowa_field_poster_10.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_10_texture.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./soil_cards/field_10_properties.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_corn.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_soybean.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/summaries/iowa_farm_report.md` | `./field_cards/` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/reports/iowa_farm_report.md` | `./field_cards/` | missing file |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/reports/iowa_farm_report.md` | `./soil_cards/` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_01.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_02.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_03.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_04.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_05.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_06.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_07.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_08.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_09.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_10.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_corn.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_soybean.png` | missing file |
| `data/reporting/legacy-backfill/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `docs/project/issues/issue-00000007-build-maturity-by-fips-pipeline.md` | `../../.sisyphus/plans/grm-by-fips-geoadmin.md` | missing file |
| `docs/project/pr/pr-00000004-build-maturity-by-fips-pipeline.md` | `../../.sisyphus/plans/grm-by-fips-geoadmin.md` | missing file |
| `docs/project/kanban/project-maturity-by-fips.md` | `../../.sisyphus/plans/grm-by-fips-geoadmin.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/issues/issue-00000001-agentic-documentation-system.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/issues/issue-00000005-cloudflare-deploy-follow-up.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |

## Lychee checker

# Summary

| Status         | Count |
|----------------|-------|
| 🔍 Total       | 837   |
| ✅ Successful  | 91    |
| ⏳ Timeouts    | 0     |
| 🔀 Redirected  | 21    |
| 👻 Excluded    | 713   |
| ❓ Unknown     | 0     |
| 🚫 Errors      | 12    |
| ⛔ Unsupported | 0     |

## Errors per input

### Errors in .opencode/skills/cdl-cropland/SKILL.md

* [ERROR] <https://nassgeodata.gmu.edu/CropScape/> | Network error: SSL certificate not trusted. Use --insecure if site is trusted (error sending request for url (https://nassgeodata.gmu.edu/CropScape/)): SSL certificate not trusted. Use --insecure if site is trusted

### Errors in .opencode/skills/nasa-power-weather/SKILL.md

* [404] <https://power.larc.nasa.gov/docs/methodology/communities/ag/> | Rejected status code: 404 Not Found (configurable with "accept" option)
* [404] <https://www.extension.umn.edu/agriculture/climate/growing-degree-days/> | Rejected status code: 404 Not Found (configurable with "accept" option)

### Errors in .opencode/skills/ssurgo-soil/SKILL.md

* [400] <https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest> | Rejected status code: 400 Bad Request (configurable with "accept" option)
* [ERROR] <https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo> | Network error: HTTP/2 protocol error. Server may not support HTTP/2 properly (error sending request for url (https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo)): HTTP/2 protocol error. Server may not support HTTP/2 properly

### Errors in docs/project/plans/ag-source-monitor-phase-2.md

* [404] <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2> | Rejected status code: 404 Not Found (configurable with "accept" option)

### Errors in docs/project/plans/farm-intelligence-reporting-prd.md

* [404] <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2> | Rejected status code: 404 Not Found (configurable with "accept" option)
* [ERROR] <https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo> | Network error: HTTP/2 protocol error. Server may not support HTTP/2 properly (error sending request for url (https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo)): HTTP/2 protocol error. Server may not support HTTP/2 properly

### Errors in docs/project/pr/pr-00000002-import-ag-skills.md

* [404] <https://github.com/SuperiorByteWorks-LLC/ag-skills-demo/pull/2> | Rejected status code: 404 Not Found (configurable with "accept" option)



## Changed file snapshots
- Read changed_files_index.json for full mapping
- Read only the specific file snapshots you need from changed_files/
- This avoids loading all code/diffs into context at once

## Diff excerpt
[DIFF BEGIN]
diff --git a/.crewai/workspace/changed_files/001_.ci-local.lock.patch.diff b/.crewai/workspace/changed_files/001_.ci-local.lock.patch.diff
deleted file mode 100644
index 97041bb..0000000
--- a/.crewai/workspace/changed_files/001_.ci-local.lock.patch.diff
+++ /dev/null
@@ -1,7 +0,0 @@
-diff --git a/.ci-local.lock b/.ci-local.lock
-index 1ce2524..c6ec760 100644
---- a/.ci-local.lock
-+++ b/.ci-local.lock
-@@ -1 +1 @@
--pid=4652 started=2026-03-08T00:39:18Z cwd=/workspaces/ag-skills-demo
-+pid=4031240 started=2026-03-08T19:31:07Z cwd=/home/clay/dev/ag-skills-demo
diff --git a/.crewai/workspace/changed_files/002_.crewai_workspace_ci_results_core-ci_summary.md.patch.diff b/.crewai/workspace/changed_files/002_.crewai_workspace_ci_results_core-ci_summary.md.patch.diff
deleted file mode 100644
index 00c9ae5..0000000
--- a/.crewai/workspace/changed_files/002_.crewai_workspace_ci_results_core-ci_summary.md.patch.diff
+++ /dev/null
@@ -1,38 +0,0 @@
-diff --git a/.crewai/workspace/ci_results/core-ci/summary.md b/.crewai/workspace/ci_results/core-ci/summary.md
-index c0e5f73..34153d4 100644
---- a/.crewai/workspace/ci_results/core-ci/summary.md
-+++ b/.crewai/workspace/ci_results/core-ci/summary.md
-@@ -1,6 +1,6 @@
- # Local CI Summary
- 
--Generated: 2026-03-08T00:40:12Z
-+Generated: 2026-03-08T19:31:24Z
- 
- ## ✅ Validate Environment
- 
-@@ -23,15 +23,16 @@ Generated: 2026-03-08T00:40:12Z
- 
- | Step | Status | Duration |
- | --- | --- | --- |
--| Prettier Format | pass | 13s |
--| ESLint | pass | 5s |
--| Markdownlint | pass | 3s |
--| Stylelint | pass | 2s |
--| Ruff | skip | 0s |
--| Commitlint | warn | 4s |
-+| Prettier Format | pass | 2s |
-+| ESLint | pass | 2s |
-+| Markdownlint | fail | 1s |
-+| Stylelint | pass | 1s |
-+| Ruff Lint | pass | 0s |
-+| Ruff Format | pass | 0s |
-+| Commitlint | warn | 1s |
- | TypeScript | skip | 0s |
--| Link Check | fail | 9s |
--| CrewAI Tests | fail | 10s |
--| Website Build | pass | 3s |
-+| Link Check | fail | 5s |
-+| CrewAI Tests | pass | 3s |
-+| Website Build | pass | 0s |
- | Preview Deploy | skip | 0s |
- | Production Deploy | skip | 0s |
diff --git a/.crewai/workspace/changed_files/003_.crewai_workspace_ci_results_test-crewai_summary.md.patch.diff b/.crewai/workspace/changed_files/003_.crewai_workspace_ci_results_test-crewai_summary.md.patch.diff
deleted file mode 100644
index 23ac7fb..0000000
--- a/.crewai/workspace/changed_files/003_.crewai_workspace_ci_results_test-crewai_summary.md.patch.diff
+++ /dev/null
@@ -1,11 +0,0 @@
-diff --git a/.crewai/workspace/ci_results/test-crewai/summary.md b/.crewai/workspace/ci_results/test-crewai/summary.md
-index bd60110..68ff9e3 100644
---- a/.crewai/workspace/ci_results/test-crewai/summary.md
-+++ b/.crewai/workspace/ci_results/test-crewai/summary.md
-@@ -1,4 +1,4 @@
- # CrewAI tests summary
- 
--- status: fail
--- duration: 10s
-+- status: pass
-+- duration: 3s
diff --git a/.crewai/workspace/changed_files/004_.crewai_workspace_ci_results_test-docs-links_summary.md.patch.diff b/.crewai/workspace/changed_files/004_.crewai_workspace_ci_results_test-docs-links_summary.md.patch.diff
deleted file mode 100644
index ba0353d..0000000
--- a/.crewai/workspace/changed_files/004_.crewai_workspace_ci_results_test-docs-links_summary.md.patch.diff
+++ /dev/null
@@ -1,12 +0,0 @@
-diff --git a/.crewai/workspace/ci_results/test-docs-links/summary.md b/.crewai/workspace/ci_results/test-docs-links/summary.md
-index 79906c6..4410ac2 100644
---- a/.crewai/workspace/ci_results/test-docs-links/summary.md
-+++ b/.crewai/workspace/ci_results/test-docs-links/summary.md
-@@ -1,6 +1,6 @@
- # Docs Link Check Summary
- 
--Generated: 2026-03-08T00:39:59Z
-+Generated: 2026-03-08T19:31:21Z
- 
- ⚠️ Link check reported issues.
- 
diff --git a/.crewai/workspace/changed_files/005_.crewai_workspace_ci_results_test-website_summary.md.patch.diff b/.crewai/workspace/changed_files/005_.crewai_workspace_ci_results_test-website_summary.md.patch.diff
deleted file mode 100644
index 28513e7..0000000
--- a/.crewai/workspace/changed_files/005_.crewai_workspace_ci_results_test-website_summary.md.patch.diff
+++ /dev/null
@@ -1,10 +0,0 @@
-diff --git a/.crewai/workspace/ci_results/test-website/summary.md b/.crewai/workspace/ci_results/test-website/summary.md
-index 51fa6a2..b42c4fe 100644
---- a/.crewai/workspace/ci_results/test-website/summary.md
-+++ b/.crewai/workspace/ci_results/test-website/summary.md
-@@ -1,4 +1,4 @@
- # Website test/build summary
- 
- - status: pass
--- duration: 3s
-+- duration: 0s
diff --git a/.crewai/workspace/changed_files/006_.crewai_workspace_link-check-internal.md.patch.diff b/.crewai/workspace/changed_files/006_.crewai_workspace_link-check-internal.md.patch.diff
deleted file mode 100644
index e0e0a93..0000000
--- a/.crewai/workspace/changed_files/006_.crewai_workspace_link-check-internal.md.patch.diff
+++ /dev/null
@@ -1,125 +0,0 @@
-diff --git a/.crewai/workspace/link-check-internal.md b/.crewai/workspace/link-check-internal.md
-index 92886d5..f041cd0 100644
---- a/.crewai/workspace/link-check-internal.md
-+++ b/.crewai/workspace/link-check-internal.md
-@@ -1,16 +1,121 @@
- # Internal Markdown Link Check
- 
--Files scanned: 103
--Links checked: 616
--Broken links: 8
-+Files scanned: 121
-+Links checked: 753
-+Broken links: 113
- 
- | Source file | Link target | Error |
- | --- | --- | --- |
--| `README.md` | `CONTRIBUTING.md` | missing file |
-+| `README.md` | `../LICENSE` | missing file |
-+| `AGENTS.md` | `data/sql/README.md` | missing file |
-+| `services/README.md` | `../data/sql/` | missing file |
-+| `apps/README.md` | `../data/sql/` | missing file |
-+| `src/README.md` | `../data/sql/` | missing file |
-+| `.opencode/skills/nasa-power-weather/SKILL.md` | `../.skills/field-boundaries/` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_01.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_corn.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_soybean.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_current_season_cumulative.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_02.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_corn.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_soybean.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_current_season_cumulative.png` | missing file |
-+| `data/EDA/iowa_farm_report.md` | `./f
...
ablish data quality baselines
@@ -1542,6 +1544,7 @@ class HyperCareProtocol:
 - [ ] Create rollback procedures
 
 ### During Migration
+
 - [ ] Run migrations with dry-run mode first
 - [ ] Process in batches with checkpoints
 - [ ] Validate at all four layers (volume, structure, content, application)
@@ -1550,6 +1553,7 @@ class HyperCareProtocol:
 - [ ] Log all operations with checksums
 
 ### Post-Migration
+
 - [ ] Execute full validation suite
 - [ ] Activate hyper-care period (2-4 weeks)
 - [ ] Compare business reports between systems
@@ -1558,6 +1562,7 @@ class HyperCareProtocol:
 - [ ] Plan legacy system decommissioning
 
 ### CI/CD Integration
+
 - [ ] Implement migration safety checks in CI
 - [ ] Require checksum verification before deployment
 - [ ] Set up environment promotion gates
@@ -1575,11 +1580,3 @@ class HyperCareProtocol:
 [^3]: [Guardrails for CI/CD: Database governance for consistency, quality, and security](https://www.liquibase.com/blog/guardrails-ci-cd), Liquibase, April 2024
 
 [^4]: [How to Add Database Migration Checks to Your CI/CD Pipeline](https://dev.to/mickelsamuel/how-to-add-database-migration-checks-to-your-cicd-pipeline-lm9), DEV Community, March 2026
-
-[^5]: [Data Migration Best Practices: Your Ultimate Guide for 2026](https://medium.com/@kanerika/data-migration-best-practices-your-ultimate-guide-for-2026-7cbd5594d92e), Kanerika Inc, December 2025
-
-[^6]: [Zero-Downtime Migration (ZDM): Guide to Migrating Critical Systems](https://insights.daffodilsw.com/blog/zero-downtime-migration-zdm-guide-to-migrating-critical-systems), Daffodil Software, February 2026
-
-[^7]: [How to Implement Idempotent Data Pipelines in GCP](https://oneuptime.com/blog/post/2026-02-17-how-to-implement-idempotent-data-pipelines-in-gcp-to-handle-retry-safe-processing/view), OneUptime, February 2026
-
-[^8]: [Data Migration Trends and Best Practices for 2026](https://www.techment.com/blogs/data-migration-trends-best-practices-2026/), Techment, January 2026
diff --git a/tests/farm_intelligence/test_pipeline.py b/tests/farm_intelligence/test_pipeline.py
index 1f433ad..82651bd 100644
--- a/tests/farm_intelligence/test_pipeline.py
+++ b/tests/farm_intelligence/test_pipeline.py
@@ -452,6 +452,91 @@ def test_aggregate_weather_to_counties_groups_by_fips_and_date():
     assert result.loc[0, "source_field_slugs"] == ["field-1", "field-2"]
 
 
+def test_compute_county_gdd_applies_base_and_ceiling():
+    import pandas as pd
+
+    county_weather = pd.DataFrame(
+        [
+            {
+                "date": "2025-06-01",
+                "year": 2025,
+                "fips": "19015",
+                "state_fips": "19",
+                "county_fips": "015",
+                "county_name": "Boone",
+                "county_name_full": "Boone County",
+                "field_count": 2,
+                "T2M_MAX": 35.0,
+                "T2M_MIN": 8.0,
+            },
+            {
+                "date": "2025-06-02",
+                "year": 2025,
+                "fips": "19015",
+                "state_fips": "19",
+                "county_fips": "015",
+                "county_name": "Boone",
+                "county_name_full": "Boone County",
+                "field_count": 2,
+                "T2M_MAX": 20.0,
+                "T2M_MIN": 12.0,
+            },
+        ]
+    )
+
+    result = mbf.compute_county_gdd(county_weather)
+    assert list(result["fips"]) == ["19015"]
+    assert result.loc[0, "observation_days"] == 2
+    assert result.loc[0, "field_count_max"] == 2
+    assert result.loc[0, "gdd_total_c"] == 16.0
+
+
+def test_compute_corn_rm_adds_banding():
+    import pandas as pd
+
+    county_gdd = pd.DataFrame(
+        [
+            {
+                "year": 2025,
+                "fips": "19015",
+                "state_fips": "19",
+                "county_fips": "015",
+                "county_name": "Boone",
+                "county_name_full": "Boone County",
+                "gdd_total_c": 2200.0,
+            }
+        ]
+    )
+
+    result = mbf.compute_corn_rm(county_gdd)
+    assert result.loc[0, "rm_relative_maturity"] == 110.0
+    assert result.loc[0, "rm_band"] == 110
+
+
+def test_compute_soybean_mg_uses_centroid_latitude():
+    import pandas as pd
+
+    county_lookup = pd.DataFrame([{"fips": "19015", "centroid_lat": 41.7}])
+    county_gdd = pd.DataFrame(
+        [
+            {
+                "year": 2025,
+                "fips": "19015",
+                "state_fips": "19",
+                "county_fips": "015",
+                "county_name": "Boone",
+                "county_name_full": "Boone County",
+                "gdd_total_c": 2200.0,
+            }
+        ]
+    )
+
+    result = mbf.compute_soybean_mg(county_lookup, county_gdd)
+    assert result.loc[0, "mg_optimal"] == 2.9
+    assert result.loc[0, "mg_early"] == 2.5
+    assert result.loc[0, "mg_late"] == 3.3
+
+
 def test_crop_years_returns_sorted_matches():
     import pandas as pd
 

[DIFF END]

## Persistent review memory
## Learned Patterns About This Codebase
- Do not flag placeholder secrets in .env.example files when values are clearly fake examples and no real credentials are present. (confidence: 1.0)

## Active Review Suppressions
Do NOT flag these patterns, the team has marked them acceptable:
- hardcoded URL in example file (files: agentic/mermaid_diagrams/*.md) - These are intentional documentation examples, not production code
- placeholder api keys and tokens (files: *.env.example) - Placeholder credentials in .env.example templates are acceptable when they are clearly fake and no real secrets are committed.

# Context Pack

## Scope
- Tier: quick
- Diff strategy: working-tree-vs-head
- Base ref: HEAD
- Merge base: HEAD

## Recent commits
- 6b27a8a feat(ssurgo-features): export per-field choropleth feature maps
- efe6e02 fix(ssurgo-reporting): restore real soil variation and improve map presentation
- 85af4b8 feat(ssurgo-maps): switch to clipped natural-breaks choropleth styling
- cd69fbd fix(reporting): include soil maps and farm summary assets in canonical outputs
- 268c7f9 feat(farm-data-rebuild): add single orchestrator skill for deterministic rebuild

## Local CI summary markdown
# Local CI Summary

Generated: 2026-03-08T19:31:24Z

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
| Prettier Format | pass | 2s |
| ESLint | pass | 2s |
| Markdownlint | fail | 1s |
| Stylelint | pass | 1s |
| Ruff Lint | pass | 0s |
| Ruff Format | pass | 0s |
| Commitlint | warn | 1s |
| TypeScript | skip | 0s |
| Link Check | fail | 5s |
| CrewAI Tests | pass | 3s |
| Website Build | pass | 0s |
| Preview Deploy | skip | 0s |
| Production Deploy | skip | 0s |


## Docs link-check summary markdown
# Docs Link Check Summary

Generated: 2026-03-08T19:31:21Z

⚠️ Link check reported issues.

- Internal checker: fail
- Lychee checker: fail
- Report file: `link-check-report.md`
- Status: fail


## Docs link-check report markdown
# Documentation Link Check Report

Generated: 2026-03-08T19:31:21Z

- Internal markdown checker: fail
- Lychee checker: fail

## Internal markdown checker

# Internal Markdown Link Check

Files scanned: 121
Links checked: 753
Broken links: 113

| Source file | Link target | Error |
| --- | --- | --- |
| `README.md` | `../LICENSE` | missing file |
| `AGENTS.md` | `data/sql/README.md` | missing file |
| `services/README.md` | `../data/sql/` | missing file |
| `apps/README.md` | `../data/sql/` | missing file |
| `src/README.md` | `../data/sql/` | missing file |
| `.opencode/skills/nasa-power-weather/SKILL.md` | `../.skills/field-boundaries/` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_01.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_02.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_03.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_04.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_05.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_06.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_07.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706550/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_08.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713335/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_09.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713337/derived/features/ndvi_current_season_cumulative.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_10.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_corn.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_soybean.png` | missing file |
| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998713346/derived/features/ndvi_current_season_cumulative.png` | missing file |
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
| 🔍 Total       | 737   |
| ✅ Successful  | 83    |
| ⏳ Timeouts    | 0     |
| 🔀 Redirected  | 21    |
| 👻 Excluded    | 621   |
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
diff --git a/.ci-local.lock b/.ci-local.lock
index 1ce2524..c6ec760 100644
--- a/.ci-local.lock
+++ b/.ci-local.lock
@@ -1 +1 @@
-pid=4652 started=2026-03-08T00:39:18Z cwd=/workspaces/ag-skills-demo
+pid=4031240 started=2026-03-08T19:31:07Z cwd=/home/clay/dev/ag-skills-demo
diff --git a/.crewai/workspace/ci_results/core-ci/summary.md b/.crewai/workspace/ci_results/core-ci/summary.md
index c0e5f73..34153d4 100644
--- a/.crewai/workspace/ci_results/core-ci/summary.md
+++ b/.crewai/workspace/ci_results/core-ci/summary.md
@@ -1,6 +1,6 @@
 # Local CI Summary
 
-Generated: 2026-03-08T00:40:12Z
+Generated: 2026-03-08T19:31:24Z
 
 ## ✅ Validate Environment
 
@@ -23,15 +23,16 @@ Generated: 2026-03-08T00:40:12Z
 
 | Step | Status | Duration |
 | --- | --- | --- |
-| Prettier Format | pass | 13s |
-| ESLint | pass | 5s |
-| Markdownlint | pass | 3s |
-| Stylelint | pass | 2s |
-| Ruff | skip | 0s |
-| Commitlint | warn | 4s |
+| Prettier Format | pass | 2s |
+| ESLint | pass | 2s |
+| Markdownlint | fail | 1s |
+| Stylelint | pass | 1s |
+| Ruff Lint | pass | 0s |
+| Ruff Format | pass | 0s |
+| Commitlint | warn | 1s |
 | TypeScript | skip | 0s |
-| Link Check | fail | 9s |
-| CrewAI Tests | fail | 10s |
-| Website Build | pass | 3s |
+| Link Check | fail | 5s |
+| CrewAI Tests | pass | 3s |
+| Website Build | pass | 0s |
 | Preview Deploy | skip | 0s |
 | Production Deploy | skip | 0s |
diff --git a/.crewai/workspace/ci_results/test-crewai/summary.md b/.crewai/workspace/ci_results/test-crewai/summary.md
index bd60110..68ff9e3 100644
--- a/.crewai/workspace/ci_results/test-crewai/summary.md
+++ b/.crewai/workspace/ci_results/test-crewai/summary.md
@@ -1,4 +1,4 @@
 # CrewAI tests summary
 
-- status: fail
-- duration: 10s
+- status: pass
+- duration: 3s
diff --git a/.crewai/workspace/ci_results/test-docs-links/summary.md b/.crewai/workspace/ci_results/test-docs-links/summary.md
index 79906c6..4410ac2 100644
--- a/.crewai/workspace/ci_results/test-docs-links/summary.md
+++ b/.crewai/workspace/ci_results/test-docs-links/summary.md
@@ -1,6 +1,6 @@
 # Docs Link Check Summary
 
-Generated: 2026-03-08T00:39:59Z
+Generated: 2026-03-08T19:31:21Z
 
 ⚠️ Link check reported issues.
 
diff --git a/.crewai/workspace/ci_results/test-website/summary.md b/.crewai/workspace/ci_results/test-website/summary.md
index 51fa6a2..b42c4fe 100644
--- a/.crewai/workspace/ci_results/test-website/summary.md
+++ b/.crewai/workspace/ci_results/test-website/summary.md
@@ -1,4 +1,4 @@
 # Website test/build summary
 
 - status: pass
-- duration: 3s
+- duration: 0s
diff --git a/.crewai/workspace/link-check-internal.md b/.crewai/workspace/link-check-internal.md
index 92886d5..f041cd0 100644
--- a/.crewai/workspace/link-check-internal.md
+++ b/.crewai/workspace/link-check-internal.md
@@ -1,16 +1,121 @@
 # Internal Markdown Link Check
 
-Files scanned: 103
-Links checked: 616
-Broken links: 8
+Files scanned: 121
+Links checked: 753
+Broken links: 113
 
 | Source file | Link target | Error |
 | --- | --- | --- |
-| `README.md` | `CONTRIBUTING.md` | missing file |
+| `README.md` | `../LICENSE` | missing file |
+| `AGENTS.md` | `data/sql/README.md` | missing file |
+| `services/README.md` | `../data/sql/` | missing file |
+| `apps/README.md` | `../data/sql/` | missing file |
+| `src/README.md` | `../data/sql/` | missing file |
+| `.opencode/skills/nasa-power-weather/SKILL.md` | `../.skills/field-boundaries/` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_01.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1428284928/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_02.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730614/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_03.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-1434730620/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_04.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998701371/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_05.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706547/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_field_poster_06.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_corn.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_soybean.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./growers/iowa-demo-grower/farms/iowa-demo-farm/fields/osm-998706549/derived/features/ndvi_current_season_cumulative.png` | missing file |
+| `data/EDA/iowa_farm_report.md` | `./field_cards/iowa_
...
"] == 2020
+    assert row["history_end_year"] == 2024
+    assert row["history_years"] == 5
+    assert row["rotation_sequence"] == "Soybeans -> Corn -> Soybeans -> Corn -> Soybeans"
+
+
+def test_summarize_crop_history_adds_rotation_outlook():
+    import pandas as pd
+
+    crop_mix = pd.DataFrame(
+        {
+            "field_id": ["F1"] * 5,
+            "year": [2020, 2021, 2022, 2023, 2024],
+            "crop_name": ["Corn", "Soybeans", "Corn", "Soybeans", "Corn"],
+            "pct": [95.0, 95.0, 95.0, 95.0, 95.0],
+        }
+    )
+
+    result = cdl.summarize_crop_history(crop_mix)
+    row = result.iloc[0]
+    assert row["predicted_next_crop"] == "Soybeans"
+    assert row["predicted_following_crop"] == "Corn"
+    assert row["rotation_confidence"] in {"medium", "high"}
+    assert "Heuristic outlook" in row["rotation_outlook"]
+
+
+def test_growing_season_range_uses_expected_window():
+    assert si.growing_season_range(2024) == "2024-03-01T00:00:00Z/2024-11-30T23:59:59Z"
+
+
+def test_feature_datetime_and_cloud_cover_helpers():
+    feature = {
+        "properties": {
+            "datetime": "2025-07-10T16:15:00Z",
+            "eo:cloud_cover": 12.5,
+        }
+    }
+    assert si.feature_datetime(feature).date().isoformat() == "2025-07-10"
+    assert si.feature_cloud_cover(feature) == 12.5
+
+
+def test_sentinel_asset_keys_accept_named_and_band_assets():
+    named = {"assets": {"red": {}, "nir": {}, "scl": {}}}
+    fallback = {"assets": {"B04": {}, "B08": {}, "SCL": {}}}
+    assert si.sentinel_asset_keys(named) == {"red": "red", "nir": "nir", "scl": "scl"}
+    assert si.sentinel_asset_keys(fallback) == {"red": "B04", "nir": "B08", "scl": "SCL"}
+
+
+def test_landsat_asset_keys_match_planetary_computer_assets():
+    feature = {"assets": {"red": {}, "nir08": {}, "qa_pixel": {}}}
+    assert si.landsat_asset_keys(feature) == {"red": "red", "nir": "nir08", "qa": "qa_pixel"}
+
+
+def test_normalize_year_entry_migrates_legacy_single_scene_shape():
+    legacy = {
+        "year": 2024,
+        "scene_id": "scene-1",
+        "scene_date": "2024-07-10",
+        "cloud_cover": 4.2,
+        "status": "complete",
+        "raw_tiffs": {"red": "red.tif"},
+        "ndvi_tif": "ndvi.tif",
+    }
+    normalized = dsi._normalize_year_entry(legacy)
+    assert normalized["scene_count"] == 1
+    assert len(normalized["scenes"]) == 1
+    assert normalized["scenes"][0]["scene_id"] == "scene-1"
+
+
+def test_select_scene_inventory_prefers_best_scene_per_month():
+    features = [
+        {"id": "a", "properties": {"datetime": "2024-06-10T00:00:00Z", "eo:cloud_cover": 10.0}},
+        {"id": "b", "properties": {"datetime": "2024-06-20T00:00:00Z", "eo:cloud_cover": 5.0}},
+        {"id": "c", "properties": {"datetime": "2024-07-05T00:00:00Z", "eo:cloud_cover": 7.0}},
+    ]
+    selected = dsi._select_scene_inventory(features, max_scenes_per_year=9)
+    assert [feature["id"] for feature in selected] == ["b", "c"]
+
+
+def test_preferred_cdl_full_composition_path_uses_available_canonical_file():
+    preferred = paths.shared_cdl_preferred_full_composition_path()
+    assert preferred.parent == paths.shared_cdl_tables_dir()
+
+
+def test_dominant_crop_lookup_uses_highest_pct_by_year(tmp_path):
+    crop_csv = tmp_path / "crop.csv"
+    crop_csv.write_text(
+        "field_id,year,crop_name,pct\nF1,2024,Corn,40\nF1,2024,Soybeans,60\nF1,2023,Corn,70\n",
+        encoding="utf-8",
+    )
+    result = dnc._dominant_crop_lookup(crop_csv)
+    assert result[("F1", 2024)] == "Soybeans"
+    assert result[("F1", 2023)] == "Corn"
+
+
+def test_crop_years_returns_sorted_matches():
+    import pandas as pd
+
+    join_df = pd.DataFrame(
+        {
+            "crop_name": ["Soybeans", "Corn", "Corn", "Unknown"],
+            "year": [2023, 2024, 2022, 2025],
+        }
+    )
+    assert gnc._crop_years(join_df, "Corn") == [2022, 2024]
+    assert gnc._crop_years(join_df, "Soybeans") == [2023]
+
+
+def test_select_current_season_scenes_prefers_sentinel_then_lower_cloud():
+    import pandas as pd
+
+    rows = [
+        {
+            "sensor": "landsat",
+            "scene_date": pd.Timestamp("2025-06-12"),
+            "cloud_cover": 1.0,
+            "month": 6,
+        },
+        {
+            "sensor": "sentinel",
+            "scene_date": pd.Timestamp("2025-06-08"),
+            "cloud_cover": 12.0,
+            "month": 6,
+        },
+        {
+            "sensor": "sentinel",
+            "scene_date": pd.Timestamp("2025-07-03"),
+            "cloud_cover": 8.0,
+            "month": 7,
+        },
+        {
+            "sensor": "sentinel",
+            "scene_date": pd.Timestamp("2025-07-20"),
+            "cloud_cover": 2.0,
+            "month": 7,
+        },
+    ]
+    selected = gnc._select_current_season_scenes(rows)
+    assert [(row["sensor"], row["month"], row["cloud_cover"]) for row in selected] == [
+        ("sentinel", 6, 12.0),
+        ("sentinel", 7, 2.0),
+    ]

[DIFF END]

## Persistent review memory
## Learned Patterns About This Codebase
- Do not flag placeholder secrets in .env.example files when values are clearly fake examples and no real credentials are present. (confidence: 1.0)

## Active Review Suppressions
Do NOT flag these patterns, the team has marked them acceptable:
- hardcoded URL in example file (files: agentic/mermaid_diagrams/*.md) - These are intentional documentation examples, not production code
- placeholder api keys and tokens (files: *.env.example) - Placeholder credentials in .env.example templates are acceptable when they are clearly fake and no real secrets are committed.

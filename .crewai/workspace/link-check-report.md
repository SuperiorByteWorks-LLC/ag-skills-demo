# Documentation Link Check Report

Generated: 2026-03-08T00:39:59Z

- Internal markdown checker: fail
- Lychee checker: fail

## Internal markdown checker

# Internal Markdown Link Check

Files scanned: 103
Links checked: 616
Broken links: 8

| Source file | Link target | Error |
| --- | --- | --- |
| `README.md` | `CONTRIBUTING.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/issues/issue-00000001-agentic-documentation-system.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/issues/issue-00000005-cloudflare-deploy-follow-up.md` | missing file |
| `docs/project/kanban/project-cloudflare-pages-deploy.md` | `../../docs/project/pr/pr-00000001-agentic-docs-and-monorepo-modernization.md` | missing file |
| `.opencode/skills/nasa-power-weather/SKILL.md` | `../.skills/field-boundaries/` | missing file |

## Lychee checker

# Summary

| Status         | Count |
|----------------|-------|
| 🔍 Total       | 624   |
| ✅ Successful  | 82    |
| ⏳ Timeouts    | 0     |
| 🔀 Redirected  | 23    |
| 👻 Excluded    | 511   |
| ❓ Unknown     | 0     |
| 🚫 Errors      | 8     |
| ⛔ Unsupported | 0     |

## Errors per input

### Errors in .opencode/skills/cdl-cropland/SKILL.md

* [ERROR] <https://nassgeodata.gmu.edu/CropScape/> | Network error: SSL certificate not trusted. Use --insecure if site is trusted (error sending request for url (https://nassgeodata.gmu.edu/CropScape/)): SSL certificate not trusted. Use --insecure if site is trusted

### Errors in .opencode/skills/nasa-power-weather/SKILL.md

* [404] <https://power.larc.nasa.gov/docs/methodology/communities/ag/> | Rejected status code: 404 Not Found (configurable with "accept" option)
* [404] <https://www.extension.umn.edu/agriculture/climate/growing-degree-days/> | Rejected status code: 404 Not Found (configurable with "accept" option)

### Errors in .opencode/skills/sentinel2-imagery/SKILL.md

* [404] <https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi> | Rejected status code: 404 Not Found (configurable with "accept" option)

### Errors in .opencode/skills/ssurgo-soil/SKILL.md

* [400] <https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest> | Rejected status code: 400 Bad Request (configurable with "accept" option)
* [ERROR] <https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo> | Network error: HTTP/2 protocol error. Server may not support HTTP/2 properly (error sending request for url (https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo)): HTTP/2 protocol error. Server may not support HTTP/2 properly

### Errors in data/weather/README.md

* [422] <https://power.larc.nasa.gov/api/temporal/daily/point> | Rejected status code: 422 Unprocessable Entity (configurable with "accept" option)

### Errors in docs/project/pr/pr-00000002-import-ag-skills.md

* [404] <https://github.com/SuperiorByteWorks-LLC/ag-skills-demo/pull/2> | Rejected status code: 404 Not Found (configurable with "accept" option)


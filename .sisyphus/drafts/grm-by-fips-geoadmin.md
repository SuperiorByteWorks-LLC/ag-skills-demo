# Draft: GRM by FIPS and geoadmin pipeline

## Requirements (confirmed)

- [goal]: Build a GRM/RM calculation pipeline by FIPS using weather-driven GDD accumulation and county-level mapping outputs.
- [goal-expansion]: Scope now includes annual corn RM by FIPS plus soybean MG by FIPS in one maturity pipeline.
- [geoadmin]: Add shared geoadmin infrastructure with Level 0 countries, Level 1 states, and Level 2 USA counties/FIPS polygon data.
- [integration]: Integrate geoadmin assignment into field metadata so fields can be linked to counties/FIPS via centroid or equivalent spatial assignment.
- [weather]: Reuse existing weather data flow and align new outputs with canonical `data/shared/...` and reporting conventions already present in the repo.
- [outputs]: Produce county-level parquet outputs and rendered RM/GRM map artifacts.
- [skills-compatibility]: Design must be compatible with this repository's skills system and existing canonical script/data layout, not a CrewAI-specific package model.
- [workflow]: "commit and push often durring this"
- [cadence]: The RM pipeline should generally run once per year after it is working, to pull in geoadmin data and create RM bands by FIPS.

## Technical Decisions

- [mode]: This conversation is being handled in planning mode; implementation is deferred to the executor after planning.
- [research-first]: Current step is repo-pattern mapping plus external-source validation before finalizing scope and guardrails.
- [commit-cadence]: The future plan should include frequent atomic commit/push checkpoints during execution rather than one large end-of-work commit.
- [operating-model]: Plan around an annual batch refresh workflow rather than a continuously updated pipeline.
- [product-positioning]: The annual RM-by-FIPS output should be planned as a heuristic agronomic planning layer, not a recommendation-grade system.
- [product-positioning-soy]: Soybean MG outputs should also be heuristic/planning-oriented, with explicit caveats and configurable lookup logic.
- [test-strategy-default]: Default plan test strategy is tests-after using the existing Python test infrastructure, plus mandatory agent-executed QA for spatial joins, parquet outputs, and rendered maps.

## Research Findings

- [status]: Parallel explore, librarian, and oracle consultations are running for codebase patterns, geoadmin sources, agronomy references, and architectural guardrails.
- [repo-signal]: Direct repo search already shows active weather/reporting/path infrastructure under `data/scripts/`, canonical grower/shared/reporting trees under `data/`, and farm-intelligence tracking records under `docs/project/`.
- [annual-run]: User clarified the desired steady-state operating cadence is annual, not continuous.
- [weather-current]: Existing weather ingestion is field-centric via `data/scripts/ingest/download_weather.py`, storing per-field CSVs under canonical grower/farm/field paths.
- [paths-current]: Canonical path conventions already exist in `data/scripts/lib/paths.py`, but there are no county/FIPS-oriented helpers yet.
- [geoadmin-gap]: There is no current county polygon ingestion, no county/state admin dataset under `data/shared/`, and no county-level FIPS assignment pipeline in the repo today.
- [reporting-pattern]: The closest output patterns to reuse are `data/scripts/reporting/generate_ssurgo_maps.py`, `.opencode/skills/ssurgo-soil/src/ssurgo_workflows.py`, `data/scripts/reporting/generate_aggregate_poster.py`, and `data/scripts/reporting/generate_farm_html.py`.
- [manifests]: Existing manifest/staleness tracking patterns in `.opencode/skills/farm-intelligence-reporting/src/pipeline.py` are a good fit for annual geoadmin and RM refresh steps.
- [polygon-sources]: Natural Earth is appropriate for global country layers; US Census TIGER/Line is the authoritative public-domain source for US state and county/FIPS polygons.
- [rm-gdd]: The '1 RM day ~= 22 GDD' rule is broadly defensible in extension literature, but only as a heuristic with important caveats around seed-company baselines, planting-date compression, regional variation, and cross-company comparability.
- [architecture-guardrail]: Oracle recommended treating geoadmin as shared infrastructure, using centroid-default field-to-county assignment with ambiguity flagging, aggregating county metrics from field-level weather/GDD, and keeping RM conversion in separate configurable GRM logic rather than embedding it into weather ingestion.

## Open Questions

- [scope-boundary]: Should the plan cover the full end-to-end GRM stack in one milestone, or should it intentionally stop at a specific intermediate deliverable such as geoadmin foundation plus FIPS-tagged weather tables?
- [scope-note]: Current direction is to include the full annual GRM stack in one plan, split into incremental waves with frequent commit/push checkpoints.

## Scope Boundaries

- INCLUDE: geoadmin data sourcing, canonical shared storage design, field-to-geoadmin assignment, county/FIPS weather aggregation, GDD accumulation, RM conversion outputs, and map/report output placement.
- EXCLUDE: direct implementation during this planning phase; any unconfirmed recommendation-grade agronomy claims until references are validated.

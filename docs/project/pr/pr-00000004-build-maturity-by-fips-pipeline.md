# PR-00000004: Build annual maturity-by-FIPS pipeline foundation

_Project: repo-native county maturity pipeline foundation · Date: 2026-03-09_

---

| Field               | Value                                                                         |
| ------------------- | ----------------------------------------------------------------------------- |
| **PR**              | `#4`                                                                          |
| **Author**          | Agent                                                                         |
| **Date**            | 2026-03-09                                                                    |
| **Status**          | Open                                                                          |
| **Branch**          | `feat/class-67-assignment-runthrough` → `main`                                |
| **Related issues**  | [Issue-00000007](../issues/issue-00000007-build-maturity-by-fips-pipeline.md) |
| **Deploy strategy** | N/A                                                                           |

---

## 📋 Summary

### What changed and why

This work starts a new repo-native agricultural maturity pipeline that will produce annual corn RM and soybean MG outputs by county/FIPS. The first checkpoint focuses on the shared integration contract: canonical paths, shared data-tree scaffolding, manifest step naming, and dedicated tracking records so the implementation lands inside the repository's existing skill and script system rather than a disconnected package layout.

### Impact classification

| Dimension         | Level             | Notes                                                                    |
| ----------------- | ----------------- | ------------------------------------------------------------------------ |
| **Risk**          | 🟡 Medium         | Adds new shared-data conventions and new annual pipeline integration     |
| **Scope**         | Moderate          | Touches shared paths, bootstrap logic, manifests, and project tracking   |
| **Reversibility** | Easily reversible | Foundation work is additive and isolated to maturity/geoadmin concerns   |
| **Security**      | Low               | Uses public-source admin geometry and existing public weather data flows |

---

## 🔍 Changes

### Change inventory

| File / Area                                                             | Change type | Description                                                                                |
| ----------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------ |
| `docs/project/issues/issue-00000007-build-maturity-by-fips-pipeline.md` | Added       | Source-of-truth feature issue for annual maturity-by-FIPS work                             |
| `docs/project/pr/pr-00000004-build-maturity-by-fips-pipeline.md`        | Added       | Source-of-truth PR record for this new workstream                                          |
| `docs/project/kanban/project-maturity-by-fips.md`                       | Added       | Live kanban board for maturity pipeline execution                                          |
| `data/scripts/lib/paths.py`                                             | Modified    | Added canonical shared paths for geoadmin, county weather, and maturity outputs            |
| `data/scripts/reporting_bootstrap.py`                                   | Modified    | Added canonical shared tree scaffolding and metadata stubs for geoadmin and maturity roots |
| `.opencode/skills/farm-intelligence-reporting/src/pipeline.py`          | Modified    | Added annual maturity step constants and step ordering contract                            |
| `.opencode/skills/geoadmin-admin/`                                      | Added       | Repo-native geoadmin skill scaffold with shared-level root discovery                       |
| `.opencode/skills/maturity-by-fips/`                                    | Added       | Repo-native maturity skill scaffold with annual output indexing                            |
| `data/scripts/run_maturity_by_fips.py`                                  | Added       | Initial annual entrypoint that bootstraps canonical roots and prints maturity targets      |
| `data/scripts/ingest/download_geoadmin.py`                              | Added       | Repo-native geoadmin downloader and standardizer for canonical shared admin layers         |
| `data/shared/geoadmin/l0_countries/`                                    | Added       | First standardized shared country outputs built from Natural Earth                         |
| `data/scripts/ingest/assign_field_fips.py`                              | Added       | Repo-native field-to-county FIPS mapper with ambiguity reporting                           |
| `data/shared/geoadmin/l1_states/metadata.json`                          | Modified    | Rebuilt state metadata with repo-relative artifact paths for portable reruns               |
| `data/shared/geoadmin/l2_counties/metadata.json`                        | Modified    | Rebuilt county metadata with repo-relative artifact paths and explicit FIPS lookup output  |
| `data/shared/geoadmin/l1_states/`                                       | Added       | Canonical US state outputs built from TIGER/Line                                           |
| `data/shared/geoadmin/l2_counties/`                                     | Added       | Canonical US county/FIPS outputs and lookup built from TIGER/Line                          |
| `data/growers/iowa-demo-grower/farms/iowa-demo-farm/derived/`           | Added       | Demo farm field-to-FIPS summary and ambiguity artifacts with portable summary paths        |

### Before and after

**Before:**

```text
No dedicated geoadmin root exists.
No shared annual maturity roots exist.
No annual maturity step manifest naming exists.
The new maturity work has no dedicated issue/PR/kanban source-of-truth records.
```

**After:**

```text
The repo has dedicated maturity tracking records.
Wave 1 establishes canonical shared roots, manifest step naming, and repo-native integration points.
Future maturity implementation is constrained to `.opencode/skills/...` and `data/scripts/...`.
An annual entrypoint already resolves the canonical output targets for a requested year.
A geoadmin ingest script now builds the first canonical shared admin layer into GeoJSON and Parquet outputs.
The demo farm can now generate a field-to-FIPS mapping summary directly from canonical county geometry.
```

---

## 🧪 Testing

### How to verify

```bash
python -m compileall data/scripts .opencode/skills
python -m pytest tests/farm_intelligence/test_pipeline.py --override-ini=addopts=
```

### Test coverage

| Test type         | Status      | Notes                                                                                                                                                   |
| ----------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unit tests        | ✅ Passing  | Existing targeted pipeline tests still pass (`28 passed`)                                                                                               |
| Integration tests | ✅ Passing  | `run_maturity_by_fips.py --year 2025 --list-steps` resolves canonical output targets                                                                    |
| Manual testing    | ✅ Verified | Shared maturity/geoadmin roots scaffold correctly, annual targets resolve, Level 0/1/2 geoadmin outputs build, and the demo farm maps 10 fields to FIPS |
| Performance       | ⬜ N/A      | Full annual flow not implemented yet                                                                                                                    |

Current verification evidence:

- `python -m compileall .opencode/skills/geoadmin-admin/src .opencode/skills/maturity-by-fips/src data/scripts/lib/paths.py data/scripts/reporting_bootstrap.py data/scripts/run_maturity_by_fips.py .opencode/skills/farm-intelligence-reporting/src/pipeline.py`
- `python data/scripts/run_maturity_by_fips.py --year 2025 --list-steps`
- `python -m compileall data/scripts/ingest/download_geoadmin.py .opencode/skills/geoadmin-admin/src`
- `python data/scripts/ingest/download_geoadmin.py --levels l0_countries`
- `python data/scripts/ingest/download_geoadmin.py --levels l1_states l2_counties`
- `python -m compileall data/scripts/ingest/assign_field_fips.py .opencode/skills/geoadmin-admin/src`
- `python data/scripts/ingest/assign_field_fips.py`
- `python data/scripts/ingest/download_geoadmin.py --levels l1_states l2_counties` (rerun after metadata portability update)
- `python -m pytest tests/farm_intelligence/test_pipeline.py --override-ini=addopts=` -> `28 passed`

### Edge cases considered

- Maturity work must not drift into a standalone package layout
- Annual invocation must not quietly become scheduler infrastructure
- Shared-data path additions must remain canonical and additive

---

## 🔄 Rollback plan

**Revert command:**

```bash
git revert [commit-sha]
```

**Additional steps needed:**

- [ ] Remove any new empty maturity/geoadmin scaffolding if the feature is abandoned

> ⚠️ **Rollback risk:** Low — this checkpoint is architectural foundation work only.

---

## 💬 Discussion

### Key review decisions

- **Repo integration:** The generic handoff `src/skills/maturity_calc/...` layout is explicitly rejected in favor of `.opencode/skills/...` and `data/scripts/...`
- **Product framing:** Corn RM and soybean MG remain heuristic planning outputs rather than recommendation-grade agronomy
- **Wave 1 checkpoint:** Canonical shared roots and repo-native scaffolding land before county logic so later implementation cannot drift off the planned integration surface
- **Geoadmin ingestion:** Shared admin layers are downloaded and standardized through a repo-native ingest script rather than ad hoc manual placement
- **Field bridge:** Field-to-FIPS mapping is persisted as canonical farm-level summary and table output before county weather or maturity transforms consume it
- **Metadata portability:** Shared geoadmin metadata now stores repo-relative artifact paths so annual runs stay portable across machines and worktrees

### Follow-up items

- [x] Extend geoadmin ingestion from countries to US states and counties with FIPS lookup output
- [ ] Add annual county weather and GDD transforms downstream of canonical field-to-FIPS mapping
- [ ] No ADR required

---

## 🔗 References

- [Issue-00000007](../issues/issue-00000007-build-maturity-by-fips-pipeline.md)
- [Work plan](../../.sisyphus/plans/grm-by-fips-geoadmin.md)

---

_Last updated: 2026-03-09_

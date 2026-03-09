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
```

---

## 🧪 Testing

### How to verify

```bash
python -m compileall data/scripts .opencode/skills
python -m pytest tests/farm_intelligence/test_pipeline.py --override-ini=addopts=
```

### Test coverage

| Test type         | Status      | Notes                                                                                                |
| ----------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| Unit tests        | ✅ Passing  | Existing targeted pipeline tests still pass (`28 passed`)                                            |
| Integration tests | ✅ Passing  | `run_maturity_by_fips.py --year 2025 --list-steps` resolves canonical output targets                 |
| Manual testing    | ✅ Verified | Shared maturity/geoadmin roots scaffold correctly and the new entrypoint reports canonical locations |
| Performance       | ⬜ N/A      | Full annual flow not implemented yet                                                                 |

Current verification evidence:

- `python -m compileall .opencode/skills/geoadmin-admin/src .opencode/skills/maturity-by-fips/src data/scripts/lib/paths.py data/scripts/reporting_bootstrap.py data/scripts/run_maturity_by_fips.py .opencode/skills/farm-intelligence-reporting/src/pipeline.py`
- `python data/scripts/run_maturity_by_fips.py --year 2025 --list-steps`
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

### Follow-up items

- [ ] Implement shared geoadmin download/standardization and shared maturity roots
- [ ] Add annual field-to-FIPS mapping and county weather/GDD transforms

---

## 🔗 References

- [Issue-00000007](../issues/issue-00000007-build-maturity-by-fips-pipeline.md)
- [Work plan](../../.sisyphus/plans/grm-by-fips-geoadmin.md)

---

_Last updated: 2026-03-09_

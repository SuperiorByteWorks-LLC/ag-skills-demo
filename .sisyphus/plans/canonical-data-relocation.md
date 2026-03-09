# Canonical data relocation and writer enforcement plan

## 🚀 TL;DR

> Fully backfill all legacy data roots into canonical locations, rewire all writers/readers to canonical paths only, hard-fail CI on regressions, then delete legacy directories.

**Deliverables**:

- Full deterministic migration of `data/cdl`, `data/EDA`, `data/field-boundaries`, `data/soil`, `data/weather`
- Canonical-only writer contract across scripts and skills
- CI/runtime enforcement preventing legacy path reintroduction
- Evidence-backed full pipeline validation

**Estimated effort**: Large
**Parallel execution**: YES (4 waves + final verification)
**Critical path**: T1 → T3 → T7/T8/T9/T10/T11 → T12/T14 → T15/T17 → F1-F4

---

## 🧭 Context

### Original request

User requires complete relocation from legacy data roots to canonical roots (`data/growers`, `data/shared`, `data/scripts`, canonical reporting outputs), then strict script/skill updates so future writes cannot drift back.

### Interview summary

- Migration order: move/backfill first, then writer logic updates.
- Legacy policy: delete legacy directories after migration.
- Enforcement policy: CI hard-fail for legacy path usage.
- Coverage policy: full backfill of everything now.
- Test strategy: tests-after.

### Gap review note

Metis tool invocation was blocked by the current session constraint (no non-Codex subagents). This plan includes an internal gap pass with explicit guardrails and edge cases.

---

## 🎯 Work objectives

### Core objective

Make canonical paths the only supported data contract for ingest/reporting/skills while preserving all legacy data by full backfill migration before deleting legacy roots.

### Concrete deliverables

- Canonical migration manifests + checksums for every migrated file
- Updated scripts/skills writing only to canonical roots
- Runtime guard blocking forbidden legacy writes
- CI check that fails on forbidden legacy path references
- Full pipeline completion with canonical outputs only

### Definition of done

- [ ] No active files remain under legacy roots
- [ ] All pipeline steps pass with canonical-only inputs/outputs
- [ ] CI/static checks fail if forbidden roots reappear
- [ ] Legacy directories are removed after verified backfill

### Must have

- Full backfill of all legacy data into canonical destinations
- Deterministic migration logs with before/after path mapping
- Tests-after implemented and passing

### Must NOT have (guardrails)

- No new write logic to `data/cdl`, `data/EDA`, `data/field-boundaries`, `data/soil`, `data/weather`
- No silent fallback writes to legacy paths
- No manual-only verification gates

---

## ✅ Verification strategy

> ZERO HUMAN INTERVENTION. All checks are command/tool executable.

- **Infrastructure exists**: YES
- **Automated tests**: Tests-after
- **Agent-executed QA**: REQUIRED for every task

Evidence directory: `.sisyphus/evidence/canonical-relocation/`

---

## ⚙️ Execution strategy

### Parallel execution waves

**Wave 1 (foundation, parallel)**: T1, T2, T3, T4, T5, T6
**Wave 2 (full backfill, parallel)**: T7, T8, T9, T10, T11
**Wave 3 (writer/skill rewiring, parallel)**: T12, T13, T14
**Wave 4 (enforcement + validation)**: T15, T16, T17
**Wave FINAL**: F1, F2, F3, F4

### Dependency matrix

- T1 → T7,T8,T9,T10,T11
- T2 → T7,T8,T9,T10,T11,T12,T13,T14
- T3 → T7,T8,T9,T10,T11,T16
- T4 → T12,T13,T14
- T5,T6 → T12,T13,T14,T15
- T7..T11 → T15,T16,T17
- T12..T14 → T15,T16,T17
- T15..T17 → F1..F4

---

## 🧩 TODOs

---

- [ ] 1. Build legacy inventory + classification table

  **What to do**:
  - Enumerate all files under legacy roots and classify by data type (raster/table/geojson/report/cache)
  - Emit canonical target mapping table used by all downstream migration tasks

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 1, independent
  **Blocked by**: None
  **Blocks**: T7-T11
  **References**: `data/scripts/lib/paths.py`, `data/scripts/reporting_bootstrap.py`

  **Acceptance criteria**:
  - [ ] Inventory file exists with source→target mapping for 100% legacy files

  **QA scenarios**:
  - Scenario (happy): Run inventory command; assert row count > 0 and every row has source+target.
  - Scenario (error): Inject missing root; assert script exits non-zero with explicit missing-root message.

- [ ] 2. Define canonical relocation contract (single source of truth)

  **What to do**:
  - Create deterministic rules for each legacy root to canonical destination
  - Include naming normalization and collision policy

  **Recommended agent profile**: `writing` + `[]`
  **Parallelization**: Wave 1, independent
  **Blocked by**: None
  **Blocks**: T7-T14
  **References**: `data/scripts/lib/paths.py`, `.opencode/skills/*/SKILL.md`

  **Acceptance criteria**:
  - [ ] Contract doc/table referenced by migration + writer tasks

  **QA scenarios**:
  - Scenario (happy): Validate sample paths from each legacy root map to canonical locations.
  - Scenario (error): Provide unsupported root; assert contract validator rejects it.

- [ ] 3. Implement migration manifest + checksum logging

  **What to do**:
  - Add migration log format containing source, target, size, checksum, status
  - Ensure reruns are idempotent and detect already-migrated files

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 1
  **Blocked by**: T2
  **Blocks**: T7-T11, T16
  **References**: `data/scripts/lib/manifest.py`, `data/scripts/reporting_bootstrap.py`

  **Acceptance criteria**:
  - [ ] Migration log is reproducible across reruns for unchanged files

  **QA scenarios**:
  - Scenario (happy): Run migration twice; second run reports zero-copy/idempotent status.
  - Scenario (error): Corrupt a target file; rerun detects checksum mismatch and repairs/reports.

- [ ] 4. Normalize canonical path helpers across scripts/skills

  **What to do**:
  - Consolidate path helper usage so all modules resolve through canonical helpers
  - Remove ad-hoc path assembly that bypasses helpers

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 1
  **Blocked by**: T2
  **Blocks**: T12-T14
  **References**: `data/scripts/lib/paths.py`, `.opencode/skills/*/src/*.py`

  **Acceptance criteria**:
  - [ ] All targeted scripts/skills use canonical helper layer for writes

  **QA scenarios**:
  - Scenario (happy): Static scan finds no direct hardcoded legacy write roots in targeted modules.
  - Scenario (error): Introduce mocked hardcoded path; check flags it.

- [ ] 5. Add static CI hard-fail rule for forbidden roots

  **What to do**:
  - Add CI check that fails on forbidden legacy root references in active scripts/skills
  - Exempt only migration history logs if needed

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 1
  **Blocked by**: T2
  **Blocks**: T15
  **References**: CI workflow files, `tests/farm_intelligence/test_pipeline.py`

  **Acceptance criteria**:
  - [ ] CI fails when legacy root string is reintroduced

  **QA scenarios**:
  - Scenario (happy): Run checker on clean tree; returns PASS.
  - Scenario (error): Add temporary forbidden path string; checker fails with file:line.

- [ ] 6. Add runtime write guard for forbidden roots

  **What to do**:
  - Implement guard utility that rejects writes targeting legacy roots
  - Integrate into core writer entry points

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 1
  **Blocked by**: T2
  **Blocks**: T12-T14,T15
  **References**: `data/scripts/lib/paths.py`, writer modules in ingest/reporting

  **Acceptance criteria**:
  - [ ] Attempted legacy write raises explicit error with blocked path

  **QA scenarios**:
  - Scenario (happy): Canonical write passes.
  - Scenario (error): Legacy-target write throws guard exception and logs evidence.

- [ ] 7. Full backfill migrate `data/cdl` to canonical shared/grower locations

  **What to do**:
  - Copy/move all CDL rasters/tables/history to canonical destinations per contract
  - Preserve provenance and checksums

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 2
  **Blocked by**: T1,T2,T3
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] 100% of `data/cdl` inventory migrated and validated

  **QA scenarios**:
  - Scenario (happy): Compare counts/checksums for source vs canonical target.
  - Scenario (error): Simulate missing file; migration reports precise failure and continues/halts per policy.

- [ ] 8. Full backfill migrate `data/weather` to canonical farm tables

  **What to do**:
  - Relocate all weather history and derived tables to canonical farm tree
  - Update metadata links

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 2
  **Blocked by**: T1,T2,T3
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] 100% of `data/weather` inventory migrated and validated

  **QA scenarios**:
  - Scenario (happy): Row counts/date ranges match before/after.
  - Scenario (error): Corrupt CSV delimiter sample; validator catches schema mismatch.

- [ ] 9. Full backfill migrate `data/soil` to canonical farm/field locations

  **What to do**:
  - Relocate all SSURGO tables, polygons, and derived soil cards/maps
  - Keep canonical structure consistent across all fields

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 2
  **Blocked by**: T1,T2,T3
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] 100% of `data/soil` inventory migrated and validated

  **QA scenarios**:
  - Scenario (happy): Field-level soil assets open successfully from canonical paths.
  - Scenario (error): Missing polygon source triggers explicit migration failure entry.

- [ ] 10. Full backfill migrate `data/field-boundaries` to canonical boundary tree

  **What to do**:
  - Migrate farm boundary collections and per-field boundary files to canonical locations
  - Ensure field slug mapping remains intact

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 2
  **Blocked by**: T1,T2,T3
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] 100% of boundary files migrated and loadable in canonical tree

  **QA scenarios**:
  - Scenario (happy): Load canonical GeoJSONs and verify feature counts match legacy.
  - Scenario (error): Invalid geometry input is logged and rejected.

- [ ] 11. Full backfill migrate `data/EDA` outputs to canonical reporting locations

  **What to do**:
  - Move EDA outputs to canonical summaries/reports locations with clear naming
  - Rebind any references consumed by report assembly

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 2
  **Blocked by**: T1,T2,T3
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] 100% of EDA artifacts migrated and linkable from canonical reports

  **QA scenarios**:
  - Scenario (happy): Render report assembly from canonical EDA paths.
  - Scenario (error): Missing migrated chart path causes deterministic failure with path detail.

- [ ] 12. Rewire ingest/reporting scripts to canonical-only reads/writes

  **What to do**:
  - Update all active `data/scripts/ingest` and `data/scripts/reporting` modules to canonical paths only
  - Remove legacy fallback read/write logic

  **Recommended agent profile**: `unspecified-high` + `[]`
  **Parallelization**: Wave 3
  **Blocked by**: T4,T6,T7-T11
  **Blocks**: T15-T17

  **Acceptance criteria**:
  - [ ] No active ingest/reporting module can write to forbidden roots

  **QA scenarios**:
  - Scenario (happy): Run key scripts; outputs appear only under canonical roots.
  - Scenario (error): Forced legacy env/path override is ignored/blocked.

- [ ] 13. Rewire skills (`SKILL.md` + `src`) to canonical path contract

  **What to do**:
  - Update skills docs and source helpers to match canonical destinations
  - Eliminate stale examples that imply legacy writes

  **Recommended agent profile**: `writing` + `[]`
  **Parallelization**: Wave 3
  **Blocked by**: T4,T7-T11
  **Blocks**: T16

  **Acceptance criteria**:
  - [ ] Skill docs/source consistently point to canonical paths

  **QA scenarios**:
  - Scenario (happy): Doc/source scan confirms canonical path consistency.
  - Scenario (error): Reintroduced legacy path in skill doc triggers CI failure.

- [ ] 14. Update orchestrators/rebuild scripts for canonical-only operation

  **What to do**:
  - Update run/rebuild entry points to consume only canonical trees
  - Ensure pipeline completes without legacy directories present

  **Recommended agent profile**: `deep` + `[]`
  **Parallelization**: Wave 3
  **Blocked by**: T4,T7-T12
  **Blocks**: T17

  **Acceptance criteria**:
  - [ ] Orchestrator succeeds with legacy directories removed

  **QA scenarios**:
  - Scenario (happy): End-to-end run from clean canonical state passes.
  - Scenario (error): Missing canonical prerequisite fails with actionable error.

- [ ] 15. Add tests-after coverage for migration + guard + CI checks

  **What to do**:
  - Add/extend tests validating migration completeness, blocked legacy writes, and static checker behavior

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 4
  **Blocked by**: T5,T6,T7-T14
  **Blocks**: T16,T17

  **Acceptance criteria**:
  - [ ] Test suite passes and includes new enforcement assertions

  **QA scenarios**:
  - Scenario (happy): `pytest` passes with new tests enabled.
  - Scenario (error): Introduced forbidden path causes test failure.

- [ ] 16. Execute canonical compliance scan + CI hard-fail validation

  **What to do**:
  - Run static scan and CI checks proving hard-fail behavior
  - Capture evidence output for pass/fail cases

  **Recommended agent profile**: `quick` + `[]`
  **Parallelization**: Wave 4
  **Blocked by**: T3,T13,T15
  **Blocks**: T17

  **Acceptance criteria**:
  - [ ] Compliance scan shows zero forbidden references in active code

  **QA scenarios**:
  - Scenario (happy): compliance check PASS with zero hits.
  - Scenario (error): seeded forbidden string yields expected fail with file:line.

- [ ] 17. Delete legacy directories post-validation + final canonical run

  **What to do**:
  - Remove `data/cdl`, `data/EDA`, `data/field-boundaries`, `data/soil`, `data/weather`
  - Run full canonical pipeline and verify outputs

  **Recommended agent profile**: `deep` + `[]`
  **Parallelization**: Wave 4 (final integration)
  **Blocked by**: T7-T16
  **Blocks**: Final verification wave

  **Acceptance criteria**:
  - [ ] Legacy directories absent
  - [ ] Full pipeline completes from canonical paths only

  **QA scenarios**:
  - Scenario (happy): pipeline complete with legacy dirs absent.
  - Scenario (error): any latent legacy dependency fails immediately with path-specific diagnostics.

---

## 🔍 Final verification wave

- [ ] F1. **Plan compliance audit** (`oracle`)
- [ ] F2. **Code quality review** (`unspecified-high`)
- [ ] F3. **Real QA execution of all scenarios** (`unspecified-high`)
- [ ] F4. **Scope fidelity check** (`deep`)

---

## 🧾 Commit strategy

- Commit A: migration framework + mapping contract
- Commit B: full data relocation + manifests/evidence
- Commit C: script/skill canonical rewiring + guards + CI checks + tests/docs

---

## 🏁 Success criteria

### Verification commands

```bash
python data/scripts/run_farm_pipeline.py
python -m pytest tests/farm_intelligence/test_pipeline.py --override-ini=addopts=
python -m compileall data/scripts
```

### Final checklist

- [ ] Legacy roots removed
- [ ] Canonical-only writes enforced
- [ ] CI hard-fail checks active
- [ ] Full pipeline green

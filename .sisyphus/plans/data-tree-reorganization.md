# Work Plan: Data Tree Reorganization Hard Cutover

## TL;DR

> Reorganize `data/` into the canonical `scripts/` + `shared/` + `growers/` hierarchy with an immediate hard cutover, preserving the current reporting pipeline and SSURGO per-field polygon cache behavior.
>
> Deliverables:
>
> - Canonical tree and metadata records under `data/growers/iowa-demo-grower/farms/iowa-demo-farm/`
> - Script reorganization and centralized helper modules under `data/scripts/lib/`
> - Updated pipeline and reporting scripts with zero active legacy path dependencies
>
> Estimated Effort: Large
> Parallel Execution: YES - 4 implementation waves + final verification wave
> Critical Path: T1 -> T2 -> T8 -> T10 -> T12 -> F1-F4

---

## Context

### Original Request

User asked to review existing draft and plan for the data tree reorganization and proceed now.

### Interview Summary

- Existing artifacts reviewed: `.sisyphus/drafts/data-tree-reorganization.md` and prior `.sisyphus/plans/data-tree-reorganization.md`.
- User selected plan regeneration (not as-is reuse).
- Fixed decisions retained: grower slug `iowa-demo-grower`, farm slug `iowa-demo-farm`, immediate hard cutover.

### Research Findings

- Current draft has strong target-tree and migration mapping details.
- Existing plan lacked strict execution details required for agent-driven implementation (detailed QA scenarios, explicit dependency and wave dispatch).

### Metis Review

Addressed during regeneration:

- Tightened scope for scaffold-first migration plus path cutover.
- Added pre-migration operational guardrails (baseline pipeline, field inventory, rollback, concurrency lockout).
- Added executable acceptance criteria and failure-path QA scenarios for every task.
- Added explicit scope-control rules to prevent logic refactor creep.

---

## Work Objectives

### Core Objective

Convert the current `data/` layout to a deterministic, scalable grower/farm/field-oriented structure and hard-cut all active script usage to canonical helper-driven paths.

### Concrete Deliverables

- Canonical directory tree rooted at `data/scripts/`, `data/shared/`, and `data/growers/`
- `data/scripts/lib/paths.py`, `data/scripts/lib/naming.py`, `data/scripts/lib/manifest.py`
- `farm.json` plus one `field.json` per field slug
- Dataset metadata/manifest files in canonical locations
- Reorganized ingest/EDA/reporting scripts with updated imports and path usage
- `data/scripts/run_farm_pipeline.py` operating entirely on the new tree
- `data/README.md` rewritten to match final reality

### Definition of Done

- [ ] Canonical tree exists and is the only active data model
- [ ] No active script depends on legacy data roots (`data/EDA`, `data/soil`, `data/weather`, `data/cdl`, `data/field-boundaries`, `data/reporting/manifests`)
- [ ] Pipeline executes against canonical paths and writes outputs to canonical destinations
- [ ] SSURGO cache behavior remains one-time-per-field and still powers downstream visual outputs
- [ ] README and filesystem structure are aligned

### Must Have

- Hard cutover with no fallback wrappers
- Helper-module-only canonical path construction
- Metadata coverage for farm, field, and data folders that hold real artifacts

### Must NOT Have (Guardrails)

- No business-logic rewrites beyond path/import/data-location migration
- No new features, CLI options, performance optimization, or architecture expansion
- No active dual-write, compatibility shims, or legacy-path fallbacks

---

## Verification Strategy

> ZERO HUMAN INTERVENTION. All verification must be executable by agents via commands and tools.

### Test Decision

- Infrastructure exists: YES (Python scripts and command-based verification flow)
- Automated tests: Tests-after (verification-focused; no broad new test framework scope)
- Framework: Command-driven verification (`python`, `grep`, `find`, `ls`, pipeline run)

### QA Policy

- Every task includes mandatory QA scenarios:
  - one happy path
  - one failure/edge path
- Evidence path for each scenario under `.sisyphus/evidence/`
- Task completion is invalid without evidence artifacts.

### Pre-Migration Gate

- Baseline pipeline run captured before cutover
- Field inventory and slug map captured
- Disk free-space and write-permission checks captured
- No concurrent data-writer process running
- Manual rollback procedure documented and validated

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (foundation, parallel start): T1, T2, T3, T4, T5
Wave 2 (data model migration, parallel): T6, T7, T8
Wave 3 (script cutover, parallel): T9, T10
Wave 4 (verification + docs): T11, T12
Wave FINAL (independent review): F1, F2, F3, F4

Critical Path: T1 -> T2 -> T7 -> T9 -> T10 -> T11 -> F1-F4

### Dependency Matrix

- T1: none -> T6, T7, T9
- T2: none -> T7, T8, T9, T10
- T3: none -> T6
- T4: none -> T11
- T5: none -> T11
- T6: T1, T3 -> T8, T10
- T7: T1, T2 -> T9, T10
- T8: T2, T6 -> T10, T11
- T9: T1, T2, T7 -> T10, T11
- T10: T2, T6, T7, T8, T9 -> T11
- T11: T4, T5, T8, T9, T10 -> T12, F1-F4
- T12: T11 -> F1-F4

### Agent Dispatch Summary

- Wave 1: T1 `quick`, T2 `quick`, T3 `quick`, T4 `quick`, T5 `quick`
- Wave 2: T6 `quick`, T7 `unspecified-high`, T8 `unspecified-high`
- Wave 3: T9 `quick`, T10 `deep`
- Wave 4: T11 `unspecified-high`, T12 `writing`
- Final: F1 `oracle`, F2 `unspecified-high`, F3 `unspecified-high`, F4 `deep`

---

## TODOs

- [ ] 1. Capture pre-migration baseline and rollback notes

  **What to do**:
  - Record baseline state: current script tree, current path references, and current pipeline behavior.
  - Document manual rollback steps (git restore targets + verification commands) in migration notes.

  **Must NOT do**:
  - Do not modify implementation files in this task.

  **Recommended Agent Profile**:
  - Category: `quick` (inventory and evidence capture)
  - Skills: `git-master` (clean baseline diff tracking)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 1 (with T2, T3, T4, T5)
  - Blocks: T6, T7, T9
  - Blocked By: None

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - canonical migration decisions and mapping.
  - `data/scripts/run_farm_pipeline.py` - baseline execution target.

  **Acceptance Criteria**:
  - [ ] Baseline command outputs saved to `.sisyphus/evidence/task-1-baseline.txt`.
  - [ ] Rollback note saved to `.sisyphus/evidence/task-1-rollback.md`.

  **QA Scenarios**:

  ```text
  Scenario: Baseline capture succeeds
    Tool: Bash
    Steps: run baseline listing and grep commands for legacy paths; save output
    Expected Result: evidence file created with non-empty output
    Evidence: .sisyphus/evidence/task-1-baseline.txt

  Scenario: Missing evidence is detected
    Tool: Bash
    Steps: run existence check for evidence file path before creation in dry run
    Expected Result: check fails before capture and passes after capture
    Evidence: .sisyphus/evidence/task-1-baseline-error.txt
  ```

- [ ] 2. Create canonical scaffold roots and helper package folders

  **What to do**:
  - Create canonical root layout under `data/scripts`, `data/shared`, and `data/growers/.../fields`.
  - Ensure `data/scripts/lib` is importable (package markers where required).

  **Must NOT do**:
  - Do not leave new active directories outside canonical top-level roots.

  **Recommended Agent Profile**:
  - Category: `quick` (deterministic filesystem scaffolding)
  - Skills: `ssurgo-soil` (domain alignment for soil folder conventions)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 1 (with T1, T3, T4, T5)
  - Blocks: T7, T8, T9, T10
  - Blocked By: None

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - target tree and slug choices.

  **Acceptance Criteria**:
  - [ ] Canonical directories exist and are listable.
  - [ ] No unexpected new top-level dataset roots introduced.

  **QA Scenarios**:

  ```text
  Scenario: Canonical scaffold exists
    Tool: Bash
    Steps: list required directories and assert each exists
    Expected Result: all required paths resolve
    Evidence: .sisyphus/evidence/task-2-scaffold.txt

  Scenario: Non-canonical top-level folder attempt fails policy
    Tool: Bash
    Steps: run top-level directory check and compare against allowed set
    Expected Result: only scripts/shared/growers are active
    Evidence: .sisyphus/evidence/task-2-scaffold-error.txt
  ```

- [ ] 3. Build field inventory and deterministic slug map

  **What to do**:
  - Extract field identifiers from the current source boundary dataset.
  - Generate deterministic slug mapping (`OSM_*` -> `osm-*`) and save as migration artifact.

  **Must NOT do**:
  - Do not hardcode partial field lists.

  **Recommended Agent Profile**:
  - Category: `quick` (data inventory extraction)
  - Skills: `field-boundaries` (field ID and geometry source conventions)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 1 (with T1, T2, T4, T5)
  - Blocks: T6
  - Blocked By: None

  **References**:
  - `data/field-boundaries/` - source field IDs if present.
  - `.sisyphus/drafts/data-tree-reorganization.md` - slug policy.

  **Acceptance Criteria**:
  - [ ] Field inventory file exists with one row per field.
  - [ ] Slug map has no collisions and matches naming rules.

  **QA Scenarios**:

  ```text
  Scenario: Slug map generation succeeds
    Tool: Bash
    Steps: run slug extraction command/script and count unique slugs
    Expected Result: unique slug count equals field count
    Evidence: .sisyphus/evidence/task-3-slugs.txt

  Scenario: Duplicate slug collision is caught
    Tool: Bash
    Steps: run collision check over generated slug map
    Expected Result: command exits non-zero if duplicates exist
    Evidence: .sisyphus/evidence/task-3-slugs-error.txt
  ```

- [ ] 4. Validate preconditions: disk, permissions, and concurrency lockout

  **What to do**:
  - Verify adequate disk space for migration artifacts.
  - Verify write permissions across target `data/` subtrees.
  - Verify no concurrent process is writing into `data/` during cutover.

  **Must NOT do**:
  - Do not start migration tasks before precondition checks pass.

  **Recommended Agent Profile**:
  - Category: `quick`
  - Skills: `git-master` (clean operation guardrails)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 1
  - Blocks: T11
  - Blocked By: None

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - hard cutover risk list.

  **Acceptance Criteria**:
  - [ ] Precondition report captured under evidence folder.

  **QA Scenarios**:

  ```text
  Scenario: Preconditions pass
    Tool: Bash
    Steps: run disk/permission/process checks and save report
    Expected Result: all checks return pass status
    Evidence: .sisyphus/evidence/task-4-preconditions.txt

  Scenario: Concurrent writer detection triggers stop
    Tool: Bash
    Steps: run process check with simulated conflicting process signature
    Expected Result: migration gate reports blocked state
    Evidence: .sisyphus/evidence/task-4-preconditions-error.txt
  ```

- [ ] 5. Capture baseline pipeline execution evidence

  **What to do**:
  - Run current pipeline entrypoint in baseline mode and capture output, return code, and key generated artifact paths.

  **Must NOT do**:
  - Do not treat migration successful without comparing post-cutover behavior to baseline.

  **Recommended Agent Profile**:
  - Category: `quick`
  - Skills: `farm-intelligence-reporting` (pipeline output expectations)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 1
  - Blocks: T11
  - Blocked By: None

  **References**:
  - `data/scripts/run_farm_pipeline.py` - baseline command target.

  **Acceptance Criteria**:
  - [ ] Baseline pipeline evidence file saved.

  **QA Scenarios**:

  ```text
  Scenario: Baseline run produces evidence
    Tool: Bash
    Steps: execute pipeline and capture stdout/stderr and exit code
    Expected Result: evidence file records command status and output
    Evidence: .sisyphus/evidence/task-5-baseline-pipeline.txt

  Scenario: Baseline failure is surfaced with non-zero exit
    Tool: Bash
    Steps: execute with intentionally invalid input arg/environment if supported
    Expected Result: non-zero exit and explicit error output captured
    Evidence: .sisyphus/evidence/task-5-baseline-pipeline-error.txt
  ```

- [ ] 6. Create farm/field identity records and dataset metadata skeletons

  **What to do**:
  - Create `farm.json` and per-field `field.json` using canonical slugs.
  - Add `metadata.json` placeholders in boundary/soil/weather (and relevant shared datasets).

  **Must NOT do**:
  - Do not use display names as directory keys.

  **Recommended Agent Profile**:
  - Category: `quick`
  - Skills: `ssurgo-poster-cards` (field-level structure alignment)

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 2
  - Blocks: T8, T10
  - Blocked By: T1, T3

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - required metadata skeletons.

  **Acceptance Criteria**:
  - [ ] `farm.json` exists at canonical farm root.
  - [ ] Every field directory has valid `field.json`.

  **QA Scenarios**:

  ```text
  Scenario: Metadata files validate and cover all fields
    Tool: Bash
    Steps: run JSON parse checks and compare field count vs slug map
    Expected Result: all JSON valid and counts match
    Evidence: .sisyphus/evidence/task-6-metadata.txt

  Scenario: Missing field metadata is detected
    Tool: Bash
    Steps: run completeness check for required json files per field
    Expected Result: check fails if any required file missing
    Evidence: .sisyphus/evidence/task-6-metadata-error.txt
  ```

- [ ] 7. Implement canonical helper modules (`paths.py`, `naming.py`, `manifest.py`)

  **What to do**:
  - Implement canonical path builders for grower/farm/field/shared locations.
  - Implement naming normalization utilities and manifest read/write helpers.
  - Replace duplicate path-building logic targets in task notes for downstream tasks.

  **Must NOT do**:
  - Do not leave active scripts constructing canonical paths via inline literals.

  **Recommended Agent Profile**:
  - Category: `unspecified-high`
  - Skills: `git-master`, `ssurgo-soil`

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 2
  - Blocks: T9, T10
  - Blocked By: T1, T2

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - proposed helper API.
  - `data/scripts/run_farm_pipeline.py` - primary consumer of helper API.

  **Acceptance Criteria**:
  - [ ] Helper modules exist and import cleanly.
  - [ ] Required helper functions for boundary/soil/weather/shared paths are present.

  **QA Scenarios**:

  ```text
  Scenario: Helper API imports and resolves canonical paths
    Tool: Bash
    Steps: run python import and sample path resolution calls
    Expected Result: paths resolve under canonical roots only
    Evidence: .sisyphus/evidence/task-7-helpers.txt

  Scenario: Legacy path literal usage scan catches regressions
    Tool: Bash
    Steps: grep helper consumers for forbidden hard-coded legacy roots
    Expected Result: no forbidden literals in updated modules
    Evidence: .sisyphus/evidence/task-7-helpers-error.txt
  ```

- [ ] 8. Migrate shared datasets and shared manifests into `data/shared/`

  **What to do**:
  - Move/normalize shared CDL assets into `data/shared/cdl/{rasters,derived,metadata,manifests}`.
  - Place shared reference artifacts in `data/shared/reference/*`.

  **Must NOT do**:
  - Do not duplicate canonical shared sources across field folders.

  **Recommended Agent Profile**:
  - Category: `unspecified-high`
  - Skills: `cdl-cropland` (CDL source conventions)

  **Parallelization**:
  - Can Run In Parallel: YES
  - Parallel Group: Wave 2 (with T6, T7)
  - Blocks: T10, T11
  - Blocked By: T2, T6

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - shared CDL mapping and manifests policy.

  **Acceptance Criteria**:
  - [ ] Shared dataset files exist in canonical shared paths.
  - [ ] Legacy shared source roots are no longer active dependencies.

  **QA Scenarios**:

  ```text
  Scenario: Shared assets are present in canonical locations
    Tool: Bash
    Steps: enumerate shared/cdl and shared/reference paths and key files
    Expected Result: required files found in canonical paths
    Evidence: .sisyphus/evidence/task-8-shared.txt

  Scenario: Canonical-vs-legacy collision check
    Tool: Bash
    Steps: verify no script references old shared roots as active source
    Expected Result: forbidden references count is zero
    Evidence: .sisyphus/evidence/task-8-shared-error.txt
  ```

- [ ] 9. Reorganize script files into ingest/eda/reporting structure

  **What to do**:
  - Move flat numbered scripts into target folders with canonical names.
  - Update import paths to reflect new module locations.

  **Must NOT do**:
  - Do not keep old numbered script locations in active invocation paths.

  **Recommended Agent Profile**:
  - Category: `quick`
  - Skills: `git-master` (safe move tracking)

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 3
  - Blocks: T10, T11
  - Blocked By: T1, T2, T7

  **References**:
  - `.sisyphus/drafts/data-tree-reorganization.md` - script migration map.

  **Acceptance Criteria**:
  - [ ] Scripts exist in new subdirectories.
  - [ ] Imports resolve from new locations.

  **QA Scenarios**:

  ```text
  Scenario: New script tree is complete
    Tool: Bash
    Steps: list scripts and match against expected canonical names
    Expected Result: expected files exist and old active names removed
    Evidence: .sisyphus/evidence/task-9-script-move.txt

  Scenario: Import resolution check catches stale module paths
    Tool: Bash
    Steps: run python compile/import check over moved scripts
    Expected Result: stale import errors are absent
    Evidence: .sisyphus/evidence/task-9-script-move-error.txt
  ```

- [ ] 10. Hard-cut script path usage to canonical helpers and migrated data locations

  **What to do**:
  - Refactor ingest, EDA, reporting, and pipeline scripts to use helper APIs.
  - Remove active path dependencies on legacy roots (`data/EDA`, `data/soil`, `data/weather`, `data/cdl`, `data/field-boundaries`, `data/reporting/manifests`).
  - Preserve SSURGO per-field cache semantics and multi-polygon downstream rendering behavior.

  **Must NOT do**:
  - Do not change business behavior unrelated to path/import/data-location migration.

  **Recommended Agent Profile**:
  - Category: `deep`
  - Skills: `ssurgo-soil`, `farm-intelligence-reporting`

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 3
  - Blocks: T11
  - Blocked By: T2, T6, T7, T8, T9

  **References**:
  - `data/scripts/run_farm_pipeline.py` - end-to-end orchestration path usage.
  - `.sisyphus/drafts/data-tree-reorganization.md` - hard-coded path clusters to eliminate.

  **Acceptance Criteria**:
  - [ ] Helper-driven path usage across active scripts.
  - [ ] Grep scan for legacy roots in active scripts returns zero allowed violations.

  **QA Scenarios**:

  ```text
  Scenario: Legacy path grep is clean after cutover
    Tool: Bash
    Steps: run canonical forbidden-path grep against active scripts
    Expected Result: zero matches except explicitly archived migration notes
    Evidence: .sisyphus/evidence/task-10-cutover-grep.txt

  Scenario: Regression check catches reintroduced legacy path
    Tool: Bash
    Steps: run same scan in strict mode and fail on any match
    Expected Result: non-zero exit if forbidden path appears
    Evidence: .sisyphus/evidence/task-10-cutover-grep-error.txt
  ```

- [ ] 11. Execute post-cutover pipeline verification and artifact checks

  **What to do**:
  - Run pipeline from canonical tree.
  - Verify expected outputs for field posters, farm poster, farm HTML/Markdown, SSURGO cards/maps in migrated paths.
  - Validate canonical metadata/manifests presence and consistency.

  **Must NOT do**:
  - Do not mark migration complete without successful pipeline evidence.

  **Recommended Agent Profile**:
  - Category: `unspecified-high`
  - Skills: `farm-intelligence-reporting`, `ssurgo-poster-cards`

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 4
  - Blocks: T12, F1-F4
  - Blocked By: T4, T5, T8, T9, T10

  **References**:
  - `data/scripts/run_farm_pipeline.py` - primary verification command.
  - `.sisyphus/drafts/data-tree-reorganization.md` - required output preservation list.

  **Acceptance Criteria**:
  - [ ] Pipeline exits successfully on canonical paths.
  - [ ] Required report artifacts exist in canonical migrated locations.
  - [ ] Evidence bundle captured for command output and artifact inventory.

  **QA Scenarios**:

  ```text
  Scenario: End-to-end pipeline succeeds after cutover
    Tool: Bash
    Steps: run pipeline, then verify required output files and manifests
    Expected Result: success exit and all required artifacts present
    Evidence: .sisyphus/evidence/task-11-post-cutover.txt

  Scenario: Missing required output is detected
    Tool: Bash
    Steps: run artifact completeness checker over required output manifest
    Expected Result: checker fails if any required output absent
    Evidence: .sisyphus/evidence/task-11-post-cutover-error.txt
  ```

- [ ] 12. Rewrite `data/README.md` to match final canonical model

  **What to do**:
  - Update `data/README.md` to describe canonical tree, naming rules, shared-vs-field scope, and run flow.
  - Include Mermaid diagram with required accessibility metadata (`accTitle`, `accDescr`).

  **Must NOT do**:
  - Do not describe legacy tree as active.

  **Recommended Agent Profile**:
  - Category: `writing`
  - Skills: `wrighter` (structured technical docs)

  **Parallelization**:
  - Can Run In Parallel: NO
  - Parallel Group: Wave 4
  - Blocks: F1-F4
  - Blocked By: T11

  **References**:
  - `agentic/markdown_style_guide.md` - markdown requirements.
  - `agentic/mermaid_style_guide.md` - diagram constraints.

  **Acceptance Criteria**:
  - [ ] README aligns with actual post-cutover filesystem.
  - [ ] Mermaid diagram passes style/accessibility requirements.

  **QA Scenarios**:

  ```text
  Scenario: README path references match filesystem
    Tool: Bash
    Steps: parse referenced paths and verify existence in migrated tree
    Expected Result: all documented canonical paths exist
    Evidence: .sisyphus/evidence/task-12-readme.txt

  Scenario: Diagram accessibility fields missing check
    Tool: Bash
    Steps: validate Mermaid blocks include accTitle and accDescr
    Expected Result: validation fails if either field is absent
    Evidence: .sisyphus/evidence/task-12-readme-error.txt
  ```

---

## Final Verification Wave

- [ ] F1. Plan Compliance Audit (`oracle`)
  - Validate all Must Have and Must NOT Have items against actual outputs and evidence files.
  - Output: `Must Have [N/N] | Must NOT Have [N/N] | VERDICT`.

- [ ] F2. Code and Script Quality Review (`unspecified-high`)
  - Run lint/static checks available for Python scripts and scan for path anti-patterns.
  - Output: `Checks [PASS/FAIL] | Anti-pattern scan [PASS/FAIL] | VERDICT`.

- [ ] F3. Full QA Scenario Replay (`unspecified-high`)
  - Execute all task QA scenarios and verify evidence artifacts exist.
  - Output: `Scenarios [N/N pass] | Evidence [N/N] | VERDICT`.

- [ ] F4. Scope Fidelity and Contamination Review (`deep`)
  - Confirm no out-of-scope refactors and no cross-task contamination.
  - Output: `Scope [CLEAN/ISSUES] | Contamination [CLEAN/ISSUES] | VERDICT`.

---

## Commit Strategy

- Single final migration commit after T11 verification and T12 documentation sync.
- Message format: `refactor(data): hard-cutover data tree to scripts-shared-growers model`
- Include verification evidence references in commit body.

---

## Success Criteria

### Verification Commands

```bash
python data/scripts/run_farm_pipeline.py
grep -R "data/field-boundaries\|data/soil\|data/weather\|data/cdl\|data/EDA\|data/reporting/manifests" data/scripts --include="*.py"
find data/growers/iowa-demo-grower -name "farm.json" -o -name "field.json" -o -name "metadata.json" -o -name "manifest.json"
```

### Final Checklist

- [ ] All implementation tasks and QA scenarios completed with evidence
- [ ] Final verification wave returns APPROVE across F1-F4
- [ ] Canonical structure and docs are consistent and complete

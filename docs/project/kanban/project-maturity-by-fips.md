# Maturity by FIPS — Kanban Board

_Project: annual corn RM + soybean MG pipeline_
_Agent · Last updated: 2026-03-09 03:02 UTC_

---

## 📋 Board overview

**Period:** 2026-03-09 -> 2026-03-09
**Goal:** Establish a repo-native annual maturity-by-FIPS pipeline foundation with canonical geoadmin and maturity integration points
**WIP Limit:** 1 item In Progress

### Visual board

```mermaid
kanban
    Backlog
        task1[Render county maturity maps]
        task2[Add annual county GDD transforms]
    In Progress
        task3[Wave 2 county weather and GDD transforms]
    In Review
        [No items yet]
    Done
        [No items yet]
    Blocked
        [No items yet]
    Won't Do
        task4[Scheduler infrastructure in v1]
```

---

## 🚦 Board status

| Column             | Count | WIP Limit | Status                                     |
| ------------------ | ----- | --------- | ------------------------------------------ |
| 📋 **Backlog**     | 2     | —         | County GDD and map work remain queued      |
| 🔄 **In Progress** | 1     | 1         | 🟢 Under limit                             |
| 🔍 **In Review**   | 0     | —         | No review items yet                        |
| ✅ **Done**        | 1     | —         | County weather transform checkpoint landed |
| 🚫 **Blocked**     | 0     | —         | Clear                                      |
| 🚫 **Won't Do**    | 1     | —         | Scheduler work explicitly deferred         |

---

## 📋 Backlog

| #   | Item                             | Priority  | Estimate | Assignee | Notes                               |
| --- | -------------------------------- | --------- | -------- | -------- | ----------------------------------- |
| 1   | Add annual county GDD transforms | 🔴 High   | L        | Agent    | Consumes new county weather outputs |
| 2   | Render county maturity maps      | 🟡 Medium | M        | Agent    | Depends on crop maturity outputs    |

---

## 🔄 In progress

| Item                                     | Assignee | Started    | Expected | Days in column | Aging | Status                                                                                                           |
| ---------------------------------------- | -------- | ---------- | -------- | -------------- | ----- | ---------------------------------------------------------------------------------------------------------------- |
| Wave 2 county weather and GDD transforms | Agent    | 2026-03-09 | 0 days   | 0              | 🟢    | County daily weather now lands under `data/shared/weather/nasa-power/2025/`; county GDD is the next active slice |

> ⚠️ **WIP limit:** 1 / 1. Finish the current item before pulling another one.

---

## 🔍 In review

| Item           | Author | Reviewer | PR  | Days in review | Aging | Status |
| -------------- | ------ | -------- | --- | -------------- | ----- | ------ |
| [No items yet] |        |          |     |                |       |        |

---

## ✅ Done

| Item                                | Assignee | Completed  | Cycle time | PR                                                                  |
| ----------------------------------- | -------- | ---------- | ---------- | ------------------------------------------------------------------- |
| County weather transform checkpoint | Agent    | 2026-03-09 | <1 day     | [PR-00000004](../pr/pr-00000004-build-maturity-by-fips-pipeline.md) |

---

## 🚫 Blocked

| Item               | Assignee | Blocked since | Blocked by | Escalated to | Unblock action |
| ------------------ | -------- | ------------- | ---------- | ------------ | -------------- |
| [No blocked items] |          |               |            |              |                |

> 🟢 **0 items blocked.**

---

## 🚫 Won't Do

| Item                           | Date decided | Decision owner | Rationale                                                                      | Revisit trigger                         |
| ------------------------------ | ------------ | -------------- | ------------------------------------------------------------------------------ | --------------------------------------- |
| Scheduler infrastructure in v1 | 2026-03-09   | Human + Agent  | Annual manual invocation is sufficient for the first maturity pipeline release | Revisit after annual pipeline is stable |

---

## 📝 Board notes

### Decisions made this period

- **2026-03-09:** The maturity work will integrate into `.opencode/skills/...` and `data/scripts/...`, not a parallel package layout
- **2026-03-09:** Corn RM and soybean MG are heuristic planning products, not recommendation-grade outputs
- **2026-03-09:** Annual invocation is in scope; scheduler infrastructure is not
- **2026-03-09:** Wave 1 lands canonical roots and repo-native scaffolding before county logic or crop heuristics are implemented
- **2026-03-09:** The first shared geoadmin ingest path is working and writes canonical Level 0 country outputs from Natural Earth
- **2026-03-09:** TIGER/Line state and county layers now build canonically, and the demo farm fields map cleanly to county FIPS with no ambiguities
- **2026-03-09:** Shared geoadmin metadata and field-FIPS summary files now use repo-relative paths to keep annual reruns portable across worktrees
- **2026-03-09:** County daily weather now aggregates from the existing field-weather source into `data/shared/weather/nasa-power/2025/`, and uncovered counties remain absent with explicit coverage metadata

### Upcoming dependencies

- County GDD transforms
- Commit/push checkpoint for county weather aggregation code and artifacts
- Corn RM and soybean MG heuristic layers

---

## 🔗 References

- [PR-00000004](../pr/pr-00000004-build-maturity-by-fips-pipeline.md)
- [Issue-00000007](../issues/issue-00000007-build-maturity-by-fips-pipeline.md)
- [Work plan](../../.sisyphus/plans/grm-by-fips-geoadmin.md)

---

_Next update: after county GDD verification · Board owner: Agent_

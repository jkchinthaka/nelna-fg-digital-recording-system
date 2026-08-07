# Checklist Recorder Role Mapping

**Document status:** Configuration worksheet — **not** an approved RBAC assignment
**Created:** 2026-08-07 (Phase 07B)
**Permission foundation:** `scheduling.record_checklisttask`
**Related:** [PHASE_06E_FG_QA_001_PROVISIONAL_WORKFLOW.md](../decisions/PHASE_06E_FG_QA_001_PROVISIONAL_WORKFLOW.md)

## Purpose

Map owner-directed **logical** recorder business categories to actual system Roles before Phase 08 recording is enabled.

Do **not** treat this table as populated by engineering guesswork.

## Capability separation

| Capability | Permission (technical) | Meaning |
| --- | --- | --- |
| View task | `scheduling.view_checklisttask` | Inspect orchestration tasks |
| Manage task | `scheduling.manage_checklisttask` | Create/cancel administrative tasks |
| Record checklist | `scheduling.record_checklisttask` | Enter responses (Phase 08) |
| Supervisor review | Future Phase 09 | Not reserved in 07B |
| QA final decision | Future Phase 10 | Not reserved in 07B |

`manage_checklisttask` does **not** imply `record_checklisttask`.

## Intended business categories (provisional)

- Production Employee
- Store Employee
- QA

These are **not** automatically assigned to any Django Role.

## Mapping table

| Business category | System role (code/UUID) | Scope | Recording permission | Approved by | Approval date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Production Employee | CONFIGURATION / APPROVAL REQUIRED | CONFIGURATION / APPROVAL REQUIRED | `scheduling.record_checklisttask` | CONFIGURATION / APPROVAL REQUIRED | — | Logical category only |
| Store Employee | CONFIGURATION / APPROVAL REQUIRED | CONFIGURATION / APPROVAL REQUIRED | `scheduling.record_checklisttask` | CONFIGURATION / APPROVAL REQUIRED | — | Logical category only |
| QA | CONFIGURATION / APPROVAL REQUIRED | CONFIGURATION / APPROVAL REQUIRED | `scheduling.record_checklisttask` | CONFIGURATION / APPROVAL REQUIRED | — | Recorder category ≠ QA disposition authority |

## Future recording eligibility (Phase 08 contract)

A task may eventually be recorded only if:

1. Task status is `PENDING`
2. Bound `ChecklistVersion` remains the historical definition used at task creation (must have been PUBLISHED when created)
3. Actor has `record_checklisttask` in the task Organization scope
4. Task is not cancelled

No `IN_PROGRESS` status and no response tables are introduced in Phase 07B.

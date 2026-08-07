# Phase 07 Readiness Gate — Scheduling / Tasks

**Document status:** Evidence-driven entry gate — **not** Phase 07 authorization
**Created:** 2026-08-07 (Phase 06B)
**Updated:** 2026-08-07 (Phase 06C)
**Depends on:** Phase 06A/06B/06C definition + response schema; TEMPLATE-001 evidence

## Purpose

Phase 07 (schedules / tasks) must not start until the following questions are answered with named evidence. Unanswered items remain **EVIDENCE REQUIRED**.

Do not invent answers. Do not create Schedule/Task models while this gate is open.

## 06C note

A **proposed** FG-QA-001 structure now exists as a project draft ([FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md)). That draft does **not** close this gate:

- Scheduling / frequency remain **EVIDENCE REQUIRED**
- Who fills / reviews / approves / QA authority remain **EVIDENCE REQUIRED**
- Product limits remain **EVIDENCE REQUIRED** (ASM-001 / MASTER-001 open)
- TEMPLATE-001 = **PROJECT-PROPOSED DRAFT — VALIDATION REQUIRED** (not fully approved)

**Phase 07 remains blocked.**

## Readiness questions

| # | Question | Status |
| --- | --- | --- |
| 1 | At least one approved checklist definition exists (real TEMPLATE content)? | EVIDENCE REQUIRED — FG-QA-001 draft is proposed only, not approved |
| 2 | Scheduling trigger / frequency defined? | EVIDENCE REQUIRED |
| 3 | Scope relationship established (Organization / Product / Shift / Site / Department as applicable)? | EVIDENCE REQUIRED |
| 4 | Version selection / effective-date policy defined? | EVIDENCE REQUIRED |
| 5 | Who receives generated tasks? | EVIDENCE REQUIRED |
| 6 | What happens when a definition changes after tasks exist? | EVIDENCE REQUIRED |
| 7 | Can tasks reference retired definitions? | EVIDENCE REQUIRED |
| 8 | Timezone / cutoff rules evidenced? | EVIDENCE REQUIRED |
| 9 | Fill / review / approve / QA verify / resubmit workflow evidenced (TEMPLATE-001 §10)? | EVIDENCE REQUIRED |
| 10 | Scheduling trigger choices evidenced (shift/batch/daily/hourly/before-after/ad hoc — TEMPLATE-001 §9)? | EVIDENCE REQUIRED |

## Technical note

Phase 06 provides a configurable definition/versioning engine and provisional response-definition schema. Existence of DRAFT/PUBLISHED/RETIRED machinery and a project-proposed FG-QA-001 draft do **not** satisfy question 1 without approved business forms.

## Related

- [proposals/FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md)
- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [ROADMAP.md](../ROADMAP.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)

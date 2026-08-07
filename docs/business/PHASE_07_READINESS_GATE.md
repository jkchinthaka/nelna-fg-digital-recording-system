# Phase 07 Readiness Gate — Scheduling / Tasks

**Document status:** Evidence-driven entry gate — **not** Phase 07 authorization
**Created:** 2026-08-07 (Phase 06B)
**Updated:** 2026-08-07 (Phase 06D)
**Depends on:** Phase 06A/06B/06C/06D definition + response schema + DRAFT loader; TEMPLATE-001 evidence

## Purpose

Phase 07 (schedules / tasks) must not start until the following questions are answered with named evidence. Unanswered items remain **EVIDENCE REQUIRED**.

Do not invent answers. Do not create Schedule/Task models while this gate is open.

## Now available (technical / proposed only)

- Proposed FG-QA-001 structure ([FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md))
- Provisional generic response-definition schema (Phase 06C)
- Ability to instantiate the proposal as an Organization-scoped **DRAFT** for review (`load_fg_qa_001_draft` — see [FG_QA_001_DRAFT_LOADING.md](../operations/FG_QA_001_DRAFT_LOADING.md))
- Internal validation worksheet ([FG_QA_001_INTERNAL_VALIDATION_CHECKLIST.md](FG_QA_001_INTERNAL_VALIDATION_CHECKLIST.md)) — existence is not approval

## Still unresolved (Phase 07 remains blocked)

- Final checklist approval (TEMPLATE-001 still **PROJECT-PROPOSED DRAFT — VALIDATION REQUIRED**)
- Product applicability (MASTER-001 / ASM-001 open)
- Shift applicability (ASM-005 / ASM-006 open)
- Site / Department applicability
- Scheduling trigger
- Frequency
- Responsible recorder
- Supervisor role
- QA authority
- Effective-version selection rule
- Rejected / corrected record behavior

**Phase 07 remains blocked.**

## Readiness questions

| # | Question | Status |
| --- | --- | --- |
| 1 | At least one approved checklist definition exists (real TEMPLATE content)? | EVIDENCE REQUIRED — FG-QA-001 draft / DRAFT load is proposed review only, not approved |
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

Phase 06 provides a configurable definition/versioning engine, provisional response-definition schema, and an explicit DRAFT-only proposal loader. Existence of DRAFT/PUBLISHED/RETIRED machinery, a project-proposed FG-QA-001 draft, or a loaded DRAFT for review do **not** satisfy question 1 without approved business forms.

## Related

- [proposals/FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md)
- [FG_QA_001_INTERNAL_VALIDATION_CHECKLIST.md](FG_QA_001_INTERNAL_VALIDATION_CHECKLIST.md)
- [FG_QA_001_DRAFT_LOADING.md](../operations/FG_QA_001_DRAFT_LOADING.md)
- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [ROADMAP.md](../ROADMAP.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)

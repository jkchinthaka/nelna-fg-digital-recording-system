# Phase 07 Readiness Gate — Scheduling / Tasks

**Document status:** Evidence-driven entry gate — **not** Phase 07 authorization
**Created:** 2026-08-07 (Phase 06B)
**Depends on:** Phase 06A/06B definition engine; TEMPLATE-001 evidence

## Purpose

Phase 07 (schedules / tasks) must not start until the following questions are answered with named evidence. Unanswered items remain **EVIDENCE REQUIRED**.

Do not invent answers. Do not create Schedule/Task models while this gate is open.

## Readiness questions

| # | Question | Status |
| --- | --- | --- |
| 1 | At least one approved checklist definition exists (real TEMPLATE content)? | EVIDENCE REQUIRED |
| 2 | Scheduling trigger / frequency defined? | EVIDENCE REQUIRED |
| 3 | Scope relationship established (Organization / Product / Shift / Site / Department as applicable)? | EVIDENCE REQUIRED |
| 4 | Version selection / effective-date policy defined? | EVIDENCE REQUIRED |
| 5 | Who receives generated tasks? | EVIDENCE REQUIRED |
| 6 | What happens when a definition changes after tasks exist? | EVIDENCE REQUIRED |
| 7 | Can tasks reference retired definitions? | EVIDENCE REQUIRED |
| 8 | Timezone / cutoff rules evidenced? | EVIDENCE REQUIRED |

## Technical note

Phase 06 provides a configurable definition/versioning engine only. Existence of DRAFT/PUBLISHED/RETIRED machinery does **not** satisfy question 1 without approved business forms.

## Related

- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [ROADMAP.md](../ROADMAP.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)

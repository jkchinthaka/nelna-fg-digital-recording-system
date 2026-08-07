# TEMPLATE-001 — Checklist Template Evidence Intake

**Document status:** Evidence collection contract — **not** approved business truth
**Requirement:** TEMPLATE-001 (related: TEMPLATE-002, TEMPLATE-003, ASM-001, ASM-003)
**Created:** 2026-08-07 (Phase 06B)
**Technical foundation:** Phase 06A/06B configurable unseeded checklist definition/versioning

## Purpose

Stakeholders must supply approved checklist/form evidence before real content loading, response-schema implementation, or Phase 07 scheduling.

Empty fields are **EVIDENCE REQUIRED**. Do not invent answers.

Companion template: [templates/CHECKLIST_ITEM_EVIDENCE_INVENTORY.csv](templates/CHECKLIST_ITEM_EVIDENCE_INVENTORY.csv) (headers only).

## Current technical baseline (not business approval)

| Aspect | Provisional technical state |
| --- | --- |
| Entities | ChecklistTemplate / ChecklistVersion / ChecklistSection / ChecklistItem |
| Scope | Organization-owned; optional provisional FG Product association |
| Lifecycle | DRAFT → PUBLISHED → RETIRED; published/retired structure immutable |
| Response types | Not modeled — EVIDENCE REQUIRED |
| Limits / temperature / instruments / training | Not modeled — EVIDENCE REQUIRED |
| Seeded content | None |

---

## A. Checklist identity

| Item | Value |
| --- | --- |
| Official checklist / form name | EVIDENCE REQUIRED |
| Official code / reference number | EVIDENCE REQUIRED |
| Business owner | EVIDENCE REQUIRED |
| Organization applicability | EVIDENCE REQUIRED |
| Product applicability | EVIDENCE REQUIRED |
| Existing paper/ERP revision identifier | EVIDENCE REQUIRED |

## B. Structure

| Item | Value |
| --- | --- |
| Sections (titles, order) | EVIDENCE REQUIRED |
| Question / item order | EVIDENCE REQUIRED |
| Item wording | EVIDENCE REQUIRED |
| Instructions / help text | EVIDENCE REQUIRED |
| Mandatory / optional rule per item | EVIDENCE REQUIRED |

## C. Response requirements

For **each** item, supply:

| Field | Value |
| --- | --- |
| Required response type | EVIDENCE REQUIRED |
| Allowed values | EVIDENCE REQUIRED |
| Data type | EVIDENCE REQUIRED |
| Unit (if applicable) | EVIDENCE REQUIRED |
| Validation rule | EVIDENCE REQUIRED |
| Null / N/A policy | EVIDENCE REQUIRED |

Do not prefill response types. Candidate types to **ask about** (not approved): text, number, boolean, select, date/time, temperature, photo, signature, other.

## D. Limits / acceptance

| Field | Value |
| --- | --- |
| Minimum | EVIDENCE REQUIRED |
| Maximum | EVIDENCE REQUIRED |
| Target | EVIDENCE REQUIRED |
| Tolerance | EVIDENCE REQUIRED |
| Pass / fail rule | EVIDENCE REQUIRED |
| Warning vs hard failure | EVIDENCE REQUIRED |

## E. Temperature requirements (ASM-001)

| Field | Value |
| --- | --- |
| Whether temperature applies | EVIDENCE REQUIRED |
| Unit | EVIDENCE REQUIRED |
| Minimum | EVIDENCE REQUIRED |
| Maximum | EVIDENCE REQUIRED |
| Source policy / document | EVIDENCE REQUIRED |

## F. Instrument requirements

| Field | Value |
| --- | --- |
| Instrument required? | EVIDENCE REQUIRED |
| Instrument type | EVIDENCE REQUIRED |
| Calibration requirement | EVIDENCE REQUIRED |
| Evidence source | EVIDENCE REQUIRED |

## G. Training / role requirements

| Field | Value |
| --- | --- |
| Who may record | EVIDENCE REQUIRED |
| Required training | EVIDENCE REQUIRED |
| Certification if applicable | EVIDENCE REQUIRED |

## H. Operational context

Questions for stakeholders — **not** schema commitments:

| Field | Value |
| --- | --- |
| Product | EVIDENCE REQUIRED |
| Shift | EVIDENCE REQUIRED |
| Site | EVIDENCE REQUIRED |
| Department | EVIDENCE REQUIRED |
| Process / stage | EVIDENCE REQUIRED |

## I. Scheduling / frequency (Phase 07 gate)

| Field | Value |
| --- | --- |
| When checklist is required | EVIDENCE REQUIRED |
| Per shift? | EVIDENCE REQUIRED |
| Per batch? | EVIDENCE REQUIRED |
| Per day? | EVIDENCE REQUIRED |
| Ad hoc / event trigger? | EVIDENCE REQUIRED |

## J. Approval / provenance

| Field | Value |
| --- | --- |
| Supplied by | EVIDENCE REQUIRED |
| Department / team | EVIDENCE REQUIRED |
| Source document | EVIDENCE REQUIRED |
| Source version | EVIDENCE REQUIRED |
| Date | EVIDENCE REQUIRED |
| Approved by | EVIDENCE REQUIRED |
| Approval date | EVIDENCE REQUIRED |

---

## Explicit non-claims

- Phase 06A/06B technical work does **not** resolve TEMPLATE-001.
- Optional Product association is provisional, not proven mandatory.
- Response-type candidate list is a question list only.
- This intake is **not** an import specification and does **not** authorize CSV import code.
- Phase 07 must not assume unanswered scheduling/scope answers.

## Related

- [ASSUMPTION_REGISTER.md](ASSUMPTION_REGISTER.md)
- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)
- [PHASE_07_READINESS_GATE.md](PHASE_07_READINESS_GATE.md)

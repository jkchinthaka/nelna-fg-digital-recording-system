# TEMPLATE-001 — Checklist Template Evidence Intake

**Document status:** Evidence collection contract — **not** approved business truth
**Requirement:** TEMPLATE-001 (related: TEMPLATE-002, TEMPLATE-003, ASM-001, ASM-003)
**Created:** 2026-08-07 (Phase 06B)
**Updated:** 2026-08-07 — Phase 06C: note no formal source form; FG-QA-001 Draft v0.1 project-proposed pending validation
**Technical foundation:** Phase 06A/06B configurable unseeded checklist definition/versioning; Phase 06C provisional response-definition schema

## Purpose

Stakeholders must supply **approved real checklist/form evidence** before:

- loading official form content into the system
- treating response types as approved business rules (06C primitives are definition-schema only)
- authorizing Phase 07 scheduling / tasks

Empty fields are **EVIDENCE REQUIRED**. Do not invent answers.

**No formal Nelna FG checklist source form is currently available.** A project-proposed draft exists for validation only:

- [proposals/FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md) — FG-QA-001 Draft v0.1
- Status: **PROJECT-PROPOSED DRAFT — VALIDATION REQUIRED**
- **Still not officially approved** for production, pilot, or operational use
- Not seeded into Organizations

Companion per-item worksheet (headers only):
[templates/CHECKLIST_ITEM_EVIDENCE_INVENTORY.csv](templates/CHECKLIST_ITEM_EVIDENCE_INVENTORY.csv)

---

## Current technical baseline (not business approval)

| Aspect | Provisional technical state |
| --- | --- |
| Entities | ChecklistTemplate / ChecklistVersion / ChecklistSection / ChecklistItem |
| Scope | Organization-owned; optional provisional FG Product association |
| Lifecycle | DRAFT → PUBLISHED → RETIRED; published/retired structure immutable |
| Response types | Provisional definition-schema primitives (YES_NO, YES_NO_NA, NUMBER, TEXT, SELECT) — business content still EVIDENCE REQUIRED |
| Limits / temperature / instruments / training | Limits unset; temperature = NUMBER+unit proposal only; instruments/training EVIDENCE REQUIRED |
| Scheduling / recording / review workflow | Not modeled — Phase 07+; EVIDENCE REQUIRED |
| Seeded content | None — FG-QA-001 draft is documentation only |

---

## 1. Actual checklist / form (source artifact)

Supply at least one real artifact. Preferred formats:

| Artifact type | Provided? | Location / filename | Notes |
| --- | --- | --- | --- |
| PDF | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| Excel | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| Word | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| Screenshot / photo | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| Existing paper form (scan/photo) | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |

Store artifacts outside invented app content (e.g. controlled document store). Record path/reference here only.

---

## 2. Checklist identity

| Item | Value |
| --- | --- |
| Official form name | EVIDENCE REQUIRED |
| Form / reference code | EVIDENCE REQUIRED |
| Revision / version | EVIDENCE REQUIRED |
| Department / business owner | EVIDENCE REQUIRED |

---

## 3. Actual sections

| Section order | Section name | Notes |
| --- | --- | --- |
| EVIDENCE REQUIRED | EVIDENCE REQUIRED | EVIDENCE REQUIRED |

Use additional rows as needed. Do not invent section titles.

---

## 4. Actual checklist items / questions

| Item order | Section | Exact wording | Mandatory / optional | Notes |
| --- | --- | --- | --- | --- |
| EVIDENCE REQUIRED | EVIDENCE REQUIRED | EVIDENCE REQUIRED | EVIDENCE REQUIRED | EVIDENCE REQUIRED |

Prefer completing the CSV inventory for item-level capture.

---

## 5. For every item — operator entry

For **each** item, state what the operator enters. Do not preselect a type as approved schema.

| Candidate entry | Applies to this item? |
| --- | --- |
| Text | EVIDENCE REQUIRED |
| Number | EVIDENCE REQUIRED |
| Yes / No | EVIDENCE REQUIRED |
| Selection (list values) | EVIDENCE REQUIRED |
| Temperature | EVIDENCE REQUIRED |
| Date / time | EVIDENCE REQUIRED |
| Photo | EVIDENCE REQUIRED |
| Signature | EVIDENCE REQUIRED |
| N/A allowed? | EVIDENCE REQUIRED |
| Other (specify) | EVIDENCE REQUIRED |

See also [RESPONSE_TYPE_DECISION_REGISTER.md](RESPONSE_TYPE_DECISION_REGISTER.md) (question list only).

---

## 6. Validation / acceptance

Per applicable item:

| Field | Value |
| --- | --- |
| Minimum | EVIDENCE REQUIRED |
| Maximum | EVIDENCE REQUIRED |
| Target | EVIDENCE REQUIRED |
| Tolerance | EVIDENCE REQUIRED |
| Pass / fail rule | EVIDENCE REQUIRED |
| Warning rule | EVIDENCE REQUIRED |

---

## 7. Measurement information

Per applicable item:

| Field | Value |
| --- | --- |
| Unit | EVIDENCE REQUIRED |
| Instrument | EVIDENCE REQUIRED |
| Calibration requirement | EVIDENCE REQUIRED |

ASM-001 temperature-class limits remain unresolved until evidenced here or in linked policy.

---

## 8. Operational scope

Questions for stakeholders — **not** schema commitments:

| Field | Value |
| --- | --- |
| Which Product? | EVIDENCE REQUIRED |
| Which Organization? | EVIDENCE REQUIRED |
| Site? | EVIDENCE REQUIRED |
| Department? | EVIDENCE REQUIRED |
| Shift? | EVIDENCE REQUIRED |
| Process / stage? | EVIDENCE REQUIRED |

---

## 9. Scheduling

(Phase 07 gate — do not invent frequency)

| Trigger / frequency | Applies? |
| --- | --- |
| Every shift? | EVIDENCE REQUIRED |
| Every batch? | EVIDENCE REQUIRED |
| Daily? | EVIDENCE REQUIRED |
| Hourly? | EVIDENCE REQUIRED |
| Before / after production? | EVIDENCE REQUIRED |
| Ad hoc? | EVIDENCE REQUIRED |
| Other (specify) | EVIDENCE REQUIRED |

See [PHASE_07_READINESS_GATE.md](PHASE_07_READINESS_GATE.md).

---

## 10. Workflow

| Question | Answer |
| --- | --- |
| Who fills it? | EVIDENCE REQUIRED |
| Who reviews it? | EVIDENCE REQUIRED |
| Who approves it? | EVIDENCE REQUIRED |
| Does QA verify it? | EVIDENCE REQUIRED |
| Can rejected records be corrected / resubmitted? | EVIDENCE REQUIRED |

---

## 11. Evidence (attachments / marks)

| Question | Answer |
| --- | --- |
| Photo required? | EVIDENCE REQUIRED |
| File attachment? | EVIDENCE REQUIRED |
| Signature? | EVIDENCE REQUIRED |
| Remarks? | EVIDENCE REQUIRED |

---

## 12. Source / approval

| Item | Value |
| --- | --- |
| Who provided the form? | EVIDENCE REQUIRED |
| Current approved revision? | EVIDENCE REQUIRED |
| Effective date? | EVIDENCE REQUIRED |
| Approved by | EVIDENCE REQUIRED |
| Approval date | EVIDENCE REQUIRED |
| Source document reference | EVIDENCE REQUIRED |

---

## Explicit non-claims

- Phase 06A/06B/06C technical work does **not** fully resolve TEMPLATE-001.
- FG-QA-001 Draft v0.1 is a **project-proposed** baseline pending QA/Production/IT validation — **not** officially approved.
- Optional Product association is provisional, not proven mandatory.
- Response-type primitives in 06C are for definition schema only — not approved operational form content.
- This intake is **not** an import specification and does **not** authorize CSV import code.
- Phase 07 must not start from unanswered scheduling / workflow / scope answers.
- Do not invent form content, limits, or temperature rules to unblock engineering.
- ASM-001 and MASTER-001 remain open.

## Related

- [proposals/FG_QA_001_DRAFT_V0_1.md](proposals/FG_QA_001_DRAFT_V0_1.md)
- [ASSUMPTION_REGISTER.md](ASSUMPTION_REGISTER.md)
- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)
- [PHASE_07_READINESS_GATE.md](PHASE_07_READINESS_GATE.md)
- [RESPONSE_TYPE_DECISION_REGISTER.md](RESPONSE_TYPE_DECISION_REGISTER.md)

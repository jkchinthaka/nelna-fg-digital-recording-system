# Response-Type Decision Register — Checklist Items

**Document status:** Evidence question list — **not** an approved schema
**Created:** 2026-08-07 (Phase 06B)
**Requirement link:** TEMPLATE-001 / TEMPLATE-003

## Current implementation

`ChecklistItem` stores definition text only (`code`, `label`, optional `help_text`, `is_required`, `position`).

No response-type enum, answer payload, select options, temperature fields, photo/signature fields, or validation limits exist in Phase 06.

## Decision required before Phase 08 recording

Stakeholders must evidence which response types are required. The following are **candidate questions only** — not approved requirements:

| Candidate type | Required for MVP? | Evidence source | Notes |
| --- | --- | --- | --- |
| text | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| number | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| boolean | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| select | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| date/time | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| temperature | EVIDENCE REQUIRED | EVIDENCE REQUIRED | Linked to ASM-001 |
| photo | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| signature | EVIDENCE REQUIRED | EVIDENCE REQUIRED | |
| other | EVIDENCE REQUIRED | EVIDENCE REQUIRED | Specify |

Do not implement these types until evidence and an explicit technical decision authorize them.

## Related

- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)

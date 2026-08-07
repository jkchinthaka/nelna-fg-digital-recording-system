# Checklist Definition Management UI (Phase 06A / 06B / 06C)

**Document status:** Phase 06A definition management UI + Phase 06B governance hardening + Phase 06C response-type / option editor
**Last updated:** 2026-08-07
**Language:** English UI pending Sinhala design/UAT resolution (DEBT-01C-R-NOTO remains open)

## Purpose

Authorized staff configure versioned checklist definitions without inventing operational form content or numerical limits.

## Boundaries

- Definition/versioning only (including provisional response-definition fields).
- No scheduling, tasks, recording, review, verification, or evidence UI.
- TEMPLATE / ASM evidence remains required for real content; FG-QA-001 draft is **NOT APPROVED** and not auto-loaded.
- Published / Retired versions are read-only; mutations require a new Draft.
- No automatic RELEASE / HOLD / REJECT behaviour from SELECT labels.

## Screens

| Screen | Route | Notes |
| --- | --- | --- |
| Template list | `/checklists/` | Search/filter/paginate; object-aware Edit via manageable org IDs |
| Create template | `/checklists/new/` | Visible only with ≥1 manageable Organization |
| Template detail | `/checklists/<uuid>/` | Versions summary; activate/deactivate when manageable |
| Edit template | `/checklists/<uuid>/edit/` | Organization immutable; catalogue fields only |
| Create/clone version | `/checklists/<uuid>/versions/new/` | Blank or clone into new DRAFT (includes options when present) |
| Version detail | `/checklists/versions/<uuid>/` | Draft editor or read-only published/retired |
| Section/item forms | nested routes | Draft-only mutations; POST + CSRF |

## Lifecycle UX

- Status shown as text: Draft / Published / Retired (not color alone).
- Publish confirms immutability.
- Retire available for published versions only.
- Unauthorized manage controls are absent (not merely CSS-hidden).

## Editor behavior

- Accessible Move up / Move down (no drag-and-drop).
- Empty version state prompts adding a section.
- Server-side ordering authoritative.

## Phase 06C — response type and option editor

- Draft item editor includes **response type** selection among provisional primitives: `YES_NO`, `YES_NO_NA`, `NUMBER`, `TEXT`, `SELECT`.
- **NUMBER:** optional unit (e.g. proposed °C for temperature items); optional minimum/maximum — both may remain empty; UI must not invent defaults that look like approved limits.
- **SELECT:** draft option editor to add/reorder/remove options; publish requires ≥1 valid option.
- Published/retired views show response type and options as read-only.
- Disposition-style option values (e.g. RELEASE / HOLD / REJECT) are displayed as labels only — no release-engine controls.

## Related

- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)
- [RESPONSE_TYPE_DECISION_REGISTER.md](../business/RESPONSE_TYPE_DECISION_REGISTER.md)
- [proposals/FG_QA_001_DRAFT_V0_1.md](../business/proposals/FG_QA_001_DRAFT_V0_1.md)
- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](../business/TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [PHASE_06C_TEST_PLAN.md](../testing/PHASE_06C_TEST_PLAN.md)

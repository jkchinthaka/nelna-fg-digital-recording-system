# Checklist Definition Management UI (Phase 06A / 06B)

**Document status:** Phase 06A definition management UI + Phase 06B governance hardening
**Last updated:** 2026-08-07
**Language:** English UI pending Sinhala design/UAT resolution (DEBT-01C-R-NOTO remains open)

## Purpose

Authorized staff configure versioned checklist definitions without inventing operational form content.

## Boundaries

- Definition/versioning only.
- No scheduling, tasks, recording, review, verification, or evidence UI.
- TEMPLATE / ASM evidence remains required for real content.
- Response-type schema deferred.
- Published / Retired versions are read-only; mutations require a new Draft.

## Screens

| Screen | Route | Notes |
| --- | --- | --- |
| Template list | `/checklists/` | Search/filter/paginate; object-aware Edit via manageable org IDs |
| Create template | `/checklists/new/` | Visible only with ≥1 manageable Organization |
| Template detail | `/checklists/<uuid>/` | Versions summary; activate/deactivate when manageable |
| Edit template | `/checklists/<uuid>/edit/` | Organization immutable; catalogue fields only |
| Create/clone version | `/checklists/<uuid>/versions/new/` | Blank or clone into new DRAFT |
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

## Related

- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)
- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](../business/TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)

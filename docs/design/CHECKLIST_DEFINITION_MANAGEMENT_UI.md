# Checklist Definition Management UI (Phase 06A)

**Document status:** Phase 06A definition management UI  
**Last updated:** 2026-08-07  
**Language:** English UI pending Sinhala design/UAT resolution (DEBT-01C-R-NOTO remains open)

## Purpose

Authorized staff configure versioned checklist definitions without inventing operational form content.

## Boundaries

- Definition/versioning only.
- No scheduling, tasks, recording, review, verification, or evidence UI.
- TEMPLATE / ASM evidence remains required for real content.
- Response-type schema deferred.

## Screens

| Screen | Route | Notes |
| --- | --- | --- |
| Template list | `/checklists/` | Search/filter/paginate; object-aware Edit |
| Create template | `/checklists/new/` | Manage-scope organizations; optional Product |
| Template detail | `/checklists/<uuid>/` | Versions summary; activate/deactivate |
| Edit template | `/checklists/<uuid>/edit/` | Organization immutable |
| Create/clone version | `/checklists/<uuid>/versions/new/` | Blank or clone into new DRAFT |
| Version detail | `/checklists/versions/<uuid>/` | Draft editor or read-only published/retired |
| Section/item forms | nested routes | Draft-only mutations; POST + CSRF |

## Editor behavior

- Accessible Move up / Move down (no drag-and-drop).
- Publish confirms immutability.
- Retire available for published versions.
- Status shown as text (Draft / Published / Retired), not color alone.

## Related

- [ADR-010-CHECKLIST-DEFINITION-VERSIONING.md](../architecture/ADR-010-CHECKLIST-DEFINITION-VERSIONING.md)
- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)

# FG Product Management UI (Phase 05A)

**Document status:** Phase 05A operational management UI  
**Last updated:** 2026-08-07  
**Language:** English UI pending Sinhala design/UAT resolution (DEBT-01C-R-NOTO remains open)

## Purpose

Authorized staff configure and maintain FG Product definitions without Django admin or direct database edits.

## Boundaries

- Configurable, unseeded foundation only.
- MASTER-001 remains evidence-required.
- No category/UOM/ERP fields.
- No checklist/recording functionality.

## Screens

| Screen | Route | Permission |
| --- | --- | --- |
| List | `/products/` | `master_data.view_fgproduct` |
| Create | `/products/new/` | `master_data.manage_fgproduct` |
| Detail | `/products/<uuid>/` | view on product organization |
| Edit | `/products/<uuid>/edit/` | manage on product organization |
| Activate / Deactivate | POST only | manage |

## UX notes

- Organization immutable after create.
- Empty states distinguish “none configured” vs “no filter matches”.
- Desktop table / mobile cards (shared management CSS with Shift UI).
- Overnight/Shift-specific concepts do not apply.

## Related

- [PHASE_05_FG_PRODUCT_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_05_FG_PRODUCT_PROVISIONAL_CONFIGURATION.md)
- [ADR-009-FG-MASTER-DATA-DOMAIN.md](../architecture/ADR-009-FG-MASTER-DATA-DOMAIN.md)

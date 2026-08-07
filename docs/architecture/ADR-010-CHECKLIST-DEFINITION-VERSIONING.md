# ADR-010 — Checklist Definition and Versioning (Phase 06A)

**Status:** Accepted (provisional technical direction for Phase 06A)  
**Date:** 2026-08-07

## Context

Phase 06 requires versioned checklist definitions for later scheduling and recording. TEMPLATE-001 / ASM-003 form inventory and official checklist content were not supplied. ASM-001 temperature-class limits remain unresolved. Waiting indefinitely blocks technical progress. The project owner directed a configurable, unseeded definition/versioning foundation.

## Decision

1. Bounded context: `apps/checklists` — **definitions only**.
2. Entities: `ChecklistTemplate`, `ChecklistVersion`, `ChecklistSection`, `ChecklistItem`.
3. Organization-scoped templates; **optional** provisional `FGProduct` association.
4. Lifecycle: DRAFT → PUBLISHED → RETIRED; published/retired structure is immutable.
5. New changes require a new DRAFT (blank or cloned). Cloning copies rows; rows are never shared.
6. Version numbers allocated under template row lock (`select_for_update` + max+1).
7. No response-type engine in 06A (deferred — EVIDENCE REQUIRED).
8. No temperature/limit/instrument/training/photo/signature/QA rule fields.
9. No Schedule/Task/Record/Submission/Review/Verification/Evidence entities.
10. Permissions: `checklists.view_checklisttemplate`, `checklists.manage_checklist` (org-scoped).
11. Audit events: `CHECKLIST_TEMPLATE_*`, `CHECKLIST_VERSION_*` with safe metadata.
12. Management UI for definition authoring only.

## Consequences

- Unblocks Phase 06 technical work without inventing form content.
- Phase 07+ can reference published versions later without mutating history.
- MASTER-001 / ASM-001 / TEMPLATE evidence remain open.
- Phase 06 roadmap “two approved checklist types” content exit criterion remains unmet.

## Related

- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [MODULE_MAP.md](MODULE_MAP.md)
- [CHECKLIST_DEFINITION_MANAGEMENT_UI.md](../design/CHECKLIST_DEFINITION_MANAGEMENT_UI.md)

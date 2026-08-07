# ADR-010 — Checklist Definition and Versioning (Phase 06A / 06B)

**Status:** Accepted (provisional technical direction; 06B governance hardening)
**Date:** 2026-08-07
**Updated:** 2026-08-07 (Phase 06B)

## Context

Phase 06 requires versioned checklist definitions for later scheduling and recording. TEMPLATE-001 / ASM-003 form inventory and official checklist content were not supplied. ASM-001 temperature-class limits remain unresolved. Waiting indefinitely blocks technical progress. The project owner directed a configurable, unseeded definition/versioning foundation. Phase 06B hardens lifecycle governance without expanding schema or inventing content.

## Decision

1. Bounded context: `apps/checklists` — **definitions only**.
2. Entities: `ChecklistTemplate`, `ChecklistVersion`, `ChecklistSection`, `ChecklistItem`.
3. Organization-scoped templates; **optional** provisional `FGProduct` association.
4. Lifecycle: DRAFT → PUBLISHED → RETIRED only. Transitions are centralized (`assert_version_transition_allowed`). Reverse / skip transitions are denied.
5. Published/retired structure is immutable through services, HTTP mutations, and admin structural paths.
6. New changes require a new DRAFT (blank or cloned). Cloning copies rows from DRAFT/PUBLISHED/RETIRED sources; rows are never shared; source remains unchanged.
7. Version numbers allocated under template row lock (`select_for_update` + max+1) with uniqueness constraint and one IntegrityError retry.
8. Contiguous positions are maintained after remove (recompact); reorder uses safe sentinel swap.
9. Template catalogue fields (`code`, `name`, `description`, `product`, `is_active`) are identity/catalogue metadata. Changing them does **not** mutate historical `ChecklistVersion` section/item rows. Historical definition text lives on version-owned rows. No snapshot fields added in 06B.
10. No response-type engine (deferred — EVIDENCE REQUIRED). See RESPONSE_TYPE_DECISION_REGISTER.
11. No temperature/limit/instrument/training/photo/signature/QA rule fields.
12. No Schedule/Task/Record/Submission/Review/Verification/Evidence entities.
13. Permissions: `checklists.view_checklisttemplate`, `checklists.manage_checklist` (org-scoped); UI uses precomputed manageable organization IDs.
14. Audit events: `CHECKLIST_TEMPLATE_*`, `CHECKLIST_VERSION_*` with safe metadata (no full question text).
15. Publish requires a non-empty technical definition graph (≥1 section and ≥1 item with non-blank titles/codes/labels). This is structural integrity, not a business minimum question count.

## Consequences

- Unblocks Phase 06 technical work without inventing form content.
- Phase 07 remains evidence-gated ([PHASE_07_READINESS_GATE.md](../business/PHASE_07_READINESS_GATE.md)).
- MASTER-001 / ASM-001 / TEMPLATE-001 evidence remain open.
- Phase 06 roadmap content exit criterion remains unmet.

## Related

- [PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md](../decisions/PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION.md)
- [TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md](../business/TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE.md)
- [MODULE_MAP.md](MODULE_MAP.md)
- [CHECKLIST_DEFINITION_MANAGEMENT_UI.md](../design/CHECKLIST_DEFINITION_MANAGEMENT_UI.md)

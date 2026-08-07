# Module Map

**Document status:** Living module boundaries — Phase 04–07A
**Phase:** 03–06E complete units · 07A batch checklist task foundation · MASTER-001 / TEMPLATE pending
**Last updated:** 2026-08-07

This map guides implementation. Do not scaffold future business apps before their phase.
Do **not** rename FG master data, checklist, recording, review, or evidence work as Phase 04.

| Module | Responsibility | Data ownership | Public service boundary | Prohibited dependencies | Planned phase |
| --- | --- | --- | --- | --- | --- |
| accounts | Identity, employee-code authentication, password/lockout lifecycle | User | Auth services; admin account management | Must not embed checklist business rules | **03 complete** |
| organizations | Organization / site / department scope hierarchy; configurable unseeded Shift (04A) + management UI (04B) | Organization, Site, Department, Shift | Hierarchy + Shift create/update/activate/deactivate services; scoped selectors; Shift management views | Must not invent or seed Nelna org/site/dept/shift business values | **03 complete** + **04A/04B** |
| access_control | Roles, scoped assignments, authorization API | Role, ScopedRoleAssignment | Permission checks; decorators/mixins | Must not seed business roles or Shift role mappings without evidence | **03 complete** |
| security_audit | Append-oriented auth/RBAC/Shift/Product/Checklist/Task security events | SecurityAuditEvent | `record_event` only; no secrets | Must not store credentials | **03+** |
| master_data | Configurable unseeded FG Product (05A); object-aware UI authz (05B); other masters only when approved | FGProduct | Product create/update/activate/deactivate; scoped selectors; management UI | Must not invent product catalogues; no silent ERP DB import | **05A/05B** |
| instruments | Instrument register and calibration status references as approved | Instrument records | Fitness-for-use queries used by recording | Must not invent calibration intervals | **05** (not started) |
| training | Training completion gates as approved | Training records / qualifications refs | Eligibility checks for task assignment | Must not invent training matrices | **05** (not started) |
| checklists | Definition/versioning (06A–06D); provisional workflow formalization docs (06E) | ChecklistTemplate, ChecklistVersion, ChecklistSection, ChecklistItem | Template/version lifecycle; DRAFT loader; management UI | No recording ownership; no automatic RELEASE/HOLD/REJECT; FG-QA-001 never auto-published | **06A–06E** |
| scheduling | Batch-triggered checklist task orchestration (07A); future recurrence planning | ChecklistTask (`batch_reference`; no ProductionBatch master yet) | create/cancel services; scoped selectors; orchestration UI | Must not store answers; no DRAFT/RETIRED tasks; no auto latest-version; no invented batch ERP fields; no auto role mapping | **07A** |
| tasks | Assignment of work to users/roles (deferred — avoid Celery name clash; 07A in `scheduling`) | Future task assignment states | Assign/claim/complete coordination | Must not store full answer payloads | **07** (beyond 07A) |
| records | Operator draft/submit and immutable submitted payloads | Records, answers/snapshots, amendment chains | Submit, amend, read record services | No in-place edit of submitted/approved records | **08–09** |
| reviews | Supervisor checking workflow | Check actions and outcomes | Check/reject/request-amendment services | Must not perform QA verification ownership | **09** |
| quality | QA verification workflow | Verification actions | Verify services | No AI final verification | **10** |
| nonconformance | Holds and NC records | NC/hold entities | Open/update NC services | Post-MVP unless approved | **12** |
| capa | Corrective and preventive actions | CAPA entities | CAPA lifecycle services | No AI final CAPA closure | **12** |
| loading | Loading controls | Loading check records | Loading workflow services | Post-MVP | **13** |
| dispatch | Dispatch-related controls | Dispatch records as approved | Dispatch services | Post-MVP; no ERP DB writes | **13** |
| evidence | Evidence metadata and storage orchestration | Evidence metadata; object keys | Upload/register/access services | No PostgreSQL BLOB storage of files | **11** |
| notifications | Email/SMS/in-app notifications | Notification outbox/status | Notify services | Must not bypass auth to spam users | **15** |
| reports | Operational and management reports | Report definitions/runs as needed | Report generation services | Must not claim unsupported compliance | **16** |
| integrations | ERP and external API adapters | Integration configs, cursors, logs | Anti-corruption adapters | **No direct ERP database writes** | **17** |
| audit | Audit event recording and export support | Audit events | Append-only audit APIs | Must not allow silent audit deletion | Cross-cutting from 03+ |
| ai_assistance | Optional local AI assistance | Prompt/output logs as required | Advisory suggestion APIs only | Must not make final FS/QA decisions | **18** |

## Phase mapping reminder

| Phase | Modules / focus |
| --- | --- |
| 06 | **06A–06D** checklist definition/response/proposal loader; **06E** provisional workflow formalization |
| 07 | **07A** `scheduling` ChecklistTask foundation; later recurrence/assignment as approved |
| 08 | `records` draft and submission |
| 09 | `reviews` supervisor checking |
| 10 | `quality` QA verification |

## References

- [ADR-001-MODULAR-MONOLITH.md](ADR-001-MODULAR-MONOLITH.md)
- [ADR-011-BATCH-CHECKLIST-TASK-FOUNDATION.md](ADR-011-BATCH-CHECKLIST-TASK-FOUNDATION.md)
- [ROADMAP.md](../ROADMAP.md)

# Module Map

**Document status:** Living module boundaries — Phase 04–08A
**Phase:** 03–07B complete units · 08A draft recording foundation · MASTER-001 / TEMPLATE pending
**Last updated:** 2026-08-08

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
| scheduling | Batch-triggered checklist task orchestration (07A); batch-source contract + integration port + recording permission foundation (07B) | ChecklistTask (`batch_reference`; no ProductionBatch master) | create/cancel services; `accept_batch_checklist_task_request` port; scoped selectors; orchestration UI | Must not store answers; no DRAFT/RETIRED tasks; no auto latest-version; no invented batch ERP fields; no auto role mapping; manage ≠ record | **07A/07B** |
| recording | Operator draft checklist recording (08A) + immutable submission snapshots (08B) | ChecklistRecord, ChecklistResponse, ChecklistSubmission, ChecklistSubmissionResponse | start/save draft; submit; scoped selectors; draft + submitted UI | No Supervisor/QA/HOLD in 08B; draft ≠ historical truth; manage ≠ record; no FG-QA-001 publish | **08A/08B** |
| tasks | Assignment of work to users/roles (deferred — avoid Celery name clash; 07A in `scheduling`) | Future task assignment states | Assign/claim/complete coordination | Must not store full answer payloads | **07** (beyond 07A) |
| records | Reserved legacy MODULE_MAP label — **do not scaffold**; use `recording` | — | — | Duplicate of `recording` forbidden | superseded by **recording** |
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
| 07 | **07A** ChecklistTask foundation; **07B** batch-source contract + recorder authorization readiness; later recurrence/assignment as approved |
| 08 | **08A** draft recording; **08B** immutable submission snapshots; correction/Supervisor later |
| 09 | `reviews` supervisor checking |
| 10 | `quality` QA verification |

## References

- [ADR-001-MODULAR-MONOLITH.md](ADR-001-MODULAR-MONOLITH.md)
- [ADR-012-BATCH-SOURCE-AND-RECORDER-AUTHORIZATION.md](ADR-012-BATCH-SOURCE-AND-RECORDER-AUTHORIZATION.md)
- [ROADMAP.md](../ROADMAP.md)

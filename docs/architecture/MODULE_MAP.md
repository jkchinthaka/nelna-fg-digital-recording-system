# Module Map

**Document status:** Living module boundaries — Phase 04A Shift foundation
**Phase:** 03 merged · 04A configurable Shift foundation · 04B UI/real-data pending
**Last updated:** 2026-08-07

This map guides implementation. Do not scaffold future business apps before their phase.
Do **not** rename FG master data, checklist, recording, review, or evidence work as Phase 04.

| Module | Responsibility | Data ownership | Public service boundary | Prohibited dependencies | Planned phase |
| --- | --- | --- | --- | --- | --- |
| accounts | Identity, employee-code authentication, password/lockout lifecycle | User | Auth services; admin account management | Must not embed checklist business rules | **03 complete** |
| organizations | Organization / site / department scope hierarchy; configurable unseeded Shift (04A) | Organization, Site, Department, Shift | Hierarchy + Shift create/update/activate/deactivate services; scoped selectors | Must not invent or seed Nelna org/site/dept/shift business values | **03 complete** + **04A foundation** |
| access_control | Roles, scoped assignments, authorization API | Role, ScopedRoleAssignment | Permission checks; decorators/mixins | Must not seed business roles or Shift role mappings without evidence | **03 complete** |
| security_audit | Append-oriented auth/RBAC/Shift security events | SecurityAuditEvent | `record_event` only; no secrets | Must not store credentials | **03 complete** + Shift events in **04A** |
| master_data | FG products and other minimal masters needed by templates | Master entities approved for digital use | Read APIs for recording; controlled write APIs for admins | No silent import from ERP DB; no unverified limits | **05** |
| instruments | Instrument register and calibration status references as approved | Instrument records | Fitness-for-use queries used by recording | Must not invent calibration intervals | **05** |
| training | Training completion gates as approved | Training records / qualifications refs | Eligibility checks for task assignment | Must not invent training matrices | **05** |
| checklists | Checklist definitions and versions | Templates, items, version snapshots metadata | Template publish/read services | No invented item limits; no record submission logic ownership | **06** |
| schedules | Recurrence and due-slot planning | Schedule definitions | Due-window calculation services | Must not assign tasks bypassing policies | **07** |
| tasks | Assignment of work to users/roles | Task instances and states | Assign, claim, list, complete-task coordination | Must not store full answer payloads (records own answers) | **07** |
| records | Operator draft/submit and immutable submitted payloads | Records, answers/snapshots, amendment chains | Submit, amend, read record services | No in-place edit of submitted/approved records; no file BLOBs | **08–09** |
| reviews | Supervisor checking workflow | Check actions and outcomes | Check/reject/request-amendment services | Must not perform QA verification ownership | **09** |
| quality | QA verification workflow | Verification actions | Verify services; deterministic critical-rule hooks | No AI final verification | **10** |
| nonconformance | Holds and NC records | NC/hold entities | Open/update NC services | Post-MVP unless approved; no AI closure | **12** |
| capa | Corrective and preventive actions | CAPA entities | CAPA lifecycle services | No AI final CAPA closure | **12** |
| loading | Loading controls | Loading check records | Loading workflow services | No AI loading release; post-MVP | **13** |
| dispatch | Dispatch-related controls | Dispatch records as approved | Dispatch services | Post-MVP; no ERP DB writes | **13** |
| evidence | Evidence metadata and storage orchestration | Evidence metadata; object keys | Upload/register/access services | No PostgreSQL BLOB storage of files | **11** |
| notifications | Email/SMS/in-app notifications | Notification outbox/status | Notify services | Must not bypass auth to spam users | **15** |
| reports | Operational and management reports | Report definitions/runs as needed | Report generation services | Must not claim unsupported compliance | **16** |
| integrations | ERP and external API adapters | Integration configs, cursors, logs | Anti-corruption adapters | **No direct ERP database writes** | **17** |
| audit | Audit event recording and export support | Audit events | Append-only audit APIs; export helpers | Must not allow silent audit deletion | Cross-cutting from 03+ |
| ai_assistance | Optional local AI assistance | Prompt/output logs as required | Advisory suggestion APIs only | Must not make final FS/QA/loading/CAPA/access decisions; must not block core flows | **18** |

## Phase mapping reminder

| Phase | Modules / focus |
| --- | --- |
| 04 | Residual hierarchy confirmation; **04A** configurable unseeded Shift foundation; **04B** UI + real-data config after evidence |
| 05 | `master_data` (+ instruments/training as approved) |
| 06 | `checklists` definition and versioning |
| 07 | `schedules`, `tasks` |
| 08 | `records` draft and submission |
| 09 | `reviews` supervisor checking |
| 10 | `quality` QA verification (when approved) |
| 11 | `evidence` attachments and object storage |

## Cross-cutting notes

- Policies may live beside modules or in a shared `policies` pattern; enforcement remains server-side.
- Redis/Celery workers call the same services as HTTP entrypoints where practical.
- Future extraction follows ADR-001 criteria.

## References

- [ADR-001-MODULAR-MONOLITH.md](ADR-001-MODULAR-MONOLITH.md)
- [ROADMAP.md](../ROADMAP.md)

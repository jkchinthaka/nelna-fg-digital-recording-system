# Module Map

**Document status:** Living module boundaries — Phase 04–06C
**Phase:** 03–05 complete units · 06A/06B/06C checklist definitions + response schema · MASTER-001 / TEMPLATE pending
**Last updated:** 2026-08-07

This map guides implementation. Do not scaffold future business apps before their phase.
Do **not** rename FG master data, checklist, recording, review, or evidence work as Phase 04.

| Module | Responsibility | Data ownership | Public service boundary | Prohibited dependencies | Planned phase |
| --- | --- | --- | --- | --- | --- |
| accounts | Identity, employee-code authentication, password/lockout lifecycle | User | Auth services; admin account management | Must not embed checklist business rules | **03 complete** |
| organizations | Organization / site / department scope hierarchy; configurable unseeded Shift (04A) + management UI (04B) | Organization, Site, Department, Shift | Hierarchy + Shift create/update/activate/deactivate services; scoped selectors; Shift management views | Must not invent or seed Nelna org/site/dept/shift business values | **03 complete** + **04A/04B** |
| access_control | Roles, scoped assignments, authorization API | Role, ScopedRoleAssignment | Permission checks; decorators/mixins | Must not seed business roles or Shift role mappings without evidence | **03 complete** |
| security_audit | Append-oriented auth/RBAC/Shift/Product/Checklist security events | SecurityAuditEvent | `record_event` only; no secrets | Must not store credentials | **03+** |
| master_data | Configurable unseeded FG Product (05A); object-aware UI authz (05B); other masters only when approved | FGProduct | Product create/update/activate/deactivate; scoped selectors; management UI with precomputed manageable orgs | Must not invent product catalogues; no silent ERP DB import; no unsupported attributes; site-only RBAC does not escalate to org Product manage | **05A/05B** |
| instruments | Instrument register and calibration status references as approved | Instrument records | Fitness-for-use queries used by recording | Must not invent calibration intervals | **05** (not started) |
| training | Training completion gates as approved | Training records / qualifications refs | Eligibility checks for task assignment | Must not invent training matrices | **05** (not started) |
| checklists | Configurable unseeded checklist definition/versioning (06A); lifecycle governance hardening (06B); provisional response-definition schema (06C) | ChecklistTemplate, ChecklistVersion, ChecklistSection, ChecklistItem (+ response_type / NUMBER metadata / SELECT options as defined in 06C) | Template/version create/clone/publish/retire; draft structure mutations; scoped selectors; management UI; response-type + option editing on drafts | No invented item limits; no record submission / scheduling ownership; no automatic RELEASE/HOLD/REJECT; FG-QA-001 draft not seeded | **06A/06B/06C** |
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
| 04 | Residual hierarchy confirmation; **04A** configurable unseeded Shift foundation; **04B** Shift management UI; real-data config after evidence |
| 05 | **05A** configurable unseeded FG Product (`master_data`); **05B** authz hardening + MASTER-001 intake; instruments/training later as approved; real catalogues after MASTER-001 |
| 06 | **06A** configurable unseeded checklist definition/versioning; **06B** governance hardening + TEMPLATE-001 intake; **06C** response-definition schema + FG-QA-001 project-proposed draft (validation required); real forms after TEMPLATE evidence |
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

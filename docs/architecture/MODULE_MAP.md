# Module Map

**Document status:** Living module boundaries — Phase 04–10B
**Phase:** 03–09C complete units · 10A QA disposition · **10B derived workflow lifecycle** · MASTER-001 / TEMPLATE pending
**Last updated:** 2026-08-10

This map guides implementation. Do not scaffold future business apps before their phase.
Do **not** rename FG master data, checklist, recording, review, or evidence work as Phase 04.

| Module | Responsibility | Data ownership | Public service boundary | Prohibited dependencies | Planned phase |
| --- | --- | --- | --- | --- | --- |
| core | Shared foundation + **10B** derived checklist operational workflow (ADR-022) | No business owner tables for workflow | `derive_checklist_workflow`; badges/filters | Must not persist duplicated workflow status on Task/Record/Submission/Review/Correction/QA; QA terminals ≠ ERP close | **02+ / 10B** |
| accounts | Identity, employee-code authentication, password/lockout lifecycle | User | Auth services; admin account management | Must not embed checklist business rules | **03 complete** |
| organizations | Organization / site / department scope hierarchy; configurable unseeded Shift (04A) + management UI (04B) + audited lifecycle/import (04C) | Organization, Site, Department, Shift | Hierarchy + Shift create/update/activate/deactivate services; controlled hierarchy import; scoped selectors; Shift management views | Must not invent or seed Nelna org/site/dept/shift business values; real catalogue gated by ASM-004/005/006 | **03 complete** + **04A/04B/04C technical** (real values pending) |
| access_control | Roles, scoped assignments, RoleTemplate governance, authorization API | Role, RoleTemplate, ScopedRoleAssignment | Permission checks; governance services; decorators/mixins; permission catalogue | Must not seed business roles/templates as OWNER_APPROVED without APR evidence; SoD not invented | **03 complete** + **03C technical** (business mapping pending) |
| security_audit | Append-oriented auth/RBAC/Shift/Product/Checklist/Task security events | SecurityAuditEvent | `record_event` only; no secrets | Must not store credentials | **03+** |
| feature_flags | Governed feature flags for staged optional modules (Phase 90) | FeatureFlag | evaluate/upsert; never bypass RBAC | Must not short-circuit permissions; risky keys default OFF | **90** |
| master_data | Configurable unseeded FG Product (05A–05C); versioned ProductSpecification (06O); other masters only when approved | FGProduct; ProductSpecification / SpecificationVersion / SpecificationParameter | Product CRUD/import; versioned specs (approve/retire/clone); optional checklist SPECIFICATION_PARAMETER pin | Must not invent catalogues or limits (APR-006/ASM-001); MASTER-001 unresolved | **05A/05B/05C + 06O technical** (limits pending evidence) |
| instruments | Equipment master + calibration records (05D); unseeded; fitness labels only | Equipment, CalibrationRecord | create/update/activate/deactivate; calibration create; fitness labels (VALID/DUE/OVERDUE/OUT_OF_SERVICE/UNKNOWN) | Must not invent calibration intervals; overdue block/warn EVIDENCE REQUIRED; no seeded assets | **05D technical** (intervals/policy pending) |
| training | Training completion gates as approved | TrainingRecord + enforcement policy mode | Currency labels + future WARN/BLOCK modes (default OFF) | Must not invent training matrices | **05E technical foundation** (unseeded) |
| checklists | Definition/versioning (06A-06D); provisional workflow (06E); form discovery (06F); Engine v2 architecture (06G / ADR-019); repeating (06H); calculated (06I); conditional rules (06J); item evaluation (06K); control-point metadata (06L); measurement semantics (06M); product-spec pin (06O); effective-version selection (07D) | ChecklistTemplate, ChecklistVersion (+ effective_from/to), ChecklistSection, ChecklistItem (+ Option; measurement semantics; item_kind/parent/repeat_*/calculation_*/condition_rules/evaluation_rule/control_point_class/criticality; decimal_precision/rounding_mode/min_inclusive/max_inclusive), ChecklistItemRule, ChecklistItemEvaluationRule | Template/version lifecycle; DRAFT loader; management UI; REPEATING_GROUP; closed CALCULATED operators; closed VISIBLE_IF/REQUIRED_IF/EVIDENCE_REQUIRED_IF predicates; explicit evaluation rules (PASS/FAIL/WARN/NOT_EVALUATED ≠ QA disposition); control-point/criticality metadata (default NONE; not disposition); Decimal-safe measurement semantics (not disposition); deterministic PUBLISHED effective-version resolve | No recording ownership in this app; no automatic RELEASE/HOLD/REJECT; FG-QA-001 never auto-published; no invented AQL/formulas/predicates/limits/CCP-OPRP/product units; no silent version pick / auto-upgrade | **06A-06O + 07D** |
| scheduling | Batch-triggered checklist task orchestration (07A); batch-source contract + integration port + recording permission foundation (07B); applicability (07C); effective-version task helper (07D); recurring schedules (07E); batch-event adapter boundary (07F); task assignment ownership (07G); due/overdue foundation (07H) | ChecklistTask (`batch_reference`; ExternalBatchMapping/Event; no ProductionBatch master) | create/cancel services; `accept_batch_checklist_task_request` / `accept_external_batch_event` ports; scoped selectors; orchestration UI; applicability preview; effective-version create helper; schedule generation; derived due display | Must not store answers; no DRAFT/RETIRED tasks; no silent auto-latest; overlap/NO_ELIGIBLE must BLOCK; no invented batch ERP fields/endpoints/credentials; no live connector without APR-011; no auto role mapping; manage ≠ record; no invented SLA; overdue ≠ NCR | **07A–07H** |
| recording | Operator draft recording (08A), immutable submissions (08B), shop-floor hardening (08C), controlled correction/resubmission (09B); server evaluation apply (06K) | ChecklistRecord (+ draft_version), ChecklistResponse (+ evaluation_*; optional equipment/evidence_hook), ChecklistSubmission, ChecklistSubmissionResponse (+ frozen evaluation_*/equipment/evidence_hook), ChecklistCorrection | start/save/autosave/submit; optimistic concurrency; scoped selectors; draft/submitted/correction UI; server-authoritative item evaluation display | Must not mutate immutable snapshots/reviews; manage/review ≠ record; no QA/HOLD; evaluation ≠ disposition; no FG-QA-001 publish; no silent last-write-wins; no IndexedDB offline (Phase 14) | **08A–08C / 09B** + **06K** |
| tasks | Assignment of work to users/roles (deferred — avoid Celery name clash; 07A in `scheduling`) | Future task assignment states | Assign/claim/complete coordination | Must not store full answer payloads | **07** (beyond 07A) |
| records | Reserved legacy MODULE_MAP label — **do not scaffold**; use `recording` | — | — | Duplicate of `recording` forbidden | superseded by **recording** |
| recording | Draft recording + 06K evaluation apply (see primary recording row) | ChecklistRecord / responses / submissions | Completeness + evaluation display | Must not perform Supervisor/QA decisions; evaluation ≠ disposition | **08A–09B** + **06K** |
| reviews | Immutable Supervisor review (09A); governance hardening (09C); queues pending/overdue/resubmission | SupervisorReview; SupervisorReviewGovernancePolicy | create_supervisor_review; governance evaluate/due/queues; temporary ScopedRoleAssignment delegation | Must not invent Supervisor titles/SLAs; PENDING self-review not enforced; no QA/HOLD/RELEASE; immutable reviews | **09A–09C** |
| quality | QA final review disposition foundation (10A) | QAReview | create immutable QA disposition; eligible selectors; QA UI | No AI final verification; no auto PASS/FAIL; no ERP/warehouse/dispatch side effects; manage/record/supervisor ≠ QA | **10A** |
| nonconformance | Holds and NC records | NC/hold entities | Open/update NC services | Post-MVP unless approved | **12** |
| capa | Corrective and preventive actions | CAPA entities | CAPA lifecycle services | No AI final CAPA closure | **12** |
| loading | Loading controls | Loading check records | Loading workflow services | Post-MVP | **13** |
| dispatch | Dispatch-related controls | Dispatch records as approved | Dispatch services | Post-MVP; no ERP DB writes | **13** |
| evidence | Evidence metadata and private storage orchestration (Phase 11) | EvidenceAttachment (no BLOBs) | upload/download/soft-retire; private store; SHA-256; scanner stub | No PostgreSQL BLOBs; no public MEDIA URLs; no fake malware scanning claims; no casual hard-delete | **11** |
| notifications | Email/SMS/in-app notifications | Notification outbox/status | Notify services | Must not bypass auth to spam users | **15** |
| reports | Operational and management reports | Report definitions/runs as needed | Report generation services | Must not claim unsupported compliance | **16** |
| integrations | ERP and external API adapters | Integration configs, cursors, logs | Anti-corruption adapters | **No direct ERP database writes** | **17** |
| audit | Audit event recording and export support | Audit events | Append-only audit APIs | Must not allow silent audit deletion | Cross-cutting from 03+ |
| ai_assistance | Optional local AI assistance | Prompt/output logs as required | Advisory suggestion APIs only | Must not make final FS/QA decisions | **18** |

## Phase mapping reminder

| Phase | Modules / focus |
| --- | --- |
| 06 | **06A–06D** checklist definition/response/proposal loader; **06E** provisional workflow formalization |
| 07 | **07A** ChecklistTask foundation; **07B** batch-source contract; **07C** applicability; **07D** effective-version; **07E** recurring schedules; **07F** batch-event adapter (live contract required); **07G** task assignment (ownership ≠ authorization); **07H** due/overdue foundation |
| 08 | **08A** draft recording; **08B** immutable submission snapshots; **08C** shop-floor recording hardening |
| 09 | **09A** `reviews` Supervisor review; **09B** `recording` ChecklistCorrection / resubmission; **09C** Supervisor governance hardening |
| 10 | **10A** QA disposition; **10B** derived workflow lifecycle (ADR-022; no duplicated status) |

## References

- [ADR-001-MODULAR-MONOLITH.md](ADR-001-MODULAR-MONOLITH.md)
- [ADR-012-BATCH-SOURCE-AND-RECORDER-AUTHORIZATION.md](ADR-012-BATCH-SOURCE-AND-RECORDER-AUTHORIZATION.md)
- [ROADMAP.md](../ROADMAP.md)

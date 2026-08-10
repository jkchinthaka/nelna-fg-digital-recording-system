# Security Event Catalogue

**Document status:** Phase 03 foundation + Phase 03C role governance + Phase 04A/04B/04C org/shift + Phase 05A FG Product + Phase 06 checklist events
**Last updated:** 2026-08-10

## Event types

| Event | When |
| --- | --- |
| `LOGIN_SUCCESS` | Successful employee-code authentication |
| `LOGIN_FAILURE` | Failed authentication (generic reasons in metadata) |
| `ACCOUNT_LOCKED` | Failure threshold reached |
| `ACCOUNT_UNLOCKED` | Explicit admin unlock |
| `LOGOUT` | Session logout |
| `PASSWORD_CHANGED` | User or forced password change |
| `PASSWORD_RESET_BY_ADMIN` | Admin sets a new password |
| `USER_ACTIVATED` / `USER_DEACTIVATED` | Active-flag changes |
| `ROLE_ASSIGNED` / `ROLE_REVOKED` | Scoped role assignment lifecycle |
| `ROLE_PERMISSIONS_UPDATED` | Role permission set replaced via governance service |
| `ROLE_TEMPLATE_CREATED` / `ROLE_TEMPLATE_UPDATED` | RoleTemplate lifecycle (technical; not business approval) |
| `ROLE_TEMPLATE_APPLIED` | Template permissions copied onto a Role (no user assignment) |
| `SHIFT_CREATED` | Configurable Shift created via domain service |
| `SHIFT_UPDATED` | Configurable Shift fields updated via domain service |
| `SHIFT_ACTIVATED` | Shift reactivated (`is_active=True`) |
| `SHIFT_DEACTIVATED` | Shift deactivated (`is_active=False`) |
| `ORGANIZATION_CREATED` / `UPDATED` / `ACTIVATED` / `DEACTIVATED` | Organization lifecycle (Phase 04C) |
| `SITE_CREATED` / `UPDATED` / `ACTIVATED` / `DEACTIVATED` | Site lifecycle (Phase 04C) |
| `DEPARTMENT_CREATED` / `UPDATED` / `ACTIVATED` / `DEACTIVATED` | Department lifecycle (Phase 04C) |
| `ORGANIZATION_HIERARCHY_IMPORT_PREVIEWED` / `COMPLETED` / `FAILED` | Controlled hierarchy import (Phase 04C) |
| `FG_PRODUCT_CREATED` | Configurable FG Product created via domain service |
| `FG_PRODUCT_UPDATED` | Configurable FG Product fields updated via domain service |
| `FG_PRODUCT_ACTIVATED` | FG Product reactivated (`is_active=True`) |
| `FG_PRODUCT_DEACTIVATED` | FG Product deactivated (`is_active=False`) |
| `FG_PRODUCT_IMPORT_PREVIEWED` / `COMPLETED` / `FAILED` | Controlled FG Product CSV import (Phase 05C) |
| `PRODUCT_SPECIFICATION_CREATED` / `SPECIFICATION_VERSION_*` / `SPECIFICATION_PARAMETER_*` | Product specification lifecycle (Phase 06O; OUT_OF_SPEC ≠ disposition) |
| `EQUIPMENT_CREATED` / `UPDATED` / `ACTIVATED` / `DEACTIVATED` / `STATUS_CHANGED` | Equipment master lifecycle (Phase 05D) |
| `CALIBRATION_RECORD_CREATED` | Calibration record created |
| `CALIBRATION_CERTIFICATE_METADATA_UPDATED` | Certificate/provider metadata updated |
| `TRAINING_RECORD_CREATED` / `UPDATED` / `STATUS_CHANGED` | Training / competency lifecycle (Phase 05E) |
| `TRAINING_ENFORCEMENT_POLICY_CREATED` / `UPDATED` | Training gate mode metadata (OFF/WARN/BLOCK; not auto-enforced) |
| `CHECKLIST_TEMPLATE_CREATED` | Checklist template created |
| `CHECKLIST_TEMPLATE_UPDATED` | Checklist template updated |
| `CHECKLIST_TEMPLATE_ACTIVATED` | Checklist template activated |
| `CHECKLIST_TEMPLATE_DEACTIVATED` | Checklist template deactivated |
| `CHECKLIST_VERSION_CREATED` | Blank draft checklist version created |
| `CHECKLIST_VERSION_CLONED` | Draft checklist version cloned from a source version |
| `CHECKLIST_VERSION_PUBLISHED` | Checklist version published (immutable thereafter); metadata includes effectivity |
| `CHECKLIST_VERSION_EFFECTIVITY_UPDATED` | Checklist version effective_from/to changed (Phase 07D) |
| `CHECKLIST_VERSION_RETIRED` | Published checklist version retired |
| `CHECKLIST_VERSION_EFFECTIVITY_UPDATED` | Checklist version `effective_from` / `effective_to` changed (Phase 07D) |
| `CHECKLIST_TASK_CREATED` | Batch checklist task created (or idempotent return of existing) |
| `CHECKLIST_TASK_CANCELLED` | Batch checklist task cancelled (soft cancel) |
| `CHECKLIST_TASK_ASSIGNED` / `REASSIGNED` / `UNASSIGNED` | Task ownership changes (Phase 07G; never grants RBAC) |
| `CHECKLIST_TASK_DUE_WINDOW_UPDATED` | Configured due_from/due_at/due_soon change (Phase 07H; overdue ≠ NCR) |
| `CHECKLIST_TASK_GENERATED` | Schedule engine created a task occurrence (system) |
| `CHECKLIST_SCHEDULE_CREATED` | Checklist schedule definition created |
| `CHECKLIST_SCHEDULE_DEACTIVATED` | Checklist schedule deactivated |
| `CHECKLIST_SCHEDULE_GENERATION_RUN` | Replay-safe schedule generation tick completed |
| `EXTERNAL_BATCH_EVENT_RECEIVED` | Inbound batch event accepted for processing (Phase 07F adapter) |
| `EXTERNAL_BATCH_EVENT_DUPLICATE` | Idempotent duplicate of a completed batch event |
| `EXTERNAL_BATCH_EVENT_MAPPING_FAILED` | External key mapping failed — no task created |
| `EXTERNAL_BATCH_EVENT_APPLICABILITY_FAILED` | Applicability not ONE_MATCH — no task created |
| `EXTERNAL_BATCH_EVENT_VERSION_FAILED` | Effective-version resolution failed — no task created |
| `EXTERNAL_BATCH_EVENT_PROCESSED` | Batch event completed to ChecklistTask |
| `EXTERNAL_BATCH_EVENT_REJECTED` | Batch event rejected at task create |
| `EXTERNAL_BATCH_MAPPING_UPSERTED` | External batch mapping created/updated |
| `CHECKLIST_APPLICABILITY_RULE_CREATED` / `UPDATED` / `DEACTIVATED` | Checklist applicability rule lifecycle (Phase 07C) |
| `CHECKLIST_APPLICABILITY_PREVIEWED` | Management applicability preview (Phase 07C; no task mutation) |
| `CHECKLIST_RECORD_STARTED` | Draft checklist record started for a PENDING task |
| `CHECKLIST_RECORD_DRAFT_SAVED` | Draft checklist responses saved (aggregate; may include `draft_version`, `save_mode`, `autosave`) |
| `CHECKLIST_RECORD_SUBMITTED` | Checklist record submitted with immutable Submission #1 snapshot |
| `SUPERVISOR_REVIEW_COMPLETED` | Immutable Supervisor review recorded for a ChecklistSubmission (09C adds self-review governance metadata) |
| `SUPERVISOR_REVIEW_GOVERNANCE_POLICY_SET` | Org Supervisor review governance policy created/updated (Phase 09C) |
| `SUPERVISOR_REVIEW_DELEGATION_GRANTED` | Temporary review delegation via time-bounded ScopedRoleAssignment (Phase 09C) |
| `SUPERVISOR_REVIEW_DELEGATION_REVOKED` | Temporary review delegation revoked (Phase 09C) |
| `CHECKLIST_CORRECTION_STARTED` | Controlled correction cycle started for a RETURNED submission |
| `CHECKLIST_CORRECTION_RESUBMITTED` | Correction resubmitted as next immutable ChecklistSubmission |
| `QA_REVIEW_COMPLETED` | Immutable QA disposition recorded for a ChecklistSubmission |
| `EVIDENCE_UPLOADED` | Evidence attachment stored in private storage (SHA-256; no answer values) |
| `EVIDENCE_DOWNLOADED` | Authorized evidence download served (attachment disposition) |
| `EVIDENCE_RETIRED` | Evidence soft-retired (no hard delete) |
| `EVIDENCE_ACCESS_DENIED` | Evidence download denied or blob missing |
| `NONCONFORMANCE_CREATED` | Formal NCR created (manual; Phase 12) |
| `NONCONFORMANCE_UPDATED` | NCR case fields updated |
| `NONCONFORMANCE_STATUS_CHANGED` | NCR proposed lifecycle transition |
| `NONCONFORMANCE_CLOSED` | NCR closed |
| `HOLD_CASE_CREATED` | Hold case opened (free-text reason/scope) |
| `HOLD_CASE_CLOSED` | Hold case closed (free-text resolution) |
| `CAPA_CREATED` | CAPA header created |
| `CAPA_STATUS_CHANGED` | CAPA proposed lifecycle transition |
| `CAPA_ACTION_ADDED` | CAPA action item added |
| `CAPA_VERIFICATION_RECORDED` | CAPA verification notes recorded |
| `CAPA_EFFECTIVENESS_REVIEWED` | CAPA effectiveness review recorded |
| `CAPA_CLOSED` | CAPA closed (human-only) |
| `DISPATCH_QUALITY_RECORD_CREATED` | Loading/dispatch quality record created (Phase 13) |
| `DISPATCH_QUALITY_RECORD_UPDATED` | Dispatch quality record fields updated |
| `DISPATCH_VEHICLE_INSPECTION_LINKED` | Dynamic vehicle inspection checklist linked |
| `DISPATCH_QA_REVIEW_LINKED` | QAReview linked for traceability / optional gate |
| `DISPATCH_TEMPERATURE_RECORDED` | Cold-chain temperature recorded (Decimal; no limits) |
| `DISPATCH_QUANTITY_LINE_SET` | Released/loaded/remaining quantity line set |
| `DISPATCH_RELEASE_POLICY_UPDATED` | Org QA RELEASE-before-loading policy updated |
| `DISPATCH_RELEASE_GATE_EVALUATED` | Release gate evaluated on completion attempt |
| `DISPATCH_RELEASE_GATE_BLOCKED` | Completion blocked by enabled QA RELEASE gate |
| `DISPATCH_QUALITY_RECORD_COMPLETED` | Dispatch quality record completed |
| `DISPATCH_QUALITY_RECORD_CANCELLED` | Dispatch quality record cancelled |
| `NOTIFICATION_POLICY_UPDATED` | Org notification event/email policy updated (Phase 15) |
| `NOTIFICATION_CREATED` | In-app notification created (safe payload only) |
| `NOTIFICATION_READ` | Notification marked read by recipient |
| `NOTIFICATION_EMAIL_DELIVERED` | Notification email delivered |
| `NOTIFICATION_EMAIL_FAILED` | Notification email delivery failed |
| `REPORT_RUN_ENQUEUED` | Governed report run enqueued for background generation (Phase 16) |
| `REPORT_RUN_COMPLETED` | Governed report run completed |
| `REPORT_EXPORTED` | Governed report exported (CSV generated for export) |
| `REPORT_EXPORT_DOWNLOADED` | Governed report CSV downloaded |
| `INTEGRATION_INBOUND_SUCCEEDED` | Integration inbound attempt succeeded (Phase 17) |
| `INTEGRATION_INBOUND_FAILED` | Integration inbound attempt failed |
| `INTEGRATION_INBOUND_DUPLICATE` | Integration inbound duplicate (idempotent) |
| `INTEGRATION_LIVE_BLOCKED` | Live Bileeta pull blocked by evidence gate |
| `INTEGRATION_DEAD_LETTER` | Integration attempt marked dead letter |
| `INTEGRATION_OUTBOUND_BLOCKED` | Outbound ERP disposition blocked pending APR-017 |
| `AI_ASSISTANCE_COMPLETED` | AI assistance request completed (advisory) (Phase 18) |
| `AI_ASSISTANCE_BLOCKED` | AI assistance request blocked (safety/auth) |
| `AI_ASSISTANCE_DISABLED` | AI assistance invoked while feature disabled |
| `AI_ASSISTANCE_FALLBACK` | AI assistance safe fallback after provider failure/timeout |
| `LAB_SAMPLE_CREATED` | Laboratory sample created (Phase 22) |
| `LAB_SAMPLE_STATUS_CHANGED` | Laboratory sample status changed |
| `LAB_RESULT_ENTERED` | Laboratory result entered |
| `LAB_RESULT_VERIFIED` | Laboratory result verified |
| `LAB_RESULT_FINALIZED` | Laboratory result finalized |
| `LAB_RESULT_AMENDED` | Laboratory result amended (new revision) |
| `LAB_EXTERNAL_CERTIFICATE_RECORDED` | Laboratory external certificate recorded |
| `LAB_POSITIVE_RELEASE_POLICY_UPDATED` | Laboratory positive-release policy updated |

## Safe metadata

Allowed examples: `reason` codes (`invalid_credentials`, `account_locked`, `inactive`), role/assignment UUIDs, organization/site/department UUIDs, boolean flags.

Organization / Site / Department events may include: entity UUID, normalized code, organization UUID, optional site UUID, active status, changed field names. Hierarchy import events may include dry_run flag, row_count, created_counts/ids, error_count, and truncated error summaries — never invent company catalogue values in metadata.

Shift events may include: Shift UUID, normalized Shift code, Organization UUID, optional Site UUID, optional Department UUID, active status, overnight derived flag, changed field names.

FG Product events may include: FG Product UUID, normalized Product code, Organization UUID, active status, changed field names.

Checklist / recording / review / correction events may include: template UUID/code, version UUID/number, organization UUID, record/task/submission/correction UUIDs, submission numbers, batch_reference, changed_item_count / answered_item_count. Do **not** store response values, Supervisor review notes, TEXT answers, or numerical measurements in security audit metadata.

Checklist task events may include: task UUID, organization UUID, template UUID/code, version UUID/number, `batch_reference`, status. Do not store checklist question text or request bodies.

Checklist draft recording events may include: record UUID, task UUID, organization UUID, template UUID, version UUID, `batch_reference`, `changed_item_count`. Do **not** store answer values, question text, remarks, or request bodies.

Checklist submission events may include: record UUID, submission UUID, submission number, task UUID, organization UUID, template UUID, version UUID, `batch_reference`, `answered_item_count`. Do **not** store answer values, question text, remarks, or request bodies.

Supervisor review events may include: review UUID, submission UUID, submission number, record UUID, task UUID, organization UUID, template UUID, version UUID, `batch_reference`, `decision`. Do **not** store review notes, answer values, question text, or request bodies.

Unknown login identifiers must be masked or hashed â€” never store raw unknown employee codes in clear text when the account is unknown.

## Prohibited fields

Passwords, session keys, cookies, Authorization headers, CSRF tokens, raw POST bodies, full database or Redis URLs, secrets.

## Privacy and retention

Retention period is **deferred** â€” not decided in Phase 03. Events are append-oriented and must not be silently editable through normal admin workflows.

## Related

- [AUTHENTICATION_AND_ACCESS_CONTROL.md](AUTHENTICATION_AND_ACCESS_CONTROL.md)
- [ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md](../architecture/ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md)
- [ADR-009-FG-MASTER-DATA-DOMAIN.md](../architecture/ADR-009-FG-MASTER-DATA-DOMAIN.md)

### HACCP (Phase 23)

| Event | Meaning |
| --- | --- |
| HACCP_PLAN_CREATED | Plan shell created |
| HACCP_PLAN_VERSION_CREATED | Draft version created |
| HACCP_PLAN_VERSION_APPROVED | Version approved (immutable) |
| HACCP_PLAN_VERSION_RETIRED | Approved version retired |
| HACCP_CONTROL_POINT_MAPPED | Control point added on draft version |
| HACCP_CHECKLIST_BINDING_SET | Checklist item bound to exact version/CP |

### Sampling (Phase 24)

| Event | Meaning |
| --- | --- |
| SAMPLING_PLAN_CREATED | Plan shell created |
| SAMPLING_PLAN_VERSION_CREATED | Draft version created |
| SAMPLING_PLAN_VERSION_APPROVED | Version approved (immutable) |
| SAMPLING_PLAN_VERSION_RETIRED | Approved version retired |
| SAMPLING_CHECKLIST_BINDING_SET | REPEATING_GROUP bound to plan version |

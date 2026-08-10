# Project Status — Nelna FG Digital Recording System

**Document status:** Canonical project-status baseline
**Authority:** Prefer this document over README phase summaries when they conflict
**Authored:** 2026-08-09
**Implementation baseline SHA (pre-governance commit):** `a1f4ef7af0572c1ddfc2487ebc9a2ab57b2f1ba2`
**Branch:** `main`

This document records **repository evidence**. It does not invent Nelna operational values, role holders, or approvals.

---

## Status vocabulary (do not treat as equivalent)

| Label | Meaning |
| --- | --- |
| **IMPLEMENTED** | Code/docs exist on `main` for the named capability |
| **TECHNICALLY VALIDATED** | Quality gates / tests / Docker validation recorded as passed for that unit |
| **BUSINESS APPROVED** | Named business/QA/IT owner approval exists in writing |
| **PRODUCTION CONFIGURED** | Real Nelna master data, roles, and environment config loaded for production use |
| **UAT PASSED** | Operator/business UAT evidence recorded and accepted |
| **PRODUCTION READY** | Explicit written go-live approval after UAT, restore test, security review |

**Silence is not approval.** Missing forms are not approvals.

---

## Snapshot

| Item | Evidence-based status |
| --- | --- |
| Current DB platform | **PostgreSQL** (authoritative; ADR-002). Redis for cache/Celery. MongoDB/Atlas **requested by company** — DB-01 ADR-018; DB-02 isolated POC evidence in `docs/migration/MONGODB_POC_RESULTS.md` (**CUTOVER BLOCKED / DO NOT MIGRATE**); **not** application SoR |
| Current deployment | **Local / developer Docker Compose only**. No staging/UAT/production deployment recorded |
| Production readiness | **NOT claimed** |
| FG-QA-001 | Project-proposed **DRAFT** only — Phase 06N **BLOCKED — BUSINESS APPROVAL REQUIRED**; **NOT APPROVED**; not auto-published |
| Phase 10A QA foundation | **IMPLEMENTED** on `main` at baseline SHA above |
| Phase 10A Docker full validation | **NOT confirmed complete** in this governance pass (prior Docker Desktop engine failures reported; re-validation remains outstanding) |
| Business role mappings (recorder / Supervisor / QA) | **NOT BUSINESS APPROVED** — Phase 03C technical governance exists; permissions unassigned; mapping tables empty |
| Segregation of duties | **EVIDENCE REQUIRED** — not invented in code as Nelna policy |
| Offline / PWA | **Offline NOT IMPLEMENTED** — Phase 14 gate retained online-only MVP (ADR-026); installable PWA still longer-term (ADR-003) |
| ERP / Bileeta connector | **BLOCKED** — `apps.integrations` contracts/mocks only; live HTTP gated (ADR-029); APR-011/012 EVIDENCE REQUIRED |

---

## Implemented Django apps (code on `main`)

| App | Phase units | Status labels |
| --- | --- | --- |
| `core` | 02+ / **10B** | IMPLEMENTED - foundation + derived checklist workflow |
| `accounts` | 03 | IMPLEMENTED · Phase 03 **Approved with conditions** (not production-configured) |
| `organizations` (incl. Shift) | 03 + 04A/04B | IMPLEMENTED · official org/site/dept/shift values **EVIDENCE REQUIRED** |
| `access_control` | 03 + **03C** | IMPLEMENTED · RoleTemplate + permission catalogue + governance services; **no** seeded business roles; **PHASE 03C BUSINESS ROLE APPROVAL PENDING** |
| `security_audit` | 03–10A | IMPLEMENTED |
| `master_data` (FG Product + specs) | 05A/05B/05C + **06O** | IMPLEMENTED foundation · MASTER-001 **EVIDENCE REQUIRED**; versioned ProductSpecification (06O) unseeded — APR-006 **EVIDENCE REQUIRED** |
| `instruments` | 05D | IMPLEMENTED foundation · unseeded equipment + calibration; intervals/overdue policy **EVIDENCE REQUIRED** |
| `training` | 05E | IMPLEMENTED foundation · unseeded competency records; gate OFF by default; matrix/WARN-BLOCK **EVIDENCE REQUIRED** (APR-042) |
| `checklists` | 06A–06O + **07D** | IMPLEMENTED · FG-QA-001 **NOT BUSINESS APPROVED**; Phase **06N BLOCKED**; optional `SPECIFICATION_PARAMETER` evaluation pin (06O); Engine v2 **designed** (ADR-019); real forms **NOT RECEIVED**; optional `requires_equipment_reference` (05D); **07D** effective-version selection |
| scheduling | 07A–07H | IMPLEMENTED · due/overdue foundation + assignment + schedules + batch-event adapter; live generation **BLOCKED** (APR-011/012) |
| `recording` | 08A–08C + 09B | IMPLEMENTED · shop-floor hardening + draft/submit; production recording **BLOCKED** |
| `reviews` | 09A–09C | IMPLEMENTED · governance hardening + immutable review; production Supervisor review **BLOCKED** |
| `quality` | 10A | IMPLEMENTED · production QA **BLOCKED**; no ERP/warehouse/dispatch side effects |
| `notifications` | **15** | IMPLEMENTED foundation · in-app + optional SMTP email; events/email default OFF; no SMS |
| `dispatch` | **13** | IMPLEMENTED foundation · loading/dispatch quality + cold-chain temps + quantity lines; QA RELEASE gate default OFF; no ERP writes |
| `evidence` | **11** | IMPLEMENTED · private attachments + SHA-256 + soft-retire; malware scanner NOT_CONFIGURED; object-store IAM **EVIDENCE REQUIRED** |
| `nonconformance` | **12** | IMPLEMENTED foundation · NCR + HoldCase + history; no FAIL/CCP auto-raise; policies **EVIDENCE REQUIRED** |
| `capa` | **12** | IMPLEMENTED foundation · CAPA + actions + verification/effectiveness; human-only close; matrices **EVIDENCE REQUIRED** |
| `dispatch` | **13** | IMPLEMENTED foundation · loading/dispatch quality + cold-chain temps + qty reconciliation; QA RELEASE gate **disabled by default**; no ERP writes; SOPs/limits **EVIDENCE REQUIRED** |
| `notifications` | **15** | IMPLEMENTED foundation · in-app + optional SMTP; events default OFF; no SMS; privacy-safe payloads only |
| `reports` | **16** | IMPLEMENTED foundation · catalogue + org-scoped CSV runs; immutable submission sources; Excel/PDF not implemented |
| `integrations` | **17** | BOUNDARY ONLY · contracts/mocks/dead-letter/reconciliation; **live Bileeta blocked** (APR-011/012) |

Not started (by MODULE_MAP): `ai_assistance`. (`loading` controls are delivered inside `dispatch` for Phase 13 — see ADR-025.)

---

## Technical completion by phase (evidence)

| Phase | Technical code/docs | Business / production |
| --- | --- | --- |
| 00 Discovery | Complete | Governance living |
| 01A–01C Design | Complete; 01C deferred Sinhala condition | Design approvals recorded; DEBT-01C-R-NOTO **open** |
| 02 Foundation | Complete | Approved with conditions |
| 03 Accounts/RBAC | Complete | Approved with conditions; no seeded users/orgs/roles |
| 03C Operational role governance | Technical foundation (catalogue, RoleTemplate, audited permission/template services, docs) | **PHASE 03C BUSINESS ROLE APPROVAL PENDING** — SoD all PENDING; APR-007..010/040 EVIDENCE REQUIRED |
| 04A/04B Shift | Complete | Official Shift values unresolved (ASM-005/006) |
| 04C Org/Shift configuration foundation | Technical complete | Real company values pending (ASM-004/005/006); controlled import only |
| 05A/05B FG Product | Complete | MASTER-001 unresolved |
| 05C FG Product master foundation | Technical complete | Optional mapping fields + import; official catalogue **not** received |
| 05D Equipment / calibration foundation | Technical complete | Unseeded equipment + calibration; no invented intervals; overdue block/warn **EVIDENCE REQUIRED** |
| 05E Training / competency foundation | Technical complete | Unseeded training records; gate modes metadata only; no invented matrices |
| 06A–06E Checklist definition | Complete (06E provisional docs) | TEMPLATE / FG-QA-001 approval unresolved |
| 06N FG-QA-001 business validation | Validation recorded; **not published** | **BLOCKED — BUSINESS APPROVAL REQUIRED**; matrix 42 × PENDING DECISION; APR-001 EVIDENCE REQUIRED |
| 06F Real form discovery framework | Docs complete (templates + registers) | Inventory **NOT RECEIVED**; no forms APPROVED FOR DIGITALIZATION |
| 06G Checklist Engine v2 design | ADR-019 + 06H–06M split | Design complete; evidence still required for business values |
| 06H Repeating / sample foundation | Schema + recording/snapshot/correction/Supervisor/QA render | Technical foundation complete; **no invented sample counts**; not BUSINESS APPROVED / not UAT |
| 06I Calculated fields | Closed operators + Decimal + frozen snapshot context | Technical foundation; **no business formulas seeded**; not BUSINESS APPROVED |
| 06J Conditional rules | VISIBLE_IF / REQUIRED_IF / EVIDENCE_REQUIRED_IF (fail-closed evidence stub) | Technical foundation; **no seeded predicates**; not BUSINESS APPROVED |
| 06K Item evaluation | Explicit bounds/choice/option/calculated rules → PASS/FAIL/WARN/NOT_EVALUATED | Technical foundation; **PASS≠RELEASE / FAIL≠HOLD/REJECT**; never auto-creates QAReview; **no seeded limits**; not BUSINESS APPROVED |
| 06L Control-point metadata | `control_point_class` + `criticality` + frozen `control_point_context` | Technical schema on `main`; default NONE; **no invented CCP/OPRP**; metadata ≠ disposition; **APR-027 / ASM-002 still EVIDENCE REQUIRED**; not BUSINESS APPROVED |
| 06M Measurement semantics | `decimal_precision` + `rounding_mode` + unit catalog + inclusivity + frozen `measurement_context` | Technical schema on `main`; Decimal-safe; **no product limits seeded**; informational bounds ≠ disposition; not BUSINESS APPROVED |
| 06N FG-QA-001 business validation | Validation matrix + evidence gap review; **no publish** | **BLOCKED — BUSINESS APPROVAL REQUIRED**; APR-001 unresolved; forms NOT RECEIVED |
| 06O Product specifications | Versioned ProductSpecification + optional checklist pin | Technical complete; **no invented limits**; APR-006/ASM-001 still EVIDENCE REQUIRED |
| 07A/07B Scheduling foundation | Complete | Real generation blocked (batch source, applicability, roles) |
| 07C Checklist applicability engine | Technical complete — version-safe rules + preview | APR-013/014/015 EVIDENCE REQUIRED; no Line/Process masters; production generation still BLOCKED |
| 07D Effective version policy | Technical complete — PUBLISHED-only selection; overlap/NO_ELIGIBLE blocked; audited effectivity | APR-015 as-of event still DECISION REQUIRED; historical pins never auto-upgrade |
| 07E Recurring tasks | Technical complete — BATCH/SHIFT_*/SCHEDULED/MANUAL; idempotent occurrence keys; Celery Beat catch-up; OVERDUE/MISSED without auto-NCR | Frequencies EVIDENCE REQUIRED; production generation still BLOCKED |
| 07F Batch event → task | Adapter boundary complete — mapping / applicability / effective version / idempotent task; no live connector | **APR-011 LIVE CONTRACT REQUIRED**; production generation still BLOCKED |
| 07G Task assignment | Technical complete — USER/ROLE/DEPT/SHIFT/TEAM ownership; append-only history; My/Unassigned/Assigned queues; assign ≠ RBAC | Future auto-assign policies EVIDENCE REQUIRED |
| 07H Due / overdue foundation | Technical complete — configured due_from/due_at/due_soon; derived NOT_DUE/DUE/DUE_SOON/OVERDUE; overdue ≠ NCR; no invented SLAs | Company SLA durations EVIDENCE REQUIRED |
| 08A/08B Recording/submit | Complete | Production recording blocked |
| 08C Recording hardening | Technical complete — autosave, optimistic concurrency, session recovery (online), UX | Production recording still BLOCKED; offline IndexedDB is Phase 14 |
| 09A/09B Supervisor review + correction | Complete | Production review/correction blocked |
| 09C Supervisor governance | Technical complete — PENDING/PROHIBIT/ALLOW self-review; configured review_sla_minutes; temporary delegation; queues | APR-010 / SOD-01 EVIDENCE REQUIRED |
| 10A QA disposition | Complete (manual RELEASE/HOLD/REJECT only) | Production QA blocked; post-QA workflows not started |
| 10B Workflow lifecycle | Technical complete - derived operational workflow (ADR-022); no duplicated status columns | Production still BLOCKED; QA does not close warehouse/ERP/dispatch |
| 10C+ Post-QA operational | Not started | EVIDENCE REQUIRED |
| 11 Evidence attachments | Technical complete — private store, SHA-256, auth download, soft-retire, scanner NOT_CONFIGURED | Object-store IAM / active malware scanner EVIDENCE REQUIRED |
| 12 NCR / HOLD / CAPA | Technical complete — proposed NCR lifecycle, HoldCase, CAPA actions/verification/effectiveness; no auto-raise | Severity/resolution catalogues / auto-raise rules EVIDENCE REQUIRED |
| 13 Loading / dispatch | Technical complete — DispatchQualityRecord, vehicle checklist links, cold-chain Decimal temps, qty reconciliation, QA RELEASE gate default OFF (ADR-025) | Dispatch SOPs / temperature limits / APR-017 gate enablement EVIDENCE REQUIRED |
| 14 Offline PWA | **Decision gate complete** — offline **not** implemented (ADR-026); online-only MVP retained + paper fallback | APR-022 / Wi-Fi / device / logout-wipe evidence still required to reopen |
| 15 Notifications | Technical complete — in-app notifications + optional SMTP; events default OFF; SMS not integrated (ADR-027) | Event matrix / SMTP / SMS provider EVIDENCE REQUIRED |
| 16 Reporting | Technical complete — catalogue, org RBAC, immutable submission sources, CSV + formula injection guard, async ReportRun (ADR-028) | Official report packs / Excel-PDF need EVIDENCE REQUIRED |
| 17 ERP / Bileeta | Adapter boundary complete — contracts/mocks, evidence gate, dead-letter, reconciliation, outbound prepare-only (ADR-029) | **BLOCKED — VENDOR API EVIDENCE REQUIRED** (APR-011/012/016/017) |
| 18–21 Later roadmap | Not started | N/A |

---

## Readiness gates (business / UAT)

| Gate document | Status |
| --- | --- |
| [PHASE_07_PRODUCTION_READINESS_GATE.md](business/PHASE_07_PRODUCTION_READINESS_GATE.md) | OPEN — production task generation BLOCKED |
| [PHASE_08_RECORDING_READINESS_GATE.md](business/PHASE_08_RECORDING_READINESS_GATE.md) | OPEN — production recording BLOCKED |
| [PHASE_09_SUPERVISOR_REVIEW_READINESS_GATE.md](business/PHASE_09_SUPERVISOR_REVIEW_READINESS_GATE.md) | OPEN — production Supervisor use BLOCKED |
| [PHASE_10_QA_REVIEW_READINESS_GATE.md](business/PHASE_10_QA_REVIEW_READINESS_GATE.md) | OPEN — production QA use BLOCKED |
| [PHASE_10_POST_QA_WORKFLOW_GATE.md](business/PHASE_10_POST_QA_WORKFLOW_GATE.md) | OPEN — all downstream items EVIDENCE REQUIRED |

**UAT PASSED:** No
**PRODUCTION READY:** No

---

## Recorded design / technical approvals (not production)

See [docs/approvals/README.md](approvals/README.md). Phase 01A–03 and selected documentation approvals exist. They do **not** approve:

- Official Nelna master data
- FG-QA-001 production content
- Role mappings
- SoD policy
- Hosting/production go-live

---

## Unresolved assumptions (summary)

Full detail: [ASSUMPTION_REGISTER.md](business/ASSUMPTION_REGISTER.md). **No assumption row is APPROVED.**

High-impact open items include ASM-001–006, ASM-008–016, MASTER-001, TEMPLATE-001 / FG-QA-001, batch source / Bileeta, recorder/Supervisor/QA mappings, SoD, retention, hosting, offline requirement.

Tracked for request/approval workflow: [governance/APPROVAL_REGISTER.md](governance/APPROVAL_REGISTER.md).

---

## Technical debt (selected)

| ID / topic | Status | Blocks |
| --- | --- | --- |
| DEBT-01C-R-NOTO (Noto Sans Sinhala) | Open | Operator Sinhala UAT / pilot / production UI claim |
| Phase 10A Docker re-validation | Outstanding | Claiming TECHNICALLY VALIDATED for 10A in Docker |
| Direct-main delivery vs PR-only rule text | Process debt | Consistency of contribution docs |
| Unseeded permissions without role assignment | By design until owners map | Operational use |
| Evidence module | Phase 11 technical complete (ADR-023) | Object-store IAM / active malware scan EVIDENCE REQUIRED |

---

## Business blockers

1. FG-QA-001 final content approval and publish policy
2. Complete paper-form inventory (ASM-003 / APR-028 / APR-036) — discovery framework exists; forms still **NOT RECEIVED**
3. Official Organization / Site / Department values (ASM-004)
4. Official Shift names/codes/times (ASM-005/006)
5. Official Product catalogue and specification limits (MASTER-001 / ASM-001)
6. Recorder / Supervisor / QA business-role mapping
7. Segregation-of-duties policy evidence
8. Product / Site / Shift / Department applicability rules
9. Checklist effective-version **as-of business event** (APR-015) — technical engine exists (07D); policy still DECISION REQUIRED
10. RELEASE / HOLD / REJECT operational meaning and downstream authority

---

## Integration blockers

1. Production batch source identity (system/API/event) — EVIDENCE REQUIRED
2. Bileeta API / sandbox availability — DECISION / EVIDENCE REQUIRED (no connector implemented)
3. Organization mapping from external batch identity — EVIDENCE REQUIRED
4. ERP write prohibition remains in force (no direct ERP DB writes)

---

## UAT blockers

1. DEBT-01C-R-NOTO open (Sinhala operator UI)
2. No approved published checklist content for pilot
3. No approved role assignments / SoD matrix
4. No hosted UAT environment decision (ASM-015)
5. Device / Wi-Fi / hygiene evidence incomplete (ASM-009–011)
6. Production readiness gates for Phases 07–10 remain OPEN

---

## Governance package

| Document | Path |
| --- | --- |
| Approval register | [governance/APPROVAL_REGISTER.md](governance/APPROVAL_REGISTER.md) |
| Decision log | [governance/DECISION_LOG.md](governance/DECISION_LOG.md) |
| Risk register | [governance/RISK_REGISTER.md](governance/RISK_REGISTER.md) |
| RACI | [governance/RACI.md](governance/RACI.md) |
| Change control | [governance/CHANGE_CONTROL.md](governance/CHANGE_CONTROL.md) |
| Continuity / handover | [operations/CONTINUITY_AND_HANDOVER_PLAN.md](operations/CONTINUITY_AND_HANDOVER_PLAN.md) |
| Real form discovery (06F) | [business/form-discovery/README.md](business/form-discovery/README.md) |
| Checklist Engine v2 design (06G) | [architecture/ADR-019-CHECKLIST-ENGINE-V2-ARCHITECTURE.md](architecture/ADR-019-CHECKLIST-ENGINE-V2-ARCHITECTURE.md) |

---

## Recommended next engineering focus (not authorization)

1. Drive owners to return paper-form inventory via [form-discovery/](business/form-discovery/) (APR-028 / APR-036) — do **not** invent forms for Checklist Engine v2.
2. Keep Engine v2 business values evidence-gated (ADR-019). **06H–06M** technical foundations are on main (06M measurement semantics technical only — no seeded product limits; 06L HACCP classifications still EVIDENCE REQUIRED).
3. Complete Phase 10A Docker/host validation when Docker engine is healthy (**no new business features** required for that gate).
4. Drive APPROVAL_REGISTER items with named owners (especially FG-QA-001, mappings, batch source).
5. Do **not** start Phase 11+ operational features until owners prioritize and evidence gates allow.

**Production readiness is not claimed by this document.**

---

## Phase 04C delivery status

**STATUS: PHASE 04C REAL COMPANY VALUES PENDING**

Technical foundation (permissions, audited lifecycle, historical hard-delete refusal, controlled CSV import, admin search/filter) is implemented. ASM-004 / ASM-005 / ASM-006 and APR-002 / APR-003 / APR-004 remain unresolved — no official Nelna Organization/Site/Department/Shift catalogue was loaded.

---

## Phase 05C delivery status

**STATUS: PHASE 05C FG PRODUCT MASTER FOUNDATION COMPLETE**

Optional mapping/attribute blanks, effective dates, historical hard-delete refusal, controlled CSV import, and expanded search/filter are implemented. MASTER-001 / APR-005 remain **EVIDENCE REQUIRED** — official Product catalogue was **not** received or loaded.

---

## Phase 05D delivery status

**STATUS: PHASE 05D EQUIPMENT CALIBRATION FOUNDATION COMPLETE**

Unseeded equipment master, calibration records, fitness labels (no block policy), checklist optional equipment-reference flag, RBAC separation, and audits are implemented. Calibration intervals and overdue block/warn remain **EVIDENCE REQUIRED** — no fake assets seeded.

---

## Phase 05E delivery status

**STATUS: PHASE 05E TRAINING FOUNDATION COMPLETE**

Technical training/competency foundation is implemented without seeded company matrices. Recording WARN/BLOCK gates remain OFF by default until APR evidence approves policy.

---

## Phase 06N delivery status

**STATUS: PHASE 06N BLOCKED — BUSINESS APPROVAL REQUIRED**

FG-QA-001 Draft v0.1 was reviewed against real-evidence gates. No company forms, owner issue log entries, or APR-001 written approval were available. The proposal remains DRAFT; no PUBLISHED version was created; no numeric limits were invented. Item validation matrix: 42 × PENDING DECISION.

---

## Phase 06O delivery status

**STATUS: PHASE 06O PRODUCT SPECIFICATIONS COMPLETE**

Versioned ProductSpecification / SpecificationVersion / SpecificationParameter foundation is implemented with immutability, effectivity overlap policy, org-scoped high-privilege RBAC, audit events, and optional checklist SPECIFICATION_PARAMETER pins. No Nelna limits were seeded — APR-006 / ASM-001 remain **EVIDENCE REQUIRED**. OUT_OF_SPEC does not auto HOLD/REJECT.

---

## Phase 07D delivery status

**STATUS: PHASE 07D EFFECTIVE VERSION POLICY COMPLETE**

Technical effective-version selection is implemented: optional inclusive `effective_from` / `effective_to` on `ChecklistVersion`, deterministic `ONE_ELIGIBLE_VERSION` resolution, explicit `NO_ELIGIBLE_VERSION` / `OVERLAPPING_ELIGIBLE_VERSIONS` blocks (never silent fallback or arbitrary pick), audited effectivity updates, and optional task helper that pins the resolved PUBLISHED version. APR-015 (which business event supplies `as_of`) remains **DECISION REQUIRED** — not invented. Existing `ChecklistTask` pins never auto-upgrade.

## Phase 07E delivery status

**STATUS: PHASE 07E RECURRING TASKS COMPLETE**

## Phase 07F delivery status

**STATUS: PHASE 07F LIVE BATCH CONTRACT REQUIRED**

Adapter/service boundary implemented: external identity (`source_system`, `source_event_id`, `external_batch_id`), configured mappings, applicability ONE_MATCH, Phase 07D effective-version selection, idempotent `ChecklistTask` creation with safe retry and concurrency controls. No live Bileeta/ERP connector, webhooks, or credentials. APR-011 remains **EVIDENCE REQUIRED**.

## Phase 07G delivery status

**STATUS: PHASE 07G TASK ASSIGNMENT COMPLETE**

Checklist task ownership workflow is implemented: assign / reassign / unassign with append-only history, VIEW-scoped My/Unassigned/Assigned queues, and `assign_checklisttask` permission. Assignment never grants RBAC. Team master remains EVIDENCE REQUIRED (opaque team code only).

## Phase 07H delivery status

**STATUS: PHASE 07H DUE MANAGEMENT COMPLETE**

Due/overdue foundation: configured `due_from` / `due_at` (`due_to`) / optional `due_soon_minutes`; derived display states (`NOT_DUE` / `DUE` / `DUE_SOON` / `OVERDUE`) without persisted redundant state; overdue queue + UI badges/filters. No invented SLA durations. Overdue never auto-creates NCR.

## Phase 08C delivery status

**STATUS: PHASE 08C RECORDING HARDENING COMPLETE**

Shop-floor recording hardening: preserved start → Save Draft → submit → immutable snapshot; safe autosave; optimistic `draft_version` (no silent last-write-wins); online session recovery (not IndexedDB); sticky save / section progress / validation summary / touch targets; optional equipment + Phase 11 evidence hooks. Production recording remains BLOCKED.

## Phase 09C delivery status

**STATUS: PHASE 09C SUPERVISOR GOVERNANCE COMPLETE**

Supervisor review governance hardening: Phase 03C permission mappings (no invented Supervisor titles); self-review PENDING by default (PROHIBIT/ALLOW only with evidence_reference); optional configured `review_sla_minutes` for overdue; temporary time-bounded review delegation via ScopedRoleAssignment; pending / overdue / resubmission queues; immutable audited decisions. Production Supervisor review remains BLOCKED.

## Phase 10B delivery status

**STATUS: PHASE 10B WORKFLOW LIFECYCLE COMPLETE**

Derived operational workflow (ADR-022): authoritative state remains on Task / Record / Submission / SupervisorReview / Correction / QAReview. One read-time lifecycle label (`PENDING` … `QA_*` / `CANCELLED`) with consistent badges and queue filters. QA terminals are provisional in-app dispositions only — they do not close warehouse / ERP / dispatch.

## Phase 11 delivery status

**STATUS: PHASE 11 EVIDENCE ATTACHMENTS COMPLETE**

Secure quality evidence attachments (ADR-023): private storage, allowlisted types, SHA-256 integrity, authorized download, soft-retire only, malware scanner interface defaulting to NOT_CONFIGURED. Production MinIO/S3 IAM and active scanning remain EVIDENCE REQUIRED.

## Phase 12 delivery status

**STATUS: PHASE 12 NCR HOLD CAPA FOUNDATION COMPLETE**

Configurable quality-case foundation (ADR-024): formal NCR lifecycle + HoldCase + CAPA actions/verification/effectiveness with human-only closure; append-only history and audit; separate create/manage/close permissions; no FAIL/CCP auto-raise; checklist correction remains distinct from NCR. Production severity/resolution/auto-raise policies remain EVIDENCE REQUIRED.

## Phase 13 delivery status

**STATUS: PHASE 13 DISPATCH QUALITY FOUNDATION COMPLETE**

Loading/dispatch quality foundation (ADR-025): DispatchQualityRecord with vehicle inspection checklist links, cold-chain Decimal temperature readings, released/loaded/remaining quantity lines (not ERP ledger), configurable QA RELEASE gate disabled by default, append-only history and audit. No AI loading release; no ERP writes; production SOPs/limits remain EVIDENCE REQUIRED.

## Phase 14 delivery status

**STATUS: PHASE 14 ONLINE ONLY APPROVED — OFFLINE NOT IMPLEMENTED**

Offline decision gate (ADR-026): Wi-Fi survey, device plan, hosting, outage profile, and APR-022 remain EVIDENCE REQUIRED / open. Standing MVP direction is online-only recording with paper fallback. No IndexedDB draft sync, service worker offline queue, or offline QA/HOLD/REJECT paths were implemented. Re-open Phase 14 only after IT + Production + QA clear APR-022 with supporting evidence.

## Phase 15 delivery status

**STATUS: PHASE 15 NOTIFICATIONS COMPLETE**

Workflow notifications foundation (ADR-027): in-app notifications with privacy-safe titles/messages; org event policy default OFF; optional SMTP email when configured (no credentials in repo); Celery idempotent email delivery; SMS not integrated. Production event matrices and SMS remain EVIDENCE REQUIRED.

## Phase 16 delivery status

**STATUS: PHASE 16 REPORTING COMPLETE**

Governed quality reporting foundation (ADR-028): org-scoped catalogue and `ReportRun` CSV generation; historical submission/review/QA/correction paths use immutable snapshots (never draft responses); formula-injection protection; background generation for large runs; export/download audited. Official Nelna report packs and Excel/PDF remain EVIDENCE REQUIRED / not implemented.

## Phase 17 delivery status

**STATUS: PHASE 17 BLOCKED — VENDOR API EVIDENCE REQUIRED**

Bileeta/ERP adapter boundary (ADR-029): `apps.integrations` with inbound contracts mapped only to the Phase 07F consumer, mock sandbox behaviours, live HTTP hard-gated, idempotent attempts + dead-letter, reconciliation, outbound disposition interface prepare-only (APR-017). No invented endpoints, no live connector, no ERP DB writes. Re-open live calls only after APR-011/012 artefacts land in the vendor evidence register.


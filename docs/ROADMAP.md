# Roadmap — Phase Delivery Plan

**Document status:** Governing roadmap for greenfield delivery
**Canonical status:** [PROJECT_STATUS.md](PROJECT_STATUS.md) (prefer when summaries conflict)
**Phase:** Through Phase **10A** technical foundations on `main`; MASTER-001 / TEMPLATE / role mappings / post-QA workflows still evidence-required
**Last updated:** 2026-08-10 (06O product specifications)

Branch naming pattern: `foundation/...`, `design/...`, `feature/phase-NN-short-name`, or `hardening/...` as appropriate. Prefer PR review; some authorized units have used direct-`main` quality-first delivery — see [governance/CHANGE_CONTROL.md](governance/CHANGE_CONTROL.md).

**Progress:** Phases **00–10A** technical foundations are on `main` (accounts/RBAC; Shift; FG Product; checklist definition + FG-QA-001 draft loader; ChecklistTask; draft/submit; Supervisor review + correction; QA manual disposition). FG-QA-001 remains **NOT APPROVED** for production (Phase **06N BLOCKED — BUSINESS APPROVAL REQUIRED**). Official master data, role mappings, SoD, batch source/Bileeta, and post-QA RELEASE/HOLD/REJECT operations remain **EVIDENCE REQUIRED**. DEBT-01C-R-NOTO remains **open**. Production readiness **not** claimed. No deployment approval exists. Details: [PROJECT_STATUS.md](PROJECT_STATUS.md).

**Numbering rule:** Preserve roadmap phase numbers. Do **not** rename FG master data, checklist templates, recording, review, or evidence work as Phase 04.

---

## Phase 00 — Discovery and governance

| Field | Content |
| --- | --- |
| Objective | Establish charter, requirements scaffolding, ADRs, risks, security/AI policies, Cursor rules, and delivery control |
| Inputs | Approved technical direction; empty greenfield repository |
| Outputs | Docs tree; Cursor rules; README; decision/assumption/risk registers |
| Approval gate | Manual PR review of foundation docs |
| Branch naming | `foundation/project-discovery` |
| Exit criteria | Required docs and rules merged; no app code; no invented Nelna values |
| Dependencies | None |
| Status | **Complete — merged to main** |

## Phase 01A — User journeys, IA, and low-fidelity specification

| Field | Content |
| --- | --- |
| Objective | Define personas, eight critical journeys, IA, screen inventory, workflow states, lo-fi wireframe specs, language/a11y/responsive rules, Figma build spec, and design approval form |
| Inputs | Phase 00 docs (charter, MVP scope, ADR-003, FIGMA_PLAN, assumptions) |
| Outputs | docs/design/* 01A set; Phase 01A approval form; updated README/ROADMAP/FIGMA_PLAN |
| Approval gate | Manual design review + [PHASE_01A_DESIGN_APPROVAL.md](approvals/PHASE_01A_DESIGN_APPROVAL.md) |
| Branch naming | `design/figma-user-journeys` |
| Exit criteria | Required 01A docs in review/merged; no app code; no false approval claims; no invented Nelna values |
| Dependencies | Phase 00 merged |
| Status | **Complete — merged; owner-approved as proposed baseline (2026-08-04)** |

## Phase 01B — Design tokens and components

| Field | Content |
| --- | --- |
| Objective | Define design tokens and core component system for Figma pages 04â€“05; document build/review/approval path |
| Inputs | Owner-approved 01A baseline; accessibility/content/responsive rules |
| Outputs | DESIGN_TOKENS; COMPONENT_SYSTEM; catalogue/anatomy/patterns; foundations; variables/build guides; tokens JSON; contrast validation; Figma draft file + implementation log; 01B checklist + approval form |
| Approval gate | Design system review + [PHASE_01B_DESIGN_APPROVAL.md](approvals/PHASE_01B_DESIGN_APPROVAL.md) |
| Branch naming | `design/figma-tokens-components` (deviation from planned `design/figma-design-system` — see PHASE_01B_DECISIONS P1B-010) |
| Exit criteria | Token/component specs + artefacts in review; JSON valid; contrast documented; Figma status truthful; no app code; no false approval claims |
| Dependencies | Phase 01A approval |
| Status | **Approved with conditions (2026-08-05) — merged via PR #3** |

## Phase 01C — High-fidelity MVP screens and prototype

| Field | Content |
| --- | --- |
| Objective | High-fidelity MVP screens (pages 06â€“12) and interactive prototype |
| Inputs | 01A journeys/IA; 01B tokens/components; 01B approval conditions |
| Outputs | Hi-fi frames; prototype; developer handoff expansion; continued variable/component/a11y completion |
| Approval gate | Business/QA UX review of MVP flows; [PHASE_01C_HIGH_FIDELITY_APPROVAL.md](approvals/PHASE_01C_HIGH_FIDELITY_APPROVAL.md) |
| Branch naming | `design/figma-high-fidelity-mvp` |
| Exit criteria | MVP journeys prototype-ready; Sinhala/EN strategy applied with pending translations marked; 01B conditions not omitted; 67 open design decisions resolved or documented |
| Dependencies | Phase 01B approval |
| Status | **Approved with deferred Sinhala typography condition (2026-08-05) — Phase 02 foundation authorized after PR #4 merge; DEBT-01C-R-NOTO remains open** |

## Phase 01 — Figma journeys and design system (umbrella)

| Field | Content |
| --- | --- |
| Objective | Umbrella for 01Aâ€“01C per FIGMA_PLAN |
| Inputs | Charter, MVP scope, questionnaire answers as available |
| Outputs | Complete Figma foundation through hi-fi prototype |
| Approval gate | See 01A/01B/01C gates |
| Branch naming | See sub-phases |
| Exit criteria | Journeys agreed; tokens/components done; hi-fi MVP reviewed |
| Dependencies | Phase 00 |

## Phase 02 — Django/PostgreSQL foundation

| Field | Content |
| --- | --- |
| Objective | Create Django 5.2 project, PostgreSQL, Docker Compose, settings layout, Pytest skeleton, CI gates, frontend build baseline |
| Inputs | ADRs; environment strategy; Phase 01C deferred-condition approval |
| Outputs | Runnable local foundation without business modules; Phase 02 docs/ADRs |
| Approval gate | Technical review — [PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md](approvals/PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md) |
| Branch naming | `foundation/django-postgresql` (obsolete planned name `feature/phase-02-django-foundation` **superseded**) |
| Exit criteria | App boots locally; base migrations OK; CI gates defined; no invented business data; approval form signed |
| Dependencies | Phase 01C approved with deferred Sinhala condition |
| Status | **Approved with conditions** — merged via PR #5 / #6; DEBT-01C-R-NOTO remains open |

## Phase 03 — Accounts and RBAC

| Field | Content |
| --- | --- |
| Objective | Employee-code identity, session auth, lockout, org/site/department scope, Django-permission roles, scoped assignments, security audit |
| Inputs | Phase 02 approved foundation; security baseline |
| Outputs | `accounts`, `organizations`, `access_control`, `security_audit`; ADRs 006â€“007; Phase 03 approval form |
| Approval gate | Security-focused PR review — [PHASE_03_ACCOUNTS_RBAC_APPROVAL.md](approvals/PHASE_03_ACCOUNTS_RBAC_APPROVAL.md) |
| Branch naming | `feature/accounts-rbac` |
| Exit criteria | Auth/RBAC/lockout/audit tests pass; no seeded users/orgs/roles; no business workflows; approval form signed |
| Dependencies | Phase 02 |
| Status | **Approved with conditions (2026-08-06)** — merged via PR #7 (and related follow-ups); DEBT-01C-R-NOTO remains open; authentication UI polish merged via PR #8 |

## Phase 03C — Operational role governance

| Field | Content |
| --- | --- |
| Objective | Strengthen operational permission catalogue, RoleTemplate technical bundles, audited role-permission updates, and SoD question register without inventing approved Nelna roles |
| Inputs | Phase 03 RBAC; APR-007..010 open; CHECKLIST_RECORDER_ROLE_MAPPING |
| Outputs | `permission_catalogue.py`; `RoleTemplate`; governance services; PERMISSION_MATRIX; PHASE_03C docs/tests; APR-040 |
| Approval gate | Business role mappings remain EVIDENCE REQUIRED — final status **PHASE 03C BUSINESS ROLE APPROVAL PENDING** |
| Exit criteria | Technical gates pass; no seeded company-approved roles; SoD questions PENDING; manage≠record≠review≠QA preserved |
| Dependencies | Phase 03 |
| Status | **Technical foundation** — BUSINESS ROLE APPROVAL PENDING |

## Phase 04 — Organization hierarchy and shifts

| Field | Content |
| --- | --- |
| Objective | Complete residual organization-hierarchy confirmation and introduce a configurable Shift foundation without inventing official Nelna business values |
| Inputs | Owner provisional technical direction (2026-08-07); later real ASM-004/005/006 evidence for production configuration |
| Outputs | Hierarchy confirmation record; configurable unseeded `organizations.Shift` foundation (Phase 04A); management UI (Phase 04B); real-data config after evidence (remaining) |
| Approval gate | Technical review of 04A/04B; real-data / UAT still blocked until ASM evidence and DEBT-01C-R-NOTO closure |
| Branch naming | Direct-main for 04A/04B quality-first workflow; feature branches optional |
| Exit criteria | Phase 04A: configurable Shift model/services/selectors/audit/admin/tests without seeded business rows. Phase 04B: authorized Shift management UI. Full Phase 04: real Shift values configured after evidence; scoped queries remain sound |
| Dependencies | Phase 03 complete; Phase 04 scope reconciliation (PR #10); owner provisional decision for configurable foundation |
| Status | **04A + 04B + 04C technical foundation implemented** — Phase 04 **not** fully complete; real-data configuration / UAT pending |

### Phase 04 scope statement

Phase 04 completes residual organization-hierarchy confirmation and introduces Shift support. Organization, Site, and Department **already exist** from Phase 03 and are not rebuilt. Phase **04A** delivers a configurable, unseeded Shift domain foundation under owner provisional direction ([PHASE_04_SHIFT_PROVISIONAL_CONFIGURATION.md](decisions/PHASE_04_SHIFT_PROVISIONAL_CONFIGURATION.md), [ADR-008](architecture/ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md)). Phase **04B** delivers the Shift management UI ([SHIFT_MANAGEMENT_UI.md](design/SHIFT_MANAGEMENT_UI.md)). Phase **04C** adds audited Org/Site/Department lifecycle + controlled hierarchy import (no seeded company values). Administrator entry of real business values after ASM evidence remains outstanding. FG products, checklist definitions, checklist records, review workflows and attachments remain explicitly **outside** Phase 04.

### Phase 04 business gates

| Gate | Requirement | Status |
| --- | --- | --- |
| ASM-004 | Confirm official organization / site / department naming and hierarchy | **DECISION REQUIRED** — remains unresolved for official names/codes; models exist; no inventing Nelna values |
| ASM-005 | Confirm shift names and codes | **EVIDENCE REQUIRED** — remains unresolved for official Shift names/codes; technical configurable foundation provisionally unblocked only |
| ASM-006 | Confirm shift timing, overnight behavior, and effective-date rules | **DECISION REQUIRED** — remains unresolved for official timings/policy; provisional overnight derivation (`end <= start`) is technical only |

Do **not** invent or seed Day/Night shift names, official shift start/end times, official shift codes, site codes, or department codes. Authorized users configure real Shift values later. Production use remains prohibited until real data and UAT are confirmed.

### Phase 04 out of scope

- FG Product / product category
- Checklist builder, definition, or versioning
- Checklist recording, draft/save/submit
- Supervisor review, approval, rejection, return
- Attachments / evidence storage
- Reports / dashboards
- ERP integration
- Offline sync
- Sinhala UI approval
- Deployment / production readiness claims

## Phase 05 — FG operational master data, instruments and training

| Field | Content |
| --- | --- |
| Objective | Minimal FG / operational master data for MVP templates; instruments/training as approved |
| Inputs | Owner provisional Product foundation decision (2026-08-07); later MASTER-001 evidence for real catalogues |
| Outputs | `master_data` FG Product foundation (05A); authz hardening + MASTER-001 intake (05B); expandable optional mapping fields + controlled CSV import (05C); `instruments` equipment + calibration foundation (05D); `training` competency foundation (05E) |
| Approval gate | Data owner review for real data; technical review of 05A/05B/05C/05D/05E |
| Branch naming | Direct-main quality-first for 05A/05B/05C/05D/05E |
| Exit criteria | 05A: configurable unseeded FG Product model/services/selectors/UI/audit without seeded business rows. 05B: object-aware Product UI affordances + MASTER-001 evidence intake readiness. 05C: optional mapping/attribute blanks + controlled import (no official catalogue). 05D: unseeded equipment + calibration records + fitness labels + checklist optional equipment flag (no invented intervals; no overdue block policy). 05E: unseeded training records + currency labels + OFF/WARN/BLOCK policy metadata (no invented matrix; no recording auto-block). Full Phase 05: evidenced entities only after MASTER-001 / calibration / training evidence |
| Dependencies | Phase 04 (04A/04B/04C technical complete; official org/shift values still pending) |
| Status | **05A–05E technical foundations implemented** — MASTER-001 unresolved; training unseeded (no invented matrices); recording training gates default OFF; official catalogues **not** received; Phase 05 **not** fully complete |
| Notes | **Not** Phase 04. Do not invent calibration intervals or training matrices. Site-only RBAC does not imply organization Product/equipment/training management under provisional ownership. No live Bileeta calls in 05C. |

## Phase 06 — Checklist definition and versioning

| Field | Content |
| --- | --- |
| Objective | Versioned checklist definitions/templates for later operational use |
| Inputs | Owner provisional definition-engine decision (2026-08-07); later TEMPLATE / ASM evidence for real forms |
| Outputs | `checklists` definition foundation (06A); governance hardening + TEMPLATE-001 intake (06B); response-definition schema + FG-QA-001 **proposed draft** artifact (06C); explicit DRAFT loader + internal validation worksheet (06D); owner-directed provisional workflow formalization (06E); **real form discovery framework (06F)**; **Checklist Engine v2 architecture design (06G / ADR-019)**; real content later as approved |
| Approval gate | QA content approval for real forms; technical review of 06A–06G |
| Branch naming | Direct-main quality-first for 06A–06G |
| Exit criteria | 06A: configurable unseeded Template/Version/Section/Item with immutable publish, RBAC, UI, audit. 06B: centralized lifecycle, concurrency/immutability hardening, evidence intake readiness. 06C: provisional response-definition primitives + draft proposal artifact (not production content). 06D: explicit Organization-scoped DRAFT load (never publish/auto-seed) + stakeholder validation package. 06E: record owner-directed provisional workflow without claiming formal QA/Production approval. 06F: formal real-company form discovery package with no invented form rows. 06G: Engine v2 architecture ADR + 06H–06M split without schema-shaping implementation. Full Phase 06: evidenced forms only after TEMPLATE evidence and APPROVED FOR DIGITALIZATION |
| Dependencies | Phase 05 technical foundation (Product optional association); TEMPLATE evidence for content |
| Status | **06A-06O** — Engine v2 designed (ADR-019); 06H-06M technical foundations; **06N FG-QA-001 validation BLOCKED**; **06O versioned product specs technical (no seeded limits; APR-006 EVIDENCE REQUIRED)**; inventory NOT RECEIVED; FG-QA-001 remains project-proposed DRAFT; Phase 06 not fully complete |
| Notes | **Not** Phase 04. Definition/versioning + response **definition** schema only for executed code path today. No invented temperature limits; no automatic RELEASE/HOLD/REJECT. FG-QA-001 draft is **NOT APPROVED**. AI industry reports are research inputs only. Engine v2 extends current domain — no parallel engine. Phase 07A technical foundation may proceed under provisional workflow; full Phase 07 production readiness remains evidence-gated. |

## Phase 07 — Scheduling and tasks

| Field | Content |
| --- | --- |
| Objective | Schedules and task assignment |
| Inputs | Owner-directed provisional per-batch trigger (06E); later frequency/applicability evidence for production generation |
| Outputs | **07A:** `scheduling.ChecklistTask` foundation; **07B:** batch-source contract + integration port + `record_checklisttask` permission foundation + production/Phase 08 readiness gates; later recurrence/`schedules` as approved |
| Approval gate | Operations review of due logic for full Phase 07; 07A/07B/07C/07D are technical/readiness only |
| Branch naming | Direct-main quality-first for 07A/07B/07C/07D |
| Exit criteria | **07A:** org-scoped create/cancel/list/detail with RBAC, audit, uniqueness, no recording/HOLD. **07B:** source contract + manage≠record permission architecture; no ERP invention. **07C:** applicability engine without silent multi-match. **07D:** deterministic PUBLISHED effective-version selection (APR-015 as-of still DECISION REQUIRED). Full Phase 07: operators see correct due work from evidenced batch source + published approved definitions |
| Dependencies | Phase 06 technical + 06E provisional workflow; FG-QA-001 publish + batch source for real generation |
| Status | **07A + 07B + 07C + 07D** — technical foundations; real production task generation still **BLOCKED** |

## Phase 08 — Checklist recording and submission (draft → submit)

| Field | Content |
| --- | --- |
| Objective | Online draft and submission UX and record services (DRAFT → SUBMITTED) |
| Inputs | Figma operator screens; published templates; approved recorder role mapping |
| Outputs | **08A:** `recording.ChecklistRecord` / `ChecklistResponse` draft foundation + Save Draft UI; **08B:** `ChecklistSubmission` / `ChecklistSubmissionResponse` immutable snapshots + Submit UI |
| Approval gate | Operator UAT sample (Sinhala UAT still blocked by DEBT-01C-R-NOTO); Phase 08 readiness gate for production use |
| Branch naming | Direct-main quality-first for 08A/08B |
| Exit criteria | **08A:** typed draft responses; record permission enforced; partial draft allowed. **08B:** completeness submit; immutable snapshot; post-submit edit blocked; no Submit/HOLD evaluation. Full Phase 08 production: evidenced published definitions + recorder mapping |
| Dependencies | Phase 07 technical; Phase 01 progress; published pilot definition + recorder mapping for production |
| Notes | **Not** Phase 04. Do not include supervisor approval in this phase. **08A+08B technical foundations complete**; **production recording remains BLOCKED** (FG-QA-001 unpublished; role mapping open). |
| Status | **08A + 08B implemented** — draft + immutable submit; Phase 09+ blocked |

## Phase 09 — Supervisor checking and amendments

| Field | Content |
| --- | --- |
| Objective | Supervisor check workflow (approve / return for correction / related amendments) and amendment history |
| Inputs | SoD rules (EVIDENCE REQUIRED) |
| Outputs | **09A:** `reviews.SupervisorReview` immutable decisions on `ChecklistSubmission` + review UI; **09B:** `ChecklistCorrection` + resubmission as Submission #N+1 |
| Approval gate | QA/operations workflow review |
| Branch naming | Direct-main quality-first for 09A/09B |
| Exit criteria | **09A:** separate review permission; one review per submission; APPROVED/RETURNED without mutating snapshots. **09B:** controlled correction without mutating source submission/review; next submission number race-safe. Full Phase 09 production: SoD evidence + role mapping + published definitions |
| Dependencies | Phase 08 |
| Notes | **Not** Phase 04. **09A+09B technical foundations complete**; production Supervisor review/correction **BLOCKED**. SoD self-review rule not invented. No QA/HOLD/RELEASE in Phase 09. Ownership locking for correction remains EVIDENCE REQUIRED. |
| Status | **09A + 09B implemented** — production use blocked |

## Phase 10 — QA verification

| Field | Content |
| --- | --- |
| Objective | QA final review with manual provisional disposition; later operational follow-up only when evidenced |
| Inputs | QA rules evidence |
| Outputs | **10A:** `quality.QAReview` immutable RELEASE/HOLD/REJECT + QA UI; later units for post-QA workflows |
| Approval gate | QA owner |
| Branch naming | Direct-main quality-first for 10A |
| Exit criteria | **10A:** separate QA permission; one immutable QAReview per submission; no auto disposition; no ERP side effects. Full production: follow-up evidence + role mapping + published definitions |
| Dependencies | Phase 09 |
| Notes | Supervisor-owned return/correction remains Phase 09. See PHASE_10_QA_REVIEW_READINESS_GATE and PHASE_10_POST_QA_WORKFLOW_GATE. Production QA **BLOCKED**. |
| Status | **10A implemented** — production use blocked; post-QA operational workflows not started |

## Phase 11 — Attachments and evidence storage

| Field | Content |
| --- | --- |
| Objective | MinIO/S3 evidence upload, attachment metadata, and controlled access |
| Inputs | Security baseline; volume assumptions (ASM-017) |
| Outputs | `evidence` module |
| Approval gate | IT security review of access patterns |
| Branch naming | `feature/phase-11-evidence-storage` |
| Exit criteria | No DB BLOBs; signed URL pattern |
| Dependencies | Phase 08+ (can start in parallel after foundation) |
| Notes | **Not** Phase 04. Malware scanning and retention remain deferred until decided. |

## Phase 12 — Non-conformance, holds and CAPA

| Field | Content |
| --- | --- |
| Objective | NC/hold/CAPA after MVP |
| Inputs | QA procedures |
| Outputs | `nonconformance`, `capa` |
| Approval gate | QA |
| Branch naming | `feature/phase-12-nc-capa` |
| Exit criteria | Human-only CAPA closure |
| Dependencies | Phase 10 |

## Phase 13 — Loading, dispatch and cold-chain controls

| Field | Content |
| --- | --- |
| Objective | Loading/dispatch digital controls |
| Inputs | Dispatch SOPs |
| Outputs | `loading`, `dispatch` |
| Approval gate | Dispatch + QA |
| Branch naming | `feature/phase-13-loading-dispatch` |
| Exit criteria | No AI loading release |
| Dependencies | Phase 10â€“11 |

## Phase 14 — Offline PWA and synchronization

| Field | Content |
| --- | --- |
| Objective | IndexedDB drafts and sync queues |
| Inputs | Risk mitigations for lost/duplicate data |
| Outputs | Offline client + sync services |
| Approval gate | IT + QA |
| Branch naming | `feature/phase-14-offline-sync` |
| Exit criteria | Offline tests pass; idempotent sync |
| Dependencies | Phase 08+ stable online flows |

## Phase 15 — Notifications

| Field | Content |
| --- | --- |
| Objective | Email/SMS/in-app notifications |
| Inputs | Provider decision |
| Outputs | `notifications` |
| Approval gate | IT |
| Branch naming | `feature/phase-15-notifications` |
| Exit criteria | Failure-safe sending; no secret leak |
| Dependencies | Provider decision |

## Phase 16 — Reports and audit export

| Field | Content |
| --- | --- |
| Objective | Broader reports and audit export maturity |
| Inputs | Internal audit expectations |
| Outputs | `reports` enhancements; export packs |
| Approval gate | QA / Internal audit |
| Branch naming | `feature/phase-16-reports-audit` |
| Exit criteria | Export matches approved pilot/prod needs |
| Dependencies | Audit events from earlier phases |

## Phase 17 — ERP integration

| Field | Content |
| --- | --- |
| Objective | Approved API integration only |
| Inputs | ERP vendor contract/API |
| Outputs | `integrations` adapters |
| Approval gate | IT + ERP vendor |
| Branch naming | `feature/phase-17-erp-integration` |
| Exit criteria | No direct ERP DB writes; recording works if ERP down |
| Dependencies | ASM-014 |

## Phase 18 — Local AI and anomaly detection

| Field | Content |
| --- | --- |
| Objective | Optional local AI assistance |
| Inputs | AI safety policy |
| Outputs | `ai_assistance` |
| Approval gate | QA + IT |
| Branch naming | `feature/phase-18-local-ai` |
| Exit criteria | Advisory only; core flows work with AI off |
| Dependencies | Stable workflows; AI policy acknowledgement |

## Phase 19 — Security, backup, monitoring and performance

| Field | Content |
| --- | --- |
| Objective | Harden, monitor, backup/restore, performance verify |
| Inputs | NFR approvals; env strategy |
| Outputs | Runbooks; monitoring; restore evidence |
| Approval gate | IT security + ops |
| Branch naming | `hardening/phase-19-security-ops` |
| Exit criteria | Restore drill passed; security review recorded |
| Dependencies | Staging-like environment |

## Phase 20 — Pilot, UAT and parallel paper run

| Field | Content |
| --- | --- |
| Objective | Pilot with parallel paper as directed |
| Inputs | Trained users; approved MVP content |
| Outputs | UAT evidence; pilot report |
| Approval gate | Business + QA + IT |
| Branch naming | `pilot/phase-20-uat` (config/docs); code fixes via fix branches |
| Exit criteria | Exit criteria met; critical defects closed |
| Dependencies | Phases through applicable MVP scope + Phase 19 as required |

## Phase 21 — Production release and handover

| Field | Content |
| --- | --- |
| Objective | Controlled production release and handover |
| Inputs | Approvals; restore + security evidence |
| Outputs | Production release record; admin handover |
| Approval gate | Project + Business + QA + IT owners |
| Branch naming | `release/phase-21-production` |
| Exit criteria | Explicit written approval; no silent go-live |
| Dependencies | Phase 20 pass |

---

**Production readiness is not claimed by the existence of this roadmap.**

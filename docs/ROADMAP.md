# Roadmap — Phase Delivery Plan

**Document status:** Governing roadmap for greenfield delivery
**Phase:** Phase 04A complete · Phase 04B Shift management UI complete · real-data config / UAT still pending
**Last updated:** 2026-08-07

Branch naming pattern: `foundation/...`, `design/...`, `feature/phase-NN-short-name`, or `hardening/...` as appropriate. Never commit directly to `main`.

**Progress:** Phase 00–01C complete (01C with deferred Sinhala condition). Phase 02 **Approved with conditions** and merged (PR #5 / #6). Phase 03 accounts/RBAC **Approved with conditions** and merged (PR #7 / related follow-up merges). Authentication UI polish **merged** (PR #8). Phase 04 scope reconciliation **merged** (PR #10). Organization, Site, and Department models exist from Phase 03. Phase **04A** implements a configurable, **unseeded** Shift domain foundation under owner provisional direction (no invented Nelna shift values). Phase **04B** delivers the Shift management web UI (list/search/filter/create/detail/edit/activate/deactivate) without seeding business values. Real-data configuration and UAT remain pending. **No FG operational modules** (`master_data`, `checklists`, `records`, `reviews`, `evidence`) have started. ASM-004 / ASM-005 / ASM-006 remain partially unresolved for official business values. DEBT-01C-R-NOTO remains **open** (blocking for operator UAT/pilot/production and final Sinhala operator UI). Production readiness **not** claimed. No deployment approval exists.

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
| Objective | Define design tokens and core component system for Figma pages 04–05; document build/review/approval path |
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
| Objective | High-fidelity MVP screens (pages 06–12) and interactive prototype |
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
| Objective | Umbrella for 01A–01C per FIGMA_PLAN |
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
| Outputs | `accounts`, `organizations`, `access_control`, `security_audit`; ADRs 006–007; Phase 03 approval form |
| Approval gate | Security-focused PR review — [PHASE_03_ACCOUNTS_RBAC_APPROVAL.md](approvals/PHASE_03_ACCOUNTS_RBAC_APPROVAL.md) |
| Branch naming | `feature/accounts-rbac` |
| Exit criteria | Auth/RBAC/lockout/audit tests pass; no seeded users/orgs/roles; no business workflows; approval form signed |
| Dependencies | Phase 02 |
| Status | **Approved with conditions (2026-08-06)** — merged via PR #7 (and related follow-ups); DEBT-01C-R-NOTO remains open; authentication UI polish merged via PR #8 |

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
| Status | **04A + 04B implemented** — Phase 04 **not** fully complete; real-data configuration / UAT pending |

### Phase 04 scope statement

Phase 04 completes residual organization-hierarchy confirmation and introduces Shift support. Organization, Site, and Department **already exist** from Phase 03 and are not rebuilt. Phase **04A** delivers a configurable, unseeded Shift domain foundation under owner provisional direction ([PHASE_04_SHIFT_PROVISIONAL_CONFIGURATION.md](decisions/PHASE_04_SHIFT_PROVISIONAL_CONFIGURATION.md), [ADR-008](architecture/ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md)). Phase **04B** delivers the Shift management UI ([SHIFT_MANAGEMENT_UI.md](design/SHIFT_MANAGEMENT_UI.md)). Administrator entry of real business values after ASM evidence remains outstanding. FG products, checklist definitions, checklist records, review workflows and attachments remain explicitly **outside** Phase 04.

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
| Inputs | Master data evidence (MASTER-001); no invented product catalogues |
| Outputs | `master_data`, `instruments`, `training` as needed |
| Approval gate | Data owner review |
| Branch naming | `feature/phase-05-master-data` |
| Exit criteria | Only evidenced entities loaded |
| Dependencies | Phase 04 (or explicit owner waiver of residual hierarchy/shift gates) |
| Notes | **Not** Phase 04. Do not combine with checklist templates or recording. |

## Phase 06 — Checklist definition and versioning

| Field | Content |
| --- | --- |
| Objective | Versioned checklist definitions/templates for two approved checklist types |
| Inputs | Approved forms (TEMPLATE evidence) |
| Outputs | `checklists` module |
| Approval gate | QA content approval |
| Branch naming | `feature/phase-06-checklist-templates` |
| Exit criteria | Two templates only unless expansion approved |
| Dependencies | Phase 05; TEMPLATE evidence |
| Notes | **Not** Phase 04. Definition/versioning only — no operator submission ownership. |

## Phase 07 — Scheduling and tasks

| Field | Content |
| --- | --- |
| Objective | Schedules and task assignment |
| Inputs | Frequency rules from approved forms |
| Outputs | `schedules`, `tasks` |
| Approval gate | Operations review of due logic |
| Branch naming | `feature/phase-07-scheduling-tasks` |
| Exit criteria | Operators see correct due work in test |
| Dependencies | Phase 06 |

## Phase 08 — Checklist recording and submission (draft → submit)

| Field | Content |
| --- | --- |
| Objective | Online draft and submission UX and record services (DRAFT → SUBMITTED) |
| Inputs | Figma operator screens; published templates |
| Outputs | `records` submit path; operator UI |
| Approval gate | Operator UAT sample (Sinhala UAT still blocked by DEBT-01C-R-NOTO) |
| Branch naming | `feature/phase-08-operator-recording` |
| Exit criteria | Submit immutability; online MVP flows; no fake success |
| Dependencies | Phase 07; Phase 01 progress |
| Notes | **Not** Phase 04. Do not include supervisor approval in this phase. |

## Phase 09 — Supervisor checking and amendments

| Field | Content |
| --- | --- |
| Objective | Supervisor check workflow (approve / return for correction / related amendments) and amendment history |
| Inputs | SoD rules (EVIDENCE REQUIRED) |
| Outputs | `reviews`; amendment services |
| Approval gate | QA/operations workflow review |
| Branch naming | `feature/phase-09-supervisor-review` |
| Exit criteria | SoD tests pass; before/after history stored |
| Dependencies | Phase 08 |
| Notes | **Not** Phase 04. Supervisor rejection/return paths belong here when approved — not in master-data or template phases. |

## Phase 10 — QA verification

| Field | Content |
| --- | --- |
| Objective | QA verify path with deterministic critical-rules hooks; QA reject / hold / reinspection only when approved by QA owner |
| Inputs | QA rules evidence |
| Outputs | `quality` verification services/UI |
| Approval gate | QA owner |
| Branch naming | `feature/phase-10-qa-verification` |
| Exit criteria | Verify path tested; no AI final decisions |
| Dependencies | Phase 09 |
| Notes | Correction/rejection/return that are **supervisor-owned** remain Phase 09. Do not merge Phases 08–10 into one mega-phase. |

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
| Dependencies | Phase 10–11 |

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

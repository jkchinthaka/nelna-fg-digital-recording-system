# Roadmap — Phase Delivery Plan

**Document status:** Governing roadmap for greenfield delivery  
**Phase:** 01A — User journeys and low-fidelity specification (current)  
**Last updated:** 2026-08-04

Branch naming pattern: `foundation/...`, `design/...`, `feature/phase-NN-short-name`, or `hardening/...` as appropriate. Never commit directly to `main`.

**Progress:** Phase 00 merged to `main`. Application development has not started. Phase 01 split into 01A (journeys/IA/lo-fi docs), 01B (tokens/components), 01C (high-fidelity + prototype).

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
| Status | **Current — awaiting manual design review** |

## Phase 01B — Design tokens and components

| Field | Content |
| --- | --- |
| Objective | Define and build Figma design tokens and core components (pages 04–05) |
| Inputs | Approved or conditionally approved 01A specs |
| Outputs | Token definitions; component library stubs/frames; doc updates |
| Approval gate | Design system review |
| Branch naming | `design/figma-tokens-components` |
| Exit criteria | Tokens/components reviewable in Figma per build spec; still no application code required |
| Dependencies | Phase 01A approval (or explicit conditional go-ahead) |
| Status | Not started — do not begin until 01A review decision |

## Phase 01C — High-fidelity MVP screens and prototype

| Field | Content |
| --- | --- |
| Objective | High-fidelity MVP screens (pages 06–12) and interactive prototype |
| Inputs | 01A journeys/IA; 01B tokens/components |
| Outputs | Hi-fi frames; prototype; developer handoff expansion |
| Approval gate | Business/QA UX review of MVP flows |
| Branch naming | `design/figma-hifi-mvp` |
| Exit criteria | MVP journeys prototype-ready; Sinhala/EN strategy applied with pending translations marked |
| Dependencies | Phase 01B |
| Status | Not started |

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
| Objective | Create Django 5.2 project, PostgreSQL, Docker Compose, settings layout, Pytest skeleton |
| Inputs | ADRs; environment strategy |
| Outputs | Runnable local foundation without business modules |
| Approval gate | Technical review of settings/security defaults |
| Branch naming | `feature/phase-02-django-foundation` |
| Exit criteria | App boots locally; DB migrations empty/base OK; no invented business data |
| Dependencies | Phase 00; hosting decisions as needed for non-local later |

## Phase 03 — Accounts and scoped RBAC

| Field | Content |
| --- | --- |
| Objective | Named accounts, roles, deny-by-default policies, audit hooks for authz |
| Inputs | Security baseline |
| Outputs | `accounts` module; auth tests |
| Approval gate | Security-focused PR review |
| Branch naming | `feature/phase-03-accounts-rbac` |
| Exit criteria | AuthZ tests pass; shared accounts prohibited |
| Dependencies | Phase 02 |

## Phase 04 — Organization hierarchy and shifts

| Field | Content |
| --- | --- |
| Objective | Model approved org hierarchy and shift constructs |
| Inputs | Confirmed hierarchy and shift evidence |
| Outputs | `organizations` (+ shift support as designed) |
| Approval gate | Business confirmation of hierarchy |
| Branch naming | `feature/phase-04-organizations-shifts` |
| Exit criteria | Scoped queries work; no invented sites |
| Dependencies | Phase 03; ASM-004/005/006 progress |

## Phase 05 — Master data, instruments and training

| Field | Content |
| --- | --- |
| Objective | Minimal masters for MVP templates; instruments/training as approved |
| Inputs | Master data evidence |
| Outputs | `master_data`, `instruments`, `training` as needed |
| Approval gate | Data owner review |
| Branch naming | `feature/phase-05-master-data` |
| Exit criteria | Only evidenced entities loaded |
| Dependencies | Phase 04 |

## Phase 06 — Checklist templates

| Field | Content |
| --- | --- |
| Objective | Versioned templates for two approved checklist types |
| Inputs | Approved forms |
| Outputs | `checklists` module |
| Approval gate | QA content approval |
| Branch naming | `feature/phase-06-checklist-templates` |
| Exit criteria | Two templates only unless expansion approved |
| Dependencies | Phase 05; TEMPLATE evidence |

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

## Phase 08 — Operator online recording

| Field | Content |
| --- | --- |
| Objective | Online submission UX and record services |
| Inputs | Figma operator screens; templates |
| Outputs | `records` submit path; operator UI |
| Approval gate | Operator UAT sample |
| Branch naming | `feature/phase-08-operator-recording` |
| Exit criteria | Sinhala-capable MVP flows; submit immutability |
| Dependencies | Phase 07; Phase 01 progress |

## Phase 09 — Supervisor checking and amendments

| Field | Content |
| --- | --- |
| Objective | Check workflow and amendment history |
| Inputs | SoD rules |
| Outputs | `reviews`; amendment services |
| Approval gate | QA/operations workflow review |
| Branch naming | `feature/phase-09-supervisor-review` |
| Exit criteria | SoD tests pass; before/after history stored |
| Dependencies | Phase 08 |

## Phase 10 — QA verification

| Field | Content |
| --- | --- |
| Objective | QA verify path with deterministic critical rules hooks |
| Inputs | QA rules evidence |
| Outputs | `quality` verification services/UI |
| Approval gate | QA owner |
| Branch naming | `feature/phase-10-qa-verification` |
| Exit criteria | Verify path tested; no AI final decisions |
| Dependencies | Phase 09 |

## Phase 11 — Evidence storage

| Field | Content |
| --- | --- |
| Objective | MinIO/S3 evidence upload and controlled access |
| Inputs | Security baseline; volume assumptions |
| Outputs | `evidence` module |
| Approval gate | IT security review of access patterns |
| Branch naming | `feature/phase-11-evidence-storage` |
| Exit criteria | No DB BLOBs; signed URL pattern |
| Dependencies | Phase 08+ (can start in parallel after foundation) |

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

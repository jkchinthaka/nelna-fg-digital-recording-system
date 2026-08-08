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
| Current DB platform | **PostgreSQL** (authoritative; ADR-002). Redis for cache/Celery. **No MongoDB** in architecture or Compose |
| Current deployment | **Local / developer Docker Compose only**. No staging/UAT/production deployment recorded |
| Production readiness | **NOT claimed** |
| FG-QA-001 | Project-proposed **DRAFT** only — **NOT APPROVED** for production; not auto-published |
| Phase 10A QA foundation | **IMPLEMENTED** on `main` at baseline SHA above |
| Phase 10A Docker full validation | **NOT confirmed complete** in this governance pass (prior Docker Desktop engine failures reported; re-validation remains outstanding) |
| Business role mappings (recorder / Supervisor / QA) | **NOT BUSINESS APPROVED** — permissions exist unassigned / mapping docs open |
| Segregation of duties | **EVIDENCE REQUIRED** — not invented in code as Nelna policy |
| Offline / PWA | **NOT IMPLEMENTED** (ADR-003 direction only) |
| ERP / Bileeta connector | **NOT IMPLEMENTED** — contract docs only |

---

## Implemented Django apps (code on `main`)

| App | Phase units | Status labels |
| --- | --- | --- |
| `core` | 02+ | IMPLEMENTED |
| `accounts` | 03 | IMPLEMENTED · Phase 03 **Approved with conditions** (not production-configured) |
| `organizations` (incl. Shift) | 03 + 04A/04B | IMPLEMENTED · official org/site/dept/shift values **EVIDENCE REQUIRED** |
| `access_control` | 03 | IMPLEMENTED · no seeded business roles |
| `security_audit` | 03–10A | IMPLEMENTED |
| `master_data` (FG Product) | 05A/05B | IMPLEMENTED · MASTER-001 **EVIDENCE REQUIRED** |
| `checklists` | 06A–06D (+ 06E docs) | IMPLEMENTED · FG-QA-001 **NOT BUSINESS APPROVED** |
| `scheduling` | 07A/07B | IMPLEMENTED · real batch generation **BLOCKED** |
| `recording` | 08A/08B + 09B | IMPLEMENTED · production recording **BLOCKED** |
| `reviews` | 09A | IMPLEMENTED · production Supervisor review **BLOCKED** |
| `quality` | 10A | IMPLEMENTED · production QA **BLOCKED**; no ERP/warehouse/dispatch side effects |

Not started (by MODULE_MAP): `instruments`, `training`, `evidence`, `nonconformance`, `capa`, `loading`, `dispatch`, `notifications`, `reports`, `integrations`, `ai_assistance`.

---

## Technical completion by phase (evidence)

| Phase | Technical code/docs | Business / production |
| --- | --- | --- |
| 00 Discovery | Complete | Governance living |
| 01A–01C Design | Complete; 01C deferred Sinhala condition | Design approvals recorded; DEBT-01C-R-NOTO **open** |
| 02 Foundation | Complete | Approved with conditions |
| 03 Accounts/RBAC | Complete | Approved with conditions; no seeded users/orgs/roles |
| 04A/04B Shift | Complete | Official Shift values unresolved (ASM-005/006) |
| 05A/05B FG Product | Complete | MASTER-001 unresolved |
| 06A–06E Checklist definition | Complete (06E provisional docs) | TEMPLATE / FG-QA-001 approval unresolved |
| 07A/07B Scheduling foundation | Complete | Real generation blocked (batch source, applicability, roles) |
| 08A/08B Recording/submit | Complete | Production recording blocked |
| 09A/09B Supervisor review + correction | Complete | Production review/correction blocked |
| 10A QA disposition | Complete (manual RELEASE/HOLD/REJECT only) | Production QA blocked; post-QA workflows not started |
| 10B+ Post-QA operational | Not started | EVIDENCE REQUIRED |
| 11–21 Later roadmap | Not started | N/A |

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
| Instruments / training / evidence modules | Not started | Later MVP completeness |

---

## Business blockers

1. FG-QA-001 final content approval and publish policy
2. Official Organization / Site / Department values (ASM-004)
3. Official Shift names/codes/times (ASM-005/006)
4. Official Product catalogue and specification limits (MASTER-001 / ASM-001)
5. Recorder / Supervisor / QA business-role mapping
6. Segregation-of-duties policy evidence
7. Product / Site / Shift / Department applicability rules
8. Checklist effective-version policy beyond explicit version FK
9. RELEASE / HOLD / REJECT operational meaning and downstream authority

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

---

## Recommended next engineering focus (not authorization)

1. Complete Phase 10A Docker/host validation when Docker engine is healthy (**no new business features**).
2. Drive APPROVAL_REGISTER items with named owners (especially FG-QA-001, mappings, batch source).
3. Do **not** start Phase 11+ operational features until owners prioritize and evidence gates allow.

**Production readiness is not claimed by this document.**

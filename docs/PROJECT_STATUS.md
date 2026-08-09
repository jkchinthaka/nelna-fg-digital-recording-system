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
| FG-QA-001 | Project-proposed **DRAFT** only — **NOT APPROVED** for production; not auto-published |
| Phase 10A QA foundation | **IMPLEMENTED** on `main` at baseline SHA above |
| Phase 10A Docker full validation | **NOT confirmed complete** in this governance pass (prior Docker Desktop engine failures reported; re-validation remains outstanding) |
| Business role mappings (recorder / Supervisor / QA) | **NOT BUSINESS APPROVED** — Phase 03C technical governance exists; permissions unassigned; mapping tables empty |
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
| `access_control` | 03 + **03C** | IMPLEMENTED · RoleTemplate + permission catalogue + governance services; **no** seeded business roles; **PHASE 03C BUSINESS ROLE APPROVAL PENDING** |
| `security_audit` | 03–10A | IMPLEMENTED |
| `master_data` (FG Product) | 05A/05B/05C | IMPLEMENTED foundation · MASTER-001 **EVIDENCE REQUIRED** (catalogue not received) |
| `instruments` | 05D | IMPLEMENTED foundation · unseeded equipment + calibration; intervals/overdue policy **EVIDENCE REQUIRED** |
| `training` | 05E | IMPLEMENTED foundation · unseeded competency records; gate OFF by default; matrix/WARN-BLOCK **EVIDENCE REQUIRED** (APR-042) |
| `checklists` | 06A–06D (+ 06E–06G docs) | IMPLEMENTED · FG-QA-001 **NOT BUSINESS APPROVED**; Engine v2 **designed** (ADR-019); real forms **NOT RECEIVED**; optional `requires_equipment_reference` (05D) |
| `scheduling` | 07A/07B | IMPLEMENTED · real batch generation **BLOCKED** |
| `recording` | 08A/08B + 09B | IMPLEMENTED · production recording **BLOCKED** |
| `reviews` | 09A | IMPLEMENTED · production Supervisor review **BLOCKED** |
| `quality` | 10A | IMPLEMENTED · production QA **BLOCKED**; no ERP/warehouse/dispatch side effects |

Not started (by MODULE_MAP): `evidence`, `nonconformance`, `capa`, `loading`, `dispatch`, `notifications`, `reports`, `integrations`, `ai_assistance`.

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
| 06F Real form discovery framework | Docs complete (templates + registers) | Inventory **NOT RECEIVED**; no forms APPROVED FOR DIGITALIZATION |
| 06G Checklist Engine v2 design | ADR-019 + 06H–06M split | Design complete; evidence still required for business values |
| 06H Repeating / sample foundation | Schema + recording/snapshot/correction/Supervisor/QA render | Technical foundation complete; **no invented sample counts**; not BUSINESS APPROVED / not UAT |
| 06I Calculated fields | Closed operators + Decimal + frozen snapshot context | Technical foundation; **no business formulas seeded**; not BUSINESS APPROVED |
| 06J Conditional rules | VISIBLE_IF / REQUIRED_IF / EVIDENCE_REQUIRED_IF (fail-closed evidence stub) | Technical foundation; **no seeded predicates**; not BUSINESS APPROVED |
| 06K Item evaluation | Explicit bounds/choice/option/calculated rules → PASS/FAIL/WARN/NOT_EVALUATED | Technical foundation; **PASS≠RELEASE / FAIL≠HOLD/REJECT**; never auto-creates QAReview; **no seeded limits**; not BUSINESS APPROVED |
| 06L Control-point metadata | `control_point_class` + `criticality` + frozen `control_point_context` | Technical schema on `main`; default NONE; **no invented CCP/OPRP**; metadata ≠ disposition; **APR-027 / ASM-002 still EVIDENCE REQUIRED**; not BUSINESS APPROVED |
| 06M Measurement semantics | `decimal_precision` + `rounding_mode` + unit catalog + inclusivity + frozen `measurement_context` | Technical schema on `main`; Decimal-safe; **no product limits seeded**; informational bounds ≠ disposition; not BUSINESS APPROVED |
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
| Evidence module | Not started | Later MVP completeness |

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
9. Checklist effective-version policy beyond explicit version FK
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

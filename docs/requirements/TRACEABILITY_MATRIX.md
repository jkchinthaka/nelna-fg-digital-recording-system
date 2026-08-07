# Traceability Matrix

**Document status:** Living matrix — no testing claimed complete for business UAT
**Phase:** Phase 04A/04B Shift + Phase 05A/05B FG Product + Phase 06A/06B/06C/06D Checklists · MASTER-001 / TEMPLATE / real-data UAT still blocked
**Last updated:** 2026-08-07

## Rules

- Rows may contain placeholders.
- **Do not** mark testing, UAT, or approval as complete until evidence exists.
- Design, test, and UAT references will be filled in later phases.
- Phase 02/03 rows cover **technical foundation** only — not business-rule approval of FG operations.
- Preserve roadmap numbering: master data = Phase 05; checklists = Phase 06; recording = Phase 08; review = Phase 09; evidence = Phase 11.

| Requirement ID | Business owner | Risk | Planned module | Design reference | Test reference | UAT reference | Evidence | Approval status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FOUND-001 | Project / IT (TBC) | Unreproducible builds | config / tooling | PHASE_02_TECHNICAL_BASELINE; ADR-004 | CI lock + sync gates | TBC | pyproject.toml; uv.lock | Phase 02 approved with conditions |
| FOUND-002 | Project / IT (TBC) | Env/secret misuse | config.settings | ADR-005; SECURE_CONFIGURATION | Production fail-closed CI | TBC | config/settings/production.py | Phase 02 approved with conditions |
| FOUND-003 | Project / IT (TBC) | Local/CI drift | operations | LOCAL_DEVELOPMENT; DOCKER_DEVELOPMENT | compose config + image build CI | TBC | compose.yaml; Dockerfile | Phase 02 approved with conditions |
| FOUND-004 | Project / IT (TBC) | Weak quality baseline | testing | TESTING_GUIDE; CI_QUALITY_GATES | pytest/ruff/mypy/bandit CI | TBC | .github/workflows/ci.yml | Phase 02 approved with conditions |
| FOUND-005 | UX / IT (TBC) | Premature PWA / CDN / fonts | frontend | FRONTEND_FOUNDATION; DEBT-01C-R-NOTO | Token/CSS build CI | TBC | package.json; static/src/css | Proposed — Noto **not** verified |
| AUTH-001 | IT owner (TBC) | Shared accounts / weak auth | accounts | ADR-006; AUTHENTICATION_AND_ACCESS_CONTROL | PHASE_03_TEST_PLAN | TBC | apps/accounts | Phase 03 approved with conditions (merged) |
| AUTH-002 | IT owner (TBC) | Credential exposure | accounts | ADR-006; SECURITY_EVENT_CATALOGUE | PHASE_03_TEST_PLAN | TBC | Django hashers; audit exclusions | Phase 03 approved with conditions (merged) |
| AUTH-003 | IT / QA (TBC) | Accountability loss | accounts / security_audit | SECURITY_EVENT_CATALOGUE | PHASE_03_TEST_PLAN | TBC | SecurityAuditEvent | Phase 03 approved with conditions (merged) |
| AUTH-004 | IT owner (TBC) | Session abuse | accounts | AUTHENTICATION_AND_ACCESS_CONTROL | PHASE_03_TEST_PLAN | TBC | Session rotation; lockout | Phase 03 approved with conditions (merged) |
| ORG-001 | Business owner (TBC) | Wrong scoping | organizations | ADR-007; MODULE_MAP | PHASE_03_TEST_PLAN | TBC | Organization/Site/Department (foundation); naming confirmation = ASM-004 | Phase 03 models merged; hierarchy naming still DECISION REQUIRED |
| ORG-003 | Operations / Business (TBC) | Incorrect Shift definitions | organizations | ADR-008; PHASE_04_SHIFT_PROVISIONAL_CONFIGURATION; SHIFT_MANAGEMENT_UI | PHASE_04A_TEST_PLAN; shift UI tests | TBC | Configurable unseeded Shift foundation (04A) + management UI (04B); official values = ASM-005/006 | Phase 04A/04B technical delivery — ASM-005/006 remain unresolved; no production authorization |
| RBAC-001 | IT / QA (TBC) | Cross-scope access | access_control | ADR-007 | PHASE_03_TEST_PLAN | TBC | ScopedRoleAssignment | Phase 03 approved with conditions (merged) |
| ORG-002 | IT / Business (TBC) | Privilege bleed | organizations / accounts | TBC | TBC | TBC | Security baseline | Proposed |
| MASTER-001 | Business / QA (TBC) | Incorrect master data | master_data | ADR-009; PHASE_05_FG_PRODUCT_PROVISIONAL_CONFIGURATION; FG_PRODUCT_MANAGEMENT_UI; MASTER_001_FG_PRODUCT_EVIDENCE_INTAKE | PHASE_05A_TEST_PLAN; FG Product authz hardening tests | TBC | Configurable unseeded FG Product foundation (05A); authz hardening (05B); official catalogue = MASTER-001 | Phase 05A/05B technical work — MASTER-001 remains EVIDENCE REQUIRED; schema expansion and real loading blocked; no production authorization |
| MASTER-002 | QA / IT (TBC) | Untracked changes | master_data / audit | TBC | TBC | TBC | Audit policy | Proposed |
| TEMPLATE-001 | Business / QA (TBC) | Uncontrolled forms | checklists | ADR-010; PHASE_06_CHECKLIST_PROVISIONAL_CONFIGURATION; CHECKLIST_DEFINITION_MANAGEMENT_UI; TEMPLATE_001_CHECKLIST_EVIDENCE_INTAKE; FG_QA_001_DRAFT_V0_1; FG_QA_001_DRAFT_LOADING; FG_QA_001_INTERNAL_VALIDATION_CHECKLIST; PHASE_06E_FG_QA_001_PROVISIONAL_WORKFLOW | PHASE_06A_TEST_PLAN; checklist governance tests; PHASE_06C_TEST_PLAN; PHASE_06D_TEST_PLAN | TBC | Configurable unseeded definition engine (06A/06B); provisional response schema (06C); explicit DRAFT loader (06D); owner-directed provisional workflow (06E — not formal sign-off); FG-QA-001 = PROJECT-PROPOSED DRAFT — VALIDATION REQUIRED | Phase 06A–06E technical/docs — TEMPLATE not fully approved; no production authorization |
| TEMPLATE-002 | QA / Business (TBC) | Scope creep | checklists | MVP scope; ADR-010 | TBC | TBC | MVP scope | Proposed — 06A engine only; no invented form expansion |
| TEMPLATE-003 | QA owner (TBC) | Invented limits | checklists | ADR-010; ASM-001 | PHASE_06A_TEST_PLAN | TBC | Controlled docs — EVIDENCE REQUIRED | Proposed — limits excluded from 06A |
| TASK-001 | Operations / FG (TBC) | Missed tasks | scheduling | ADR-011; ADR-012; PHASE_06E; PHASE_07_PRODUCTION_READINESS_GATE; PRODUCTION_BATCH_SOURCE_CONTRACT | PHASE_07A_TEST_PLAN; PHASE_07B_TEST_PLAN | TBC | Per-batch provisional trigger; ChecklistTask + batch_reference; source contract without ERP invention | 07A/07B — real generation blocked |
| TASK-002 | IT / Security (TBC) | Unauthorized task view | scheduling | ADR-011; ADR-012 | PHASE_07A_TEST_PLAN; PHASE_07B_TEST_PLAN | TBC | Org-scoped view/manage; record permission separate and unassigned | Phase 07B |
| RECORD-001 | FG Operations (TBC) | Incomplete digital adoption | recording | ADR-013; ADR-014; CHECKLIST_RECORDING_UI; CHECKLIST_SUBMISSION_UI; PHASE_08_RECORDING_READINESS_GATE; CHECKLIST_RECORDER_ROLE_MAPPING | PHASE_08A_TEST_PLAN; PHASE_08B_TEST_PLAN | TBC | 08A draft + 08B immutable submit; production gated | 08A/08B technical — production BLOCKED |
| RECORD-002 | Business / QA (TBC) | Slow / unusable UX | recording (UI) | CHECKLIST_RECORDING_UI; CHECKLIST_SUBMISSION_UI; FIGMA_PLAN | PHASE_08A_TEST_PLAN; PHASE_08B_TEST_PLAN | TBC | Save Draft + Submit confirm + submitted read-only | 08A/08B technical |
| RECORD-003 | QA owner (TBC) | Silent alteration | recording | ADR-014 | PHASE_08B_TEST_PLAN | TBC | Submission snapshots immutable; no overwrite of Submission #1 | 08B technical |
| RECORD-004 | Business / IT (TBC) | ERP outage blocks floor | recording / integrations | TBC | TBC | TBC | Constitution | Proposed |
| REVIEW-001 | FG / Operations (TBC) | Weak checking | reviews | ADR-015; PHASE_09_SUPERVISOR_REVIEW_READINESS_GATE; SUPERVISOR_REVIEW_UI; CHECKLIST_RECORDER_ROLE_MAPPING | PHASE_09A_TEST_PLAN | TBC | Immutable SupervisorReview on ChecklistSubmission (09A) | Phase 09A technical — production review blocked; SoD EVIDENCE REQUIRED |
| REVIEW-002 | QA / IT (TBC) | SoD bypass | reviews / accounts | ADR-015; CHECKLIST_RECORDER_ROLE_MAPPING | PHASE_09A_TEST_PLAN | TBC | SoD rule documented open; architecture keeps submitted_by ≠ reviewed_by fields | Proposed — not enforced in 09A |
| REVIEW-003 | QA owner (TBC) | Lost correction history | records / reviews | ADR-014; ADR-015 | PHASE_09A_TEST_PLAN | TBC | Submission #1 immutable; RETURNED does not overwrite; 09B creates #2 later | Phase 09A records return decision only |
| QA-001 | QA owner (TBC) | Incomplete verification | quality / reviews | ADR-015 (contract only) | TBC — Phase 10 | TBC | Future QA eligibility: SupervisorReview(APPROVED) | Proposed — not implemented |
| QA-002 | QA owner (TBC) | Non-deterministic critical handling | quality | TBC | TBC | TBC | AI safety policy | Proposed |
| EVIDENCE-001 | IT owner (TBC) | DB bloat / backup failure | evidence | TBC — Phase 11 | TBC | TBC | ADR-002 | Proposed |
| EVIDENCE-002 | QA / IT (TBC) | Unauthorized evidence access | evidence / audit | TBC | TBC | TBC | Security baseline | Proposed |
| CAPA-001 | QA owner (TBC) | Scope creep | nonconformance / capa | Roadmap Phase 12 | N/A (MVP out) | N/A | MVP scope | Proposed |
| CAPA-002 | QA owner (TBC) | AI misuse | capa / ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |
| LOADING-001 | Dispatch / QA (TBC) | Scope creep | loading / dispatch | Roadmap Phase 13 | N/A (MVP out) | N/A | Roadmap | Proposed |
| LOADING-002 | QA / Dispatch (TBC) | AI misuse | loading / ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |
| OFFLINE-001 | IT / Operations (TBC) | Premature offline | (PWA client) | Roadmap Phase 14 | N/A (MVP out) | N/A | MVP scope | Proposed |
| OFFLINE-002 | IT / QA (TBC) | Duplicate sync | records / sync | TBC — Phase 14 | TBC | TBC | Risk register | Proposed |
| REPORT-001 | QA / Internal audit (TBC) | Missing audit pack | reports / audit | TBC — Phase 16 | TBC | TBC | MVP scope | Proposed |
| REPORT-002 | Management (TBC) | Scope creep | reports | Roadmap | N/A (later) | N/A | Roadmap | Proposed |
| AUDIT-001 | QA / IT (TBC) | Missing audit events | audit | TBC | TBC | TBC | Constitution | Proposed |
| AUDIT-002 | QA owner (TBC) | History loss | audit / records | TBC | TBC | TBC | Constitution | Proposed |
| ERP-001 | IT / Business (TBC) | False ERP dependency | integrations | MVP scope | TBC | TBC | MVP scope | Proposed |
| ERP-002 | IT owner (TBC) | Data corruption / vendor risk | integrations | Security baseline | TBC | TBC | Security baseline | Proposed |
| SECURITY-001 | IT / Security (TBC) | Privilege escalation | accounts / policies | Security baseline | TBC | TBC | Security baseline | Proposed |
| SECURITY-002 | IT owner (TBC) | Secret leak | operations | Security baseline; SECURE_CONFIGURATION | detect-secrets; CI | TBC | Repo policy | Proposed |
| SECURITY-003 | Project owner (TBC) | Premature production | operations | Release process | TBC | TBC | Workflow rules | Proposed |
| OPERATIONS-001 | IT owner (TBC) | Env confusion | operations | Environment strategy; CONFIGURATION_REFERENCE | TBC | TBC | Environment strategy | Proposed |
| OPERATIONS-002 | QA owner (TBC) | Unsafe fallback | operations | BC draft | TBC | TBC | BC draft — not approved | Proposed |
| AI-001 | Project owner (TBC) | Distraction / scope | ai_assistance | MVP scope | N/A (MVP out) | N/A | MVP scope | Proposed |
| AI-002 | QA / IT (TBC) | AI hallucination in critical path | ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |
| AI-003 | IT / Business (TBC) | AI outage blocks floor | ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |

**Testing status:** Foundation automated tests run in CI / Docker; business UAT is **not** started. Phase 02 and Phase 03 approval forms are **signed with conditions**. Authentication UI polish merged via PR #8. Phase 04 scope reconciliation merged via PR #10. Phase **04A/04B** Shift foundation + UI; Phase **05A/05B** FG Product foundation + authz hardening; Phase **06A/06B/06C/06D** checklist definition/versioning + governance hardening + provisional response schema / FG-QA-001 draft proposal + explicit DRAFT loader — MASTER-001 / TEMPLATE / ASM-001 remain evidence-required (TEMPLATE-001 = PROJECT-PROPOSED DRAFT — VALIDATION REQUIRED). ASM-004/005/006 remain partially unresolved. DEBT-01C-R-NOTO remains **open**. No scheduling/recording modules started. No deployment authorization.

# Traceability Matrix

**Document status:** Initial placeholder matrix — no testing claimed complete  
**Phase:** 00 — Discovery and governance  
**Last updated:** 2026-08-04

## Rules

- Rows may contain placeholders.
- **Do not** mark testing, UAT, or approval as complete until evidence exists.
- Design, test, and UAT references will be filled in later phases.

| Requirement ID | Business owner | Risk | Planned module | Design reference | Test reference | UAT reference | Evidence | Approval status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUTH-001 | IT owner (TBC) | Shared accounts / weak auth | accounts | TBC — Phase 01/03 | TBC | TBC | Security baseline | Proposed |
| AUTH-002 | IT owner (TBC) | Credential exposure | accounts | TBC | TBC | TBC | Django defaults | Proposed |
| AUTH-003 | IT / QA (TBC) | Accountability loss | accounts | TBC | TBC | TBC | Security baseline | Proposed |
| AUTH-004 | IT owner (TBC) | Session abuse | accounts | TBC | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| ORG-001 | Business owner (TBC) | Wrong scoping | organizations | TBC — Phase 01/04 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| ORG-002 | IT / Business (TBC) | Privilege bleed | organizations / accounts | TBC | TBC | TBC | Security baseline | Proposed |
| MASTER-001 | Business / QA (TBC) | Incorrect master data | master_data | TBC — Phase 05 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| MASTER-002 | QA / IT (TBC) | Untracked changes | master_data / audit | TBC | TBC | TBC | Audit policy | Proposed |
| TEMPLATE-001 | QA owner (TBC) | Uncontrolled forms | checklists | TBC — Phase 06 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| TEMPLATE-002 | QA / Business (TBC) | Scope creep | checklists | MVP scope | TBC | TBC | MVP scope | Proposed |
| TEMPLATE-003 | QA owner (TBC) | Invented limits | checklists | TBC | TBC | TBC | Controlled docs — EVIDENCE REQUIRED | Proposed |
| TASK-001 | Operations / FG (TBC) | Missed tasks | tasks / schedules | TBC — Phase 07 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| TASK-002 | IT / Security (TBC) | Unauthorized task view | tasks | TBC | TBC | TBC | Security baseline | Proposed |
| RECORD-001 | FG Operations (TBC) | Incomplete digital adoption | records | TBC — Phase 08 | TBC | TBC | MVP scope | Proposed |
| RECORD-002 | Business / QA (TBC) | Slow / unusable UX | records (UI) | FIGMA_PLAN | TBC | TBC | Constitution | Proposed |
| RECORD-003 | QA owner (TBC) | Silent alteration | records | TBC — Phase 09 | TBC | TBC | Architecture principles | Proposed |
| RECORD-004 | Business / IT (TBC) | ERP outage blocks floor | records / integrations | TBC | TBC | TBC | Constitution | Proposed |
| REVIEW-001 | FG / Operations (TBC) | Weak checking | reviews | TBC — Phase 09 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
| REVIEW-002 | QA / IT (TBC) | SoD bypass | reviews / accounts | TBC | TBC | TBC | Security baseline | Proposed |
| REVIEW-003 | QA owner (TBC) | Lost correction history | records / reviews | TBC | TBC | TBC | Architecture principles | Proposed |
| QA-001 | QA owner (TBC) | Incomplete verification | quality / reviews | TBC — Phase 10 | TBC | TBC | EVIDENCE REQUIRED | Proposed |
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
| SECURITY-002 | IT owner (TBC) | Secret leak | operations | Security baseline | TBC | TBC | Repo policy | Proposed |
| SECURITY-003 | Project owner (TBC) | Premature production | operations | Release process | TBC | TBC | Workflow rules | Proposed |
| OPERATIONS-001 | IT owner (TBC) | Env confusion | operations | Environment strategy | TBC | TBC | Environment strategy | Proposed |
| OPERATIONS-002 | QA owner (TBC) | Unsafe fallback | operations | BC draft | TBC | TBC | BC draft — not approved | Proposed |
| AI-001 | Project owner (TBC) | Distraction / scope | ai_assistance | MVP scope | N/A (MVP out) | N/A | MVP scope | Proposed |
| AI-002 | QA / IT (TBC) | AI hallucination in critical path | ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |
| AI-003 | IT / Business (TBC) | AI outage blocks floor | ai_assistance | AI safety policy | TBC | TBC | AI safety policy | Proposed |

**Testing status:** Not started. No UAT references are complete.

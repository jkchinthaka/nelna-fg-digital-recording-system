# Design Decision Register

**Document status:** Living register for design decisions  
**Phase:** 01A  
**Last updated:** 2026-08-04

Statuses: Proposed · Accepted (design direction) · Deferred · Rejected · Superseded  
None of the Proposed rows are stakeholder-approved until the Phase 01A approval form is signed.

| ID | Decision | Status | Owner | Reason | Alternatives | Impact | Evidence | Review trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DES-001 | One responsive PWA; no native app in initial phases | Accepted (aligns ADR-003) | Project owner (TBC) | Single codebase | Native dual apps | Mobile = responsive web | ADR-003 | Pilot PWA failure |
| DES-002 | Operator bottom nav ≤5 items; proposed Home/Tasks/Scan/Records/More | Proposed | Business/UX (TBC) | Cognitive load | 4 items without Scan | IA + Figma frames | INFORMATION_ARCHITECTURE | Usability test |
| DES-003 | Failures-first supervisor queue ordering | Proposed | QA/Operations (TBC) | Safety visibility | Strict FIFO | Queue sort | USER_JOURNEYS J3 | Ops review |
| DES-004 | Never label pre-ACK local data as submitted | Accepted (design direction) | QA/IT (TBC) | Prevent false assurance | “Pending submit” ambiguity | Copy + sync UI | CONTENT guide; J6 | Any sync wording change |
| DES-005 | Critical status = text + icon + pattern (colour optional) | Accepted (design direction) | UX (TBC) | A11y | Colour-only | All status components | ACCESSIBILITY doc | Design system 01B |
| DES-006 | Touch targets min 48px; operator primary 48–56px | Proposed | UX (TBC) | Gloves/factory | 44px only | Wireframes/components | ACCESSIBILITY | Device pilot |
| DES-007 | Sinhala-first operator labels; EN admin terms | Proposed | Business (TBC) | Constitution + ASM-008 | Full bilingual always | Content + layout | CONTENT guide | Language survey |
| DES-008 | Employee code login field label | Proposed | IT (TBC) | Factory familiarity | Username/email | Login wireframe | J1 | Identity source decision |
| DES-009 | Loading dual-authorization override | Deferred / Decision required | QA (TBC) | High risk | Single override | Journey 5 | WORKFLOW_STATE_MAP | Loading phase design |
| DES-010 | Scan in operator primary nav | Proposed / optional | Operations (TBC) | Speed | Manual only | Nav IA | IA-01 | Evidence of scan need |
| DES-011 | Management dashboard limited to 4–6 KPIs | Proposed | Management (TBC) | Actionability | Large KPI walls | MG screens | IA | KPI workshop |
| DES-012 | NC/CAPA in QA nav as Later-labeled | Proposed | QA (TBC) | Honest roadmap | Hide until Phase 12 | QA IA | MVP_SCOPE | MVP approval |
| DES-013 | Lo-fi grayscale only in 01A; tokens in 01B | Accepted (phase plan) | Project owner (TBC) | Sequence control | Jump to hi-fi | Figma pages 04–05 stub | FIGMA_BUILD_SPEC | Start 01B |
| DES-014 | Attestation required before operator submit | Assumption | QA (TBC) | Accountability | Submit without attestation | OP-REV | J1.8 | QA policy |
| DES-015 | Date/time display format | Decision required | IT/QA (TBC) | Consistency | Locale-only | All timestamps | CONTENT guide | Locale policy |

Update this register when Phase 01A review concludes.

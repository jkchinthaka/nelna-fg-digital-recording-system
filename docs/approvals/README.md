# Approvals

Place approved charter, scope, UAT, design, and release approval records in this directory.

## Recorded approvals

| Record | Status | Date |
| --- | --- | --- |
| [PHASE_01A_DESIGN_APPROVAL.md](PHASE_01A_DESIGN_APPROVAL.md) | **Approved** as proposed design baseline | 2026-08-04 |
| [PHASE_01B_DESIGN_APPROVAL.md](PHASE_01B_DESIGN_APPROVAL.md) | **Approved with conditions** (Project Owner / Developer) | 2026-08-05 |
| [PHASE_01C_HIGH_FIDELITY_APPROVAL.md](PHASE_01C_HIGH_FIDELITY_APPROVAL.md) | **Approved with deferred condition** — Sinhala typography (DEBT-01C-R-NOTO) remains open | 2026-08-05 |
| [PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md](PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md) | **Approved with conditions** — merged via PR #5 / #6 | 2026-08-05 |
| [PHASE_03_ACCOUNTS_RBAC_APPROVAL.md](PHASE_03_ACCOUNTS_RBAC_APPROVAL.md) | **Unsigned** — Phase 03 under implementation on `feature/accounts-rbac` | — |

## Notes

- Phase 01A approval does **not** approve open Nelna operational values (limits, sites, forms, SoD matrices, etc.).
- Phase 01B and 01C approvals are Project Owner / Developer only — not QA, IT management, or other Nelna stakeholder approval.
- Phase 01C deferred condition: Noto Sans Sinhala is **not** verified; Abhaya Libre is **not** production-approved; operator UAT / pilot / production remain blocked until DEBT-01C-R-NOTO is closed with evidence.
- Phase 02 is **approved with conditions** (see form). PostgreSQL remains authoritative.
- Phase 03 is **not approved** until the Phase 03 form is signed. Branch: `feature/accounts-rbac`.
- Do not treat other draft documents as approved unless listed here with a completed approval form.
- Do not publish the Figma library without final design-system review.

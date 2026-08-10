# Phase 21 — Production release & handover package

**Hard rule:** Direct commits on `main` ≠ production deployment.  
**Hard rule:** Do not invent go-live PASS, production smoke PASS, or business signatures.

| Document | Purpose |
| --- | --- |
| [RELEASE_GATE.md](RELEASE_GATE.md) | Hard prerequisite / approval checklist |
| [PRODUCTION_ENVIRONMENT.md](PRODUCTION_ENVIRONMENT.md) | Prod stack verification (empty until approved) |
| [ENVIRONMENT_SEPARATION.md](ENVIRONMENT_SEPARATION.md) | Local / test / UAT / prod separation |
| [PRODUCTION_DATA_LOAD.md](PRODUCTION_DATA_LOAD.md) | Approved config import checklist |
| [SECRETS_AND_VAULT.md](SECRETS_AND_VAULT.md) | Company vault custody |
| [RELEASE_PIPELINE.md](RELEASE_PIPELINE.md) | CI/CD + explicit prod gate |
| [DATABASE_CHANGE_CONTROL.md](DATABASE_CHANGE_CONTROL.md) | Backup-before-migrate / rollback |
| [PRODUCTION_SMOKE_TEST.md](PRODUCTION_SMOKE_TEST.md) | Controlled smoke (NOT EXECUTED) |
| [SUPPORT_MODEL.md](SUPPORT_MODEL.md) | Owner / severity / escalation |
| [HANDOVER_CHECKLIST.md](HANDOVER_CHECKLIST.md) | Docs + bus-factor access |
| [PAPER_DECOMMISSION.md](PAPER_DECOMMISSION.md) | Paper remains until formal approval |
| [POST_GO_LIVE_MONITORING.md](POST_GO_LIVE_MONITORING.md) | Post-release watch list |
| [PHASE_21_FINAL_REPORT.md](PHASE_21_FINAL_REPORT.md) | Go / no-go |
| [../business/PHASE_21_PRODUCTION_RELEASE.md](../business/PHASE_21_PRODUCTION_RELEASE.md) | Phase narrative |

## Decision

**STOP** — Phase 20 UAT/pilot not passed. See final report.

## STATUS: PHASE 21 GO-LIVE BLOCKED

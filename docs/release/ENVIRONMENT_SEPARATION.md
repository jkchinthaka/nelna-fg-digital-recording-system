# Phase 21 — Environment separation

Strategy baseline: [../operations/ENVIRONMENT_STRATEGY.md](../operations/ENVIRONMENT_STRATEGY.md)

| Environment | Exists today? | Separation status |
| --- | --- | --- |
| Local | Yes (Compose) | OK for developers |
| Test / CI | Yes (GitHub Actions / ephemeral) | OK |
| Staging / UAT | **No hosted evidence** | **GAP** — APR-021 / ASM-015 |
| Production | **No** | **GAP** — gate CLOSED |

## Rules (in force)

- No test credentials or synthetic fixtures in production.
- No production secrets in git or developer `.env` committed to GitHub.
- Promote only via explicit production gate ([RELEASE_PIPELINE.md](RELEASE_PIPELINE.md)).

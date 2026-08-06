# Nelna FG Digital Recording System

Secure, auditable Finished Goods digital recording delivered as a modular Django monolith with a responsive web UI. Longer-term direction includes an installable PWA (ADR-003); **PWA is not implemented yet**.

## Project purpose

Provide named-account, scoped-role digital recording, checking, verification, evidence capture, and audit export for Finished Goods operations — using approved business rules only, with Sinhala-capable operator experiences, without requiring ERP availability for factory-floor recording.

## Current phase

**Phase 04 — Organization hierarchy and shifts** (next numbered phase; Shift coding blocked until ASM-004 / ASM-005 / ASM-006 evidence)

| Phase | Status |
| --- | --- |
| Phase 00 — Discovery and governance | Merged to `main` |
| Phase 01A — Journeys, IA, lo-fi specification | **Approved** as proposed design baseline (2026-08-04) |
| Phase 01B — Design tokens and components | **Approved with conditions** (2026-08-05) |
| Phase 01C — High-fidelity MVP screens and prototype | **Approved with deferred condition** — DEBT-01C-R-NOTO remains open |
| Phase 02 — Django/PostgreSQL foundation | **Approved with conditions** and merged (PR #5 / #6) |
| Phase 03 — Accounts / auth / scoped RBAC | **Approved with conditions** and merged (PR #7) |
| Authentication UI polish | **Merged** (PR #8) — English foundation screens; not Sinhala UI approval |
| Phase 04 — Organization hierarchy and shifts | **Next** — hierarchy confirmation + Shift only after ASM evidence |
| Phase 05+ — FG master data, checklists, recording, review, evidence | **Not started** |

**Numbering rule:** Preserve roadmap phase numbers. FG master data is Phase 05; checklist definitions are Phase 06; recording is Phase 08; supervisor review is Phase 09; evidence is Phase 11. Do **not** label those as Phase 04.

**Deferred Sinhala condition:** Noto Sans Sinhala is **not** finally verified. Operator Sinhala UAT, pilot, and production remain **blocked** until DEBT-01C-R-NOTO is closed with evidence. Abhaya Libre is **not** the approved production font. No font binaries; no verification claim.

## Approved architecture (technical direction)

| Area | Direction |
| --- | --- |
| Backend | Python 3.13.14, Django 5.2.16 LTS |
| Architecture | Modular monolith |
| Database | PostgreSQL 17.10 (+ JSONB where appropriate) |
| Cache / jobs | Redis 7.4.10, Celery 5.6.3 |
| Dependency mgmt | uv 0.11.29 (`pyproject.toml` + `uv.lock`) |
| UI | Django Templates, HTMX 2.0.10, Tailwind 4.3.3; **no Alpine**; **no CDN**; **no PWA yet** |
| Evidence | MinIO locally later; S3-compatible object storage in production (Phase 11) |
| Local dev | Docker Compose (`compose.yaml`); host publish ports via `COMPOSE_POSTGRES_HOST_PORT` / `COMPOSE_REDIS_HOST_PORT` (defaults 5433 / 6380) |
| Identity | Employee-code session authentication; scoped RBAC; security audit events — **no seeded users/orgs/roles** |
| Organization scope | Organization, Site, Department models exist (Phase 03); Shift deferred to Phase 04 after evidence |
| Tests | Pytest (+ pytest-django / pytest-cov) via host `uv` **or** Compose profile `test`; Playwright later |
| Docker images | `web` = lean runtime (no pytest); `test` = dedicated validation image |
| CI | GitHub Actions quality gates (host + Docker test path) |
| Design | Figma Professional (design phases) |
| AI | Optional local assistance later; never final FS/QA/loading/CAPA/access decisions |

Exact pins: [docs/architecture/PHASE_02_TECHNICAL_BASELINE.md](docs/architecture/PHASE_02_TECHNICAL_BASELINE.md).

## Repository status

| Item | Status |
| --- | --- |
| Greenfield repository | Yes |
| Application foundation | Present — accounts, organizations, access_control, security_audit |
| FG operational modules | **Not started** |
| Phase 02 approval | **Approved with conditions** (merged) |
| Phase 03 approval | **Approved with conditions** (merged) |
| Authentication UI polish | Merged via PR #8; local and Docker validation passed; GitHub Actions evidence was unavailable during a GitHub Actions incident — **do not claim the missing CI check passed** |
| Production readiness | **Not claimed** |
| Secrets in repo | None intended; do not add any |

## Quick start (local)

Prefer `C:\Projects\nelna-fg-digital-recording-system` on Windows (not OneDrive). See [docs/operations/LOCAL_DEVELOPMENT.md](docs/operations/LOCAL_DEVELOPMENT.md).

```powershell
Copy-Item .env.example .env
uv sync --locked
npm ci
npm run build
docker compose up -d postgres redis
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8000
```

Docker validation (dedicated `test` service — not `web`):

```powershell
docker compose up -d postgres redis
docker compose --profile test build test
docker compose --profile test run --rm test pytest --cov=apps --cov=config --cov-report=term-missing --cov-fail-under=80
docker compose down --volumes
```

Do **not** use `docker compose run --rm web pytest` — pytest is intentionally absent from the runtime image. See [docs/operations/DOCKER_DEVELOPMENT.md](docs/operations/DOCKER_DEVELOPMENT.md).

## Documentation map (selected)

| Document | Path |
| --- | --- |
| Roadmap (governing phase numbering) | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Module map | [docs/architecture/MODULE_MAP.md](docs/architecture/MODULE_MAP.md) |
| Assumption register | [docs/business/ASSUMPTION_REGISTER.md](docs/business/ASSUMPTION_REGISTER.md) |
| Phase 02 technical baseline | [docs/architecture/PHASE_02_TECHNICAL_BASELINE.md](docs/architecture/PHASE_02_TECHNICAL_BASELINE.md) |
| Local development | [docs/operations/LOCAL_DEVELOPMENT.md](docs/operations/LOCAL_DEVELOPMENT.md) |
| Docker development | [docs/operations/DOCKER_DEVELOPMENT.md](docs/operations/DOCKER_DEVELOPMENT.md) |
| Testing guide | [docs/testing/TESTING_GUIDE.md](docs/testing/TESTING_GUIDE.md) |
| Approvals index | [docs/approvals/](docs/approvals/) |
| Design debt register | [docs/design/DESIGN_DEBT_REGISTER.md](docs/design/DESIGN_DEBT_REGISTER.md) |
| Authentication UI polish note | [docs/design/AUTHENTICATION_UI_POLISH.md](docs/design/AUTHENTICATION_UI_POLISH.md) |

Earlier discovery, requirements, design, and ADR documents remain under `docs/`.

## Contribution workflow

1. Work on a phase-specific branch (never commit directly to `main`).
2. Open a pull request for manual review.
3. Do not force-push to `main` or merge without human review.
4. Do not invent Nelna operational values; use assumption/evidence gates.
5. Do not deploy to production without explicit written approval.
6. Follow version-controlled Cursor rules under `.cursor/rules/`.

## Next action

1. Obtain owner evidence for **ASM-004**, **ASM-005**, and **ASM-006** before implementing Shift.
2. Keep **DEBT-01C-R-NOTO** open until Noto Sans Sinhala is evidenced (do not treat Abhaya Libre as production).
3. Do **not** start FG master data, checklist, recording, review, or evidence modules as Phase 04.
4. Do **not** start operator UAT, pilot, or production until the Sinhala debt is closed.
5. Do **not** seed real users, organizations, shifts, or business roles.
6. Do **not** deploy to production without separate explicit written approval.

## Important

This project is **not production-ready**. Production readiness requires UAT, restore testing, security review, and owner approval.

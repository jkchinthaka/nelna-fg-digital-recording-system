# Nelna FG Digital Recording System

Secure, auditable Finished Goods digital recording delivered as a modular Django monolith with a responsive web UI. Longer-term direction includes an installable PWA (ADR-003); **PWA is not implemented in Phase 02**.

## Project purpose

Provide named-account, scoped-role digital recording, checking, verification, evidence capture, and audit export for Finished Goods operations — using approved business rules only, with Sinhala-capable operator experiences, without requiring ERP availability for factory-floor recording.

## Current phase

**Phase 03 — Accounts, authentication and scoped RBAC** (**under implementation / pending approval**)

| Phase | Status |
| --- | --- |
| Phase 00 — Discovery and governance | Merged to `main` |
| Phase 01A — Journeys, IA, lo-fi specification | **Approved** as proposed design baseline (2026-08-04) |
| Phase 01B — Design tokens and components | **Approved with conditions** (2026-08-05) |
| Phase 01C — High-fidelity MVP screens and prototype | **Approved with deferred condition** — DEBT-01C-R-NOTO remains open |
| Phase 02 — Django/PostgreSQL foundation | **Approved with conditions** and merged (PR #5 / #6) |
| Phase 03 — Accounts / auth / scoped RBAC | **Under implementation** on `feature/accounts-rbac` — **not approved** until [PHASE_03_ACCOUNTS_RBAC_APPROVAL.md](docs/approvals/PHASE_03_ACCOUNTS_RBAC_APPROVAL.md) is signed |

**Deferred Sinhala condition:** Noto Sans Sinhala is **not** finally verified. Operator Sinhala UAT, pilot, and production remain **blocked** until DEBT-01C-R-NOTO is closed with evidence. Abhaya Libre is **not** the approved production font. No font binaries; no verification claim. Phase 03 backend auth work may proceed while the debt remains open.

## Approved architecture (technical direction)

| Area | Direction |
| --- | --- |
| Backend | Python 3.13.14, Django 5.2.16 LTS |
| Architecture | Modular monolith |
| Database | PostgreSQL 17.10 (+ JSONB where appropriate) |
| Cache / jobs | Redis 7.4.10, Celery 5.6.3 |
| Dependency mgmt | uv 0.11.29 (`pyproject.toml` + `uv.lock`) |
| UI (Phase 02) | Django Templates, HTMX 2.0.10, Tailwind 4.3.3; **no Alpine**; **no CDN**; **no PWA yet** |
| Evidence | MinIO locally later; S3-compatible object storage in production (not Phase 02 scope) |
| Local dev | Docker Compose (`compose.yaml`); host publish ports via `COMPOSE_POSTGRES_HOST_PORT` / `COMPOSE_REDIS_HOST_PORT` (defaults 5433 / 6380) |
| Identity (Phase 03) | Employee-code session authentication; scoped RBAC; security audit events — **no seeded users/orgs/roles** |
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
| Application foundation code | Present on Phase 02 branch (scaffold — not business MVP) |
| Phase 02 approval | **Approved with conditions** (merged) |
| Phase 03 approval | **Unsigned** — under implementation on `feature/accounts-rbac` |
| Production readiness | **Not claimed** |
| Secrets in repo | None intended; do not add any |
| Previous repository code | Not used |

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
| Phase 02 technical baseline | [docs/architecture/PHASE_02_TECHNICAL_BASELINE.md](docs/architecture/PHASE_02_TECHNICAL_BASELINE.md) |
| ADR-004 dependency management | [docs/architecture/ADR-004-PYTHON-DEPENDENCY-MANAGEMENT.md](docs/architecture/ADR-004-PYTHON-DEPENDENCY-MANAGEMENT.md) |
| ADR-005 settings / environments | [docs/architecture/ADR-005-DJANGO-SETTINGS-AND-ENVIRONMENTS.md](docs/architecture/ADR-005-DJANGO-SETTINGS-AND-ENVIRONMENTS.md) |
| Local development | [docs/operations/LOCAL_DEVELOPMENT.md](docs/operations/LOCAL_DEVELOPMENT.md) |
| Docker development | [docs/operations/DOCKER_DEVELOPMENT.md](docs/operations/DOCKER_DEVELOPMENT.md) |
| Configuration reference | [docs/operations/CONFIGURATION_REFERENCE.md](docs/operations/CONFIGURATION_REFERENCE.md) |
| Logging / observability | [docs/operations/LOGGING_AND_OBSERVABILITY.md](docs/operations/LOGGING_AND_OBSERVABILITY.md) |
| Testing guide | [docs/testing/TESTING_GUIDE.md](docs/testing/TESTING_GUIDE.md) |
| CI quality gates | [docs/testing/CI_QUALITY_GATES.md](docs/testing/CI_QUALITY_GATES.md) |
| Secure configuration | [docs/security/SECURE_CONFIGURATION.md](docs/security/SECURE_CONFIGURATION.md) |
| Frontend foundation | [docs/frontend/FRONTEND_FOUNDATION.md](docs/frontend/FRONTEND_FOUNDATION.md) |
| Phase 02 approval form | [docs/approvals/PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md](docs/approvals/PHASE_02_TECHNICAL_FOUNDATION_APPROVAL.md) |
| Roadmap | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Approvals index | [docs/approvals/](docs/approvals/) |
| Design debt register | [docs/design/DESIGN_DEBT_REGISTER.md](docs/design/DESIGN_DEBT_REGISTER.md) |

Earlier discovery, requirements, design, and ADR-001–003 documents remain under `docs/`.

## Contribution workflow

1. Work on a phase-specific branch (never commit directly to `main`).
2. Open a pull request for manual review.
3. Do not force-push to `main` or merge without human review.
4. Do not invent Nelna operational values; use assumption/evidence gates.
5. Do not deploy to production without explicit written approval.
6. Follow version-controlled Cursor rules under `.cursor/rules/`.

## Next action

1. Complete Phase 03 review on `feature/accounts-rbac` and obtain signature on [PHASE_03_ACCOUNTS_RBAC_APPROVAL.md](docs/approvals/PHASE_03_ACCOUNTS_RBAC_APPROVAL.md).
2. Keep **DEBT-01C-R-NOTO** open until Noto Sans Sinhala is evidenced (do not treat Abhaya Libre as production).
3. Do **not** start operator UAT, pilot, or production until the Sinhala debt is closed.
4. Do **not** seed real users, organizations, or business roles.
5. Do **not** deploy to production without separate explicit written approval.

## Important

This project is **not production-ready**. Production readiness requires UAT, restore testing, security review, and owner approval.

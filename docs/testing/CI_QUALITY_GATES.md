# CI Quality Gates

**Document status:** Phase 02 foundation guidance
**Branch:** `foundation/django-postgresql`
**Last updated:** 2026-08-05

## Workflow

File: `.github/workflows/ci.yml`
Triggers: pull requests and pushes to `main`.

Services: `postgres:17.10-alpine3.23`, `redis:7.4.10-alpine3.21` (CI ports 5432 / 6379).

Toolchain setup: uv **0.11.29**, Python **3.13.14**, Node **24.18.0**.

## Gates (ordered)

| Gate | Command / check |
| --- | --- |
| Lockfile | `uv lock --check` |
| Sync | `uv sync --locked --all-groups` |
| Ruff lint | `uv run ruff check .` |
| Ruff format | `uv run ruff format --check .` |
| mypy | `uv run mypy apps config scripts` |
| Template lint | `uv run djlint templates --check` |
| JSON/YAML validate | Scripted parse of JSON + key YAML files |
| Frontend | `npm ci` + `npm run build` + design token `--check` |
| Pytest + coverage | fail-under **80** |
| Migrations | `makemigrations --check` |
| Django check | `manage.py check` |
| Production fail-closed | Import production settings without secret must fail |
| Deploy check | `manage.py check --deploy` with CI placeholders |
| Bandit | `uv run bandit -r apps config scripts` |
| pip-audit | `uv run pip-audit` |
| Compose | `docker compose config` |
| Image | `docker build --target runtime` |

## Pre-commit (local)

`.pre-commit-config.yaml` mirrors subset: whitespace/EOF, YAML/JSON, large files, private key detect, ruff, djlint, detect-secrets.

Pinned locally via project: pre-commit **4.5.1**; ruff hook **v0.15.0**; djlint **v1.36.4**.

## Non-claims

- Green CI does **not** mean Phase 02 is approved or production-ready.
- CI does not close DEBT-01C-R-NOTO.
- Security scans are baseline hygiene, not a completed security assessment.

## Related

- [TESTING_GUIDE.md](TESTING_GUIDE.md)
- [SECURE_CONFIGURATION.md](../security/SECURE_CONFIGURATION.md)
- [PHASE_02_TECHNICAL_BASELINE.md](../architecture/PHASE_02_TECHNICAL_BASELINE.md)

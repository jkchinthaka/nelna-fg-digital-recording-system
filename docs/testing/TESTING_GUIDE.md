# Testing Guide

**Document status:** Phase 02 foundation guidance
**Branch:** `foundation/django-postgresql`
**Last updated:** 2026-08-05

## Tooling (pinned)

| Tool | Version |
| --- | --- |
| pytest | 9.0.2 |
| pytest-django | 4.11.1 |
| pytest-cov | 7.0.0 |

Settings module for tests: `config.settings.test` (`DJANGO_SETTINGS_MODULE` / `tool.pytest.ini_options`).

## Running tests

From project root (with Postgres/Redis available as required by markers):

```powershell
uv run pytest
uv run pytest --cov=apps --cov=config --cov-report=term-missing --cov-fail-under=80
```

Coverage fail-under **80** is enforced in `pyproject.toml` and CI.

## Layout and markers

| Location | Role |
| --- | --- |
| `tests/` | Project-level tests |
| `apps/*/tests/` | App tests |

Markers (see `pyproject.toml`):

| Marker | Meaning |
| --- | --- |
| `integration` | Requires PostgreSQL and/or Redis |
| `architecture` | Architecture boundary checks |

## What Phase 02 tests cover

- Foundation smoke / health / settings fail-closed behaviour as implemented
- Architecture and config guards where present
- No claim of UAT, browser E2E (Playwright), or business-workflow validation completeness

Playwright remains planned per [VALIDATION_STRATEGY.md](VALIDATION_STRATEGY.md); not a Phase 02 exit requirement unless later expanded.

## Local DB for tests

CI uses service containers on 5432/6379. Locally, point test env at compose-published **5433** / **6380** (or run against compose network equivalents). Use synthetic credentials only.

## Related

- [CI_QUALITY_GATES.md](CI_QUALITY_GATES.md)
- [VALIDATION_STRATEGY.md](VALIDATION_STRATEGY.md)
- [PHASE_02_TECHNICAL_BASELINE.md](../architecture/PHASE_02_TECHNICAL_BASELINE.md)

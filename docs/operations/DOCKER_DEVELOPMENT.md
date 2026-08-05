# Docker Development

**Document status:** Phase 02 foundation guidance
**Branch:** `foundation/django-postgresql`
**Last updated:** 2026-08-05

## Compose file

Primary file: `compose.yaml` at repository root.

| Service | Image / build | Role |
| --- | --- | --- |
| `postgres` | `postgres:17.10-alpine3.23` | Operational database |
| `redis` | `redis:7.4.10-alpine3.21` | Cache and Celery broker |
| `web` | Build `Dockerfile` target `runtime` | Django `runserver` (local compose override command) |
| `celery-worker` | Same image | Celery worker |

Volumes: `postgres_data` for local persistence.

## Host vs container ports

| Service | Host bind (default) | Internal |
| --- | --- | --- |
| PostgreSQL | `127.0.0.1:${POSTGRES_PORT:-5433}` → 5432 | 5432 |
| Redis | `127.0.0.1:${REDIS_PORT:-6380}` → 6379 | 6379 |
| Web | `127.0.0.1:${WEB_PORT:-8000}` → 8000 | 8000 |

Defaults **5433** / **6380** reduce Windows conflicts with local 5432 / 6379 listeners. Inside the compose network, `web` and `celery-worker` always use container DNS names and internal ports (`postgres:5432`, `redis:6379`).

## Common workflows

Infra only (app on host via uv):

```powershell
docker compose up -d postgres redis
```

Full stack:

```powershell
docker compose up --build
```

Config validation:

```powershell
docker compose config
```

Stop / reset data (destructive for local volume):

```powershell
docker compose down
# optional: docker volume rm <postgres_data volume name>
```

## Dockerfile stages

| Stage | Purpose |
| --- | --- |
| `frontend-build` | Node 24.18.0 — vendor copy + Tailwind build |
| `python-deps` | uv 0.11.29 sync of locked runtime deps |
| `runtime` | Non-root user `nelna`, gunicorn default CMD, healthcheck on `/health/live/` |

Notes:

- Entrypoint does **not** auto-run migrations or create superusers.
- Runtime default settings module is `config.settings.production`; compose `web` overrides to `config.settings.local`.
- Image build is exercised in CI; that is **not** a production release approval.

## Related

- [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md)
- [SECURE_CONFIGURATION.md](../security/SECURE_CONFIGURATION.md)
- [PHASE_02_TECHNICAL_BASELINE.md](../architecture/PHASE_02_TECHNICAL_BASELINE.md)

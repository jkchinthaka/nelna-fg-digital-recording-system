# Multi-stage production-oriented image for Nelna FG foundation.
# Does not run migrations automatically. Does not create superusers.

############################
# Stage 1: frontend build
############################
FROM node:24.18.0-bookworm-slim AS frontend-build
WORKDIR /build
COPY package.json package-lock.json ./
RUN npm ci
COPY design/tokens ./design/tokens
COPY scripts/build_design_tokens.py scripts/copy_frontend_vendor_assets.js ./scripts/
COPY static/src ./static/src
# Token script needs Python only for generation in CI/local; in Docker we run via node copy + prebuilt
# Generate tokens using a temporary python if available is awkward — copy pre-generated in build context
# Prefer running token generation via node-free approach: include generated CSS from build context
COPY design/generated ./design/generated
COPY static/src/css/generated-tokens.css ./static/src/css/generated-tokens.css
RUN npm run copy:vendor && npm run build:css

############################
# Stage 2: Python deps
############################
FROM python:3.13.14-slim-bookworm AS python-deps
COPY --from=ghcr.io/astral-sh/uv:0.11.29 /uv /uvx /usr/local/bin/
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0
WORKDIR /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml uv.lock README.md ./
COPY apps ./apps
COPY config ./config
COPY manage.py ./
RUN uv sync --frozen --no-dev --no-group development --no-group testing --no-group security

############################
# Stage 3: runtime
############################
FROM python:3.13.14-slim-bookworm AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings.production \
    PATH="/app/.venv/bin:$PATH"
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq5 curl \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 10001 nelna \
    && useradd --uid 10001 --gid 10001 --create-home --shell /usr/sbin/nologin nelna

COPY --from=python-deps /app/.venv /app/.venv
COPY --chown=nelna:nelna apps ./apps
COPY --chown=nelna:nelna config ./config
COPY --chown=nelna:nelna manage.py pyproject.toml uv.lock ./
COPY --chown=nelna:nelna templates ./templates
COPY --chown=nelna:nelna scripts ./scripts
COPY --chown=nelna:nelna infra/docker/entrypoint.sh /entrypoint.sh
COPY --from=frontend-build --chown=nelna:nelna /build/static/dist ./static/dist

RUN chmod +x /entrypoint.sh scripts/*.py \
    && mkdir -p staticfiles media \
    && chown -R nelna:nelna /app

USER nelna
EXPOSE 8000
STOPSIGNAL SIGTERM
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/health/live/ || exit 1

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "2"]

"""Liveness and readiness probes."""

from __future__ import annotations

from contextlib import suppress
from typing import Any

import redis
from django.conf import settings
from django.db import connection
from django.http import HttpRequest, JsonResponse


def check_postgres() -> dict[str, Any]:
    try:
        connection.ensure_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return {"name": "postgresql", "status": "ok"}
    except Exception:  # noqa: BLE001 — readiness must not leak exception details
        return {"name": "postgresql", "status": "unavailable"}


def check_redis() -> dict[str, Any]:
    client: Any = None
    try:
        client = redis.Redis.from_url(settings.REDIS_URL, socket_connect_timeout=2)
        if client.ping():
            status = {"name": "redis", "status": "ok"}
        else:
            status = {"name": "redis", "status": "unavailable"}
        return status
    except Exception:  # noqa: BLE001
        return {"name": "redis", "status": "unavailable"}
    finally:
        if client is not None:
            with suppress(Exception):
                client.close()


def liveness(_request: HttpRequest) -> JsonResponse:
    """Process-alive check — does not depend on PostgreSQL or Redis."""
    return JsonResponse(
        {
            "status": "alive",
            "service": "nelna-fg",
            "version": getattr(settings, "APP_VERSION", "unknown"),
        }
    )


def readiness(_request: HttpRequest) -> JsonResponse:
    """Dependency readiness — PostgreSQL and Redis required."""
    checks = [check_postgres(), check_redis()]
    ready = all(item["status"] == "ok" for item in checks)
    payload = {
        "status": "ready" if ready else "not_ready",
        "checks": checks,
    }
    return JsonResponse(payload, status=200 if ready else 503)

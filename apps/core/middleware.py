"""Correlation ID and request logging middleware."""

from __future__ import annotations

import re
import time
import uuid
from collections.abc import Callable
from typing import Any

import structlog
from django.conf import settings
from django.http import HttpRequest, HttpResponse

logger = structlog.get_logger(__name__)

_VALID_REQUEST_ID = re.compile(r"^[A-Za-z0-9._-]{8,128}$")
_SENSITIVE_KEYS = frozenset(
    {
        "password",
        "password1",
        "password2",
        "passwd",
        "secret",
        "token",
        "csrfmiddlewaretoken",
        "authorization",
        "cookie",
        "sessionid",
        "api_key",
        "apikey",
        "redis_url",
        "database_url",
        "secret_key",
    }
)


def _sanitize_path(path: str) -> str:
    return path.split("?", 1)[0]


def _incoming_correlation_id(request: HttpRequest) -> str:
    header_name = getattr(settings, "CORRELATION_ID_HEADER", "HTTP_X_REQUEST_ID")
    raw = request.META.get(header_name, "")
    if isinstance(raw, str) and _VALID_REQUEST_ID.fullmatch(raw.strip()):
        return raw.strip()
    return str(uuid.uuid4())


class CorrelationIdMiddleware:
    """Attach a correlation ID to the request, response, and structlog context."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        correlation_id = _incoming_correlation_id(request)
        request.correlation_id = correlation_id  # type: ignore[attr-defined]
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            correlation_id=correlation_id,
            environment=getattr(settings, "ENVIRONMENT_LABEL", "unspecified"),
            app_version=getattr(settings, "APP_VERSION", "unknown"),
        )
        response = self.get_response(request)
        header = getattr(settings, "CORRELATION_ID_RESPONSE_HEADER", "X-Request-ID")
        response[header] = correlation_id
        return response


class RequestLoggingMiddleware:
    """Log safe request metadata without secrets or connection strings."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        started = time.perf_counter()
        response = self.get_response(request)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        logger.info(
            "http_request",
            method=request.method,
            path=_sanitize_path(request.path),
            status_code=response.status_code,
            duration_ms=duration_ms,
        )
        return response


def redact_mapping(data: dict[str, Any]) -> dict[str, Any]:
    """Return a shallow copy with sensitive keys redacted."""
    redacted: dict[str, Any] = {}
    for key, value in data.items():
        if key.lower() in _SENSITIVE_KEYS:
            redacted[key] = "[REDACTED]"
        else:
            redacted[key] = value
    return redacted

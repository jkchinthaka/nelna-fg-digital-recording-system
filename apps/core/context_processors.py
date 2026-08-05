"""Template context for foundation shell."""

from __future__ import annotations

from typing import Any

from django.conf import settings
from django.http import HttpRequest


def foundation(request: HttpRequest) -> dict[str, Any]:
    return {
        "APP_VERSION": getattr(settings, "APP_VERSION", "unknown"),
        "ENVIRONMENT_LABEL": getattr(settings, "ENVIRONMENT_LABEL", "unspecified"),
        "correlation_id": getattr(request, "correlation_id", ""),
    }

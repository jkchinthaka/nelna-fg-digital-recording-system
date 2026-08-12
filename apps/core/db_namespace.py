"""FG MongoDB collection namespace helpers (same logical DB as MaintainPro).

When enabled, all FG-owned Django models use an explicit ``fg_`` collection prefix
so FG data never collides with MaintainPro Prisma collections (PascalCase names).

MaintainPro collections must never be read or written by FG code.
"""

from __future__ import annotations

from django.apps import apps
from django.conf import settings

_SKIPPED_APP_LABELS = frozenset({"mongo_poc"})


def fg_collection_name(app_label: str, model_name: str) -> str:
    """Default FG namespaced collection: fg_{app_label}_{model_name}."""
    prefix = getattr(settings, "FG_COLLECTION_PREFIX", "fg_")
    return f"{prefix}{app_label}_{model_name}"


def apply_fg_collection_namespace() -> int:
    """Patch ``model._meta.db_table`` at runtime when namespace mode is enabled.

    Returns the number of models patched. Idempotent.
    """
    if not getattr(settings, "FG_COLLECTION_NAMESPACE_ENABLED", False):
        return 0

    prefix = getattr(settings, "FG_COLLECTION_PREFIX", "fg_")
    patched = 0

    for model in apps.get_models(include_auto_created=True):
        if model._meta.app_label in _SKIPPED_APP_LABELS:
            continue
        current = model._meta.db_table
        if current.startswith(prefix):
            continue
        model._meta.db_table = f"{prefix}{current}"
        patched += 1

    return patched


def planned_fg_collections(*, prefix: str = "fg_") -> list[tuple[str, str, str]]:
    """Return (app_label, model_name, collection_name) without mutating models."""
    rows: list[tuple[str, str, str]] = []
    for model in apps.get_models(include_auto_created=True):
        if model._meta.proxy or model._meta.app_label in _SKIPPED_APP_LABELS:
            continue
        base = model._meta.db_table
        if not base.startswith(prefix):
            base = f"{prefix}{base}"
        rows.append((model._meta.app_label, model._meta.model_name, base))
    rows.sort(key=lambda r: r[2])
    return rows

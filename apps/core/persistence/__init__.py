"""Backend-neutral persistence / concurrency facade for Mongo migration.

Business services should prefer these helpers over scattering::

    if mongo: ...
    else: ...

PostgreSQL remains the ``main`` safety baseline until Mongo parity is proven.
"""

from __future__ import annotations

from apps.core.persistence.backend import DatabaseVendor, detect_database_vendor, is_mongodb
from apps.core.persistence.concurrency import (
    TransitionConflictError,
    TransitionIdempotentHitError,
    TransitionResult,
    cas_versioned_update,
    conditional_update,
    create_immutable_unique,
    require_conditional_update,
)
from apps.core.persistence.transactions import atomic, on_commit

__all__ = [
    "DatabaseVendor",
    "TransitionConflictError",
    "TransitionIdempotentHitError",
    "TransitionResult",
    "atomic",
    "cas_versioned_update",
    "conditional_update",
    "create_immutable_unique",
    "detect_database_vendor",
    "is_mongodb",
    "on_commit",
    "require_conditional_update",
]

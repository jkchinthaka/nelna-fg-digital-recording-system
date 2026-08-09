"""Historical safety for FG Product — soft lifecycle only."""

from __future__ import annotations

from django.core.exceptions import ValidationError

from apps.master_data.models import FGProduct


def refuse_hard_delete_fg_product(product: FGProduct) -> None:
    """
    Hard delete is never permitted for FG Product rows.

    Checklist / recording historical references use PROTECT FKs; deactivate
    (and set effective_to when applicable) instead of deleting.
    """
    raise ValidationError(
        {
            "delete": (
                "Hard delete of FG Product is not permitted. "
                "Deactivate and/or set effective_to instead."
            )
        }
    )

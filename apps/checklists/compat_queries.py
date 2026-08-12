"""Mongo-safe checklist definition loaders (no prefetch_related)."""

from __future__ import annotations

import uuid

from apps.checklists.models import ChecklistItem, ChecklistItemOption, ChecklistSection
from apps.core.persistence import attach_reverse_relation


def load_sections_with_items_and_options(version_id: uuid.UUID) -> list[ChecklistSection]:
    """Load sections → items → options using batched queries + prefetch cache."""
    sections = list(
        ChecklistSection.objects.filter(version_id=version_id).order_by("position")
    )
    if not sections:
        return sections
    items = list(
        ChecklistItem.objects.filter(section_id__in=[s.id for s in sections]).order_by(
            "section__position", "position"
        )
    )
    options = list(
        ChecklistItemOption.objects.filter(item_id__in=[i.id for i in items]).order_by(
            "position"
        )
    )
    attach_reverse_relation(items, options, fk_attr="item_id", related_name="options")
    attach_reverse_relation(sections, items, fk_attr="section_id", related_name="items")
    return sections

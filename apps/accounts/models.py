"""Minimal custom user — UUID primary key, no business identity fields yet."""

from __future__ import annotations

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Foundation user model configured before initial migrations.

    Phase 03 will add identity, authentication workflows, and scoped RBAC.
    Do not invent employee codes, sites, departments, or business roles here.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

"""Organization hierarchy foundation models — no invented Nelna operational values."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower


class Organization(models.Model):
    """Top-level organization container. Codes are synthetic until owners confirm values."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("code",)
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                name="org_organization_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(fields=["is_active"], name="org_org_active_idx"),
            models.Index(Lower("code"), name="org_org_code_lower_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.code} — {self.name}"


class Site(models.Model):
    """Site belonging to an organization. Code unique within organization (case-insensitive)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="sites",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="org_site_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(fields=["organization", "is_active"], name="org_site_org_act_idx"),
            models.Index(Lower("code"), name="org_site_code_lower_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"


class Department(models.Model):
    """
    Department belonging to an organization, optionally bound to a site.

    When site is set, it must belong to the same organization.
    Code uniqueness is scoped: within organization when site is null;
    within site when site is set.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="departments",
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.PROTECT,
        related_name="departments",
        null=True,
        blank=True,
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                condition=models.Q(site__isnull=True),
                name="org_dept_org_code_ci_uniq",
            ),
            models.UniqueConstraint(
                Lower("code"),
                "site",
                condition=models.Q(site__isnull=False),
                name="org_dept_site_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(fields=["organization", "is_active"], name="org_dept_org_act_idx"),
            models.Index(fields=["site", "is_active"], name="org_dept_site_act_idx"),
            models.Index(Lower("code"), name="org_dept_code_lower_idx"),
        ]

    def __str__(self) -> str:
        site = self.site
        if site is not None:
            return f"{self.organization.code}/{site.code}/{self.code}"
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        site = self.site
        if site is not None and site.organization_id != self.organization_id:
            raise ValidationError(
                {"site": "Site must belong to the same organization as the department."}
            )

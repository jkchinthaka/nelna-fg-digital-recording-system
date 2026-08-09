"""Applicability preview form — management tool only (Phase 07C)."""

from __future__ import annotations

from django import forms

from apps.access_control.services import organization_ids_with_permission
from apps.master_data.models import FGProduct
from apps.organizations.models import Department, Organization, Shift, Site
from apps.scheduling.applicability import VIEW_APPLICABILITY


class ApplicabilityPreviewForm(forms.Form):
    organization = forms.ModelChoiceField(queryset=Organization.objects.none())
    product = forms.ModelChoiceField(queryset=FGProduct.objects.none(), required=False)
    site = forms.ModelChoiceField(queryset=Site.objects.none(), required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.none(), required=False)
    shift = forms.ModelChoiceField(queryset=Shift.objects.none(), required=False)
    process_reference = forms.CharField(required=False, max_length=128)
    as_of = forms.DateField(required=False, input_formats=["%Y-%m-%d"])

    def __init__(self, *args, actor=None, **kwargs):  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        allowed = (
            organization_ids_with_permission(actor, VIEW_APPLICABILITY) if actor else []
        )
        self.fields["organization"].queryset = Organization.objects.filter(
            pk__in=allowed
        ).order_by("code")
        org = None
        if self.is_bound:
            org_id = self.data.get("organization")
            org = self.fields["organization"].queryset.filter(pk=org_id).first()
        elif self.initial.get("organization"):
            org = self.fields["organization"].queryset.filter(
                pk=self.initial["organization"]
            ).first()
        if org is not None:
            self.fields["product"].queryset = FGProduct.objects.filter(
                organization=org, is_active=True
            ).order_by("code")
            self.fields["site"].queryset = Site.objects.filter(
                organization=org, is_active=True
            ).order_by("code")
            self.fields["department"].queryset = Department.objects.filter(
                organization=org, is_active=True
            ).order_by("code")
            self.fields["shift"].queryset = Shift.objects.filter(
                organization=org, is_active=True
            ).order_by("code")

"""Phase 03C role governance - templates, catalogue, permission separation, audit."""

from __future__ import annotations

from datetime import timedelta

import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.utils import timezone
from tests.factories import (
    grant_role,
    make_org,
    make_permission,
    make_role_with_permission,
    make_user,
)

from apps.access_control.governance_services import (
    create_role_from_template,
    create_role_template,
    set_role_permissions,
    set_role_template_permissions,
    update_role_template,
)
from apps.access_control.models import RoleTemplateBusinessStatus, ScopedRoleAssignment
from apps.access_control.permission_catalogue import (
    CATALOGUE_BY_KEY,
    PERMISSION_CATALOGUE,
    CapabilityBucket,
    catalogue_keys,
)
from apps.access_control.services import (
    Scope,
    assign_role,
    create_role,
    revoke_role_assignment,
    user_has_permission,
)
from apps.security_audit.models import SecurityAuditEvent


REQUIRED_CATALOGUE_KEYS = frozenset(
    {
        "view_checklisttask",
        "manage_checklisttask",
        "manage_checklist",
        "record_checklisttask",
        "submit_via_record",
        "correction_via_record",
        "review_checklistsubmission",
        "qa_review_checklistsubmission",
        "manage_fgproduct",
        "audit_event_view",
        "system_administration_superuser",
    }
)


def _perm(codename: str, app_label: str = "accounts") -> Permission:
    from django.contrib.contenttypes.models import ContentType as CT

    existing = Permission.objects.filter(
        codename=codename, content_type__app_label=app_label
    ).first()
    if existing:
        return existing
    ct, _ = CT.objects.get_or_create(app_label=app_label, model=f"synthetic_{codename}")
    perm, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename=codename,
        defaults={"name": codename},
    )
    return perm


@pytest.mark.django_db
def test_permission_catalogue_non_empty_known_keys() -> None:
    assert len(PERMISSION_CATALOGUE) >= 10
    keys = catalogue_keys()
    missing = REQUIRED_CATALOGUE_KEYS - keys
    assert not missing, f"missing catalogue keys: {missing}"
    assert CATALOGUE_BY_KEY["record_checklisttask"].bucket == CapabilityBucket.RECORD
    assert (
        CATALOGUE_BY_KEY["review_checklistsubmission"].bucket == CapabilityBucket.SUPERVISOR_REVIEW
    )
    assert CATALOGUE_BY_KEY["qa_review_checklistsubmission"].bucket == CapabilityBucket.QA_REVIEW


@pytest.mark.django_db
def test_role_template_create_proposed_set_permissions_create_role() -> None:
    actor = make_user(employee_code="TST03C01", is_staff=True)
    template = create_role_template(
        actor=actor,
        code="tmpl_rec_demo",
        name="Demo recorder template",
        description="Synthetic - not Nelna approved",
    )
    assert template.business_status == RoleTemplateBusinessStatus.PROPOSED

    p_record = _perm("record_checklisttask", "scheduling")
    set_role_template_permissions(
        actor=actor,
        template_id=template.id,
        permission_ids=[p_record.id],
    )
    template.refresh_from_db()
    assert template.permissions.filter(pk=p_record.id).exists()

    role = create_role_from_template(
        actor=actor,
        template_id=template.id,
        role_code="ROLE_FROM_TMPL_1",
        role_name="Role from template 1",
    )
    assert role.permissions.filter(pk=p_record.id).exists()
    assert not ScopedRoleAssignment.objects.filter(role=role).exists()

    assert SecurityAuditEvent.objects.filter(event_type="ROLE_TEMPLATE_CREATED").exists()
    assert SecurityAuditEvent.objects.filter(event_type="ROLE_TEMPLATE_PERMISSIONS_SET").exists()
    assert SecurityAuditEvent.objects.filter(
        event_type="ROLE_PERMISSIONS_SET",
        metadata__user_assigned=False,
    ).exists()


@pytest.mark.django_db
def test_owner_approved_requires_evidence_reference() -> None:
    actor = make_user(employee_code="TST03C02")
    with pytest.raises(ValidationError):
        create_role_template(
            actor=actor,
            code="tmpl_bad_approved",
            name="Bad",
            business_status=RoleTemplateBusinessStatus.OWNER_APPROVED,
            evidence_reference="",
        )

    template = create_role_template(
        actor=actor,
        code="tmpl_pending",
        name="Pending",
        business_status=RoleTemplateBusinessStatus.PENDING_OWNER_APPROVAL,
    )
    with pytest.raises(ValidationError):
        update_role_template(
            actor=actor,
            template_id=template.id,
            business_status=RoleTemplateBusinessStatus.OWNER_APPROVED,
            evidence_reference="   ",
        )

    updated = update_role_template(
        actor=actor,
        template_id=template.id,
        business_status=RoleTemplateBusinessStatus.OWNER_APPROVED,
        evidence_reference="docs/governance/APPROVAL_REGISTER.md#APR-040",
    )
    assert updated.business_status == RoleTemplateBusinessStatus.OWNER_APPROVED


@pytest.mark.django_db
def test_create_role_from_proposed_template_not_company_approved_metadata() -> None:
    actor = make_user(employee_code="TST03C03")
    template = create_role_template(actor=actor, code="tmpl_prop", name="Proposed only")
    create_role_from_template(
        actor=actor,
        template_id=template.id,
        role_code="ROLE_PROP_COPY",
        role_name="Copy",
    )
    evt = SecurityAuditEvent.objects.filter(event_type="ROLE_PERMISSIONS_SET").latest("created_at")
    assert evt.metadata.get("treated_as_company_approved") is False
    assert evt.metadata.get("source_template_business_status") == "PROPOSED"


@pytest.mark.django_db
def test_cross_org_denial() -> None:
    user = make_user(employee_code="TST03C04")
    org_a = make_org(code="ORG03CA")
    org_b = make_org(code="ORG03CB")
    role = make_role_with_permission(code="ROLE03C_CROSS")
    grant_role(user, role, organization=org_a)
    assert user_has_permission(
        user, "accounts.test_permission", scope=Scope(organization_id=org_a.id)
    )
    assert not user_has_permission(
        user, "accounts.test_permission", scope=Scope(organization_id=org_b.id)
    )


@pytest.mark.django_db
def test_inactive_and_expired_assignment_grants_nothing() -> None:
    user = make_user(employee_code="TST03C05")
    role = make_role_with_permission(code="ROLE03C_EXP")
    now = timezone.now()
    expired = assign_role(
        user=user,
        role=role,
        valid_from=now - timedelta(days=5),
        valid_until=now - timedelta(hours=1),
    )
    assert not user_has_permission(user, "accounts.test_permission")

    expired.valid_until = now + timedelta(days=1)
    expired.save(update_fields=["valid_until", "updated_at"])
    assert user_has_permission(user, "accounts.test_permission")
    revoke_role_assignment(expired, actor=user)
    assert not user_has_permission(user, "accounts.test_permission")


@pytest.mark.django_db
def test_manage_does_not_imply_record() -> None:
    user = make_user(employee_code="TST03C06")
    p_manage = _perm("manage_checklisttask", "scheduling")
    role = create_role(code="ROLE03C_MANAGE", name="Manage only", permissions=[p_manage])
    grant_role(user, role)
    assert user_has_permission(user, "scheduling.manage_checklisttask")
    assert not user_has_permission(user, "scheduling.record_checklisttask")


@pytest.mark.django_db
def test_record_does_not_imply_supervisor_or_qa() -> None:
    user = make_user(employee_code="TST03C07")
    p_record = _perm("record_checklisttask", "scheduling")
    role = create_role(code="ROLE03C_REC", name="Record only", permissions=[p_record])
    grant_role(user, role)
    assert user_has_permission(user, "scheduling.record_checklisttask")
    assert not user_has_permission(user, "reviews.review_checklistsubmission")
    assert not user_has_permission(user, "quality.qa_review_checklistsubmission")


@pytest.mark.django_db
def test_supervisor_does_not_imply_qa() -> None:
    user = make_user(employee_code="TST03C08")
    p_rev = _perm("review_checklistsubmission", "reviews")
    role = create_role(code="ROLE03C_SUP", name="Supervisor only", permissions=[p_rev])
    grant_role(user, role)
    assert user_has_permission(user, "reviews.review_checklistsubmission")
    assert not user_has_permission(user, "quality.qa_review_checklistsubmission")
    assert not user_has_permission(user, "scheduling.record_checklisttask")


@pytest.mark.django_db
def test_role_assign_revoke_audit_events() -> None:
    actor = make_user(employee_code="TST03C09")
    subject = make_user(employee_code="TST03C10")
    role = make_role_with_permission(code="ROLE03C_AUD")
    assignment = assign_role(user=subject, role=role, assigned_by=actor)
    assert SecurityAuditEvent.objects.filter(
        event_type="ROLE_ASSIGNED", subject_user=subject
    ).exists()
    revoke_role_assignment(assignment, actor=actor)
    assert SecurityAuditEvent.objects.filter(
        event_type="ROLE_REVOKED", subject_user=subject
    ).exists()


@pytest.mark.django_db
def test_template_permission_change_audited() -> None:
    actor = make_user(employee_code="TST03C11")
    template = create_role_template(actor=actor, code="tmpl_aud", name="Audit tmpl")
    p1 = make_permission(codename="synth_perm_a")
    p2 = make_permission(codename="synth_perm_b")
    set_role_template_permissions(actor=actor, template_id=template.id, permission_ids=[p1.id])
    set_role_template_permissions(
        actor=actor, template_id=template.id, permission_ids=[p1.id, p2.id]
    )
    events = SecurityAuditEvent.objects.filter(event_type="ROLE_TEMPLATE_PERMISSIONS_SET")
    assert events.count() >= 2


@pytest.mark.django_db
def test_permission_escalation_attempt_fails() -> None:
    user = make_user(employee_code="TST03C12")
    p_record = _perm("record_checklisttask", "scheduling")
    p_qa = _perm("qa_review_checklistsubmission", "quality")
    role = create_role(code="ROLE03C_ESC", name="Escalation victim", permissions=[p_record])
    grant_role(user, role)

    assert not user_has_permission(user, "quality.qa_review_checklistsubmission")

    other = create_role(code="ROLE03C_QA_ONLY", name="QA only", permissions=[p_qa])
    assert not user_has_permission(user, "quality.qa_review_checklistsubmission")
    assert other.permissions.filter(pk=p_qa.id).exists()
    assert ScopedRoleAssignment.objects.filter(user=user, role=other, is_active=True).count() == 0


@pytest.mark.django_db
def test_set_role_permissions_audited() -> None:
    actor = make_user(employee_code="TST03C13")
    role = create_role(code="ROLE03C_SETP", name="Set perms")
    p1 = make_permission(codename="synth_set_a")
    set_role_permissions(actor=actor, role_id=role.id, permission_ids=[p1.id])
    assert role.permissions.filter(pk=p1.id).exists()
    assert SecurityAuditEvent.objects.filter(
        event_type="ROLE_PERMISSIONS_SET", metadata__role_code="ROLE03C_SETP"
    ).exists()

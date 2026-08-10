"""Phase 22 — laboratory / LIMS foundation tests."""

from __future__ import annotations

import uuid
from decimal import Decimal
from typing import Any

import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied, ValidationError
from django.test import override_settings

from apps.accounts.models import User
from apps.laboratory.models import (
    LabResult,
    LabResultStatus,
    LabResultType,
    LabSample,
    LabSampleStatus,
    LabTestParameter,
)
from apps.laboratory.coa import empty_coa_payload
from apps.laboratory.policy import evaluate_batch_positive_release_gate
from apps.laboratory.selectors import latest_results_for_sample, samples_for_organization
from apps.laboratory.services import (
    amend_lab_result,
    create_lab_test,
    create_lab_test_parameter,
    create_test_method_reference,
    enter_lab_result,
    finalize_lab_result,
    record_external_lab_certificate,
    register_lab_sample,
    transition_lab_sample,
    update_positive_release_policy,
    verify_lab_result,
)
from apps.organizations.models import Organization
from apps.security_audit.models import SecurityAuditEvent
from tests.factories import grant_role, make_org, make_role_with_permission, make_user


def _perm(model: type[Any], codename: str) -> Permission:
    ct = ContentType.objects.get_for_model(model)
    permission, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename=codename,
        defaults={"name": f"Can {codename.replace('_', ' ')}"},
    )
    return permission


def _grant(user: User, org: Organization, model: type[Any], *codenames: str) -> None:
    suffix = uuid.uuid4().hex[:6].upper()
    role = make_role_with_permission(
        code=f"L{suffix}",
        name=f"Lab role {suffix}",
        permission=_perm(model, codenames[0]),
    )
    for code in codenames[1:]:
        role.permissions.add(_perm(model, code))
    grant_role(user, role, organization=org)


@pytest.mark.django_db
def test_sample_provenance_and_lifecycle() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample", "view_laboratory")
    sample = register_lab_sample(
        actor=user,
        organization=org,
        code=f"S-{uuid.uuid4().hex[:6].upper()}",
        batch_reference="BATCH-LAB-1",
        sub_lot_reference="SUB-1",
        provenance_note="manual intake",
    )
    assert sample.status == LabSampleStatus.REGISTERED
    assert sample.batch_reference == "BATCH-LAB-1"
    assert sample.organization_id == org.id
    sample = transition_lab_sample(
        actor=user, sample_id=sample.id, to_status=LabSampleStatus.RECEIVED
    )
    assert sample.status == LabSampleStatus.RECEIVED
    assert SecurityAuditEvent.objects.filter(event_type="LAB_SAMPLE_CREATED").exists()


@pytest.mark.django_db
def test_numeric_and_qualitative_results_finalize_immutable() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample", "view_laboratory")
    _grant(
        user,
        org,
        LabResult,
        "enter_labresult",
        "verify_labresult",
        "finalize_labresult",
    )
    _grant(user, org, LabTestParameter, "manage_laboratory")

    sample = register_lab_sample(
        actor=user, organization=org, code=f"S-{uuid.uuid4().hex[:6].upper()}"
    )
    method = create_test_method_reference(
        actor=user, organization=org, code="M-REF-1", title="Placeholder method"
    )
    numeric_param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P-NUM",
        name="Numeric placeholder",
        result_type=LabResultType.NUMERIC,
        unit="unit",
        method_reference=method,
    )
    qual_param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P-QUAL",
        name="Qualitative placeholder",
        result_type=LabResultType.SELECT,
        select_options=["PASS", "FAIL"],
    )
    test = create_lab_test(
        actor=user, sample_id=sample.id, code="T1", method_reference=method
    )
    num = enter_lab_result(
        actor=user,
        lab_test_id=test.id,
        parameter_id=numeric_param.id,
        numeric_value=Decimal("12.5"),
    )
    qual = enter_lab_result(
        actor=user,
        lab_test_id=test.id,
        parameter_id=qual_param.id,
        select_value="PASS",
    )
    assert num.numeric_value == Decimal("12.5")
    assert qual.select_value == "PASS"

    num = verify_lab_result(actor=user, result_id=num.id)
    num = finalize_lab_result(actor=user, result_id=num.id)
    assert num.status == LabResultStatus.FINALIZED
    assert num.is_immutable

    with pytest.raises(ValidationError):
        enter_lab_result(
            actor=user,
            lab_test_id=test.id,
            parameter_id=numeric_param.id,
            numeric_value=Decimal("99"),
        )


@pytest.mark.django_db
def test_amendment_creates_revision_chain() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample")
    _grant(
        user,
        org,
        LabResult,
        "enter_labresult",
        "verify_labresult",
        "finalize_labresult",
    )
    _grant(user, org, LabTestParameter, "manage_laboratory")
    sample = register_lab_sample(
        actor=user, organization=org, code=f"S-{uuid.uuid4().hex[:6].upper()}"
    )
    param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P1",
        name="P1",
        result_type=LabResultType.TEXT,
    )
    test = create_lab_test(actor=user, sample_id=sample.id, code="T1")
    result = enter_lab_result(
        actor=user, lab_test_id=test.id, parameter_id=param.id, text_value="initial"
    )
    result = verify_lab_result(actor=user, result_id=result.id)
    result = finalize_lab_result(actor=user, result_id=result.id)
    amended = amend_lab_result(
        actor=user,
        result_id=result.id,
        reason="Correction after review",
        text_value="corrected",
    )
    result.refresh_from_db()
    assert result.status == LabResultStatus.SUPERSEDED
    assert amended.revision_number == 2
    assert amended.previous_result_id == result.id
    assert amended.status == LabResultStatus.ENTERED
    assert amended.amendment_reason.startswith("Correction")
    assert SecurityAuditEvent.objects.filter(event_type="LAB_RESULT_AMENDED").exists()


@pytest.mark.django_db
def test_authorization_and_cross_org_denied() -> None:
    org_a = make_org(code=f"A{uuid.uuid4().hex[:6].upper()}")
    org_b = make_org(code=f"B{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    stranger = make_user(employee_code=f"S{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org_a, LabSample, "register_labsample")
    with pytest.raises(PermissionDenied):
        register_lab_sample(
            actor=stranger, organization=org_a, code=f"S-{uuid.uuid4().hex[:6].upper()}"
        )
    with pytest.raises(PermissionDenied):
        register_lab_sample(
            actor=user, organization=org_b, code=f"S-{uuid.uuid4().hex[:6].upper()}"
        )


@pytest.mark.django_db
def test_external_lab_certificate_and_positive_release_default_off(settings) -> None:
    settings.LAB_POSITIVE_RELEASE_BLOCKING_APPROVED = False
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample")
    _grant(user, org, LabResult, "enter_labresult")
    _grant(user, org, LabTestParameter, "manage_laboratory")
    sample = register_lab_sample(
        actor=user,
        organization=org,
        code=f"S-{uuid.uuid4().hex[:6].upper()}",
        batch_reference="BATCH-X",
    )
    cert = record_external_lab_certificate(
        actor=user,
        sample_id=sample.id,
        external_lab_reference="EXT-LAB-OPAQUE-1",
        certificate_reference="CERT-1",
    )
    assert cert.verification_status == "PENDING"

    gate = evaluate_batch_positive_release_gate(
        organization=org, batch_reference="BATCH-X"
    )
    assert gate.blocking is False
    assert gate.reason_code == "POLICY_DISABLED"

    update_positive_release_policy(
        actor=user, organization=org, policy_enabled=True, notes="pending QA approval"
    )
    gate2 = evaluate_batch_positive_release_gate(
        organization=org, batch_reference="BATCH-X"
    )
    assert gate2.blocking is False
    assert gate2.reason_code == "BLOCKING_NOT_APPROVED"

    with override_settings(LAB_POSITIVE_RELEASE_BLOCKING_APPROVED=True):
        gate3 = evaluate_batch_positive_release_gate(
            organization=org, batch_reference="BATCH-X"
        )
        assert gate3.blocking is True
        assert gate3.reason_code == "PENDING_LAB_RESULTS"


@pytest.mark.django_db
def test_specification_reference_optional_same_org_only() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabTestParameter, "manage_laboratory")
    param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P-SPEC",
        name="Spec-linked placeholder",
        result_type=LabResultType.NUMERIC,
    )
    assert param.bound_min is None
    assert param.bound_max is None
    assert param.specification_parameter_id is None


@pytest.mark.django_db
def test_selectors_and_coa_hook() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample")
    _grant(
        user,
        org,
        LabResult,
        "enter_labresult",
        "verify_labresult",
        "finalize_labresult",
    )
    _grant(user, org, LabTestParameter, "manage_laboratory")
    sample = register_lab_sample(
        actor=user,
        organization=org,
        code=f"S-{uuid.uuid4().hex[:6].upper()}",
        batch_reference="BATCH-SEL",
    )
    param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P-SEL",
        name="Selector param",
        result_type=LabResultType.TEXT,
    )
    test = create_lab_test(actor=user, sample_id=sample.id, code="T-SEL")
    result = enter_lab_result(
        actor=user, lab_test_id=test.id, parameter_id=param.id, text_value="ok"
    )
    result = verify_lab_result(actor=user, result_id=result.id)
    result = finalize_lab_result(actor=user, result_id=result.id)

    assert samples_for_organization(org.id).filter(id=sample.id).exists()
    latest = latest_results_for_sample(sample.id)
    assert len(latest) == 1
    assert latest[0].id == result.id

    payload = empty_coa_payload(
        organization_id=org.id,
        sample_id=sample.id,
        batch_reference="BATCH-SEL",
    )
    assert payload.advisory_only is True
    assert payload.lines == ()
    assert payload.batch_reference == "BATCH-SEL"


@pytest.mark.django_db
def test_positive_release_requirements_met_when_approved() -> None:
    org = make_org(code=f"L{uuid.uuid4().hex[:6].upper()}")
    user = make_user(employee_code=f"U{uuid.uuid4().hex[:6].upper()}")
    _grant(user, org, LabSample, "register_labsample")
    _grant(
        user,
        org,
        LabResult,
        "enter_labresult",
        "verify_labresult",
        "finalize_labresult",
    )
    _grant(user, org, LabTestParameter, "manage_laboratory")
    sample = register_lab_sample(
        actor=user,
        organization=org,
        code=f"S-{uuid.uuid4().hex[:6].upper()}",
        batch_reference="BATCH-MET",
    )
    param = create_lab_test_parameter(
        actor=user,
        organization=org,
        code="P-MET",
        name="Met param",
        result_type=LabResultType.TEXT,
    )
    test = create_lab_test(actor=user, sample_id=sample.id, code="T-MET")
    result = enter_lab_result(
        actor=user, lab_test_id=test.id, parameter_id=param.id, text_value="ok"
    )
    result = verify_lab_result(actor=user, result_id=result.id)
    finalize_lab_result(actor=user, result_id=result.id)
    update_positive_release_policy(actor=user, organization=org, policy_enabled=True)

    with override_settings(LAB_POSITIVE_RELEASE_BLOCKING_APPROVED=True):
        gate = evaluate_batch_positive_release_gate(
            organization=org, batch_reference="BATCH-MET"
        )
        assert gate.blocking is False
        assert gate.reason_code == "LAB_REQUIREMENTS_MET"
        assert gate.as_dict()["blocking"] is False

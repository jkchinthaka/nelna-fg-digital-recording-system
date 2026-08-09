"""Phase 06J — server-authoritative conditional checklist rules."""

from __future__ import annotations

import uuid
from typing import Any

import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from tests.factories import grant_role, make_org, make_role_with_permission, make_user

from apps.accounts.models import User
from apps.checklists.models import (
    ChecklistConditionRuleKind,
    ChecklistResponseType,
    ChecklistTemplate,
)
from apps.checklists.services import (
    add_checklist_item,
    add_checklist_section,
    create_checklist_template,
    create_checklist_version,
    publish_checklist_version,
    set_checklist_item_rule,
)
from apps.organizations.models import Organization
from apps.recording.models import ChecklistResponse, ChecklistSubmissionResponse
from apps.recording.services import (
    collect_submission_completeness,
    save_checklist_draft_responses,
    start_checklist_recording,
    submit_checklist_record,
)
from apps.scheduling.models import ChecklistTask
from apps.scheduling.services import create_batch_checklist_task


def _perm(model: type[Any], codename: str) -> Permission:
    ct = ContentType.objects.get_for_model(model)
    permission, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename=codename,
        defaults={"name": f"Can {codename.replace('_', ' ')}"},
    )
    return permission


def _manager(*, org: Organization) -> User:
    suffix = uuid.uuid4().hex[:8].upper()
    user = make_user(employee_code=f"H06JM{suffix}", is_staff=True)
    manage = _perm(ChecklistTemplate, "manage_checklist")
    role = make_role_with_permission(
        code=f"CHKM{suffix}",
        name=f"Checklist Manager {suffix}",
        permission=manage,
    )
    role.permissions.add(_perm(ChecklistTemplate, "view_checklisttemplate"))
    grant_role(user, role, organization=org)
    task_role = make_role_with_permission(
        code=f"TMGR{suffix}",
        name=f"Task Manager {suffix}",
        permission=_perm(ChecklistTask, "manage_checklisttask"),
    )
    task_role.permissions.add(_perm(ChecklistTask, "view_checklisttask"))
    grant_role(user, task_role, organization=org)
    return user


def _recorder(*, org: Organization) -> User:
    suffix = uuid.uuid4().hex[:8].upper()
    user = make_user(employee_code=f"H06JR{suffix}", is_staff=True)
    role = make_role_with_permission(
        code=f"RECR{suffix}",
        name=f"Recorder {suffix}",
        permission=_perm(ChecklistTask, "record_checklisttask"),
    )
    role.permissions.add(_perm(ChecklistTask, "view_checklisttask"))
    grant_role(user, role, organization=org)
    return user


def _published_gate(*, org: Organization, actor: User) -> dict[str, Any]:
    suffix = uuid.uuid4().hex[:6].upper()
    template = create_checklist_template(
        actor=actor, organization=org, code=f"T06J{suffix}", name=f"Cond {suffix}"
    )
    version = create_checklist_version(actor=actor, template_id=template.id)
    section = add_checklist_section(actor=actor, version_id=version.id, title="S1")
    gate = add_checklist_item(
        actor=actor,
        section_id=section.id,
        code="GATE",
        label="Gate",
        is_required=True,
        response_type=ChecklistResponseType.YES_NO,
    )
    detail = add_checklist_item(
        actor=actor,
        section_id=section.id,
        code="DETAIL",
        label="Detail",
        is_required=False,
        response_type=ChecklistResponseType.TEXT,
    )
    set_checklist_item_rule(
        actor=actor,
        target_item_id=detail.id,
        rule_kind=ChecklistConditionRuleKind.VISIBLE_IF,
        operand_item_id=gate.id,
        comparator="EQ",
        expected_text="YES",
    )
    set_checklist_item_rule(
        actor=actor,
        target_item_id=detail.id,
        rule_kind=ChecklistConditionRuleKind.REQUIRED_IF,
        operand_item_id=gate.id,
        comparator="EQ",
        expected_text="YES",
    )
    publish_checklist_version(actor=actor, version_id=version.id)
    version.refresh_from_db()
    return {"template": template, "version": version, "gate": gate, "detail": detail}


@pytest.mark.django_db
def test_hidden_bypass_rejected() -> None:
    org = make_org(code=f"O06J{uuid.uuid4().hex[:6].upper()}")
    manager = _manager(org=org)
    recorder = _recorder(org=org)
    published = _published_gate(org=org, actor=manager)
    task = create_batch_checklist_task(
        actor=manager,
        organization_id=org.id,
        checklist_template_id=published["template"].id,
        checklist_version_id=published["version"].id,
        batch_reference=f"B06J{uuid.uuid4().hex[:6]}",
    )
    record = start_checklist_recording(actor=recorder, task_id=task.id)
    save_checklist_draft_responses(
        actor=recorder,
        record_id=record.id,
        answers={str(published["gate"].id): "NO"},
    )
    with pytest.raises(ValidationError, match="not applicable"):
        save_checklist_draft_responses(
            actor=recorder,
            record_id=record.id,
            answers={str(published["detail"].id): "secret"},
        )
    assert not ChecklistResponse.objects.filter(
        checklist_record_id=record.id, checklist_item_id=published["detail"].id
    ).exists()


@pytest.mark.django_db
def test_required_if_and_submit_snapshot() -> None:
    org = make_org(code=f"O06J{uuid.uuid4().hex[:6].upper()}")
    manager = _manager(org=org)
    recorder = _recorder(org=org)
    published = _published_gate(org=org, actor=manager)
    gate = published["gate"]
    detail = published["detail"]
    task = create_batch_checklist_task(
        actor=manager,
        organization_id=org.id,
        checklist_template_id=published["template"].id,
        checklist_version_id=published["version"].id,
        batch_reference=f"B06J{uuid.uuid4().hex[:6]}",
    )
    record = start_checklist_recording(actor=recorder, task_id=task.id)
    save_checklist_draft_responses(
        actor=recorder,
        record_id=record.id,
        answers={str(gate.id): "YES"},
    )
    stats = collect_submission_completeness(record=record)
    assert detail in stats["missing_required_items"]
    with pytest.raises(ValidationError):
        submit_checklist_record(actor=recorder, record_id=record.id)

    save_checklist_draft_responses(
        actor=recorder,
        record_id=record.id,
        answers={str(gate.id): "YES", str(detail.id): "ok"},
    )
    draft = ChecklistResponse.objects.get(
        checklist_record_id=record.id, checklist_item_id=detail.id
    )
    assert draft.condition_context is not None
    assert draft.condition_context["visible"] is True
    assert draft.condition_context["required"] is True
    frozen = dict(draft.condition_context)

    submission = submit_checklist_record(actor=recorder, record_id=record.id)
    snap = ChecklistSubmissionResponse.objects.get(
        checklist_submission_id=submission.id, checklist_item_id=detail.id
    )
    assert snap.condition_context == frozen


@pytest.mark.django_db
def test_evidence_required_if_fail_closed() -> None:
    org = make_org(code=f"O06J{uuid.uuid4().hex[:6].upper()}")
    manager = _manager(org=org)
    recorder = _recorder(org=org)
    suffix = uuid.uuid4().hex[:6].upper()
    template = create_checklist_template(
        actor=manager, organization=org, code=f"TE{suffix}", name=f"Evid {suffix}"
    )
    version = create_checklist_version(actor=manager, template_id=template.id)
    section = add_checklist_section(actor=manager, version_id=version.id, title="S")
    gate = add_checklist_item(
        actor=manager,
        section_id=section.id,
        code="G",
        label="G",
        is_required=True,
        response_type=ChecklistResponseType.YES_NO,
    )
    note = add_checklist_item(
        actor=manager,
        section_id=section.id,
        code="N",
        label="N",
        is_required=False,
        response_type=ChecklistResponseType.TEXT,
    )
    set_checklist_item_rule(
        actor=manager,
        target_item_id=note.id,
        rule_kind=ChecklistConditionRuleKind.EVIDENCE_REQUIRED_IF,
        operand_item_id=gate.id,
        comparator="EQ",
        expected_text="YES",
    )
    publish_checklist_version(actor=manager, version_id=version.id)
    version.refresh_from_db()
    task = create_batch_checklist_task(
        actor=manager,
        organization_id=org.id,
        checklist_template_id=template.id,
        checklist_version_id=version.id,
        batch_reference=f"BE{uuid.uuid4().hex[:6]}",
    )
    record = start_checklist_recording(actor=recorder, task_id=task.id)
    save_checklist_draft_responses(
        actor=recorder,
        record_id=record.id,
        answers={str(gate.id): "YES", str(note.id): "x"},
    )
    with pytest.raises(ValidationError, match="evidence module"):
        submit_checklist_record(actor=recorder, record_id=record.id)

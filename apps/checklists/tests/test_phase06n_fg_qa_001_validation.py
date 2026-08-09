"""Phase 06N — FG-QA-001 evidence validation (blocked; no self-publish)."""

from __future__ import annotations

import csv
import uuid
from pathlib import Path

import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied, ValidationError
from tests.factories import grant_role, make_org, make_role_with_permission, make_user

from apps.checklists.models import (
    ChecklistItem,
    ChecklistItemKind,
    ChecklistResponseType,
    ChecklistTemplate,
    ChecklistVersion,
    ChecklistVersionStatus,
)
from apps.checklists.proposal_loader import (
    FG_QA_001_TEMPLATE_CODE,
    load_fg_qa_001_draft,
    parse_fg_qa_001_csv,
)
from apps.checklists.services import (
    add_checklist_item,
    add_checklist_section,
    create_checklist_template,
    create_checklist_version,
    publish_checklist_version,
    update_checklist_item,
)
from apps.organizations.models import Organization
from apps.recording.services import (
    save_checklist_draft_responses,
    start_checklist_recording,
    submit_checklist_record,
)
from apps.scheduling.models import ChecklistTask
from apps.scheduling.models import ChecklistTask
from apps.scheduling.services import create_batch_checklist_task
from apps.security_audit.models import SecurityAuditEvent

ROOT = Path(__file__).resolve().parents[3]
PROPOSAL_CSV = ROOT / "docs/business/proposals/FG_QA_001_DRAFT_V0_1.csv"
MATRIX_CSV = ROOT / "docs/business/templates/FG_QA_001_ITEM_VALIDATION_MATRIX.csv"
VALIDATION_DOC = ROOT / "docs/business/PHASE_06N_FG_QA_001_VALIDATION.md"
PROPOSAL_MD = ROOT / "docs/business/proposals/FG_QA_001_DRAFT_V0_1.md"
ISSUES_CSV = ROOT / "docs/business/templates/FG_QA_001_VALIDATION_ISSUES.csv"


def _perm(codename: str) -> Permission:
    ct = ContentType.objects.get_for_model(ChecklistTemplate)
    permission, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename=codename,
        defaults={"name": f"Can {codename.replace('_', ' ')}"},
    )
    return permission


def _manager(*, org: Organization):
    suffix = uuid.uuid4().hex[:6].upper()
    user = make_user(employee_code=f"N06N{suffix}", is_staff=True)
    role = make_role_with_permission(
        code=f"R06N{suffix}",
        name=f"Checklist manager 06N {suffix}",
        permission=_perm("manage_checklist"),
    )
    role.permissions.add(_perm("view_checklisttemplate"))
    grant_role(user, role, organization=org)
    ct_task = ContentType.objects.get_for_model(ChecklistTask)
    manage_task, _ = Permission.objects.get_or_create(
        content_type=ct_task,
        codename="manage_checklisttask",
        defaults={"name": "Can manage checklist task"},
    )
    view_task, _ = Permission.objects.get_or_create(
        content_type=ct_task,
        codename="view_checklisttask",
        defaults={"name": "Can view checklist task"},
    )
    task_role = make_role_with_permission(
        code=f"T06N{suffix}",
        name=f"Task manager 06N {suffix}",
        permission=manage_task,
    )
    task_role.permissions.add(view_task)
    grant_role(user, task_role, organization=org)
    return user


def _recorder(*, org: Organization):
    suffix = uuid.uuid4().hex[:6].upper()
    user = make_user(employee_code=f"N06NR{suffix}")
    ct = ContentType.objects.get_for_model(ChecklistTask)
    record_perm, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename="record_checklisttask",
        defaults={"name": "Can record checklist task"},
    )
    role = make_role_with_permission(
        code=f"R06NR{suffix}",
        name=f"Recorder 06N {suffix}",
        permission=record_perm,
    )
    grant_role(user, role, organization=org)
    return user


def test_proposal_inspection_shape_and_no_invented_limits() -> None:
    definition = parse_fg_qa_001_csv(PROPOSAL_CSV)
    assert definition.template_code == FG_QA_001_TEMPLATE_CODE
    assert len(definition.section_titles) == 7
    assert len(definition.items) == 42
    codes = [item.code for item in definition.items]
    assert codes[0] == "FGQA-01"
    assert codes[-1] == "FGQA-42"
    for item in definition.items:
        assert item.minimum_value is None
        assert item.maximum_value is None
    select_items = [item for item in definition.items if item.response_type == "SELECT"]
    assert len(select_items) == 1
    assert select_items[0].code == "FGQA-41"
    assert {opt.value for opt in select_items[0].options} == {"RELEASE", "HOLD", "REJECT"}
    numbered = {item.code for item in definition.items if item.response_type == "NUMBER"}
    assert {"FGQA-19", "FGQA-20", "FGQA-21", "FGQA-23", "FGQA-33"}.issubset(numbered)
    celsius = {item.code for item in definition.items if (item.unit or "").strip() == "°C"}
    assert celsius == {"FGQA-21", "FGQA-23", "FGQA-33"}


def test_item_validation_matrix_all_pending_decision() -> None:
    assert MATRIX_CSV.is_file()
    rows = list(csv.DictReader(MATRIX_CSV.open(encoding="utf-8")))
    assert len(rows) == 42
    assert {row["disposition"] for row in rows} == {"PENDING DECISION"}
    assert all(row["evidence"].startswith("NOT RECEIVED") for row in rows)
    assert all("no invented values" in row["limit"] for row in rows)


def test_validation_issues_and_governance_docs_blocked() -> None:
    assert list(csv.DictReader(ISSUES_CSV.open(encoding="utf-8"))) == []
    validation = VALIDATION_DOC.read_text(encoding="utf-8")
    proposal = PROPOSAL_MD.read_text(encoding="utf-8")
    assert "STATUS: PHASE 06N BLOCKED — BUSINESS APPROVAL REQUIRED" in validation
    assert "NOT APPROVED" in proposal
    assert "PROJECT-PROPOSED DRAFT" in proposal


@pytest.mark.django_db
def test_loader_creates_draft_never_publishes() -> None:
    org = make_org(code=f"O06ND{uuid.uuid4().hex[:5].upper()}")
    actor = _manager(org=org)
    result = load_fg_qa_001_draft(actor=actor, organization_id=org.id)
    assert result.status == "created"
    template = ChecklistTemplate.objects.get(organization=org, code=FG_QA_001_TEMPLATE_CODE)
    versions = list(ChecklistVersion.objects.filter(template=template))
    assert len(versions) == 1
    assert versions[0].status == ChecklistVersionStatus.DRAFT
    assert versions[0].is_draft is True
    assert ChecklistItem.objects.filter(section__version=versions[0]).count() == 42
    assert not SecurityAuditEvent.objects.filter(event_type="CHECKLIST_VERSION_PUBLISHED").exists()


@pytest.mark.django_db
def test_authorization_operator_cannot_load_or_publish() -> None:
    org = make_org(code=f"O06NA{uuid.uuid4().hex[:5].upper()}")
    manager = _manager(org=org)
    operator = make_user(employee_code=f"OP06N{uuid.uuid4().hex[:5].upper()}")
    with pytest.raises(PermissionDenied):
        load_fg_qa_001_draft(actor=operator, organization_id=org.id)
    load_fg_qa_001_draft(actor=manager, organization_id=org.id)
    version = ChecklistVersion.objects.get(
        template__organization=org, template__code=FG_QA_001_TEMPLATE_CODE
    )
    with pytest.raises(PermissionDenied):
        publish_checklist_version(actor=operator, version_id=version.id)
    version.refresh_from_db()
    assert version.status == ChecklistVersionStatus.DRAFT


@pytest.mark.django_db
def test_clone_preserves_proposal_structure_without_approving() -> None:
    org = make_org(code=f"O06NC{uuid.uuid4().hex[:5].upper()}")
    manager = _manager(org=org)
    load_fg_qa_001_draft(actor=manager, organization_id=org.id)
    source = ChecklistVersion.objects.get(
        template__organization=org, template__code=FG_QA_001_TEMPLATE_CODE
    )
    cloned = create_checklist_version(
        actor=manager, template_id=source.template_id, source_version_id=source.id
    )
    assert cloned.status == ChecklistVersionStatus.DRAFT
    assert cloned.id != source.id
    assert ChecklistItem.objects.filter(section__version=cloned).count() == 42
    assert "NOT APPROVED" in PROPOSAL_MD.read_text(encoding="utf-8")


@pytest.mark.django_db
def test_published_immutability_and_version_pinning_recording() -> None:
    """Lifecycle immutability on a technical template — not FG-QA-001 business approval."""
    org = make_org(code=f"O06NP{uuid.uuid4().hex[:5].upper()}")
    manager = _manager(org=org)
    from apps.scheduling.models import ChecklistTask as TaskModel

    task_ct = ContentType.objects.get_for_model(TaskModel)
    manage_task, _ = Permission.objects.get_or_create(
        content_type=task_ct,
        codename="manage_checklisttask",
        defaults={"name": "Can manage checklist task"},
    )
    # Attach task-manage to the same user's roles for this org.
    from apps.access_control.models import ScopedRoleAssignment

    assignment = ScopedRoleAssignment.objects.filter(
        user=manager, organization=org, is_active=True
    ).select_related("role").first()
    assert assignment is not None
    assignment.role.permissions.add(manage_task)
    recorder = _recorder(org=org)
    template = create_checklist_template(
        actor=manager,
        organization=org,
        code=f"T06NP{uuid.uuid4().hex[:5].upper()}",
        name="06N pin",
    )
    version = create_checklist_version(actor=manager, template_id=template.id)
    section = add_checklist_section(actor=manager, version_id=version.id, title="S")
    item = add_checklist_item(
        actor=manager,
        section_id=section.id,
        code="YN1",
        label="Ok?",
        is_required=True,
        response_type=ChecklistResponseType.YES_NO,
    )
    published = publish_checklist_version(actor=manager, version_id=version.id)
    assert published.status == ChecklistVersionStatus.PUBLISHED
    with pytest.raises(ValidationError):
        update_checklist_item(actor=manager, item_id=item.id, label="Changed")
    task = create_batch_checklist_task(
        actor=manager,
        organization_id=org.id,
        checklist_template_id=template.id,
        checklist_version_id=published.id,
        batch_reference=f"B06N{uuid.uuid4().hex[:4]}",
    )
    assert task.checklist_version_id == published.id
    record = start_checklist_recording(actor=recorder, task_id=task.id)
    record.refresh_from_db()
    assert record.checklist_task.checklist_version_id == published.id
    save_checklist_draft_responses(
        actor=recorder,
        record_id=record.id,
        answers={str(item.id): "YES"},
    )
    submission = submit_checklist_record(actor=recorder, record_id=record.id)
    assert submission.checklist_record_id == record.id
    # Task remains pinned to the published definition version used at generation.
    task.refresh_from_db()
    assert task.checklist_version_id == published.id
    draft = create_checklist_version(
        actor=manager, template_id=template.id, source_version_id=published.id
    )
    cloned_item = ChecklistItem.objects.get(section__version_id=draft.id, code="YN1")
    update_checklist_item(actor=manager, item_id=cloned_item.id, label="Draft-only label")
    item.refresh_from_db()
    assert item.label == "Ok?"


@pytest.mark.django_db
def test_proposal_has_no_repeating_calculated_kinds() -> None:
    org = make_org(code=f"O06NE{uuid.uuid4().hex[:5].upper()}")
    manager = _manager(org=org)
    load_fg_qa_001_draft(actor=manager, organization_id=org.id)
    fg_items = ChecklistItem.objects.filter(
        section__version__template__organization=org,
        section__version__template__code=FG_QA_001_TEMPLATE_CODE,
    )
    assert fg_items.filter(item_kind=ChecklistItemKind.REPEATING_GROUP).count() == 0
    assert fg_items.filter(item_kind=ChecklistItemKind.CALCULATED).count() == 0
    assert set(fg_items.values_list("item_kind", flat=True)) == {ChecklistItemKind.SIMPLE}

    template = create_checklist_template(
        actor=manager,
        organization=org,
        code=f"T06NE{uuid.uuid4().hex[:5].upper()}",
        name="06N engine",
    )
    version = create_checklist_version(actor=manager, template_id=template.id)
    section = add_checklist_section(actor=manager, version_id=version.id, title="Engine")
    group = add_checklist_item(
        actor=manager,
        section_id=section.id,
        code="RG1",
        label="Samples",
        is_required=False,
        response_type="",
        item_kind=ChecklistItemKind.REPEATING_GROUP,
        repeat_max=3,
    )
    assert group.is_repeating_group is True
    child = add_checklist_item(
        actor=manager,
        section_id=section.id,
        code="RG1A",
        label="Reading",
        is_required=True,
        response_type=ChecklistResponseType.NUMBER,
        parent_item_id=group.id,
    )
    assert child.parent_item_id == group.id

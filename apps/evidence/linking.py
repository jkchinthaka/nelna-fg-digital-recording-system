"""Resolve allowlisted evidence link targets and organization scope."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError

from apps.access_control.services import Scope, user_has_permission
from apps.accounts.models import User
from apps.capa.models import CorrectiveAction
from apps.evidence.models import EvidenceLinkedKind
from apps.nonconformance.models import NonConformanceRecord
from apps.quality.models import QAReview
from apps.recording.models import (
    ChecklistRecordStatus,
    ChecklistResponse,
    ChecklistSubmission,
)
from apps.reviews.models import SupervisorReview
from apps.scheduling.services import RECORD_CHECKLIST_TASK

UPLOAD_EVIDENCE = "evidence.upload_evidenceattachment"
VIEW_EVIDENCE = "evidence.view_evidenceattachment"
RETIRE_EVIDENCE = "evidence.retire_evidenceattachment"

# Parent-domain permissions used with evidence upload/view (deny by default).
REVIEW_SUBMISSION = "reviews.review_checklistsubmission"
QA_REVIEW_SUBMISSION = "quality.qa_review_checklistsubmission"
MANAGE_NCR = "nonconformance.manage_nonconformance"
MANAGE_CAPA = "capa.manage_capa"


@dataclass(frozen=True, slots=True)
class LinkedTarget:
    kind: str
    object_id: uuid.UUID
    organization_id: uuid.UUID
    linkage_immutable: bool
    obj: Any


def _scope(organization_id: uuid.UUID) -> Scope:
    return Scope(organization_id=organization_id)


def resolve_linked_target(*, kind: str, object_id: uuid.UUID) -> LinkedTarget:
    if kind not in EvidenceLinkedKind.values:
        raise ValidationError({"linked_kind": "Linked object kind is not architecture-approved."})

    if kind == EvidenceLinkedKind.CHECKLIST_RESPONSE:
        response = (
            ChecklistResponse.objects.select_related(
                "checklist_record",
                "checklist_record__organization",
            )
            .filter(pk=object_id)
            .first()
        )
        if response is None:
            raise ValidationError({"linked_object_id": "Checklist response not found."})
        record = response.checklist_record
        immutable = record.status != ChecklistRecordStatus.DRAFT
        return LinkedTarget(
            kind=kind,
            object_id=response.id,
            organization_id=record.organization_id,
            linkage_immutable=immutable,
            obj=response,
        )

    if kind == EvidenceLinkedKind.CHECKLIST_SUBMISSION:
        submission = (
            ChecklistSubmission.objects.select_related(
                "checklist_record",
                "checklist_record__organization",
            )
            .filter(pk=object_id)
            .first()
        )
        if submission is None:
            raise ValidationError({"linked_object_id": "Checklist submission not found."})
        return LinkedTarget(
            kind=kind,
            object_id=submission.id,
            organization_id=submission.checklist_record.organization_id,
            linkage_immutable=True,
            obj=submission,
        )

    if kind == EvidenceLinkedKind.SUPERVISOR_REVIEW:
        review = (
            SupervisorReview.objects.select_related(
                "organization",
                "checklist_submission",
                "checklist_submission__checklist_record",
            )
            .filter(pk=object_id)
            .first()
        )
        if review is None:
            raise ValidationError({"linked_object_id": "Supervisor review not found."})
        return LinkedTarget(
            kind=kind,
            object_id=review.id,
            organization_id=review.organization_id,
            linkage_immutable=True,
            obj=review,
        )

    if kind == EvidenceLinkedKind.QA_REVIEW:
        review = (
            QAReview.objects.select_related(
                "organization",
                "checklist_submission",
                "checklist_submission__checklist_record",
            )
            .filter(pk=object_id)
            .first()
        )
        if review is None:
            raise ValidationError({"linked_object_id": "QA review not found."})
        return LinkedTarget(
            kind=kind,
            object_id=review.id,
            organization_id=review.organization_id,
            linkage_immutable=True,
            obj=review,
        )

    if kind == EvidenceLinkedKind.NONCONFORMANCE:
        ncr = NonConformanceRecord.objects.filter(pk=object_id).first()
        if ncr is None:
            raise ValidationError({"linked_object_id": "Nonconformance record not found."})
        return LinkedTarget(
            kind=kind,
            object_id=ncr.id,
            organization_id=ncr.organization_id,
            linkage_immutable=True,
            obj=ncr,
        )

    if kind == EvidenceLinkedKind.CAPA:
        capa = CorrectiveAction.objects.filter(pk=object_id).first()
        if capa is None:
            raise ValidationError({"linked_object_id": "CAPA record not found."})
        return LinkedTarget(
            kind=kind,
            object_id=capa.id,
            organization_id=capa.organization_id,
            linkage_immutable=True,
            obj=capa,
        )

    raise ValidationError({"linked_kind": "Unsupported linked kind."})


def assert_can_upload_to_target(*, actor: User, target: LinkedTarget) -> None:
    if not user_has_permission(actor, UPLOAD_EVIDENCE, scope=_scope(target.organization_id)):
        raise PermissionDenied("Permission denied.")
    _assert_parent_access(actor=actor, target=target, for_mutate=True)


def assert_can_view_target(*, actor: User, target: LinkedTarget) -> None:
    if not user_has_permission(actor, VIEW_EVIDENCE, scope=_scope(target.organization_id)):
        # Fall back: upload grant implies view of own org evidence for Phase 11
        # only when parent access also holds — still require explicit view OR upload.
        if not user_has_permission(actor, UPLOAD_EVIDENCE, scope=_scope(target.organization_id)):
            raise PermissionDenied("Permission denied.")
    _assert_parent_access(actor=actor, target=target, for_mutate=False)


def assert_can_retire(*, actor: User, target: LinkedTarget) -> None:
    """
    Soft-retire requires explicit retire permission plus parent view access.

    Does not use for_mutate=True so immutable linkages can still be soft-retired
    under controlled policy (reason required in the retire service).
    """
    if not user_has_permission(actor, RETIRE_EVIDENCE, scope=_scope(target.organization_id)):
        raise PermissionDenied("Permission denied.")
    _assert_parent_access(actor=actor, target=target, for_mutate=False)


def _assert_parent_access(*, actor: User, target: LinkedTarget, for_mutate: bool) -> None:
    org_scope = _scope(target.organization_id)
    kind = target.kind

    if kind == EvidenceLinkedKind.CHECKLIST_RESPONSE:
        if not user_has_permission(actor, RECORD_CHECKLIST_TASK, scope=org_scope):
            raise PermissionDenied("Permission denied.")
        response: ChecklistResponse = target.obj
        if for_mutate and response.checklist_record.status != ChecklistRecordStatus.DRAFT:
            raise ValidationError(
                {
                    "linked_object_id": (
                        "Evidence cannot be attached/changed on a non-draft checklist response "
                        "without controlled retirement policy."
                    )
                }
            )
        return

    if kind == EvidenceLinkedKind.CHECKLIST_SUBMISSION:
        # Submission evidence: recorder, supervisor, or QA in org may view;
        # upload requires upload permission (already checked) + any of these.
        allowed = (
            user_has_permission(actor, RECORD_CHECKLIST_TASK, scope=org_scope)
            or user_has_permission(actor, REVIEW_SUBMISSION, scope=org_scope)
            or user_has_permission(actor, QA_REVIEW_SUBMISSION, scope=org_scope)
        )
        if not allowed:
            raise PermissionDenied("Permission denied.")
        return

    if kind == EvidenceLinkedKind.SUPERVISOR_REVIEW:
        if not user_has_permission(actor, REVIEW_SUBMISSION, scope=org_scope):
            raise PermissionDenied("Permission denied.")
        return

    if kind == EvidenceLinkedKind.QA_REVIEW:
        if not user_has_permission(actor, QA_REVIEW_SUBMISSION, scope=org_scope):
            raise PermissionDenied("Permission denied.")
        return

    if kind == EvidenceLinkedKind.NONCONFORMANCE:
        if not user_has_permission(actor, MANAGE_NCR, scope=org_scope):
            raise PermissionDenied("Permission denied.")
        return

    if kind == EvidenceLinkedKind.CAPA:
        if not user_has_permission(actor, MANAGE_CAPA, scope=org_scope):
            raise PermissionDenied("Permission denied.")
        return

    raise PermissionDenied("Permission denied.")

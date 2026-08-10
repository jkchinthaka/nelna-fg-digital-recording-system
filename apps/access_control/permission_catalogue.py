"""Technical permission catalogue — not company-approved role mappings.

Each entry is TECHNICALLY SUPPORTED in code. Mapping any entry to a Nelna
business responsibility requires owner evidence (APR-007/008/009/010 and related).
Do not treat this module as an approved organizational chart or SoD policy.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Final


class CapabilityBucket(StrEnum):
    VIEW = "view"
    MANAGE = "manage"
    RECORD = "record"
    SUBMIT = "submit"
    SUPERVISOR_REVIEW = "supervisor_review"
    CORRECTION = "correction"
    QA_REVIEW = "qa_review"
    QUALITY_CASE = "quality_case"
    EVIDENCE = "evidence"
    MASTER_DATA = "master_data"
    CHECKLIST_PUBLISH = "checklist_publish"
    AUDIT_ACCESS = "audit_access"
    SYSTEM_ADMINISTRATION = "system_administration"


class ObjectScope(StrEnum):
    ORGANIZATION = "Organization"
    SITE = "Site"
    DEPARTMENT = "Department"
    SYSTEM_WIDE = "system-wide"


class TechnicalSupportStatus(StrEnum):
    TECHNICALLY_SUPPORTED = "TECHNICALLY SUPPORTED"


class BusinessMappingStatus(StrEnum):
    APPROVAL_REQUIRED = "APPROVAL REQUIRED"


@dataclass(frozen=True, slots=True)
class PermissionCatalogueEntry:
    """One technical permission (or capability note) in the catalogue."""

    key: str
    permission: str
    bucket: CapabilityBucket
    scopes: tuple[ObjectScope, ...]
    description: str
    technical_status: TechnicalSupportStatus = TechnicalSupportStatus.TECHNICALLY_SUPPORTED
    business_mapping_status: BusinessMappingStatus = BusinessMappingStatus.APPROVAL_REQUIRED
    notes: str = ""


# Catalogue keys are stable identifiers for docs/tests — not business role codes.
PERMISSION_CATALOGUE: Final[tuple[PermissionCatalogueEntry, ...]] = (
    PermissionCatalogueEntry(
        key="view_checklisttask",
        permission="scheduling.view_checklisttask",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Inspect checklist orchestration tasks (Django default view).",
    ),
    PermissionCatalogueEntry(
        key="view_checklisttemplate",
        permission="checklists.view_checklisttemplate",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SYSTEM_WIDE),
        description="Inspect checklist template definitions (Django default view).",
    ),
    PermissionCatalogueEntry(
        key="view_fgproduct",
        permission="master_data.view_fgproduct",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SYSTEM_WIDE),
        description="Inspect FG Product master rows (Django default view).",
    ),
    PermissionCatalogueEntry(
        key="view_shift",
        permission="organizations.view_shift",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Inspect Shift configuration (Django default view).",
    ),
    PermissionCatalogueEntry(
        key="view_checklistsubmission",
        permission="reviews.view_supervisorreview",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Inspect Supervisor review objects where authorized (default view).",
        notes="Does not grant review_checklistsubmission.",
    ),
    PermissionCatalogueEntry(
        key="manage_checklisttask",
        permission="scheduling.manage_checklisttask",
        bucket=CapabilityBucket.MANAGE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Create/cancel administrative checklist tasks.",
        notes="Does not imply record_checklisttask or assign_checklisttask.",
    ),
    PermissionCatalogueEntry(
        key="assign_checklisttask",
        permission="scheduling.assign_checklisttask",
        bucket=CapabilityBucket.MANAGE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Assign / reassign / unassign checklist task ownership.",
        notes=(
            "Ownership only — assignment never grants view/manage/record permission. "
            "Assignee must still hold valid scoped RBAC independently."
        ),
    ),
    PermissionCatalogueEntry(
        key="view_checklistapplicability",
        permission="scheduling.view_checklistapplicability",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Preview / inspect checklist applicability rules.",
        notes="Does not auto-create tasks; APR-013/014/015 remain evidence-gated.",
    ),
    PermissionCatalogueEntry(
        key="view_checklistschedule",
        permission="scheduling.view_checklistschedule",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="View checklist schedule definitions.",
        notes="Frequencies remain EVIDENCE REQUIRED; no seeded Nelna cadences.",
    ),
    PermissionCatalogueEntry(
        key="manage_checklistschedule",
        permission="scheduling.manage_checklistschedule",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Configure checklist schedules (shift/window/interval).",
        notes=(
            "Never invent frequencies. Missed windows never auto-create NCR. "
            "Celery Beat poll is infrastructure only."
        ),
    ),
    PermissionCatalogueEntry(
        key="manage_checklistapplicability",
        permission="scheduling.manage_checklistapplicability",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Configure checklist applicability rules (org-scoped).",
        notes=(
            "Never silently picks among conflicts. Production Line dimension not modeled. "
            "APR-013/014/015 EVIDENCE REQUIRED for production policy."
        ),
    ),
    PermissionCatalogueEntry(
        key="manage_externalbatchmapping",
        permission="scheduling.manage_externalbatchmapping",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION,),
        description="Configure external batch identity mappings (org/product/site/shift).",
        notes=(
            "Adapter boundary only — no live Bileeta/ERP connector. "
            "APR-011/012 remain EVIDENCE REQUIRED for production ingestion."
        ),
    ),
    PermissionCatalogueEntry(
        key="manage_checklist",
        permission="checklists.manage_checklist",
        bucket=CapabilityBucket.CHECKLIST_PUBLISH,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SYSTEM_WIDE),
        description="Manage checklist definitions including publish lifecycle.",
        notes="Publish capability is technical; content approval remains APR/TEMPLATE evidence.",
    ),
    PermissionCatalogueEntry(
        key="manage_fgproduct",
        permission="master_data.manage_fgproduct",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Manage FG Product master-data rows.",
    ),
    PermissionCatalogueEntry(
        key="view_productspecification",
        permission="master_data.view_productspecification",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Inspect product quality specifications and versions (Django default view).",
        notes="Limits remain empty until APR-006 / ASM-001 evidence.",
    ),
    PermissionCatalogueEntry(
        key="manage_productspecification",
        permission="master_data.manage_productspecification",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Create/edit/approve/retire versioned product quality specifications.",
        notes=(
            "High-privilege technical capability; publishing is audited. "
            "Do not invent temperature/weight/microbiological limits."
        ),
    ),
    PermissionCatalogueEntry(
        key="view_equipment",
        permission="instruments.view_equipment",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Inspect equipment master and calibration history (Django default view).",
        notes="Separate from operator record permissions.",
    ),
    PermissionCatalogueEntry(
        key="manage_equipment",
        permission="instruments.manage_equipment",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Manage equipment assets and calibration records.",
        notes="Not implied by scheduling.record_checklisttask / operator roles.",
    ),
    PermissionCatalogueEntry(
        key="view_trainingrecord",
        permission="training.view_trainingrecord",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Inspect training / competency records (Django default view).",
        notes="Separate from operator record permissions.",
    ),
    PermissionCatalogueEntry(
        key="manage_trainingrecord",
        permission="training.manage_trainingrecord",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Manage training and competency records / enforcement policy metadata.",
        notes=(
            "Not implied by scheduling.record_checklisttask / operator roles. "
            "Gate WARN/BLOCK EVIDENCE REQUIRED."
        ),
    ),
    PermissionCatalogueEntry(
        key="manage_shift",
        permission="organizations.manage_shift",
        bucket=CapabilityBucket.MASTER_DATA,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE),
        description="Manage Shift configuration rows.",
    ),
    PermissionCatalogueEntry(
        key="create_nonconformance",
        permission="nonconformance.create_nonconformance",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Create formal nonconformance cases (manual only; no FAIL/CCP auto-raise).",
        notes="Distinct from recording ChecklistCorrection / resubmission.",
    ),
    PermissionCatalogueEntry(
        key="manage_nonconformance",
        permission="nonconformance.manage_nonconformance",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Update/transition open nonconformance cases.",
        notes="Does not invent severity or auto-HOLD rules.",
    ),
    PermissionCatalogueEntry(
        key="close_nonconformance",
        permission="nonconformance.close_nonconformance",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Close nonconformance cases (separate from manage).",
    ),
    PermissionCatalogueEntry(
        key="create_holdcase",
        permission="nonconformance.create_holdcase",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Open Hold cases manually (free-text reason/scope).",
        notes="Resolution catalogues remain EVIDENCE REQUIRED — not seeded.",
    ),
    PermissionCatalogueEntry(
        key="manage_holdcase",
        permission="nonconformance.manage_holdcase",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Manage open Hold cases.",
    ),
    PermissionCatalogueEntry(
        key="close_holdcase",
        permission="nonconformance.close_holdcase",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Close Hold cases with free-text resolution.",
    ),
    PermissionCatalogueEntry(
        key="create_capa",
        permission="capa.create_capa",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Create CAPA headers (human workflow foundation).",
    ),
    PermissionCatalogueEntry(
        key="manage_capa",
        permission="capa.manage_capa",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Manage CAPA actions, verification, and effectiveness review fields.",
        notes="No AI final CAPA closure.",
    ),
    PermissionCatalogueEntry(
        key="close_capa",
        permission="capa.close_capa",
        bucket=CapabilityBucket.QUALITY_CASE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Human-only CAPA closure.",
    ),
    PermissionCatalogueEntry(
        key="manage_supplierquality_qa",
        permission="supplier_quality.manage_supplierquality_qa",
        bucket=CapabilityBucket.MANAGE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SYSTEM_WIDE),
        description="Manage supplier quality profiles (QA-oriented technical permission).",
    ),
    PermissionCatalogueEntry(
        key="view_supplierquality_procurement",
        permission="supplier_quality.view_supplierquality_procurement",
        bucket=CapabilityBucket.VIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SYSTEM_WIDE),
        description="View supplier quality profiles (procurement-oriented technical permission).",
    ),
    PermissionCatalogueEntry(
        key="record_checklisttask",
        permission="scheduling.record_checklisttask",
        bucket=CapabilityBucket.RECORD,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Enter draft checklist responses.",
        notes="Also used for correction/resubmission entry (same technical permission).",
    ),
    PermissionCatalogueEntry(
        key="submit_via_record",
        permission="scheduling.record_checklisttask",
        bucket=CapabilityBucket.SUBMIT,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description=(
            "Submit draft records (submit rides on record permission; no separate codename)."
        ),
        notes="Distinct capability bucket for documentation; same Django permission as record.",
    ),
    PermissionCatalogueEntry(
        key="correction_via_record",
        permission="scheduling.record_checklisttask",
        bucket=CapabilityBucket.CORRECTION,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description=(
            "Start/edit/resubmit corrections (technical permission is record_checklisttask)."
        ),
        notes="Ownership locking EVIDENCE REQUIRED; manage/review do not imply correction.",
    ),
    PermissionCatalogueEntry(
        key="review_checklistsubmission",
        permission="reviews.review_checklistsubmission",
        bucket=CapabilityBucket.SUPERVISOR_REVIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Record immutable Supervisor review on submissions.",
        notes="Does not imply record or QA review.",
    ),
    PermissionCatalogueEntry(
        key="qa_review_checklistsubmission",
        permission="quality.qa_review_checklistsubmission",
        bucket=CapabilityBucket.QA_REVIEW,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Record immutable QA final disposition (RELEASE/HOLD/REJECT labels).",
        notes="Does not imply Supervisor review or recording.",
    ),
    PermissionCatalogueEntry(
        key="upload_evidenceattachment",
        permission="evidence.upload_evidenceattachment",
        bucket=CapabilityBucket.EVIDENCE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Upload optional evidence attachments to allowlisted quality objects.",
        notes="Does not force evidence for checklist items; parent capability also required.",
    ),
    PermissionCatalogueEntry(
        key="view_evidenceattachment",
        permission="evidence.view_evidenceattachment",
        bucket=CapabilityBucket.EVIDENCE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="View/download evidence via authorized endpoints (no public URLs).",
        notes="Every download is authorization-checked; binaries stay in private storage.",
    ),
    PermissionCatalogueEntry(
        key="retire_evidenceattachment",
        permission="evidence.retire_evidenceattachment",
        bucket=CapabilityBucket.EVIDENCE,
        scopes=(ObjectScope.ORGANIZATION, ObjectScope.SITE, ObjectScope.DEPARTMENT),
        description="Soft-retire evidence (no casual hard-delete), including immutable linkages.",
        notes="Immutable parent linkages require this permission plus a retirement reason.",
    ),
    PermissionCatalogueEntry(
        key="audit_event_view",
        permission="security_audit.view_securityauditevent",
        bucket=CapabilityBucket.AUDIT_ACCESS,
        scopes=(ObjectScope.SYSTEM_WIDE,),
        description="View security audit events via Django admin/default view (if granted).",
        notes="No separate custom audit-export permission in Phase 03C.",
    ),
    PermissionCatalogueEntry(
        key="system_administration_superuser",
        permission="__django_superuser__",
        bucket=CapabilityBucket.SYSTEM_ADMINISTRATION,
        scopes=(ObjectScope.SYSTEM_WIDE,),
        description="Django is_superuser bypasses scoped RBAC checks (tested separately).",
        notes=(
            "Not a Permission row. Prefer scoped roles for operational work; "
            "superuser is break-glass."
        ),
    ),
)


CATALOGUE_BY_KEY: Final[dict[str, PermissionCatalogueEntry]] = {
    entry.key: entry for entry in PERMISSION_CATALOGUE
}


def catalogue_keys() -> frozenset[str]:
    return frozenset(CATALOGUE_BY_KEY)


def entries_for_bucket(bucket: CapabilityBucket) -> tuple[PermissionCatalogueEntry, ...]:
    return tuple(e for e in PERMISSION_CATALOGUE if e.bucket == bucket)


def technical_permission_codenames() -> frozenset[str]:
    """Django app_label.codename values (excludes superuser sentinel)."""
    return frozenset(
        e.permission for e in PERMISSION_CATALOGUE if e.permission != "__django_superuser__"
    )

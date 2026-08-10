"""Security audit event model — append-oriented auth/RBAC events."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models


class SecurityAuditEvent(models.Model):
    class EventType(models.TextChoices):
        LOGIN_SUCCESS = "LOGIN_SUCCESS", "Login success"
        LOGIN_FAILURE = "LOGIN_FAILURE", "Login failure"
        ACCOUNT_LOCKED = "ACCOUNT_LOCKED", "Account locked"
        ACCOUNT_UNLOCKED = "ACCOUNT_UNLOCKED", "Account unlocked"
        LOGOUT = "LOGOUT", "Logout"
        PASSWORD_CHANGED = "PASSWORD_CHANGED", "Password changed"
        PASSWORD_RESET_BY_ADMIN = "PASSWORD_RESET_BY_ADMIN", "Password reset by admin"
        USER_ACTIVATED = "USER_ACTIVATED", "User activated"
        USER_DEACTIVATED = "USER_DEACTIVATED", "User deactivated"
        ROLE_ASSIGNED = "ROLE_ASSIGNED", "Role assigned"
        ROLE_REVOKED = "ROLE_REVOKED", "Role revoked"
        ROLE_PERMISSIONS_UPDATED = "ROLE_PERMISSIONS_UPDATED", "Role permissions updated"
        ROLE_TEMPLATE_CREATED = "ROLE_TEMPLATE_CREATED", "Role template created"
        ROLE_TEMPLATE_UPDATED = "ROLE_TEMPLATE_UPDATED", "Role template updated"
        ROLE_TEMPLATE_APPLIED = "ROLE_TEMPLATE_APPLIED", "Role template applied to role"
        SHIFT_CREATED = "SHIFT_CREATED", "Shift created"
        SHIFT_UPDATED = "SHIFT_UPDATED", "Shift updated"
        SHIFT_ACTIVATED = "SHIFT_ACTIVATED", "Shift activated"
        SHIFT_DEACTIVATED = "SHIFT_DEACTIVATED", "Shift deactivated"
        ORGANIZATION_CREATED = "ORGANIZATION_CREATED", "Organization created"
        ORGANIZATION_UPDATED = "ORGANIZATION_UPDATED", "Organization updated"
        ORGANIZATION_ACTIVATED = "ORGANIZATION_ACTIVATED", "Organization activated"
        ORGANIZATION_DEACTIVATED = "ORGANIZATION_DEACTIVATED", "Organization deactivated"
        SITE_CREATED = "SITE_CREATED", "Site created"
        SITE_UPDATED = "SITE_UPDATED", "Site updated"
        SITE_ACTIVATED = "SITE_ACTIVATED", "Site activated"
        SITE_DEACTIVATED = "SITE_DEACTIVATED", "Site deactivated"
        DEPARTMENT_CREATED = "DEPARTMENT_CREATED", "Department created"
        DEPARTMENT_UPDATED = "DEPARTMENT_UPDATED", "Department updated"
        DEPARTMENT_ACTIVATED = "DEPARTMENT_ACTIVATED", "Department activated"
        DEPARTMENT_DEACTIVATED = "DEPARTMENT_DEACTIVATED", "Department deactivated"
        ORGANIZATION_HIERARCHY_IMPORT_PREVIEWED = (
            "ORGANIZATION_HIERARCHY_IMPORT_PREVIEWED",
            "Organization hierarchy import previewed",
        )
        ORGANIZATION_HIERARCHY_IMPORT_COMPLETED = (
            "ORGANIZATION_HIERARCHY_IMPORT_COMPLETED",
            "Organization hierarchy import completed",
        )
        ORGANIZATION_HIERARCHY_IMPORT_FAILED = (
            "ORGANIZATION_HIERARCHY_IMPORT_FAILED",
            "Organization hierarchy import failed",
        )
        FG_PRODUCT_CREATED = "FG_PRODUCT_CREATED", "FG Product created"
        FG_PRODUCT_UPDATED = "FG_PRODUCT_UPDATED", "FG Product updated"
        FG_PRODUCT_ACTIVATED = "FG_PRODUCT_ACTIVATED", "FG Product activated"
        FG_PRODUCT_DEACTIVATED = "FG_PRODUCT_DEACTIVATED", "FG Product deactivated"
        FG_PRODUCT_IMPORT_PREVIEWED = (
            "FG_PRODUCT_IMPORT_PREVIEWED",
            "FG Product import previewed",
        )
        FG_PRODUCT_IMPORT_COMPLETED = (
            "FG_PRODUCT_IMPORT_COMPLETED",
            "FG Product import completed",
        )
        FG_PRODUCT_IMPORT_FAILED = (
            "FG_PRODUCT_IMPORT_FAILED",
            "FG Product import failed",
        )
        EQUIPMENT_CREATED = "EQUIPMENT_CREATED", "Equipment created"
        EQUIPMENT_UPDATED = "EQUIPMENT_UPDATED", "Equipment updated"
        EQUIPMENT_ACTIVATED = "EQUIPMENT_ACTIVATED", "Equipment activated"
        EQUIPMENT_DEACTIVATED = "EQUIPMENT_DEACTIVATED", "Equipment deactivated"
        EQUIPMENT_STATUS_CHANGED = (
            "EQUIPMENT_STATUS_CHANGED",
            "Equipment operational status changed",
        )
        CALIBRATION_RECORD_CREATED = (
            "CALIBRATION_RECORD_CREATED",
            "Calibration record created",
        )
        CALIBRATION_CERTIFICATE_METADATA_UPDATED = (
            "CALIBRATION_CERTIFICATE_METADATA_UPDATED",
            "Calibration certificate metadata updated",
        )
        TRAINING_RECORD_CREATED = "TRAINING_RECORD_CREATED", "Training record created"
        TRAINING_RECORD_UPDATED = "TRAINING_RECORD_UPDATED", "Training record updated"
        TRAINING_RECORD_STATUS_CHANGED = (
            "TRAINING_RECORD_STATUS_CHANGED",
            "Training record status changed",
        )
        TRAINING_ENFORCEMENT_POLICY_CREATED = (
            "TRAINING_ENFORCEMENT_POLICY_CREATED",
            "Training enforcement policy created",
        )
        TRAINING_ENFORCEMENT_POLICY_UPDATED = (
            "TRAINING_ENFORCEMENT_POLICY_UPDATED",
            "Training enforcement policy updated",
        )
        PRODUCT_SPECIFICATION_CREATED = (
            "PRODUCT_SPECIFICATION_CREATED",
            "Product specification created",
        )
        SPECIFICATION_VERSION_CREATED = (
            "SPECIFICATION_VERSION_CREATED",
            "Specification version created",
        )
        SPECIFICATION_VERSION_UPDATED = (
            "SPECIFICATION_VERSION_UPDATED",
            "Specification version updated",
        )
        SPECIFICATION_VERSION_APPROVED = (
            "SPECIFICATION_VERSION_APPROVED",
            "Specification version approved",
        )
        SPECIFICATION_VERSION_RETIRED = (
            "SPECIFICATION_VERSION_RETIRED",
            "Specification version retired",
        )
        SPECIFICATION_VERSION_CLONED = (
            "SPECIFICATION_VERSION_CLONED",
            "Specification version cloned",
        )
        SPECIFICATION_PARAMETER_CREATED = (
            "SPECIFICATION_PARAMETER_CREATED",
            "Specification parameter created",
        )
        SPECIFICATION_PARAMETER_UPDATED = (
            "SPECIFICATION_PARAMETER_UPDATED",
            "Specification parameter updated",
        )
        SPECIFICATION_PARAMETER_REMOVED = (
            "SPECIFICATION_PARAMETER_REMOVED",
            "Specification parameter removed",
        )
        CHECKLIST_TEMPLATE_CREATED = "CHECKLIST_TEMPLATE_CREATED", "Checklist template created"
        CHECKLIST_TEMPLATE_UPDATED = "CHECKLIST_TEMPLATE_UPDATED", "Checklist template updated"
        CHECKLIST_TEMPLATE_ACTIVATED = (
            "CHECKLIST_TEMPLATE_ACTIVATED",
            "Checklist template activated",
        )
        CHECKLIST_TEMPLATE_DEACTIVATED = (
            "CHECKLIST_TEMPLATE_DEACTIVATED",
            "Checklist template deactivated",
        )
        CHECKLIST_VERSION_CREATED = "CHECKLIST_VERSION_CREATED", "Checklist version created"
        CHECKLIST_VERSION_CLONED = "CHECKLIST_VERSION_CLONED", "Checklist version cloned"
        CHECKLIST_VERSION_PUBLISHED = "CHECKLIST_VERSION_PUBLISHED", "Checklist version published"
        CHECKLIST_VERSION_RETIRED = "CHECKLIST_VERSION_RETIRED", "Checklist version retired"
        CHECKLIST_VERSION_EFFECTIVITY_UPDATED = (
            "CHECKLIST_VERSION_EFFECTIVITY_UPDATED",
            "Checklist version effectivity updated",
        )
        CHECKLIST_ITEM_EVALUATION_RULE_SET = (
            "CHECKLIST_ITEM_EVALUATION_RULE_SET",
            "Checklist item evaluation rule set",
        )
        CHECKLIST_ITEM_EVALUATION_RULE_CLEARED = (
            "CHECKLIST_ITEM_EVALUATION_RULE_CLEARED",
            "Checklist item evaluation rule cleared",
        )
        CHECKLIST_ITEM_CONTROL_POINT_METADATA_UPDATED = (
            "CHECKLIST_ITEM_CONTROL_POINT_METADATA_UPDATED",
            "Checklist item control-point metadata updated",
        )
        CHECKLIST_ITEM_MEASUREMENT_SEMANTICS_UPDATED = (
            "CHECKLIST_ITEM_MEASUREMENT_SEMANTICS_UPDATED",
            "Checklist item measurement semantics updated",
        )
        CHECKLIST_TASK_CREATED = "CHECKLIST_TASK_CREATED", "Checklist task created"
        CHECKLIST_TASK_CANCELLED = "CHECKLIST_TASK_CANCELLED", "Checklist task cancelled"
        CHECKLIST_TASK_ASSIGNED = "CHECKLIST_TASK_ASSIGNED", "Checklist task assigned"
        CHECKLIST_TASK_REASSIGNED = (
            "CHECKLIST_TASK_REASSIGNED",
            "Checklist task reassigned",
        )
        CHECKLIST_TASK_UNASSIGNED = (
            "CHECKLIST_TASK_UNASSIGNED",
            "Checklist task unassigned",
        )
        CHECKLIST_TASK_DUE_WINDOW_UPDATED = (
            "CHECKLIST_TASK_DUE_WINDOW_UPDATED",
            "Checklist task due window updated",
        )
        CHECKLIST_TASK_GENERATED = (
            "CHECKLIST_TASK_GENERATED",
            "Checklist task generated by schedule engine",
        )
        CHECKLIST_SCHEDULE_CREATED = (
            "CHECKLIST_SCHEDULE_CREATED",
            "Checklist schedule created",
        )
        CHECKLIST_SCHEDULE_DEACTIVATED = (
            "CHECKLIST_SCHEDULE_DEACTIVATED",
            "Checklist schedule deactivated",
        )
        CHECKLIST_SCHEDULE_GENERATION_RUN = (
            "CHECKLIST_SCHEDULE_GENERATION_RUN",
            "Checklist schedule generation run",
        )
        EXTERNAL_BATCH_EVENT_RECEIVED = (
            "EXTERNAL_BATCH_EVENT_RECEIVED",
            "External batch event received",
        )
        EXTERNAL_BATCH_EVENT_DUPLICATE = (
            "EXTERNAL_BATCH_EVENT_DUPLICATE",
            "External batch event duplicate (idempotent)",
        )
        EXTERNAL_BATCH_EVENT_MAPPING_FAILED = (
            "EXTERNAL_BATCH_EVENT_MAPPING_FAILED",
            "External batch event mapping failed",
        )
        EXTERNAL_BATCH_EVENT_APPLICABILITY_FAILED = (
            "EXTERNAL_BATCH_EVENT_APPLICABILITY_FAILED",
            "External batch event applicability failed",
        )
        EXTERNAL_BATCH_EVENT_VERSION_FAILED = (
            "EXTERNAL_BATCH_EVENT_VERSION_FAILED",
            "External batch event effective-version failed",
        )
        EXTERNAL_BATCH_EVENT_PROCESSED = (
            "EXTERNAL_BATCH_EVENT_PROCESSED",
            "External batch event processed to checklist task",
        )
        EXTERNAL_BATCH_EVENT_REJECTED = (
            "EXTERNAL_BATCH_EVENT_REJECTED",
            "External batch event rejected",
        )
        EXTERNAL_BATCH_MAPPING_UPSERTED = (
            "EXTERNAL_BATCH_MAPPING_UPSERTED",
            "External batch mapping upserted",
        )
        CHECKLIST_APPLICABILITY_RULE_CREATED = (
            "CHECKLIST_APPLICABILITY_RULE_CREATED",
            "Checklist applicability rule created",
        )
        CHECKLIST_APPLICABILITY_RULE_UPDATED = (
            "CHECKLIST_APPLICABILITY_RULE_UPDATED",
            "Checklist applicability rule updated",
        )
        CHECKLIST_APPLICABILITY_RULE_DEACTIVATED = (
            "CHECKLIST_APPLICABILITY_RULE_DEACTIVATED",
            "Checklist applicability rule deactivated",
        )
        CHECKLIST_APPLICABILITY_PREVIEWED = (
            "CHECKLIST_APPLICABILITY_PREVIEWED",
            "Checklist applicability previewed",
        )
        CHECKLIST_RECORD_STARTED = "CHECKLIST_RECORD_STARTED", "Checklist record started"
        CHECKLIST_RECORD_DRAFT_SAVED = (
            "CHECKLIST_RECORD_DRAFT_SAVED",
            "Checklist record draft saved",
        )
        CHECKLIST_RECORD_SUBMITTED = (
            "CHECKLIST_RECORD_SUBMITTED",
            "Checklist record submitted",
        )
        SUPERVISOR_REVIEW_COMPLETED = (
            "SUPERVISOR_REVIEW_COMPLETED",
            "Supervisor review completed",
        )
        SUPERVISOR_REVIEW_GOVERNANCE_POLICY_SET = (
            "SUPERVISOR_REVIEW_GOVERNANCE_POLICY_SET",
            "Supervisor review governance policy set",
        )
        SUPERVISOR_REVIEW_DELEGATION_GRANTED = (
            "SUPERVISOR_REVIEW_DELEGATION_GRANTED",
            "Supervisor review temporary delegation granted",
        )
        SUPERVISOR_REVIEW_DELEGATION_REVOKED = (
            "SUPERVISOR_REVIEW_DELEGATION_REVOKED",
            "Supervisor review temporary delegation revoked",
        )
        CHECKLIST_CORRECTION_STARTED = (
            "CHECKLIST_CORRECTION_STARTED",
            "Checklist correction started",
        )
        CHECKLIST_CORRECTION_RESUBMITTED = (
            "CHECKLIST_CORRECTION_RESUBMITTED",
            "Checklist correction resubmitted",
        )
        QA_REVIEW_COMPLETED = (
            "QA_REVIEW_COMPLETED",
            "QA review disposition completed",
        )
        NONCONFORMANCE_CREATED = "NONCONFORMANCE_CREATED", "Nonconformance created"
        NONCONFORMANCE_UPDATED = "NONCONFORMANCE_UPDATED", "Nonconformance updated"
        NONCONFORMANCE_STATUS_CHANGED = (
            "NONCONFORMANCE_STATUS_CHANGED",
            "Nonconformance status changed",
        )
        NONCONFORMANCE_CLOSED = "NONCONFORMANCE_CLOSED", "Nonconformance closed"
        HOLD_CASE_CREATED = "HOLD_CASE_CREATED", "Hold case created"
        HOLD_CASE_CLOSED = "HOLD_CASE_CLOSED", "Hold case closed"
        CAPA_CREATED = "CAPA_CREATED", "CAPA created"
        CAPA_STATUS_CHANGED = "CAPA_STATUS_CHANGED", "CAPA status changed"
        CAPA_ACTION_ADDED = "CAPA_ACTION_ADDED", "CAPA action item added"
        CAPA_VERIFICATION_RECORDED = (
            "CAPA_VERIFICATION_RECORDED",
            "CAPA verification recorded",
        )
        CAPA_EFFECTIVENESS_REVIEWED = (
            "CAPA_EFFECTIVENESS_REVIEWED",
            "CAPA effectiveness review recorded",
        )
        CAPA_CLOSED = "CAPA_CLOSED", "CAPA closed"
        DISPATCH_QUALITY_RECORD_CREATED = (
            "DISPATCH_QUALITY_RECORD_CREATED",
            "Dispatch quality record created",
        )
        DISPATCH_QUALITY_RECORD_UPDATED = (
            "DISPATCH_QUALITY_RECORD_UPDATED",
            "Dispatch quality record updated",
        )
        DISPATCH_VEHICLE_INSPECTION_LINKED = (
            "DISPATCH_VEHICLE_INSPECTION_LINKED",
            "Dispatch vehicle inspection linked",
        )
        DISPATCH_QA_REVIEW_LINKED = (
            "DISPATCH_QA_REVIEW_LINKED",
            "Dispatch QA review linked",
        )
        DISPATCH_TEMPERATURE_RECORDED = (
            "DISPATCH_TEMPERATURE_RECORDED",
            "Dispatch cold-chain temperature recorded",
        )
        DISPATCH_QUANTITY_LINE_SET = (
            "DISPATCH_QUANTITY_LINE_SET",
            "Dispatch quantity line set",
        )
        DISPATCH_RELEASE_POLICY_UPDATED = (
            "DISPATCH_RELEASE_POLICY_UPDATED",
            "Dispatch QA release policy updated",
        )
        DISPATCH_RELEASE_GATE_EVALUATED = (
            "DISPATCH_RELEASE_GATE_EVALUATED",
            "Dispatch QA release gate evaluated",
        )
        DISPATCH_QUALITY_RECORD_COMPLETED = (
            "DISPATCH_QUALITY_RECORD_COMPLETED",
            "Dispatch quality record completed",
        )
        DISPATCH_QUALITY_RECORD_CANCELLED = (
            "DISPATCH_QUALITY_RECORD_CANCELLED",
            "Dispatch quality record cancelled",
        )
        SUPPLIER_QUALITY_PROFILE_CREATED = (
            "SUPPLIER_QUALITY_PROFILE_CREATED",
            "Supplier quality profile created",
        )
        SUPPLIER_QUALITY_PROFILE_UPDATED = (
            "SUPPLIER_QUALITY_PROFILE_UPDATED",
            "Supplier quality profile updated",
        )
        SUPPLIER_CERTIFICATE_RECORDED = (
            "SUPPLIER_CERTIFICATE_RECORDED",
            "Supplier certificate recorded",
        )
        SUPPLIER_CERTIFICATE_VERIFIED = (
            "SUPPLIER_CERTIFICATE_VERIFIED",
            "Supplier certificate verified",
        )
        SUPPLIER_QUALITY_EVENT_RECORDED = (
            "SUPPLIER_QUALITY_EVENT_RECORDED",
            "Supplier quality event recorded",
        )
        EVIDENCE_UPLOADED = (
            "EVIDENCE_UPLOADED",
            "Evidence attachment uploaded",
        )
        EVIDENCE_DOWNLOADED = (
            "EVIDENCE_DOWNLOADED",
            "Evidence attachment downloaded",
        )
        EVIDENCE_RETIRED = (
            "EVIDENCE_RETIRED",
            "Evidence attachment soft-retired",
        )
        EVIDENCE_ACCESS_DENIED = (
            "EVIDENCE_ACCESS_DENIED",
            "Evidence attachment access denied or missing blob",
        )
        DISPATCH_RELEASE_GATE_BLOCKED = (
            "DISPATCH_RELEASE_GATE_BLOCKED",
            "Dispatch completion blocked by QA release gate",
        )
        NOTIFICATION_POLICY_UPDATED = (
            "NOTIFICATION_POLICY_UPDATED",
            "Notification policy updated",
        )
        NOTIFICATION_CREATED = (
            "NOTIFICATION_CREATED",
            "In-app notification created",
        )
        NOTIFICATION_READ = (
            "NOTIFICATION_READ",
            "Notification marked read",
        )
        NOTIFICATION_EMAIL_DELIVERED = (
            "NOTIFICATION_EMAIL_DELIVERED",
            "Notification email delivered",
        )
        NOTIFICATION_EMAIL_FAILED = (
            "NOTIFICATION_EMAIL_FAILED",
            "Notification email delivery failed",
        )
        REPORT_RUN_ENQUEUED = (
            "REPORT_RUN_ENQUEUED",
            "Governed report run enqueued for background generation",
        )
        REPORT_RUN_COMPLETED = (
            "REPORT_RUN_COMPLETED",
            "Governed report run completed",
        )
        REPORT_EXPORTED = (
            "REPORT_EXPORTED",
            "Governed report exported (CSV generated for export)",
        )
        REPORT_EXPORT_DOWNLOADED = (
            "REPORT_EXPORT_DOWNLOADED",
            "Governed report CSV downloaded",
        )
        INTEGRATION_INBOUND_SUCCEEDED = (
            "INTEGRATION_INBOUND_SUCCEEDED",
            "Integration inbound attempt succeeded",
        )
        INTEGRATION_INBOUND_FAILED = (
            "INTEGRATION_INBOUND_FAILED",
            "Integration inbound attempt failed",
        )
        INTEGRATION_INBOUND_DUPLICATE = (
            "INTEGRATION_INBOUND_DUPLICATE",
            "Integration inbound duplicate (idempotent)",
        )
        INTEGRATION_LIVE_BLOCKED = (
            "INTEGRATION_LIVE_BLOCKED",
            "Live Bileeta pull blocked by evidence gate",
        )
        INTEGRATION_DEAD_LETTER = (
            "INTEGRATION_DEAD_LETTER",
            "Integration attempt marked dead letter",
        )
        INTEGRATION_OUTBOUND_BLOCKED = (
            "INTEGRATION_OUTBOUND_BLOCKED",
            "Outbound ERP disposition blocked pending approval",
        )
        AI_ASSISTANCE_COMPLETED = (
            "AI_ASSISTANCE_COMPLETED",
            "AI assistance request completed (advisory)",
        )
        AI_ASSISTANCE_BLOCKED = (
            "AI_ASSISTANCE_BLOCKED",
            "AI assistance request blocked (safety/auth)",
        )
        AI_ASSISTANCE_DISABLED = (
            "AI_ASSISTANCE_DISABLED",
            "AI assistance invoked while feature disabled",
        )
        AI_ASSISTANCE_FALLBACK = (
            "AI_ASSISTANCE_FALLBACK",
            "AI assistance safe fallback after provider failure/timeout",
        )
        LAB_SAMPLE_CREATED = "LAB_SAMPLE_CREATED", "Laboratory sample created"
        LAB_SAMPLE_STATUS_CHANGED = (
            "LAB_SAMPLE_STATUS_CHANGED",
            "Laboratory sample status changed",
        )
        LAB_RESULT_ENTERED = "LAB_RESULT_ENTERED", "Laboratory result entered"
        LAB_RESULT_VERIFIED = "LAB_RESULT_VERIFIED", "Laboratory result verified"
        LAB_RESULT_FINALIZED = "LAB_RESULT_FINALIZED", "Laboratory result finalized"
        LAB_RESULT_AMENDED = "LAB_RESULT_AMENDED", "Laboratory result amended"
        LAB_EXTERNAL_CERTIFICATE_RECORDED = (
            "LAB_EXTERNAL_CERTIFICATE_RECORDED",
            "Laboratory external certificate recorded",
        )
        LAB_POSITIVE_RELEASE_POLICY_UPDATED = (
            "LAB_POSITIVE_RELEASE_POLICY_UPDATED",
            "Laboratory positive-release policy updated",
        )

        HACCP_PLAN_CREATED = "HACCP_PLAN_CREATED", "HACCP plan created"
        HACCP_PLAN_VERSION_CREATED = (
            "HACCP_PLAN_VERSION_CREATED",
            "HACCP plan version created",
        )
        HACCP_PLAN_VERSION_APPROVED = (
            "HACCP_PLAN_VERSION_APPROVED",
            "HACCP plan version approved",
        )
        HACCP_PLAN_VERSION_RETIRED = (
            "HACCP_PLAN_VERSION_RETIRED",
            "HACCP plan version retired",
        )
        HACCP_CONTROL_POINT_MAPPED = (
            "HACCP_CONTROL_POINT_MAPPED",
            "HACCP control point mapped",
        )
        HACCP_CHECKLIST_BINDING_SET = (
            "HACCP_CHECKLIST_BINDING_SET",
            "HACCP checklist item binding set",
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    event_type = models.CharField(max_length=64, choices=EventType.choices)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="security_audit_actions",
    )
    subject_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="security_audit_subjects",
    )
    request_id = models.CharField(max_length=128, blank=True, default="")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent_summary = models.CharField(max_length=512, blank=True, default="")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["event_type", "created_at"], name="sa_type_created_idx"),
            models.Index(fields=["subject_user", "created_at"], name="sa_subject_idx"),
            models.Index(fields=["actor", "created_at"], name="sa_actor_idx"),
            models.Index(fields=["request_id"], name="sa_request_id_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.event_type} @ {self.created_at}"

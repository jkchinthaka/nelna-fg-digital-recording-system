from __future__ import annotations

from typing import TYPE_CHECKING, Any

from django.contrib import admin

from apps.rca.models import (
    RcaCapaLink,
    RcaCause,
    RcaEvent,
    RcaEvidenceLink,
    RcaFishboneEntry,
    RcaFiveWhyStep,
    RcaParticipant,
    RootCauseAnalysis,
)

if TYPE_CHECKING:
    _SoftRetentionBase = admin.ModelAdmin[Any]
else:
    _SoftRetentionBase = admin.ModelAdmin


class SoftRetentionAdmin(_SoftRetentionBase):
    def has_delete_permission(self, request: Any, obj: Any = None) -> bool:
        return False


@admin.register(RootCauseAnalysis)
class RootCauseAnalysisAdmin(SoftRetentionAdmin):
    list_display = ("rca_code", "source_kind", "status", "organization", "started_at")
    list_filter = ("status", "source_kind", "organization")
    search_fields = ("rca_code", "problem_statement")
    readonly_fields = ("created_at", "updated_at", "started_at", "verified_at", "closed_at")


@admin.register(RcaParticipant)
class RcaParticipantAdmin(SoftRetentionAdmin):
    list_display = ("rca", "participant", "name_reference")


@admin.register(RcaFiveWhyStep)
class RcaFiveWhyStepAdmin(SoftRetentionAdmin):
    list_display = ("rca", "sequence", "why_question")


@admin.register(RcaFishboneEntry)
class RcaFishboneEntryAdmin(SoftRetentionAdmin):
    list_display = ("rca", "category")


@admin.register(RcaCause)
class RcaCauseAdmin(SoftRetentionAdmin):
    list_display = ("rca", "state", "suggested_by_ai", "confirmed_at")
    readonly_fields = ("confirmed_by", "confirmed_at", "created_at", "updated_at")


@admin.register(RcaEvidenceLink)
class RcaEvidenceLinkAdmin(SoftRetentionAdmin):
    list_display = ("rca", "cause", "citation")


@admin.register(RcaCapaLink)
class RcaCapaLinkAdmin(SoftRetentionAdmin):
    list_display = ("cause", "corrective_action")


@admin.register(RcaEvent)
class RcaEventAdmin(_SoftRetentionBase):
    list_display = ("rca", "event_type", "actor", "created_at")
    readonly_fields = ("rca", "event_type", "summary", "payload", "actor", "created_at")

    def has_add_permission(self, request: Any) -> bool:
        return False

    def has_change_permission(self, request: Any, obj: Any = None) -> bool:
        return False

    def has_delete_permission(self, request: Any, obj: Any = None) -> bool:
        return False

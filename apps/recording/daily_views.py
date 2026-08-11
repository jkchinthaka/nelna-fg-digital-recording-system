"""Daily Records workspace for SOURCE RECEIVED company forms."""

from __future__ import annotations

import uuid
from datetime import date, datetime
from typing import cast

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_http_methods

from apps.accounts.models import User
from apps.checklists.controlled_forms import (
    COLD_ROOM_KEYS,
    CONTROLLED_FORMS,
    get_controlled_form,
)
from apps.recording.models import ChecklistRecord, ChecklistSubmission
from apps.recording.selectors import actor_can_access_recording_module
from apps.recording.services import start_checklist_recording
from apps.scheduling.selectors import organizations_for_task_record
from apps.scheduling.services import ensure_controlled_daily_task


def _actor(request: HttpRequest) -> User:
    return cast(User, request.user)


def _require_recording(request: HttpRequest) -> None:
    if not actor_can_access_recording_module(_actor(request)):
        raise PermissionDenied("Permission denied.")


def _parse_date(raw: str | None) -> date:
    if not raw:
        return timezone.localdate()
    return date.fromisoformat(raw)


@login_required
@require_GET
def daily_records_home(request: HttpRequest) -> HttpResponse:
    _require_recording(request)
    record_date = _parse_date(request.GET.get("date"))
    return render(
        request,
        "recording/daily/home.html",
        {
            "page_title": "Daily Records",
            "record_date": record_date,
            "forms": CONTROLLED_FORMS,
            "cold_rooms": COLD_ROOM_KEYS,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def daily_record_open(request: HttpRequest, form_code: str) -> HttpResponse:
    _require_recording(request)
    spec = get_controlled_form(form_code) or get_controlled_form(form_code.replace("-", "/"))
    if spec is None:
        raise PermissionDenied("Unknown controlled form.")
    record_date = _parse_date(request.GET.get("date") or request.POST.get("date"))
    room_key = (request.GET.get("room") or request.POST.get("room") or "").strip()
    if spec.code == "NMS/PPU/CL/39" and room_key not in COLD_ROOM_KEYS:
        room_key = "CR1"
    orgs = organizations_for_task_record(_actor(request))
    org = orgs.first()
    if org is None:
        raise PermissionDenied("Permission denied.")
    try:
        task = ensure_controlled_daily_task(
            actor=_actor(request),
            organization_id=org.id,
            form_code=spec.code,
            record_date=record_date,
            room_key=room_key if spec.code == "NMS/PPU/CL/39" else "",
        )
        record = start_checklist_recording(actor=_actor(request), task_id=task.id)
    except ValidationError as exc:
        messages.error(request, "; ".join(exc.messages) if hasattr(exc, "messages") else str(exc))
        return redirect("recording:daily_home")
    return redirect("recording:record_detail", record_id=record.id)


@login_required
@require_GET
def daily_record_print(request: HttpRequest, record_id: uuid.UUID) -> HttpResponse:
    _require_recording(request)
    record = (
        ChecklistRecord.objects.select_related(
            "checklist_task__checklist_template",
            "checklist_task__checklist_version",
            "checklist_task__organization",
        )
        .filter(pk=record_id)
        .first()
    )
    if record is None:
        raise PermissionDenied("Record not found.")
    spec = get_controlled_form(record.checklist_task.checklist_template.code)
    submission = (
        ChecklistSubmission.objects.filter(checklist_record=record)
        .select_related("submitted_by")
        .order_by("-submitted_at")
        .first()
    )
    return render(
        request,
        "recording/daily/print_record.html",
        {
            "page_title": "Print record",
            "record": record,
            "task": record.checklist_task,
            "spec": spec,
            "submission": submission,
            "generated_at": timezone.now(),
        },
    )


@login_required
@require_GET
def daily_monthly_print(request: HttpRequest) -> HttpResponse:
    _require_recording(request)
    form_code = (request.GET.get("form") or "").strip()
    spec = get_controlled_form(form_code)
    month_raw = (request.GET.get("month") or timezone.localdate().strftime("%Y-%m")).strip()
    year, month = [int(part) for part in month_raw.split("-", 1)]
    start = date(year, month, 1)
    if month == 12:
        end = date(year + 1, 1, 1)
    else:
        end = date(year, month + 1, 1)
    orgs = organizations_for_task_record(_actor(request))
    submissions = ChecklistSubmission.objects.none()
    if spec is not None and orgs.exists():
        submissions = (
            ChecklistSubmission.objects.filter(
                checklist_record__checklist_task__organization__in=orgs,
                checklist_record__checklist_task__checklist_template__code=spec.code,
                submitted_at__gte=datetime.combine(start, datetime.min.time()),
                submitted_at__lt=datetime.combine(end, datetime.min.time()),
            )
            .select_related(
                "checklist_record__checklist_task__checklist_template",
                "submitted_by",
            )
            .order_by("submitted_at")
        )
    return render(
        request,
        "recording/daily/print_monthly.html",
        {
            "page_title": "Monthly print pack",
            "spec": spec,
            "month_label": month_raw,
            "submissions": submissions,
            "generated_at": timezone.now(),
        },
    )

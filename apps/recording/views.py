"""Checklist recording views — draft save + submit confirmation + submitted read-only."""

from __future__ import annotations

import uuid
from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from apps.accounts.models import User
from apps.checklists.models import ChecklistResponseType
from apps.recording.forms import ChecklistDraftForm, response_field_name
from apps.recording.models import ChecklistRecord, ChecklistRecordStatus, ChecklistResponse
from apps.recording.selectors import (
    actor_can_access_recording_module,
    get_recordable_task,
    list_recordable_checklist_tasks,
    load_record_editor_context,
    load_submitted_record_context,
)
from apps.recording.services import (
    save_checklist_draft_responses,
    start_checklist_recording,
    submit_checklist_record,
)
from apps.scheduling.models import ChecklistTask

PAGE_SIZE = 25


def _actor(request: HttpRequest) -> User:
    return request.user  # type: ignore[return-value]


def _require_recording_module(request: HttpRequest) -> None:
    if not actor_can_access_recording_module(_actor(request)):
        raise PermissionDenied("Permission denied.")


def _initial_from_responses(
    responses: dict[uuid.UUID, ChecklistResponse],
    items: list[Any],
) -> dict[uuid.UUID, Any]:
    initial: dict[uuid.UUID, Any] = {}
    for item in items:
        response = responses.get(item.id)
        if response is None:
            continue
        if item.response_type in {
            ChecklistResponseType.YES_NO,
            ChecklistResponseType.YES_NO_NA,
        }:
            initial[item.id] = response.choice_value
        elif item.response_type == ChecklistResponseType.NUMBER:
            initial[item.id] = response.number_value
        elif item.response_type == ChecklistResponseType.TEXT:
            initial[item.id] = response.text_value
        elif item.response_type == ChecklistResponseType.SELECT:
            initial[item.id] = response.selected_option_id
    return initial


def _apply_validation_error(form: ChecklistDraftForm, exc: ValidationError) -> None:
    if hasattr(exc, "message_dict"):
        for field, errors in exc.message_dict.items():
            target = None
            try:
                item_id = uuid.UUID(str(field))
                candidate = response_field_name(item_id)
                if candidate in form.fields:
                    target = candidate
            except (TypeError, ValueError, AttributeError):
                target = field if field in form.fields else None
            for error in errors:
                form.add_error(target, error)
        return
    form.add_error(None, "; ".join(str(m) for m in exc.messages))


def _display_snapshot_value(item: Any, response: Any) -> str:
    if response is None:
        return "—"
    if item.response_type in {
        ChecklistResponseType.YES_NO,
        ChecklistResponseType.YES_NO_NA,
    }:
        return response.choice_value or "—"
    if item.response_type == ChecklistResponseType.NUMBER:
        if response.number_value is None:
            return "—"
        unit = f" {item.unit}" if item.unit else ""
        return f"{response.number_value}{unit}"
    if item.response_type == ChecklistResponseType.TEXT:
        return response.text_value or "—"
    if item.response_type == ChecklistResponseType.SELECT:
        option = response.selected_option
        return option.label if option is not None else "—"
    return "—"


@login_required
@require_GET
def recordable_task_list(request: HttpRequest) -> HttpResponse:
    _require_recording_module(request)
    tasks = list_recordable_checklist_tasks(_actor(request))
    page = Paginator(tasks, PAGE_SIZE).get_page(request.GET.get("page") or 1)
    return render(
        request,
        "recording/tasks/list.html",
        {
            "page": page,
            "tasks": page.object_list,
            "ChecklistRecordStatus": ChecklistRecordStatus,
        },
    )


@login_required
@require_POST
def start_recording(request: HttpRequest, task_id: uuid.UUID) -> HttpResponse:
    _require_recording_module(request)
    try:
        task = get_recordable_task(_actor(request), task_id)
    except PermissionDenied:
        raise
    if task is None:
        raise Http404("Checklist task not found.")
    try:
        record = start_checklist_recording(actor=_actor(request), task_id=task.id)
    except ValidationError as exc:
        messages.error(request, "; ".join(exc.messages))
        return redirect("recording:task_list")
    messages.success(request, "Draft recording ready.")
    if record.status == ChecklistRecordStatus.SUBMITTED:
        return redirect("recording:record_submitted", record_id=record.id)
    return redirect("recording:record_detail", record_id=record.id)


@login_required
@require_http_methods(["GET", "POST"])
def record_detail(request: HttpRequest, record_id: uuid.UUID) -> HttpResponse:
    _require_recording_module(request)
    try:
        draft_context = load_record_editor_context(_actor(request), record_id)
    except PermissionDenied:
        raise
    if draft_context is None:
        raise Http404("Checklist record not found.")

    record: ChecklistRecord = draft_context["record"]
    if record.status == ChecklistRecordStatus.SUBMITTED:
        return redirect("recording:record_submitted", record_id=record.id)

    task: ChecklistTask = draft_context["task"]
    sections = draft_context["sections"]
    responses = draft_context["responses"]
    completeness = draft_context["completeness"]
    items = [item for section in sections for item in section.items.all()]
    initial = _initial_from_responses(responses, items)

    if request.method == "POST":
        form = ChecklistDraftForm(request.POST, items=items, initial_responses=initial)
        if form.is_valid():
            try:
                save_checklist_draft_responses(
                    actor=_actor(request),
                    record_id=record.id,
                    answers=form.answers_by_item_id(),
                )
                messages.success(request, "Draft saved.")
                return redirect("recording:record_detail", record_id=record.id)
            except ValidationError as exc:
                _apply_validation_error(form, exc)
    else:
        form = ChecklistDraftForm(items=items, initial_responses=initial)

    return render(
        request,
        "recording/records/editor.html",
        {
            "record": record,
            "task": task,
            "sections": sections,
            "form": form,
            "completeness": completeness,
            "response_field_name": response_field_name,
            "ChecklistResponseType": ChecklistResponseType,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def submit_confirm(request: HttpRequest, record_id: uuid.UUID) -> HttpResponse:
    _require_recording_module(request)
    try:
        context = load_record_editor_context(_actor(request), record_id)
    except PermissionDenied:
        raise
    if context is None:
        raise Http404("Checklist record not found.")

    record: ChecklistRecord = context["record"]
    if record.status == ChecklistRecordStatus.SUBMITTED:
        return redirect("recording:record_submitted", record_id=record.id)

    task = context["task"]
    completeness = context["completeness"]
    missing = completeness["missing_required_items"]

    if request.method == "POST":
        if missing:
            messages.error(
                request,
                f"{len(missing)} required item(s) remain unanswered. "
                "Complete them before submitting.",
            )
            return redirect("recording:record_detail", record_id=record.id)
        try:
            submission = submit_checklist_record(actor=_actor(request), record_id=record.id)
        except ValidationError as exc:
            messages.error(request, "; ".join(exc.messages))
            return redirect("recording:record_detail", record_id=record.id)
        messages.success(
            request,
            f"Checklist submitted (Submission #{submission.submission_number}).",
        )
        return redirect("recording:record_submitted", record_id=record.id)

    return render(
        request,
        "recording/records/submit_confirm.html",
        {
            "record": record,
            "task": task,
            "completeness": completeness,
            "can_submit": not missing,
        },
    )


@login_required
@require_GET
def record_submitted(request: HttpRequest, record_id: uuid.UUID) -> HttpResponse:
    _require_recording_module(request)
    try:
        context = load_submitted_record_context(_actor(request), record_id)
    except PermissionDenied:
        raise
    if context is None:
        # May still be a draft — send to editor.
        try:
            draft = load_record_editor_context(_actor(request), record_id)
        except PermissionDenied:
            raise
        if draft is None:
            raise Http404("Checklist record not found.")
        return redirect("recording:record_detail", record_id=record_id)

    sections = context["sections"]
    snapshots = context["snapshot_responses"]
    rendered_sections = []
    for section in sections:
        items_out = []
        for item in section.items.all():
            items_out.append(
                {
                    "item": item,
                    "display_value": _display_snapshot_value(item, snapshots.get(item.id)),
                    "answered": item.id in snapshots,
                }
            )
        rendered_sections.append({"section": section, "items": items_out})

    return render(
        request,
        "recording/records/submitted.html",
        {
            "record": context["record"],
            "task": context["task"],
            "submission": context["submission"],
            "rendered_sections": rendered_sections,
        },
    )

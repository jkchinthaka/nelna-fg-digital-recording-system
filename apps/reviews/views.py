"""Supervisor review views — queue, detail, confirm, immutable result."""

from __future__ import annotations

import uuid
from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from apps.accounts.models import User
from apps.checklists.models import ChecklistResponseType
from apps.reviews.forms import SupervisorReviewConfirmForm
from apps.reviews.models import SupervisorReviewDecision
from apps.reviews.selectors import (
    actor_can_access_review_module,
    get_supervisor_review,
    list_supervisor_reviewable_submissions,
    load_submission_review_context,
)
from apps.reviews.services import create_supervisor_review

PAGE_SIZE = 25


def _actor(request: HttpRequest) -> User:
    return request.user  # type: ignore[return-value]


def _require_review_module(request: HttpRequest) -> None:
    if not actor_can_access_review_module(_actor(request)):
        raise PermissionDenied("Permission denied.")


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


def _render_sections(sections: list[Any], snapshots: dict[uuid.UUID, Any]) -> list[dict[str, Any]]:
    rendered: list[dict[str, Any]] = []
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
        rendered.append({"section": section, "items": items_out})
    return rendered


def _validation_message(exc: ValidationError) -> str:
    if hasattr(exc, "message_dict"):
        parts: list[str] = []
        for msgs in exc.message_dict.values():
            parts.extend(str(m) for m in msgs)
        return "; ".join(parts)
    return "; ".join(str(m) for m in exc.messages)


@login_required
@require_GET
def review_queue(request: HttpRequest) -> HttpResponse:
    _require_review_module(request)
    submissions = list_supervisor_reviewable_submissions(_actor(request))
    page = Paginator(submissions, PAGE_SIZE).get_page(request.GET.get("page") or 1)
    return render(
        request,
        "reviews/queue/list.html",
        {
            "page": page,
            "submissions": page.object_list,
        },
    )


@login_required
@require_GET
def submission_detail(request: HttpRequest, submission_id: uuid.UUID) -> HttpResponse:
    _require_review_module(request)
    try:
        context = load_submission_review_context(_actor(request), submission_id)
    except PermissionDenied:
        raise
    if context is None:
        raise Http404("Checklist submission not found.")

    if context["review"] is not None:
        return redirect("reviews:review_result", review_id=context["review"].id)

    return render(
        request,
        "reviews/submissions/detail.html",
        {
            "submission": context["submission"],
            "record": context["record"],
            "task": context["task"],
            "rendered_sections": _render_sections(
                context["sections"], context["snapshot_responses"]
            ),
            "SupervisorReviewDecision": SupervisorReviewDecision,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def confirm_decision(request: HttpRequest, submission_id: uuid.UUID, decision: str) -> HttpResponse:
    _require_review_module(request)
    if decision not in {
        SupervisorReviewDecision.APPROVED,
        SupervisorReviewDecision.RETURNED_FOR_CORRECTION,
    }:
        raise Http404("Unknown review decision.")

    try:
        context = load_submission_review_context(_actor(request), submission_id)
    except PermissionDenied:
        raise
    if context is None:
        raise Http404("Checklist submission not found.")

    if context["review"] is not None:
        messages.info(request, "This submission already has a Supervisor review.")
        return redirect("reviews:review_result", review_id=context["review"].id)

    if request.method == "POST":
        form = SupervisorReviewConfirmForm(request.POST)
        if form.is_valid():
            try:
                review = create_supervisor_review(
                    actor=_actor(request),
                    submission_id=submission_id,
                    decision=decision,
                    review_note=form.cleaned_data["review_note"],
                )
            except ValidationError as exc:
                messages.error(request, _validation_message(exc))
                return redirect("reviews:submission_detail", submission_id=submission_id)
            messages.success(request, "Supervisor review recorded.")
            return redirect("reviews:review_result", review_id=review.id)
    else:
        form = SupervisorReviewConfirmForm()

    decision_label = (
        "Approve for future QA stage"
        if decision == SupervisorReviewDecision.APPROVED
        else "Return for correction"
    )
    return render(
        request,
        "reviews/submissions/confirm.html",
        {
            "submission": context["submission"],
            "record": context["record"],
            "task": context["task"],
            "form": form,
            "decision": decision,
            "decision_label": decision_label,
            "SupervisorReviewDecision": SupervisorReviewDecision,
        },
    )


@login_required
@require_GET
def review_result(request: HttpRequest, review_id: uuid.UUID) -> HttpResponse:
    _require_review_module(request)
    try:
        review = get_supervisor_review(_actor(request), review_id)
    except PermissionDenied:
        raise
    if review is None:
        raise Http404("Supervisor review not found.")

    submission = review.checklist_submission
    try:
        context = load_submission_review_context(_actor(request), submission.id)
    except PermissionDenied:
        raise
    if context is None:
        raise Http404("Checklist submission not found.")

    return render(
        request,
        "reviews/reviews/result.html",
        {
            "review": review,
            "submission": submission,
            "record": context["record"],
            "task": context["task"],
            "rendered_sections": _render_sections(
                context["sections"], context["snapshot_responses"]
            ),
            "SupervisorReviewDecision": SupervisorReviewDecision,
        },
    )

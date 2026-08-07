"""Checklist task management views — orchestration only; no recording."""

from __future__ import annotations

import uuid
from typing import Any

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from apps.accounts.models import User
from apps.checklists.models import ChecklistTemplate, ChecklistVersion
from apps.scheduling.forms import ChecklistTaskCreateForm
from apps.scheduling.models import ChecklistTask, ChecklistTaskStatus
from apps.scheduling.selectors import (
    StatusFilter,
    actor_can_manage_task,
    actor_can_view_checklist_tasks,
    get_checklist_task,
    list_checklist_tasks,
    manageable_organization_ids,
    organizations_for_task_manage,
    organizations_for_task_view,
    published_versions_for_template,
    templates_for_task_manage,
)
from apps.scheduling.services import cancel_checklist_task, create_batch_checklist_task

PAGE_SIZE = 25


def _actor(request: HttpRequest) -> User:
    return request.user  # type: ignore[return-value]


def _parse_uuid(raw: str | None) -> uuid.UUID | None:
    if not raw:
        return None
    try:
        return uuid.UUID(str(raw))
    except (TypeError, ValueError, AttributeError):
        return None


def _require_view_module(request: HttpRequest) -> None:
    if not actor_can_view_checklist_tasks(_actor(request)):
        raise PermissionDenied("Permission denied.")


def _require_manage_module(request: HttpRequest) -> None:
    if not manageable_organization_ids(_actor(request)):
        raise PermissionDenied("Permission denied.")


def _get_task_or_404(request: HttpRequest, task_id: uuid.UUID) -> ChecklistTask:
    try:
        task = get_checklist_task(_actor(request), task_id)
    except PermissionDenied:
        raise
    if task is None:
        raise Http404("Checklist task not found.")
    return task


def _apply_validation_error(form: Any, exc: ValidationError) -> None:
    if hasattr(exc, "message_dict"):
        for field, errors in exc.message_dict.items():
            target = field if field in getattr(form, "fields", {}) else None
            for error in errors:
                form.add_error(target, error)
        return
    if hasattr(exc, "error_list"):
        for err in exc.error_list:
            form.add_error(None, err)
        return
    form.add_error(None, "; ".join(str(m) for m in exc.messages))


def _create_form(
    request: HttpRequest,
    data: dict[str, Any] | None = None,
) -> ChecklistTaskCreateForm:
    actor = _actor(request)
    orgs = organizations_for_task_manage(actor)
    org_id = _parse_uuid((data or request.GET).get("organization") if data or request.GET else None)
    if data is not None:
        org_id = _parse_uuid(data.get("organization"))
    elif request.method == "GET":
        org_id = _parse_uuid(request.GET.get("organization"))

    organization = orgs.filter(pk=org_id).first() if org_id else None
    templates = templates_for_task_manage(actor, organization=organization)

    template_id = None
    if data is not None:
        template_id = _parse_uuid(data.get("checklist_template"))
    elif request.method == "GET":
        template_id = _parse_uuid(request.GET.get("checklist_template"))

    template = templates.filter(pk=template_id).first() if template_id else None
    versions = (
        published_versions_for_template(actor, template=template)
        if template is not None
        else ChecklistVersion.objects.none()
    )
    return ChecklistTaskCreateForm(
        data,
        organizations=orgs,
        templates=templates,
        versions=versions,
    )


@login_required
@require_GET
def task_list(request: HttpRequest) -> HttpResponse:
    _require_view_module(request)
    batch_q = (request.GET.get("q") or "").strip()
    status_raw = (request.GET.get("status") or "all").strip()
    status: StatusFilter = (
        status_raw
        if status_raw in {"all", ChecklistTaskStatus.PENDING, ChecklistTaskStatus.CANCELLED}
        else "all"  # type: ignore[assignment]
    )
    org_id = _parse_uuid(request.GET.get("organization"))
    template_id = _parse_uuid(request.GET.get("template"))
    organizations = organizations_for_task_view(_actor(request))
    organization = organizations.filter(pk=org_id).first() if org_id else None
    view_org_ids = set(organizations.values_list("pk", flat=True))
    filter_templates = (
        ChecklistTemplate.objects.filter(organization_id__in=view_org_ids)
        .select_related("organization")
        .order_by("organization__code", "code")
    )
    template = filter_templates.filter(pk=template_id).first() if template_id else None

    tasks = list_checklist_tasks(
        _actor(request),
        organization=organization,
        template=template,
        status=status,
        batch_reference=batch_q or None,
    )
    paginator = Paginator(tasks, PAGE_SIZE)
    page_obj = paginator.get_page(request.GET.get("page"))
    manage_org_ids = manageable_organization_ids(_actor(request))
    context = {
        "page_obj": page_obj,
        "tasks": page_obj.object_list,
        "search": batch_q,
        "status": status,
        "organizations": organizations,
        "selected_organization": organization,
        "templates": filter_templates,
        "selected_template": template,
        "filters_active": bool(batch_q or org_id or template_id or status != "all"),
        "manageable_organization_ids": manage_org_ids,
        "can_create": bool(manage_org_ids),
        "total_count": paginator.count,
    }
    if request.headers.get("HX-Request") == "true":
        return render(request, "scheduling/tasks/_list_results.html", context)
    return render(request, "scheduling/tasks/list.html", context)


def _refresh_create_form_querysets(request: HttpRequest, form: ChecklistTaskCreateForm) -> None:
    actor = _actor(request)
    orgs = organizations_for_task_manage(actor)
    org_raw = form.data.get("organization") if form.is_bound else request.GET.get("organization")
    org_uuid = _parse_uuid(str(org_raw) if org_raw else None)
    organization = orgs.filter(pk=org_uuid).first() if org_uuid else None
    templates = templates_for_task_manage(actor, organization=organization)
    template_raw = (
        form.data.get("checklist_template")
        if form.is_bound
        else request.GET.get("checklist_template")
    )
    template_uuid = _parse_uuid(str(template_raw) if template_raw else None)
    template = templates.filter(pk=template_uuid).first() if template_uuid else None
    versions = (
        published_versions_for_template(actor, template=template)
        if template is not None
        else ChecklistVersion.objects.none()
    )
    org_field = form.fields["organization"]
    template_field = form.fields["checklist_template"]
    version_field = form.fields["checklist_version"]
    assert isinstance(org_field, forms.ModelChoiceField)
    assert isinstance(template_field, forms.ModelChoiceField)
    assert isinstance(version_field, forms.ModelChoiceField)
    org_field.queryset = orgs
    template_field.queryset = templates
    version_field.queryset = versions


@login_required
@require_http_methods(["GET", "POST"])
def task_create(request: HttpRequest) -> HttpResponse:
    _require_manage_module(request)
    form = _create_form(request, request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            task = create_batch_checklist_task(
                actor=_actor(request),
                organization_id=form.cleaned_data["organization"].id,
                checklist_template_id=form.cleaned_data["checklist_template"].id,
                checklist_version_id=form.cleaned_data["checklist_version"].id,
                batch_reference=form.cleaned_data["batch_reference"],
            )
        except ValidationError as exc:
            _apply_validation_error(form, exc)
            _refresh_create_form_querysets(request, form)
        except PermissionDenied:
            raise
        else:
            messages.success(
                request,
                (
                    f"Checklist task for batch {task.batch_reference} "
                    f"({task.checklist_template.code} v{task.checklist_version.version_number}) "
                    f"is ready."
                ),
            )
            return redirect("scheduling:task_detail", task_id=task.id)
    elif request.method == "POST":
        _refresh_create_form_querysets(request, form)

    version_field = form.fields["checklist_version"]
    assert isinstance(version_field, forms.ModelChoiceField)
    version_qs = version_field.queryset
    published_available = bool(version_qs is not None and version_qs.exists())
    return render(
        request,
        "scheduling/tasks/create.html",
        {
            "form": form,
            "published_available": published_available,
        },
    )


@login_required
@require_GET
def task_template_options(request: HttpRequest) -> HttpResponse:
    """HTMX: templates for selected organization."""
    _require_manage_module(request)
    org_id = _parse_uuid(request.GET.get("organization"))
    organization = (
        organizations_for_task_manage(_actor(request)).filter(pk=org_id).first() if org_id else None
    )
    templates = templates_for_task_manage(_actor(request), organization=organization)
    return render(
        request,
        "scheduling/tasks/_template_options.html",
        {"templates": templates},
    )


@login_required
@require_GET
def task_version_options(request: HttpRequest) -> HttpResponse:
    """HTMX: published versions for selected template."""
    _require_manage_module(request)
    template_id = _parse_uuid(request.GET.get("checklist_template"))
    template = (
        templates_for_task_manage(_actor(request)).filter(pk=template_id).first()
        if template_id
        else None
    )
    versions = (
        published_versions_for_template(_actor(request), template=template)
        if template is not None
        else ChecklistVersion.objects.none()
    )
    return render(
        request,
        "scheduling/tasks/_version_options.html",
        {"versions": versions},
    )


@login_required
@require_GET
def task_detail(request: HttpRequest, task_id: uuid.UUID) -> HttpResponse:
    task = _get_task_or_404(request, task_id)
    return render(
        request,
        "scheduling/tasks/detail.html",
        {
            "task": task,
            "can_cancel": actor_can_manage_task(_actor(request), task) and task.is_pending,
        },
    )


@login_required
@require_POST
def task_cancel(request: HttpRequest, task_id: uuid.UUID) -> HttpResponse:
    task = _get_task_or_404(request, task_id)
    if not actor_can_manage_task(_actor(request), task):
        raise PermissionDenied("Permission denied.")
    try:
        cancel_checklist_task(actor=_actor(request), task_id=task.id)
    except ValidationError as exc:
        messages.error(request, "; ".join(exc.messages))
    else:
        messages.success(request, f"Checklist task for batch {task.batch_reference} cancelled.")
    return redirect("scheduling:task_detail", task_id=task.id)

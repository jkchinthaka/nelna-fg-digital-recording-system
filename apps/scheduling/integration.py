"""External batch-source integration port — no ERP connector.

Delegates to domain task services. Does not invent ProductionBatch fields,
source-system schemas, webhooks, or credentials.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from apps.accounts.models import User
from apps.scheduling.models import ChecklistTask
from apps.scheduling.services import create_batch_checklist_task


@dataclass(frozen=True)
class BatchChecklistTaskRequest:
    """
    Narrow technical input for future external batch events.

    Only currently supported fields. Product / Shift / Site / Department /
    ERP order / quantity are intentionally absent until evidenced.
    """

    organization_id: uuid.UUID
    batch_reference: str
    checklist_template_id: uuid.UUID
    checklist_version_id: uuid.UUID


def accept_batch_checklist_task_request(
    *,
    actor: User | None,
    request: BatchChecklistTaskRequest,
) -> ChecklistTask:
    """
    Accept a technical batch checklist request and create/return a task.

    Authn/authz, PUBLISHED-only rules, idempotency, and version-conflict
    semantics remain owned by ``create_batch_checklist_task``.
    """
    return create_batch_checklist_task(
        actor=actor,
        organization_id=request.organization_id,
        checklist_template_id=request.checklist_template_id,
        checklist_version_id=request.checklist_version_id,
        batch_reference=request.batch_reference,
    )

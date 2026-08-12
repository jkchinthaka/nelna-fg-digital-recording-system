# Mongo Concurrency Inventory (`select_for_update`)

**Generated (UTC):** 2026-08-12T09:55:17Z  
**Exact call-site count:** 137  

PostgreSQL row locks are **not** supported by django-mongodb-backend.
Do not delete these call sites without a proven Mongo-safe replacement.

## Domain summary

| Domain | Count |
| --- | ---: |
| other | 52 |
| inventory-related quality modules | 22 |
| checklists | 17 |
| scheduling | 8 |
| CAPA | 6 |
| correction | 6 |
| laboratory | 5 |
| recording | 5 |
| NCR | 4 |
| HACCP | 3 |
| RCA | 3 |
| quality | 3 |
| reviews | 3 |

## Replacement policy

Approved pattern: **optimistic conditional transition** (atomic compare-and-set / conditional update + unique indexes + retry).
See `apps/core/optimistic_transition.py` and `docs/migration/MONGO_CONCURRENCY_PATTERN.md`.

Do **not** rewrite all sites blindly. Spike order:
1. Supervisor review
2. QA review
3. Recording / submission / correction
4. RCA

## Domain: CAPA

### `apps/capa/services.py:153` — `transition_capa_status`

- **File:** `apps/capa/services.py`
- **Function:** `transition_capa_status`
- **Locked model (heuristic):** `CorrectiveAction`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CorrectiveAction.
- **Source:** `action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()`

### `apps/capa/services.py:199` — `record_capa_verification`

- **File:** `apps/capa/services.py`
- **Function:** `record_capa_verification`
- **Locked model (heuristic):** `CorrectiveAction`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CorrectiveAction.
- **Source:** `action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()`

### `apps/capa/services.py:260` — `record_capa_effectiveness_review`

- **File:** `apps/capa/services.py`
- **Function:** `record_capa_effectiveness_review`
- **Locked model (heuristic):** `CorrectiveAction`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CorrectiveAction.
- **Source:** `action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()`

### `apps/capa/services.py:322` — `add_capa_action_item`

- **File:** `apps/capa/services.py`
- **Function:** `add_capa_action_item`
- **Locked model (heuristic):** `CorrectiveAction`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CorrectiveAction.
- **Source:** `action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()`

### `apps/capa/services.py:370` — `complete_capa_action_item`

- **File:** `apps/capa/services.py`
- **Function:** `complete_capa_action_item`
- **Locked model (heuristic):** `CapaActionItem`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CapaActionItem.
- **Source:** `CapaActionItem.objects.select_for_update()`

### `apps/capa/services.py:408` — `close_corrective_action`

- **File:** `apps/capa/services.py`
- **Function:** `close_corrective_action`
- **Locked model (heuristic):** `CorrectiveAction`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=CAPA; locked=CorrectiveAction.
- **Source:** `action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()`

## Domain: checklists

### `apps/checklists/effective_version.py:324` — `set_checklist_version_effectivity`

- **File:** `apps/checklists/effective_version.py`
- **Function:** `set_checklist_version_effectivity`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=UNKNOWN.
- **Source:** `ChecklistVersion.objects.select_related("template", "template__organization")`

### `apps/checklists/services.py:197` — `_lock_version`

- **File:** `apps/checklists/services.py`
- **Function:** `_lock_version`
- **Locked model (heuristic):** `ChecklistVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistVersion.
- **Source:** `ChecklistVersion.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:648` — `_swap_positions`

- **File:** `apps/checklists/services.py`
- **Function:** `_swap_positions`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=UNKNOWN.
- **Source:** `queryset_model.objects.select_for_update()`

### `apps/checklists/services.py:725` — `update_checklist_template`

- **File:** `apps/checklists/services.py`
- **Function:** `update_checklist_template`
- **Locked model (heuristic):** `ChecklistTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistTemplate.
- **Source:** `ChecklistTemplate.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:781` — `activate_checklist_template`

- **File:** `apps/checklists/services.py`
- **Function:** `activate_checklist_template`
- **Locked model (heuristic):** `ChecklistTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistTemplate.
- **Source:** `template = ChecklistTemplate.objects.select_for_update().filter(pk=template_id).first()`

### `apps/checklists/services.py:802` — `deactivate_checklist_template`

- **File:** `apps/checklists/services.py`
- **Function:** `deactivate_checklist_template`
- **Locked model (heuristic):** `ChecklistTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistTemplate.
- **Source:** `template = ChecklistTemplate.objects.select_for_update().filter(pk=template_id).first()`

### `apps/checklists/services.py:819` — `_allocate_next_version_number`

- **File:** `apps/checklists/services.py`
- **Function:** `_allocate_next_version_number`
- **Locked model (heuristic):** `ChecklistTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistTemplate.
- **Source:** `locked = ChecklistTemplate.objects.select_for_update().filter(pk=template.pk).first()`

### `apps/checklists/services.py:899` — `_lock_item`

- **File:** `apps/checklists/services.py`
- **Function:** `_lock_item`
- **Locked model (heuristic):** `ChecklistItem`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistItem.
- **Source:** `ChecklistItem.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1089` — `create_checklist_version`

- **File:** `apps/checklists/services.py`
- **Function:** `create_checklist_version`
- **Locked model (heuristic):** `ChecklistTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistTemplate.
- **Source:** `ChecklistTemplate.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1198` — `update_checklist_section`

- **File:** `apps/checklists/services.py`
- **Function:** `update_checklist_section`
- **Locked model (heuristic):** `ChecklistSection`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistSection.
- **Source:** `ChecklistSection.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1226` — `remove_checklist_section`

- **File:** `apps/checklists/services.py`
- **Function:** `remove_checklist_section`
- **Locked model (heuristic):** `ChecklistSection`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistSection.
- **Source:** `ChecklistSection.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1256` — `move_checklist_section`

- **File:** `apps/checklists/services.py`
- **Function:** `move_checklist_section`
- **Locked model (heuristic):** `ChecklistSection`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistSection.
- **Source:** `ChecklistSection.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1306` — `add_checklist_item`

- **File:** `apps/checklists/services.py`
- **Function:** `add_checklist_item`
- **Locked model (heuristic):** `ChecklistSection`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistSection.
- **Source:** `ChecklistSection.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1325` — `add_checklist_item`

- **File:** `apps/checklists/services.py`
- **Function:** `add_checklist_item`
- **Locked model (heuristic):** `ChecklistItem`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistItem.
- **Source:** `ChecklistItem.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1741` — `update_checklist_item_option`

- **File:** `apps/checklists/services.py`
- **Function:** `update_checklist_item_option`
- **Locked model (heuristic):** `ChecklistItemOption`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistItemOption.
- **Source:** `ChecklistItemOption.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1786` — `remove_checklist_item_option`

- **File:** `apps/checklists/services.py`
- **Function:** `remove_checklist_item_option`
- **Locked model (heuristic):** `ChecklistItemOption`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistItemOption.
- **Source:** `ChecklistItemOption.objects.select_for_update(of=("self",))`

### `apps/checklists/services.py:1821` — `move_checklist_item_option`

- **File:** `apps/checklists/services.py`
- **Function:** `move_checklist_item_option`
- **Locked model (heuristic):** `ChecklistItemOption`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=checklists; locked=ChecklistItemOption.
- **Source:** `ChecklistItemOption.objects.select_for_update(of=("self",))`

## Domain: correction

### `apps/recording/correction_services.py:241` — `start_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `start_checklist_correction`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=UNKNOWN.
- **Source:** `ChecklistSubmission.objects.select_related(`

### `apps/recording/correction_services.py:257` — `start_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `start_checklist_correction`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=UNKNOWN.
- **Source:** `ChecklistRecord.objects.select_related(`

### `apps/recording/correction_services.py:278` — `start_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `start_checklist_correction`
- **Locked model (heuristic):** `ChecklistCorrection`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=ChecklistCorrection.
- **Source:** `ChecklistCorrection.objects.select_for_update()`

### `apps/recording/correction_services.py:442` — `resubmit_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `resubmit_checklist_correction`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=UNKNOWN.
- **Source:** `ChecklistCorrection.objects.select_related(`

### `apps/recording/correction_services.py:468` — `resubmit_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `resubmit_checklist_correction`
- **Locked model (heuristic):** `ChecklistSubmission`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=ChecklistSubmission.
- **Source:** `ChecklistRecord.objects.select_related(`

### `apps/recording/correction_services.py:517` — `resubmit_checklist_correction`

- **File:** `apps/recording/correction_services.py`
- **Function:** `resubmit_checklist_correction`
- **Locked model (heuristic):** `ChecklistResponse`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=correction; locked=ChecklistResponse.
- **Source:** `ChecklistResponse.objects.select_for_update(of=("self",))`

## Domain: HACCP

### `apps/haccp/services.py:175` — `create_draft_plan_version`

- **File:** `apps/haccp/services.py`
- **Function:** `create_draft_plan_version`
- **Locked model (heuristic):** `HaccpPlan`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=HACCP; locked=HaccpPlan.
- **Source:** `plan = HaccpPlan.objects.select_for_update().filter(pk=plan_id).first()`

### `apps/haccp/services.py:536` — `approve_plan_version`

- **File:** `apps/haccp/services.py`
- **Function:** `approve_plan_version`
- **Locked model (heuristic):** `HaccpPlanVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=HACCP; locked=HaccpPlanVersion.
- **Source:** `HaccpPlanVersion.objects.select_for_update()`

### `apps/haccp/services.py:595` — `retire_plan_version`

- **File:** `apps/haccp/services.py`
- **Function:** `retire_plan_version`
- **Locked model (heuristic):** `HaccpPlanVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=HACCP; locked=HaccpPlanVersion.
- **Source:** `HaccpPlanVersion.objects.select_for_update()`

## Domain: inventory-related quality modules

### `apps/batch_dossier/services.py:147` — `upsert_batch_dossier_policy`

- **File:** `apps/batch_dossier/services.py`
- **Function:** `upsert_batch_dossier_policy`
- **Locked model (heuristic):** `BatchDossierPolicy`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=BatchDossierPolicy.
- **Source:** `policy, _created = BatchDossierPolicy.objects.select_for_update().get_or_create(`

### `apps/batch_genealogy/services.py:150` — `upsert_genealogy_policy`

- **File:** `apps/batch_genealogy/services.py`
- **Function:** `upsert_genealogy_policy`
- **Locked model (heuristic):** `GenealogyPolicy`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=GenealogyPolicy.
- **Source:** `policy, _ = GenealogyPolicy.objects.select_for_update().get_or_create(`

### `apps/dispatch/services.py:248` — `update_dispatch_quality_record`

- **File:** `apps/dispatch/services.py`
- **Function:** `update_dispatch_quality_record`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/dispatch/services.py:330` — `link_vehicle_inspection`

- **File:** `apps/dispatch/services.py`
- **Function:** `link_vehicle_inspection`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/dispatch/services.py:377` — `link_qa_review`

- **File:** `apps/dispatch/services.py`
- **Function:** `link_qa_review`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/dispatch/services.py:423` — `record_cold_chain_temperature`

- **File:** `apps/dispatch/services.py`
- **Function:** `record_cold_chain_temperature`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/dispatch/services.py:487` — `set_dispatch_quantity_line`

- **File:** `apps/dispatch/services.py`
- **Function:** `set_dispatch_quantity_line`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/dispatch/services.py:502` — `set_dispatch_quantity_line`

- **File:** `apps/dispatch/services.py`
- **Function:** `set_dispatch_quantity_line`
- **Locked model (heuristic):** `DispatchQuantityLine`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQuantityLine.
- **Source:** `DispatchQuantityLine.objects.select_for_update()`

### `apps/dispatch/services.py:614` — `complete_dispatch_quality_record`

- **File:** `apps/dispatch/services.py`
- **Function:** `complete_dispatch_quality_record`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `DispatchQualityRecord.objects.select_for_update()`

### `apps/dispatch/services.py:709` — `cancel_dispatch_quality_record`

- **File:** `apps/dispatch/services.py`
- **Function:** `cancel_dispatch_quality_record`
- **Locked model (heuristic):** `DispatchQualityRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=DispatchQualityRecord.
- **Source:** `record = DispatchQualityRecord.objects.select_for_update().filter(pk=dispatch_record_id).first()`

### `apps/quality_quarantine/services.py:174` — `update_quarantine_quantity`

- **File:** `apps/quality_quarantine/services.py`
- **Function:** `update_quarantine_quantity`
- **Locked model (heuristic):** `QualityQuarantineRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=QualityQuarantineRecord.
- **Source:** `record = QualityQuarantineRecord.objects.select_for_update().get(pk=quarantine.pk)`

### `apps/quality_quarantine/services.py:230` — `release_quarantine_record`

- **File:** `apps/quality_quarantine/services.py`
- **Function:** `release_quarantine_record`
- **Locked model (heuristic):** `QualityQuarantineRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=QualityQuarantineRecord.
- **Source:** `record = QualityQuarantineRecord.objects.select_for_update().get(pk=quarantine.pk)`

### `apps/quality_quarantine/services.py:290` — `cancel_quarantine_record`

- **File:** `apps/quality_quarantine/services.py`
- **Function:** `cancel_quarantine_record`
- **Locked model (heuristic):** `QualityQuarantineRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=QualityQuarantineRecord.
- **Source:** `record = QualityQuarantineRecord.objects.select_for_update().get(pk=quarantine.pk)`

### `apps/quality_quarantine/services.py:329` — `record_erp_sync_status`

- **File:** `apps/quality_quarantine/services.py`
- **Function:** `record_erp_sync_status`
- **Locked model (heuristic):** `QualityQuarantineRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=QualityQuarantineRecord.
- **Source:** `record = QualityQuarantineRecord.objects.select_for_update().get(pk=quarantine.pk)`

### `apps/rework/services.py:208` — `authorize_rework_case`

- **File:** `apps/rework/services.py`
- **Function:** `authorize_rework_case`
- **Locked model (heuristic):** `ReworkCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=ReworkCase.
- **Source:** `locked = ReworkCase.objects.select_for_update().get(pk=case.pk)`

### `apps/rework/services.py:234` — `start_rework_case`

- **File:** `apps/rework/services.py`
- **Function:** `start_rework_case`
- **Locked model (heuristic):** `ReworkCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=ReworkCase.
- **Source:** `locked = ReworkCase.objects.select_for_update().get(pk=case.pk)`

### `apps/rework/services.py:318` — `complete_rework_case`

- **File:** `apps/rework/services.py`
- **Function:** `complete_rework_case`
- **Locked model (heuristic):** `ReworkCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=ReworkCase.
- **Source:** `locked = ReworkCase.objects.select_for_update().get(pk=case.pk)`

### `apps/rework/services.py:390` — `cancel_rework_case`

- **File:** `apps/rework/services.py`
- **Function:** `cancel_rework_case`
- **Locked model (heuristic):** `ReworkCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=ReworkCase.
- **Source:** `locked = ReworkCase.objects.select_for_update().get(pk=case.pk)`

### `apps/rework/services.py:425` — `open_rework_reinspection`

- **File:** `apps/rework/services.py`
- **Function:** `open_rework_reinspection`
- **Locked model (heuristic):** `ReworkCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=ReworkCase.
- **Source:** `locked = ReworkCase.objects.select_for_update().get(pk=case.pk)`

### `apps/sampling/services.py:124` — `create_draft_plan_version`

- **File:** `apps/sampling/services.py`
- **Function:** `create_draft_plan_version`
- **Locked model (heuristic):** `SamplingPlan`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=SamplingPlan.
- **Source:** `plan = SamplingPlan.objects.select_for_update().filter(pk=plan_id).first()`

### `apps/sampling/services.py:288` — `approve_plan_version`

- **File:** `apps/sampling/services.py`
- **Function:** `approve_plan_version`
- **Locked model (heuristic):** `SamplingPlanVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=SamplingPlanVersion.
- **Source:** `SamplingPlanVersion.objects.select_for_update()`

### `apps/sampling/services.py:344` — `retire_plan_version`

- **File:** `apps/sampling/services.py`
- **Function:** `retire_plan_version`
- **Locked model (heuristic):** `SamplingPlanVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=inventory-related quality modules; locked=SamplingPlanVersion.
- **Source:** `SamplingPlanVersion.objects.select_for_update()`

## Domain: laboratory

### `apps/laboratory/services.py:172` — `transition_lab_sample`

- **File:** `apps/laboratory/services.py`
- **Function:** `transition_lab_sample`
- **Locked model (heuristic):** `LabSample`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=laboratory; locked=LabSample.
- **Source:** `sample = LabSample.objects.select_for_update().filter(pk=sample_id).first()`

### `apps/laboratory/services.py:217` — `create_lab_test`

- **File:** `apps/laboratory/services.py`
- **Function:** `create_lab_test`
- **Locked model (heuristic):** `LabSample`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=laboratory; locked=LabSample.
- **Source:** `sample = LabSample.objects.select_for_update().filter(pk=sample_id).first()`

### `apps/laboratory/services.py:361` — `verify_lab_result`

- **File:** `apps/laboratory/services.py`
- **Function:** `verify_lab_result`
- **Locked model (heuristic):** `LabResult`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=laboratory; locked=LabResult.
- **Source:** `result = LabResult.objects.select_for_update().filter(pk=result_id).first()`

### `apps/laboratory/services.py:394` — `finalize_lab_result`

- **File:** `apps/laboratory/services.py`
- **Function:** `finalize_lab_result`
- **Locked model (heuristic):** `LabResult`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=laboratory; locked=LabResult.
- **Source:** `result = LabResult.objects.select_for_update().filter(pk=result_id).first()`

### `apps/laboratory/services.py:440` — `amend_lab_result`

- **File:** `apps/laboratory/services.py`
- **Function:** `amend_lab_result`
- **Locked model (heuristic):** `LabResult`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=laboratory; locked=LabResult.
- **Source:** `previous = LabResult.objects.select_for_update().filter(pk=result_id).first()`

## Domain: NCR

### `apps/nonconformance/services.py:188` — `update_nonconformance_case_fields`

- **File:** `apps/nonconformance/services.py`
- **Function:** `update_nonconformance_case_fields`
- **Locked model (heuristic):** `NonConformanceRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=NCR; locked=NonConformanceRecord.
- **Source:** `record = NonConformanceRecord.objects.select_for_update().filter(pk=nonconformance_id).first()`

### `apps/nonconformance/services.py:258` — `transition_nonconformance_status`

- **File:** `apps/nonconformance/services.py`
- **Function:** `transition_nonconformance_status`
- **Locked model (heuristic):** `NonConformanceRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=NCR; locked=NonConformanceRecord.
- **Source:** `record = NonConformanceRecord.objects.select_for_update().filter(pk=nonconformance_id).first()`

### `apps/nonconformance/services.py:308` — `close_nonconformance`

- **File:** `apps/nonconformance/services.py`
- **Function:** `close_nonconformance`
- **Locked model (heuristic):** `NonConformanceRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=NCR; locked=NonConformanceRecord.
- **Source:** `record = NonConformanceRecord.objects.select_for_update().filter(pk=nonconformance_id).first()`

### `apps/nonconformance/services.py:435` — `close_hold_case`

- **File:** `apps/nonconformance/services.py`
- **Function:** `close_hold_case`
- **Locked model (heuristic):** `HoldCase`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=NCR; locked=HoldCase.
- **Source:** `hold = HoldCase.objects.select_for_update().filter(pk=hold_case_id).first()`

## Domain: other

### `apps/access_control/governance_services.py:92` — `set_role_permissions`

- **File:** `apps/access_control/governance_services.py`
- **Function:** `set_role_permissions`
- **Locked model (heuristic):** `Role`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Role.
- **Source:** `role = Role.objects.select_for_update().get(pk=role_id)`

### `apps/access_control/governance_services.py:179` — `update_role_template_permissions`

- **File:** `apps/access_control/governance_services.py`
- **Function:** `update_role_template_permissions`
- **Locked model (heuristic):** `RoleTemplate`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=RoleTemplate.
- **Source:** `template = RoleTemplate.objects.select_for_update().get(pk=template_id)`

### `apps/access_control/governance_services.py:235` — `apply_role_template_to_role`

- **File:** `apps/access_control/governance_services.py`
- **Function:** `apply_role_template_to_role`
- **Locked model (heuristic):** `Role`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Role.
- **Source:** `role = Role.objects.select_for_update().get(pk=role_id)`

### `apps/accounts/services.py:218` — `record_failed_login`

- **File:** `apps/accounts/services.py`
- **Function:** `record_failed_login`
- **Locked model (heuristic):** `User`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=User.
- **Source:** `User.objects.select_for_update().get(pk=user.pk),`

### `apps/accounts/services.py:252` — `record_successful_login`

- **File:** `apps/accounts/services.py`
- **Function:** `record_successful_login`
- **Locked model (heuristic):** `User`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=User.
- **Source:** `User.objects.select_for_update().get(pk=user.pk),`

### `apps/accounts/services.py:364` — `unlock_account`

- **File:** `apps/accounts/services.py`
- **Function:** `unlock_account`
- **Locked model (heuristic):** `User`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=User.
- **Source:** `User.objects.select_for_update().get(pk=user.pk),`

### `apps/customer_complaints/services.py:101` — `upsert_complaint_policy`

- **File:** `apps/customer_complaints/services.py`
- **Function:** `upsert_complaint_policy`
- **Locked model (heuristic):** `CustomerComplaintPolicy`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=CustomerComplaintPolicy.
- **Source:** `policy, _ = CustomerComplaintPolicy.objects.select_for_update().get_or_create(`

### `apps/document_control/services.py:358` — `make_version_effective`

- **File:** `apps/document_control/services.py`
- **Function:** `make_version_effective`
- **Locked model (heuristic):** `QualityDocumentVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=QualityDocumentVersion.
- **Source:** `QualityDocumentVersion.objects.select_for_update()`

### `apps/environmental/services.py:229` — `create_draft_spec_version`

- **File:** `apps/environmental/services.py`
- **Function:** `create_draft_spec_version`
- **Locked model (heuristic):** `MonitoringSpec`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=MonitoringSpec.
- **Source:** `spec = MonitoringSpec.objects.select_for_update().filter(pk=spec_id).first()`

### `apps/environmental/services.py:269` — `add_limit_rule`

- **File:** `apps/environmental/services.py`
- **Function:** `add_limit_rule`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `MonitoringSpecVersion.objects.select_related("spec")`

### `apps/environmental/services.py:306` — `approve_spec_version`

- **File:** `apps/environmental/services.py`
- **Function:** `approve_spec_version`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `MonitoringSpecVersion.objects.select_related("spec")`

### `apps/environmental/services.py:336` — `retire_spec_version`

- **File:** `apps/environmental/services.py`
- **Function:** `retire_spec_version`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `MonitoringSpecVersion.objects.select_related("spec")`

### `apps/evidence/services.py:262` — `retire_evidence_attachment`

- **File:** `apps/evidence/services.py`
- **Function:** `retire_evidence_attachment`
- **Locked model (heuristic):** `EvidenceAttachment`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=EvidenceAttachment.
- **Source:** `attachment = EvidenceAttachment.objects.select_for_update().filter(pk=attachment_id).first()`

### `apps/foreign_body/services.py:304` — `verify_challenge_test`

- **File:** `apps/foreign_body/services.py`
- **Function:** `verify_challenge_test`
- **Locked model (heuristic):** `MetalDetectorChallengeTest`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=MetalDetectorChallengeTest.
- **Source:** `MetalDetectorChallengeTest.objects.select_for_update()`

### `apps/foreign_body/services.py:348` — `void_challenge_test`

- **File:** `apps/foreign_body/services.py`
- **Function:** `void_challenge_test`
- **Locked model (heuristic):** `MetalDetectorChallengeTest`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=MetalDetectorChallengeTest.
- **Source:** `MetalDetectorChallengeTest.objects.select_for_update().filter(pk=challenge_test_id).first()`

### `apps/instruments/services.py:179` — `update_equipment`

- **File:** `apps/instruments/services.py`
- **Function:** `update_equipment`
- **Locked model (heuristic):** `Equipment`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Equipment.
- **Source:** `Equipment.objects.select_for_update(of=("self",))`

### `apps/instruments/services.py:247` — `set_equipment_operational_status`

- **File:** `apps/instruments/services.py`
- **Function:** `set_equipment_operational_status`
- **Locked model (heuristic):** `Equipment`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Equipment.
- **Source:** `equipment = Equipment.objects.select_for_update().filter(pk=equipment_id).first()`

### `apps/instruments/services.py:273` — `activate_equipment`

- **File:** `apps/instruments/services.py`
- **Function:** `activate_equipment`
- **Locked model (heuristic):** `Equipment`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Equipment.
- **Source:** `equipment = Equipment.objects.select_for_update().filter(pk=equipment_id).first()`

### `apps/instruments/services.py:292` — `deactivate_equipment`

- **File:** `apps/instruments/services.py`
- **Function:** `deactivate_equipment`
- **Locked model (heuristic):** `Equipment`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Equipment.
- **Source:** `equipment = Equipment.objects.select_for_update().filter(pk=equipment_id).first()`

### `apps/instruments/services.py:364` — `update_calibration_certificate_metadata`

- **File:** `apps/instruments/services.py`
- **Function:** `update_calibration_certificate_metadata`
- **Locked model (heuristic):** `CalibrationRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=CalibrationRecord.
- **Source:** `CalibrationRecord.objects.select_for_update(of=("self",))`

### `apps/integrations/services.py:299` — `mark_attempt_dead_letter`

- **File:** `apps/integrations/services.py`
- **Function:** `mark_attempt_dead_letter`
- **Locked model (heuristic):** `IntegrationAttempt`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=IntegrationAttempt.
- **Source:** `attempt = IntegrationAttempt.objects.select_for_update().filter(pk=attempt_id).first()`

### `apps/master_data/services.py:224` — `update_fg_product`

- **File:** `apps/master_data/services.py`
- **Function:** `update_fg_product`
- **Locked model (heuristic):** `FGProduct`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=FGProduct.
- **Source:** `FGProduct.objects.select_for_update(of=("self",))`

### `apps/master_data/services.py:285` — `activate_fg_product`

- **File:** `apps/master_data/services.py`
- **Function:** `activate_fg_product`
- **Locked model (heuristic):** `FGProduct`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=FGProduct.
- **Source:** `product = FGProduct.objects.select_for_update().filter(pk=product_id).first()`

### `apps/master_data/services.py:304` — `deactivate_fg_product`

- **File:** `apps/master_data/services.py`
- **Function:** `deactivate_fg_product`
- **Locked model (heuristic):** `FGProduct`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=FGProduct.
- **Source:** `product = FGProduct.objects.select_for_update().filter(pk=product_id).first()`

### `apps/master_data/specification_services.py:243` — `create_specification_version`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `create_specification_version`
- **Locked model (heuristic):** `ProductSpecification`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=ProductSpecification.
- **Source:** `ProductSpecification.objects.select_for_update(of=("self",))`

### `apps/master_data/specification_services.py:290` — `update_draft_specification_version`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `update_draft_specification_version`
- **Locked model (heuristic):** `SpecificationVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationVersion.
- **Source:** `SpecificationVersion.objects.select_for_update(of=("self",))`

### `apps/master_data/specification_services.py:356` — `upsert_specification_parameter`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `upsert_specification_parameter`
- **Locked model (heuristic):** `SpecificationVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationVersion.
- **Source:** `SpecificationVersion.objects.select_for_update(of=("self",))`

### `apps/master_data/specification_services.py:376` — `upsert_specification_parameter`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `upsert_specification_parameter`
- **Locked model (heuristic):** `SpecificationParameter`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationParameter.
- **Source:** `SpecificationParameter.objects.select_for_update()`

### `apps/master_data/specification_services.py:441` — `remove_specification_parameter`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `remove_specification_parameter`
- **Locked model (heuristic):** `SpecificationParameter`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationParameter.
- **Source:** `SpecificationParameter.objects.select_for_update(of=("self",))`

### `apps/master_data/specification_services.py:476` — `approve_specification_version`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `approve_specification_version`
- **Locked model (heuristic):** `SpecificationVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationVersion.
- **Source:** `SpecificationVersion.objects.select_for_update(of=("self",))`

### `apps/master_data/specification_services.py:517` — `retire_specification_version`

- **File:** `apps/master_data/specification_services.py`
- **Function:** `retire_specification_version`
- **Locked model (heuristic):** `SpecificationVersion`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SpecificationVersion.
- **Source:** `SpecificationVersion.objects.select_for_update(of=("self",))`

### `apps/notifications/services.py:242` — `mark_notification_read`

- **File:** `apps/notifications/services.py`
- **Function:** `mark_notification_read`
- **Locked model (heuristic):** `Notification`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Notification.
- **Source:** `notification = Notification.objects.select_for_update().filter(pk=notification_id).first()`

### `apps/notifications/tasks.py:36` — `deliver_notification_email`

- **File:** `apps/notifications/tasks.py`
- **Function:** `deliver_notification_email`
- **Locked model (heuristic):** `NotificationDeliveryAttempt`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=NotificationDeliveryAttempt.
- **Source:** `NotificationDeliveryAttempt.objects.select_for_update()`

### `apps/organizations/services.py:221` — `update_organization`

- **File:** `apps/organizations/services.py`
- **Function:** `update_organization`
- **Locked model (heuristic):** `Organization`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Organization.
- **Source:** `organization = Organization.objects.select_for_update().filter(pk=organization_id).first()`

### `apps/organizations/services.py:347` — `update_site`

- **File:** `apps/organizations/services.py`
- **Function:** `update_site`
- **Locked model (heuristic):** `Site`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Site.
- **Source:** `Site.objects.select_for_update(of=("self",))`

### `apps/organizations/services.py:477` — `update_department`

- **File:** `apps/organizations/services.py`
- **Function:** `update_department`
- **Locked model (heuristic):** `Department`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Department.
- **Source:** `Department.objects.select_for_update(of=("self",))`

### `apps/organizations/services.py:685` — `update_shift`

- **File:** `apps/organizations/services.py`
- **Function:** `update_shift`
- **Locked model (heuristic):** `Shift`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Shift.
- **Source:** `Shift.objects.select_for_update(of=("self",))`

### `apps/organizations/services.py:752` — `activate_shift`

- **File:** `apps/organizations/services.py`
- **Function:** `activate_shift`
- **Locked model (heuristic):** `Shift`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Shift.
- **Source:** `shift = Shift.objects.select_for_update().filter(pk=shift_id).first()`

### `apps/organizations/services.py:771` — `deactivate_shift`

- **File:** `apps/organizations/services.py`
- **Function:** `deactivate_shift`
- **Locked model (heuristic):** `Shift`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=Shift.
- **Source:** `shift = Shift.objects.select_for_update().filter(pk=shift_id).first()`

### `apps/reports/services.py:268` — `execute_report_run_by_id`

- **File:** `apps/reports/services.py`
- **Function:** `execute_report_run_by_id`
- **Locked model (heuristic):** `ReportRun`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=ReportRun.
- **Source:** `run = ReportRun.objects.select_for_update().filter(pk=report_run_id).first()`

### `apps/sanitation/services.py:141` — `create_draft_program_version`

- **File:** `apps/sanitation/services.py`
- **Function:** `create_draft_program_version`
- **Locked model (heuristic):** `SanitationProgram`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SanitationProgram.
- **Source:** `program = SanitationProgram.objects.select_for_update().filter(pk=program_id).first()`

### `apps/sanitation/services.py:196` — `add_sanitation_scope`

- **File:** `apps/sanitation/services.py`
- **Function:** `add_sanitation_scope`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program")`

### `apps/sanitation/services.py:239` — `add_schedule_link`

- **File:** `apps/sanitation/services.py`
- **Function:** `add_schedule_link`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program")`

### `apps/sanitation/services.py:303` — `link_chemical_to_version`

- **File:** `apps/sanitation/services.py`
- **Function:** `link_chemical_to_version`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program")`

### `apps/sanitation/services.py:336` — `approve_program_version`

- **File:** `apps/sanitation/services.py`
- **Function:** `approve_program_version`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program")`

### `apps/sanitation/services.py:377` — `retire_program_version`

- **File:** `apps/sanitation/services.py`
- **Function:** `retire_program_version`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program")`

### `apps/sanitation/services.py:413` — `bind_checklist_template_to_sanitation_program`

- **File:** `apps/sanitation/services.py`
- **Function:** `bind_checklist_template_to_sanitation_program`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SanitationProgramVersion.objects.select_related("program", "program__checklist_template")`

### `apps/supplier_quality/services.py:127` — `update_supplier_quality_profile`

- **File:** `apps/supplier_quality/services.py`
- **Function:** `update_supplier_quality_profile`
- **Locked model (heuristic):** `SupplierQualityProfile`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=SupplierQualityProfile.
- **Source:** `profile = SupplierQualityProfile.objects.select_for_update().filter(pk=profile_id).first()`

### `apps/supplier_quality/services.py:208` — `verify_supplier_certificate`

- **File:** `apps/supplier_quality/services.py`
- **Function:** `verify_supplier_certificate`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=UNKNOWN.
- **Source:** `SupplierCertificate.objects.select_related("profile")`

### `apps/training/services.py:267` — `update_training_record`

- **File:** `apps/training/services.py`
- **Function:** `update_training_record`
- **Locked model (heuristic):** `TrainingRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=TrainingRecord.
- **Source:** `TrainingRecord.objects.select_for_update(of=("self",))`

### `apps/training/services.py:334` — `set_training_record_status`

- **File:** `apps/training/services.py`
- **Function:** `set_training_record_status`
- **Locked model (heuristic):** `TrainingRecord`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=TrainingRecord.
- **Source:** `record = TrainingRecord.objects.select_for_update().filter(pk=training_record_id).first()`

### `apps/training/services.py:384` — `set_training_enforcement_policy`

- **File:** `apps/training/services.py`
- **Function:** `set_training_enforcement_policy`
- **Locked model (heuristic):** `TrainingEnforcementPolicy`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=other; locked=TrainingEnforcementPolicy.
- **Source:** `TrainingEnforcementPolicy.objects.select_for_update()`

## Domain: quality

### `apps/quality/services.py:97` — `create_qa_review`

- **File:** `apps/quality/services.py`
- **Function:** `create_qa_review`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=quality; locked=UNKNOWN.
- **Source:** `ChecklistSubmission.objects.select_related(`

### `apps/quality/services.py:147` — `create_qa_review`

- **File:** `apps/quality/services.py`
- **Function:** `create_qa_review`
- **Locked model (heuristic):** `SupervisorReview`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=quality; locked=SupervisorReview.
- **Source:** `SupervisorReview.objects.select_for_update()`

### `apps/quality/services.py:170` — `create_qa_review`

- **File:** `apps/quality/services.py`
- **Function:** `create_qa_review`
- **Locked model (heuristic):** `QAReview`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=quality; locked=QAReview.
- **Source:** `QAReview.objects.select_for_update()`

## Domain: RCA

### `apps/rca/services.py:93` — `_locked_rca`

- **File:** `apps/rca/services.py`
- **Function:** `_locked_rca`
- **Locked model (heuristic):** `RootCauseAnalysis`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=RCA; locked=RootCauseAnalysis.
- **Source:** `RootCauseAnalysis.objects.select_for_update()`

### `apps/rca/services.py:110` — `_locked_cause`

- **File:** `apps/rca/services.py`
- **Function:** `_locked_cause`
- **Locked model (heuristic):** `RcaCause`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=RCA; locked=RcaCause.
- **Source:** `RcaCause.objects.select_for_update()`

### `apps/rca/services.py:426` — `add_rca_evidence`

- **File:** `apps/rca/services.py`
- **Function:** `add_rca_evidence`
- **Locked model (heuristic):** `RcaCause`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=RCA; locked=RcaCause.
- **Source:** `cause = RcaCause.objects.select_for_update().filter(pk=cause_id, rca=rca).first()`

## Domain: recording

### `apps/recording/services.py:164` — `start_checklist_recording`

- **File:** `apps/recording/services.py`
- **Function:** `start_checklist_recording`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=recording; locked=UNKNOWN.
- **Source:** `ChecklistTask.objects.select_related(`

### `apps/recording/services.py:694` — `save_checklist_draft_responses`

- **File:** `apps/recording/services.py`
- **Function:** `save_checklist_draft_responses`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=recording; locked=UNKNOWN.
- **Source:** `ChecklistRecord.objects.select_related(`

### `apps/recording/services.py:730` — `save_checklist_draft_responses`

- **File:** `apps/recording/services.py`
- **Function:** `save_checklist_draft_responses`
- **Locked model (heuristic):** `ChecklistResponse`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=recording; locked=ChecklistResponse.
- **Source:** `ChecklistResponse.objects.select_for_update().filter(checklist_record_id=record.id)`

### `apps/recording/services.py:939` — `submit_checklist_record`

- **File:** `apps/recording/services.py`
- **Function:** `submit_checklist_record`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=recording; locked=UNKNOWN.
- **Source:** `ChecklistRecord.objects.select_related(`

### `apps/recording/services.py:993` — `submit_checklist_record`

- **File:** `apps/recording/services.py`
- **Function:** `submit_checklist_record`
- **Locked model (heuristic):** `ChecklistResponse`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=recording; locked=ChecklistResponse.
- **Source:** `ChecklistResponse.objects.select_for_update(of=("self",))`

## Domain: reviews

### `apps/reviews/governance.py:205` — `upsert_supervisor_review_governance_policy`

- **File:** `apps/reviews/governance.py`
- **Function:** `upsert_supervisor_review_governance_policy`
- **Locked model (heuristic):** `SupervisorReviewGovernancePolicy`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=reviews; locked=SupervisorReviewGovernancePolicy.
- **Source:** `SupervisorReviewGovernancePolicy.objects.select_for_update()`

### `apps/reviews/services.py:89` — `create_supervisor_review`

- **File:** `apps/reviews/services.py`
- **Function:** `create_supervisor_review`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=reviews; locked=UNKNOWN.
- **Source:** `ChecklistSubmission.objects.select_related(`

### `apps/reviews/services.py:140` — `create_supervisor_review`

- **File:** `apps/reviews/services.py`
- **Function:** `create_supervisor_review`
- **Locked model (heuristic):** `SupervisorReview`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=reviews; locked=SupervisorReview.
- **Source:** `SupervisorReview.objects.select_for_update()`

## Domain: scheduling

### `apps/scheduling/applicability.py:537` — `update_checklist_applicability_rule`

- **File:** `apps/scheduling/applicability.py`
- **Function:** `update_checklist_applicability_rule`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=UNKNOWN.
- **Source:** `ChecklistApplicabilityRule.objects.select_related(`

### `apps/scheduling/applicability.py:604` — `deactivate_checklist_applicability_rule`

- **File:** `apps/scheduling/applicability.py`
- **Function:** `deactivate_checklist_applicability_rule`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=UNKNOWN.
- **Source:** `ChecklistApplicabilityRule.objects.select_related(`

### `apps/scheduling/assignment.py:278` — `assign_checklist_task`

- **File:** `apps/scheduling/assignment.py`
- **Function:** `assign_checklist_task`
- **Locked model (heuristic):** `ChecklistTask`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=ChecklistTask.
- **Source:** `ChecklistTask.objects.select_for_update(of=("self",))`

### `apps/scheduling/assignment.py:354` — `unassign_checklist_task`

- **File:** `apps/scheduling/assignment.py`
- **Function:** `unassign_checklist_task`
- **Locked model (heuristic):** `ChecklistTask`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=ChecklistTask.
- **Source:** `ChecklistTask.objects.select_for_update(of=("self",))`

### `apps/scheduling/batch_events.py:337` — `process_external_batch_event`

- **File:** `apps/scheduling/batch_events.py`
- **Function:** `process_external_batch_event`
- **Locked model (heuristic):** `ExternalBatchEvent`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=ExternalBatchEvent.
- **Source:** `ExternalBatchEvent.objects.select_for_update(of=("self",))`

### `apps/scheduling/due.py:229` — `set_checklist_task_due_window`

- **File:** `apps/scheduling/due.py`
- **Function:** `set_checklist_task_due_window`
- **Locked model (heuristic):** `ChecklistTask`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=ChecklistTask.
- **Source:** `ChecklistTask.objects.select_for_update(of=("self",))`

### `apps/scheduling/generation.py:636` — `deactivate_checklist_schedule`

- **File:** `apps/scheduling/generation.py`
- **Function:** `deactivate_checklist_schedule`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=UNKNOWN.
- **Source:** `ChecklistSchedule.objects.select_related("organization")`

### `apps/scheduling/services.py:292` — `cancel_checklist_task`

- **File:** `apps/scheduling/services.py`
- **Function:** `cancel_checklist_task`
- **Locked model (heuristic):** `UNKNOWN`
- **Invariant protected:** serialize competing writes on this row/aggregate (exact invariant requires service-level review)
- **Competing operation:** concurrent service calls touching the same entity
- **Failure if race occurs:** duplicate decisions, lost updates, invalid state transitions, or broken idempotency
- **Proposed Mongo replacement:** Optimistic conditional transition (compare-and-set) via `apps.core.optimistic_transition` — unique constraint + filter(status/version/decision) update; retry on conflict. Domain=scheduling; locked=UNKNOWN.
- **Source:** `ChecklistTask.objects.select_related(`


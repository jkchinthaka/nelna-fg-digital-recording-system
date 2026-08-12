# Mongo Full Compatibility Inventory

**Generated (UTC):** 2026-08-12T10:13:47Z  
**Files scanned:** 957  
**Findings:** 1511  

Exact machine-generated inventory. Do not treat approximate historical counts as current.

## Token summary

| Token | Count | Risk band |
| --- | ---: | --- |
| `select_related` | 414 | LOW-MEDIUM |
| `transaction.atomic` | 396 | MEDIUM |
| `select_for_update` | 137 | HIGH |
| `get_or_create` | 118 | MEDIUM |
| `IntegrityError` | 113 | MEDIUM |
| `Q` | 113 | LOW-MEDIUM |
| `Lower` | 87 | LOW-MEDIUM |
| `prefetch_related` | 34 | HIGH |
| `update_or_create` | 17 | MEDIUM |
| `psql` | 14 | LOW-MEDIUM |
| `Max` | 11 | LOW-MEDIUM |
| `aggregate` | 10 | LOW-MEDIUM |
| `F` | 8 | LOW-MEDIUM |
| `UniqueConstraint` | 8 | LOW-MEDIUM |
| `annotate` | 8 | LOW-MEDIUM |
| `Count` | 6 | LOW-MEDIUM |
| `pg_dump` | 5 | LOW-MEDIUM |
| `bulk_create` | 3 | LOW-MEDIUM |
| `pg_restore` | 3 | LOW-MEDIUM |
| `OuterRef` | 2 | HIGH |
| `Subquery` | 2 | HIGH |
| `dumpdata` | 1 | LOW-MEDIUM |
| `loaddata` | 1 | LOW-MEDIUM |

## Findings

### MC-0001

- **ID:** MC-0001
- **File:** `apps/checklists/services.py:208`
- **Function/Class:** `_next_section_position`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0002

- **ID:** MC-0002
- **File:** `apps/checklists/services.py:219`
- **Function/Class:** `_next_item_position`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0003

- **ID:** MC-0003
- **File:** `apps/checklists/services.py:822`
- **Function/Class:** `_allocate_next_version_number`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0004

- **ID:** MC-0004
- **File:** `apps/checklists/services.py:893`
- **Function/Class:** `_next_option_position`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0005

- **ID:** MC-0005
- **File:** `apps/mongo_poc/services.py:89`
- **Function/Class:** `allocate_version_number`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0006

- **ID:** MC-0006
- **File:** `apps/mongo_poc/services.py:112`
- **Function/Class:** `submit_immutable_snapshot`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0007

- **ID:** MC-0007
- **File:** `apps/process_fmea/services.py:415`
- **Function/Class:** `record_failure_mode_assessment`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0008

- **ID:** MC-0008
- **File:** `apps/process_fmea/services.py:805`
- **Function/Class:** `revise_process_fmea`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0009

- **ID:** MC-0009
- **File:** `apps/quality_risks/services.py:375`
- **Function/Class:** `record_risk_assessment`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0010

- **ID:** MC-0010
- **File:** `apps/recording/correction_services.py:539`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `aggregate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0011

- **ID:** MC-0011
- **File:** `apps/checklists/proposal_loader.py:439`
- **Function/Class:** `_get_org_template`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0012

- **ID:** MC-0012
- **File:** `apps/checklists/selectors.py:108`
- **Function/Class:** `list_checklist_templates`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0013

- **ID:** MC-0013
- **File:** `apps/checklists/selectors.py:153`
- **Function/Class:** `list_checklist_versions`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0014

- **ID:** MC-0014
- **File:** `apps/compliance_mapping/selectors.py:87`
- **Function/Class:** `report_mapping_status`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0015

- **ID:** MC-0015
- **File:** `apps/quality_audits/selectors.py:96`
- **Function/Class:** `report_audit_status`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0016

- **ID:** MC-0016
- **File:** `apps/quality_audits/selectors.py:119`
- **Function/Class:** `report_site_process_trends`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0017

- **ID:** MC-0017
- **File:** `apps/quality_risks/selectors.py:89`
- **Function/Class:** `report_high_rated_risks`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0018

- **ID:** MC-0018
- **File:** `apps/reviews/selectors.py:54`
- **Function/Class:** `_base_pending_queryset`
- **Token:** `annotate` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0019

- **ID:** MC-0019
- **File:** `apps/recording/correction_services.py:219`
- **Function/Class:** `_clone_working_responses_from_snapshot`
- **Token:** `bulk_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0020

- **ID:** MC-0020
- **File:** `apps/recording/correction_services.py:612`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `bulk_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0021

- **ID:** MC-0021
- **File:** `apps/recording/services.py:1082`
- **Function/Class:** `submit_checklist_record`
- **Token:** `bulk_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0022

- **ID:** MC-0022
- **File:** `apps/checklists/selectors.py:111`
- **Function/Class:** `list_checklist_templates`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0023

- **ID:** MC-0023
- **File:** `apps/checklists/selectors.py:155`
- **Function/Class:** `list_checklist_versions`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0024

- **ID:** MC-0024
- **File:** `apps/checklists/selectors.py:156`
- **Function/Class:** `list_checklist_versions`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0025

- **ID:** MC-0025
- **File:** `apps/compliance_mapping/selectors.py:89`
- **Function/Class:** `report_mapping_status`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0026

- **ID:** MC-0026
- **File:** `apps/quality_audits/selectors.py:98`
- **Function/Class:** `report_audit_status`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0027

- **ID:** MC-0027
- **File:** `apps/quality_audits/selectors.py:121`
- **Function/Class:** `report_site_process_trends`
- **Token:** `Count` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0028

- **ID:** MC-0028
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:36`
- **Function/Class:** `<text>`
- **Token:** `dumpdata` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0029

- **ID:** MC-0029
- **File:** `apps/access_control/decorators.py:15`
- **Function/Class:** `<module>`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0030

- **ID:** MC-0030
- **File:** `apps/access_control/decorators.py:22`
- **Function/Class:** `permission_required`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0031

- **ID:** MC-0031
- **File:** `apps/access_control/decorators.py:22`
- **Function/Class:** `permission_required`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0032

- **ID:** MC-0032
- **File:** `apps/access_control/decorators.py:23`
- **Function/Class:** `decorator`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0033

- **ID:** MC-0033
- **File:** `apps/access_control/decorators.py:23`
- **Function/Class:** `decorator`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0034

- **ID:** MC-0034
- **File:** `apps/core/persistence/transactions.py:20`
- **Function/Class:** `<module>`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0035

- **ID:** MC-0035
- **File:** `apps/core/persistence/transactions.py:47`
- **Function/Class:** `on_commit`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0036

- **ID:** MC-0036
- **File:** `apps/reviews/selectors.py:67`
- **Function/Class:** `_base_pending_queryset`
- **Token:** `F` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0037

- **ID:** MC-0037
- **File:** `tests/test_enterprise_ui.py:18`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0038

- **ID:** MC-0038
- **File:** `tests/test_phase18_safe_ai.py:29`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0039

- **ID:** MC-0039
- **File:** `apps/batch_dossier/services.py:147`
- **Function/Class:** `upsert_batch_dossier_policy`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0040

- **ID:** MC-0040
- **File:** `tests/test_phase35_batch_dossier.py:79`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0041

- **ID:** MC-0041
- **File:** `apps/batch_genealogy/services.py:150`
- **Function/Class:** `upsert_genealogy_policy`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0042

- **ID:** MC-0042
- **File:** `tests/test_phase36_batch_genealogy.py:57`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0043

- **ID:** MC-0043
- **File:** `apps/change_control/services.py:175`
- **Function/Class:** `record_change_impact_assessment`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0044

- **ID:** MC-0044
- **File:** `tests/test_phase44_change_control.py:50`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0045

- **ID:** MC-0045
- **File:** `tests/test_phase30_allergen_changeover.py:60`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0046

- **ID:** MC-0046
- **File:** `tests/test_checklist_foundation.py:44`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0047

- **ID:** MC-0047
- **File:** `tests/test_checklist_foundation.py:120`
- **Function/Class:** `test_optional_product_same_org_only`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0048

- **ID:** MC-0048
- **File:** `tests/test_checklist_foundation.py:125`
- **Function/Class:** `test_optional_product_same_org_only`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0049

- **ID:** MC-0049
- **File:** `tests/test_checklist_governance.py:52`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0050

- **ID:** MC-0050
- **File:** `tests/test_checklist_response_schema.py:47`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0051

- **ID:** MC-0051
- **File:** `tests/test_checklist_ui.py:33`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0052

- **ID:** MC-0052
- **File:** `tests/test_fg_qa_001_draft_loader.py:48`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0053

- **ID:** MC-0053
- **File:** `tests/test_phase06l_control_point_metadata.py:53`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0054

- **ID:** MC-0054
- **File:** `tests/test_phase06m_measurement_semantics.py:59`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0055

- **ID:** MC-0055
- **File:** `tests/test_phase06n_fg_qa_001_validation.py:72`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0056

- **ID:** MC-0056
- **File:** `tests/test_phase07d_effective_version.py:46`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0057

- **ID:** MC-0057
- **File:** `tests/test_phase46_compliance_mapping.py:70`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0058

- **ID:** MC-0058
- **File:** `tests/test_phase10b_workflow_lifecycle.py:58`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0059

- **ID:** MC-0059
- **File:** `apps/customer_complaints/services.py:101`
- **Function/Class:** `upsert_complaint_policy`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0060

- **ID:** MC-0060
- **File:** `apps/customer_complaints/services.py:145`
- **Function/Class:** `upsert_category_config`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0061

- **ID:** MC-0061
- **File:** `apps/customer_complaints/services.py:352`
- **Function/Class:** `upsert_batch_trace`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0062

- **ID:** MC-0062
- **File:** `apps/customer_complaints/services.py:434`
- **Function/Class:** `link_complaint_evidence`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0063

- **ID:** MC-0063
- **File:** `tests/test_complaint_operator_views.py:22`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0064

- **ID:** MC-0064
- **File:** `tests/test_complaint_operator_views.py:33`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0065

- **ID:** MC-0065
- **File:** `tests/test_phase39_customer_complaints.py:53`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0066

- **ID:** MC-0066
- **File:** `tests/test_dispatch_operator_views.py:22`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0067

- **ID:** MC-0067
- **File:** `tests/test_dispatch_operator_views.py:33`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0068

- **ID:** MC-0068
- **File:** `tests/test_phase13_dispatch_quality.py:44`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0069

- **ID:** MC-0069
- **File:** `tests/test_phase43_document_control.py:56`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0070

- **ID:** MC-0070
- **File:** `tests/test_phase28_environmental_monitoring.py:65`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0071

- **ID:** MC-0071
- **File:** `tests/test_phase11_evidence_attachments.py:57`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0072

- **ID:** MC-0072
- **File:** `tests/test_phase26_foreign_body_control.py:66`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0073

- **ID:** MC-0073
- **File:** `tests/test_phase23_haccp_foundation.py:52`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0074

- **ID:** MC-0074
- **File:** `tests/test_phase23_haccp_foundation.py:178`
- **Function/Class:** `test_control_point_link_and_checklist_historical_integrity`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0075

- **ID:** MC-0075
- **File:** `tests/test_phase23_haccp_foundation.py:295`
- **Function/Class:** `test_published_checklist_binding_immutable`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0076

- **ID:** MC-0076
- **File:** `tests/test_phase23_haccp_foundation.py:490`
- **Function/Class:** `test_snapshot_prefers_frozen_binding_context`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0077

- **ID:** MC-0077
- **File:** `tests/test_phase05d_equipment_calibration.py:60`
- **Function/Class:** `_equip_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0078

- **ID:** MC-0078
- **File:** `tests/test_phase25_device_traceability.py:56`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0079

- **ID:** MC-0079
- **File:** `tests/test_phase17_bileeta_boundary.py:45`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0080

- **ID:** MC-0080
- **File:** `tests/test_phase34_ipqc_workflows.py:80`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0081

- **ID:** MC-0081
- **File:** `tests/test_phase33_iqc_workflow.py:61`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0082

- **ID:** MC-0082
- **File:** `apps/laboratory/policy.py:46`
- **Function/Class:** `get_or_init_policy`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0083

- **ID:** MC-0083
- **File:** `tests/test_lab_haccp_operator_views.py:23`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0084

- **ID:** MC-0084
- **File:** `tests/test_lab_haccp_operator_views.py:34`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0085

- **ID:** MC-0085
- **File:** `tests/test_phase22_laboratory_foundation.py:47`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0086

- **ID:** MC-0086
- **File:** `tests/test_fg_product_authz_hardening.py:30`
- **Function/Class:** `_product_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0087

- **ID:** MC-0087
- **File:** `tests/test_fg_product_foundation.py:32`
- **Function/Class:** `_product_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0088

- **ID:** MC-0088
- **File:** `tests/test_fg_product_ui.py:23`
- **Function/Class:** `_product_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0089

- **ID:** MC-0089
- **File:** `tests/test_phase05c_fg_product_master.py:38`
- **Function/Class:** `_product_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0090

- **ID:** MC-0090
- **File:** `tests/test_phase06o_product_specifications.py:63`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0091

- **ID:** MC-0091
- **File:** `apps/mongo_poc/services.py:36`
- **Function/Class:** `get_or_create_organization`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0092

- **ID:** MC-0092
- **File:** `tests/test_ncr_capa_operator_views.py:23`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0093

- **ID:** MC-0093
- **File:** `tests/test_ncr_capa_operator_views.py:34`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0094

- **ID:** MC-0094
- **File:** `tests/test_phase12_ncr_hold_capa.py:50`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0095

- **ID:** MC-0095
- **File:** `apps/notifications/services.py:209`
- **Function/Class:** `_enqueue_email_delivery`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0096

- **ID:** MC-0096
- **File:** `tests/test_phase15_notifications.py:38`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0097

- **ID:** MC-0097
- **File:** `tests/test_shift_foundation.py:45`
- **Function/Class:** `_shift_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0098

- **ID:** MC-0098
- **File:** `tests/test_shift_ui.py:30`
- **Function/Class:** `_shift_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0099

- **ID:** MC-0099
- **File:** `tests/test_phase29_label_artwork_control.py:55`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0100

- **ID:** MC-0100
- **File:** `tests/test_phase29_packaging_artwork.py:51`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0101

- **ID:** MC-0101
- **File:** `tests/test_phase48_process_fmea.py:72`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0102

- **ID:** MC-0102
- **File:** `tests/test_phase40_product_returns.py:53`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0103

- **ID:** MC-0103
- **File:** `tests/test_phase10a_qa_review.py:55`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0104

- **ID:** MC-0104
- **File:** `apps/quality_audits/services.py:636`
- **Function/Class:** `upsert_finding_code`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0105

- **ID:** MC-0105
- **File:** `tests/test_phase45_quality_audits.py:83`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0106

- **ID:** MC-0106
- **File:** `tests/test_phase41_quality_quarantine.py:49`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0107

- **ID:** MC-0107
- **File:** `tests/test_quarantine_operator_views.py:22`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0108

- **ID:** MC-0108
- **File:** `tests/test_quarantine_operator_views.py:33`
- **Function/Class:** `_grant`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0109

- **ID:** MC-0109
- **File:** `apps/quality_risks/services.py:656`
- **Function/Class:** `upsert_risk_category`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0110

- **ID:** MC-0110
- **File:** `tests/test_phase47_quality_risks.py:63`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0111

- **ID:** MC-0111
- **File:** `tests/test_phase49_rca.py:51`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0112

- **ID:** MC-0112
- **File:** `tests/test_pre_uat_rca_hardening.py:41`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0113

- **ID:** MC-0113
- **File:** `apps/recall/mock_services.py:87`
- **Function/Class:** `_ensure_metrics`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0114

- **ID:** MC-0114
- **File:** `apps/recall/services.py:319`
- **Function/Class:** `add_affected_product`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0115

- **ID:** MC-0115
- **File:** `apps/recall/services.py:366`
- **Function/Class:** `add_affected_batch`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0116

- **ID:** MC-0116
- **File:** `apps/recall/services.py:476`
- **Function/Class:** `expand_genealogy_for_recall`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0117

- **ID:** MC-0117
- **File:** `tests/test_phase37_product_recall.py:60`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0118

- **ID:** MC-0118
- **File:** `tests/test_phase37_recall_management.py:47`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0119

- **ID:** MC-0119
- **File:** `tests/test_phase38_mock_recall.py:57`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0120

- **ID:** MC-0120
- **File:** `tests/test_phase31_raw_material_quality.py:48`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0121

- **ID:** MC-0121
- **File:** `apps/recording/synthetic_demo.py:74`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0122

- **ID:** MC-0122
- **File:** `tests/test_phase06h_repeating_samples.py:44`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0123

- **ID:** MC-0123
- **File:** `tests/test_phase06i_calculated_fields.py:47`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0124

- **ID:** MC-0124
- **File:** `tests/test_phase06j_conditional_fields.py:43`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0125

- **ID:** MC-0125
- **File:** `tests/test_phase06k_item_evaluation.py:54`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0126

- **ID:** MC-0126
- **File:** `tests/test_phase08a_draft_recording.py:46`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0127

- **ID:** MC-0127
- **File:** `tests/test_phase08b_submission.py:51`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0128

- **ID:** MC-0128
- **File:** `tests/test_phase08c_recording_hardening.py:40`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0129

- **ID:** MC-0129
- **File:** `tests/test_phase09b_correction.py:60`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0130

- **ID:** MC-0130
- **File:** `tests/test_phase16_reporting.py:42`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0131

- **ID:** MC-0131
- **File:** `apps/reviews/governance.py:245`
- **Function/Class:** `_technical_review_delegate_role`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0132

- **ID:** MC-0132
- **File:** `tests/test_phase09a_supervisor_review.py:57`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0133

- **ID:** MC-0133
- **File:** `tests/test_phase09c_supervisor_governance.py:66`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0134

- **ID:** MC-0134
- **File:** `tests/test_phase42_rework.py:63`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0135

- **ID:** MC-0135
- **File:** `tests/test_phase24_sampling_coverage.py:54`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0136

- **ID:** MC-0136
- **File:** `tests/test_phase24_sampling_coverage.py:252`
- **Function/Class:** `test_binding_rejects_non_repeating_and_cross_org`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0137

- **ID:** MC-0137
- **File:** `tests/test_phase24_sampling_engine.py:52`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0138

- **ID:** MC-0138
- **File:** `tests/test_phase24_sampling_engine.py:220`
- **Function/Class:** `test_historical_snapshot_binding`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0139

- **ID:** MC-0139
- **File:** `tests/test_phase24_sampling_engine.py:430`
- **Function/Class:** `test_dimension_filters_and_snapshot_helpers`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0140

- **ID:** MC-0140
- **File:** `tests/test_phase27_sanitation_management.py:73`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0141

- **ID:** MC-0141
- **File:** `tests/test_batch_checklist_task.py:41`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0142

- **ID:** MC-0142
- **File:** `tests/test_batch_checklist_task.py:78`
- **Function/Class:** `_grant_checklist_manage`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0143

- **ID:** MC-0143
- **File:** `tests/test_batch_checklist_task.py:83`
- **Function/Class:** `_grant_checklist_manage`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0144

- **ID:** MC-0144
- **File:** `tests/test_phase07b_integration_rbac.py:43`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0145

- **ID:** MC-0145
- **File:** `tests/test_phase07b_integration_rbac.py:68`
- **Function/Class:** `_grant_checklist_manage`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0146

- **ID:** MC-0146
- **File:** `tests/test_phase07b_integration_rbac.py:73`
- **Function/Class:** `_grant_checklist_manage`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0147

- **ID:** MC-0147
- **File:** `tests/test_phase07c_applicability_engine.py:56`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0148

- **ID:** MC-0148
- **File:** `tests/test_phase07e_recurring_schedules.py:59`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0149

- **ID:** MC-0149
- **File:** `tests/test_phase07f_batch_event_generation.py:59`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0150

- **ID:** MC-0150
- **File:** `tests/test_phase07g_task_assignment.py:53`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0151

- **ID:** MC-0151
- **File:** `tests/test_phase07h_due_management.py:49`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0152

- **ID:** MC-0152
- **File:** `tests/test_phase32_supplier_quality.py:40`
- **Function/Class:** `_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0153

- **ID:** MC-0153
- **File:** `tests/test_phase05e_training_foundation.py:62`
- **Function/Class:** `_trn_perm`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0154

- **ID:** MC-0154
- **File:** `tests/factories.py:110`
- **Function/Class:** `make_permission`
- **Token:** `get_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0155

- **ID:** MC-0155
- **File:** `apps/access_control/admin.py:74`
- **Function/Class:** `save_model`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0156

- **ID:** MC-0156
- **File:** `apps/access_control/services.py:375`
- **Function/Class:** `assign_role`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0157

- **ID:** MC-0157
- **File:** `tests/test_assignment_uniqueness.py:29`
- **Function/Class:** `test_db_rejects_duplicate_active_global_assignment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0158

- **ID:** MC-0158
- **File:** `tests/test_assignment_uniqueness.py:39`
- **Function/Class:** `test_db_rejects_duplicate_active_organization_assignment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0159

- **ID:** MC-0159
- **File:** `tests/test_assignment_uniqueness.py:52`
- **Function/Class:** `test_db_rejects_duplicate_active_site_assignment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0160

- **ID:** MC-0160
- **File:** `tests/test_assignment_uniqueness.py:73`
- **Function/Class:** `test_db_rejects_duplicate_active_department_assignment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0161

- **ID:** MC-0161
- **File:** `tests/test_assignment_uniqueness.py:139`
- **Function/Class:** `test_reactivating_duplicate_assignment_rejected`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0162

- **ID:** MC-0162
- **File:** `tests/test_assignment_uniqueness.py:190`
- **Function/Class:** `worker`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0163

- **ID:** MC-0163
- **File:** `tests/test_auth.py:48`
- **Function/Class:** `test_employee_code_case_insensitive_unique`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0164

- **ID:** MC-0164
- **File:** `apps/batch_genealogy/services.py:356`
- **Function/Class:** `ingest_erp_genealogy_edge`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0165

- **ID:** MC-0165
- **File:** `apps/capa/services.py:66`
- **Function/Class:** `_code_conflict`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0166

- **ID:** MC-0166
- **File:** `apps/capa/services.py:121`
- **Function/Class:** `create_corrective_action`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0167

- **ID:** MC-0167
- **File:** `apps/changeover/services.py:103`
- **Function/Class:** `create_allergen_reference`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0168

- **ID:** MC-0168
- **File:** `apps/checklists/services.py:171`
- **Function/Class:** `_reraise_template_persistence_error`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0169

- **ID:** MC-0169
- **File:** `apps/checklists/services.py:702`
- **Function/Class:** `create_checklist_template`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0170

- **ID:** MC-0170
- **File:** `apps/checklists/services.py:767`
- **Function/Class:** `update_checklist_template`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0171

- **ID:** MC-0171
- **File:** `apps/checklists/services.py:1125`
- **Function/Class:** `create_checklist_version`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0172

- **ID:** MC-0172
- **File:** `apps/checklists/services.py:1183`
- **Function/Class:** `add_checklist_section`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0173

- **ID:** MC-0173
- **File:** `apps/checklists/services.py:1217`
- **Function/Class:** `update_checklist_section`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0174

- **ID:** MC-0174
- **File:** `apps/checklists/services.py:1395`
- **Function/Class:** `add_checklist_item`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0175

- **ID:** MC-0175
- **File:** `apps/checklists/services.py:1576`
- **Function/Class:** `update_checklist_item`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0176

- **ID:** MC-0176
- **File:** `apps/checklists/services.py:1721`
- **Function/Class:** `add_checklist_item_option`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0177

- **ID:** MC-0177
- **File:** `apps/checklists/services.py:1772`
- **Function/Class:** `update_checklist_item_option`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0178

- **ID:** MC-0178
- **File:** `apps/core/optimistic_transition.py:137`
- **Function/Class:** `create_immutable_unique`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0179

- **ID:** MC-0179
- **File:** `apps/dispatch/services.py:70`
- **Function/Class:** `_code_conflict`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0180

- **ID:** MC-0180
- **File:** `apps/dispatch/services.py:204`
- **Function/Class:** `create_dispatch_quality_record`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0181

- **ID:** MC-0181
- **File:** `apps/environmental/services.py:130`
- **Function/Class:** `create_monitoring_point`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0182

- **ID:** MC-0182
- **File:** `apps/environmental/services.py:173`
- **Function/Class:** `create_monitoring_parameter`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0183

- **ID:** MC-0183
- **File:** `apps/environmental/services.py:205`
- **Function/Class:** `create_monitoring_spec`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0184

- **ID:** MC-0184
- **File:** `apps/environmental/services.py:291`
- **Function/Class:** `add_limit_rule`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0185

- **ID:** MC-0185
- **File:** `apps/foreign_body/services.py:128`
- **Function/Class:** `create_test_piece`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0186

- **ID:** MC-0186
- **File:** `apps/foreign_body/services.py:178`
- **Function/Class:** `create_schedule_rule`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0187

- **ID:** MC-0187
- **File:** `apps/haccp/services.py:149`
- **Function/Class:** `create_haccp_plan`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0188

- **ID:** MC-0188
- **File:** `apps/haccp/services.py:245`
- **Function/Class:** `add_process_step`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0189

- **ID:** MC-0189
- **File:** `apps/haccp/services.py:294`
- **Function/Class:** `add_hazard`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0190

- **ID:** MC-0190
- **File:** `apps/haccp/services.py:333`
- **Function/Class:** `add_control_measure`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0191

- **ID:** MC-0191
- **File:** `apps/haccp/services.py:378`
- **Function/Class:** `add_control_point`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0192

- **ID:** MC-0192
- **File:** `apps/instruments/services.py:92`
- **Function/Class:** `_reraise_equipment_unique`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0193

- **ID:** MC-0193
- **File:** `apps/instruments/services.py:151`
- **Function/Class:** `create_equipment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0194

- **ID:** MC-0194
- **File:** `apps/instruments/services.py:229`
- **Function/Class:** `update_equipment`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0195

- **ID:** MC-0195
- **File:** `tests/test_phase05d_equipment_calibration.py:372`
- **Function/Class:** `test_authorization_and_validation_coverage_edges`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0196

- **ID:** MC-0196
- **File:** `apps/integrations/services.py:151`
- **Function/Class:** `ingest_inbound_batch_event`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0197

- **ID:** MC-0197
- **File:** `apps/ipqc/services.py:237`
- **Function/Class:** `create_ipqc_process_check_definition`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0198

- **ID:** MC-0198
- **File:** `apps/ipqc/services.py:377`
- **Function/Class:** `generate_ipqc_case`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0199

- **ID:** MC-0199
- **File:** `apps/iqc/services.py:537`
- **Function/Class:** `ingest_incoming_receipt_event`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0200

- **ID:** MC-0200
- **File:** `apps/laboratory/services.py:138`
- **Function/Class:** `register_lab_sample`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0201

- **ID:** MC-0201
- **File:** `apps/laboratory/services.py:235`
- **Function/Class:** `create_lab_test`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0202

- **ID:** MC-0202
- **File:** `apps/laboratory/services.py:523`
- **Function/Class:** `create_test_method_reference`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0203

- **ID:** MC-0203
- **File:** `apps/laboratory/services.py:568`
- **Function/Class:** `create_lab_test_parameter`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0204

- **ID:** MC-0204
- **File:** `apps/master_data/services.py:127`
- **Function/Class:** `_reraise_product_persistence_error`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0205

- **ID:** MC-0205
- **File:** `apps/master_data/services.py:191`
- **Function/Class:** `create_fg_product`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0206

- **ID:** MC-0206
- **File:** `apps/master_data/services.py:271`
- **Function/Class:** `update_fg_product`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0207

- **ID:** MC-0207
- **File:** `apps/master_data/specification_services.py:204`
- **Function/Class:** `create_product_specification`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0208

- **ID:** MC-0208
- **File:** `apps/master_data/specification_services.py:205`
- **Function/Class:** `create_product_specification`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0209

- **ID:** MC-0209
- **File:** `tests/test_fg_product_foundation.py:119`
- **Function/Class:** `test_db_unique_constraint`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0210

- **ID:** MC-0210
- **File:** `apps/mongo_poc/services.py:47`
- **Function/Class:** `create_employee_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0211

- **ID:** MC-0211
- **File:** `apps/mongo_poc/services.py:66`
- **Function/Class:** `create_task_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0212

- **ID:** MC-0212
- **File:** `apps/mongo_poc/services.py:81`
- **Function/Class:** `start_record_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0213

- **ID:** MC-0213
- **File:** `apps/mongo_poc/services.py:97`
- **Function/Class:** `allocate_version_number`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0214

- **ID:** MC-0214
- **File:** `apps/mongo_poc/services.py:137`
- **Function/Class:** `_is_retryable_db_error`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0215

- **ID:** MC-0215
- **File:** `apps/mongo_poc/services.py:178`
- **Function/Class:** `start_supervisor_review_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0216

- **ID:** MC-0216
- **File:** `apps/mongo_poc/services.py:194`
- **Function/Class:** `start_correction_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0217

- **ID:** MC-0217
- **File:** `apps/mongo_poc/services.py:212`
- **Function/Class:** `start_qa_review_idempotent`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0218

- **ID:** MC-0218
- **File:** `apps/mongo_poc/services.py:226`
- **Function/Class:** `idempotent_request`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0219

- **ID:** MC-0219
- **File:** `tests/test_poc_guarantees.py:267`
- **Function/Class:** `test_duplicate_employee_raises_integrity_error_raw`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0220

- **ID:** MC-0220
- **File:** `apps/nonconformance/services.py:79`
- **Function/Class:** `_code_conflict`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0221

- **ID:** MC-0221
- **File:** `apps/nonconformance/services.py:146`
- **Function/Class:** `create_nonconformance`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0222

- **ID:** MC-0222
- **File:** `apps/nonconformance/services.py:399`
- **Function/Class:** `create_hold_case`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0223

- **ID:** MC-0223
- **File:** `apps/notifications/services.py:178`
- **Function/Class:** `create_in_app_notification`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0224

- **ID:** MC-0224
- **File:** `apps/organizations/services.py:161`
- **Function/Class:** `_reraise_unique`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0225

- **ID:** MC-0225
- **File:** `apps/organizations/services.py:197`
- **Function/Class:** `create_organization`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0226

- **ID:** MC-0226
- **File:** `apps/organizations/services.py:241`
- **Function/Class:** `update_organization`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0227

- **ID:** MC-0227
- **File:** `apps/organizations/services.py:327`
- **Function/Class:** `create_site`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0228

- **ID:** MC-0228
- **File:** `apps/organizations/services.py:371`
- **Function/Class:** `update_site`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0229

- **ID:** MC-0229
- **File:** `apps/organizations/services.py:452`
- **Function/Class:** `create_department`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0230

- **ID:** MC-0230
- **File:** `apps/organizations/services.py:516`
- **Function/Class:** `update_department`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0231

- **ID:** MC-0231
- **File:** `apps/organizations/services.py:606`
- **Function/Class:** `_reraise_shift_persistence_error`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0232

- **ID:** MC-0232
- **File:** `apps/organizations/services.py:658`
- **Function/Class:** `create_shift`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0233

- **ID:** MC-0233
- **File:** `apps/organizations/services.py:738`
- **Function/Class:** `update_shift`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0234

- **ID:** MC-0234
- **File:** `tests/test_models_services.py:30`
- **Function/Class:** `test_organization_code_case_insensitive_unique`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0235

- **ID:** MC-0235
- **File:** `tests/test_models_services.py:40`
- **Function/Class:** `test_site_code_unique_within_organization`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0236

- **ID:** MC-0236
- **File:** `tests/test_models_services.py:62`
- **Function/Class:** `test_department_code_unique_in_org_scope_without_site`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0237

- **ID:** MC-0237
- **File:** `tests/test_shift_foundation.py:347`
- **Function/Class:** `test_nulls_distinct_duplicate_org_wide_via_orm`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0238

- **ID:** MC-0238
- **File:** `apps/packaging/services.py:105`
- **Function/Class:** `create_packaging_artwork`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0239

- **ID:** MC-0239
- **File:** `apps/packaging/services.py:398`
- **Function/Class:** `create_line_clearance_hook`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0240

- **ID:** MC-0240
- **File:** `apps/quality/services.py:202`
- **Function/Class:** `create_qa_review`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0241

- **ID:** MC-0241
- **File:** `apps/rca/services.py:122`
- **Function/Class:** `_rca_code_conflict`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0242

- **ID:** MC-0242
- **File:** `apps/rca/services.py:216`
- **Function/Class:** `create_rca`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0243

- **ID:** MC-0243
- **File:** `tests/test_pre_uat_rca_hardening.py:103`
- **Function/Class:** `test_create_rca_duplicate_and_integrity_error_are_validation_errors`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0244

- **ID:** MC-0244
- **File:** `apps/receiving/services.py:114`
- **Function/Class:** `create_material_reference`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0245

- **ID:** MC-0245
- **File:** `apps/receiving/services.py:155`
- **Function/Class:** `create_material_specification`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0246

- **ID:** MC-0246
- **File:** `apps/receiving/services.py:199`
- **Function/Class:** `add_material_specification_parameter`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0247

- **ID:** MC-0247
- **File:** `apps/receiving/services.py:320`
- **Function/Class:** `create_receipt_quality_record`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0248

- **ID:** MC-0248
- **File:** `apps/receiving/services.py:423`
- **Function/Class:** `link_lab_sample_to_receipt`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0249

- **ID:** MC-0249
- **File:** `apps/recording/correction_services.py:302`
- **Function/Class:** `start_checklist_correction`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0250

- **ID:** MC-0250
- **File:** `apps/recording/correction_services.py:636`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0251

- **ID:** MC-0251
- **File:** `apps/recording/services.py:204`
- **Function/Class:** `start_checklist_recording`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0252

- **ID:** MC-0252
- **File:** `apps/recording/services.py:1097`
- **Function/Class:** `submit_checklist_record`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0253

- **ID:** MC-0253
- **File:** `apps/reviews/services.py:176`
- **Function/Class:** `create_supervisor_review`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0254

- **ID:** MC-0254
- **File:** `apps/rework/services.py:186`
- **Function/Class:** `create_rework_case`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0255

- **ID:** MC-0255
- **File:** `apps/sampling/services.py:98`
- **Function/Class:** `create_sampling_plan`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0256

- **ID:** MC-0256
- **File:** `apps/sampling/services.py:216`
- **Function/Class:** `add_sampling_rule`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0257

- **ID:** MC-0257
- **File:** `apps/sanitation/services.py:111`
- **Function/Class:** `create_sanitation_program`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0258

- **ID:** MC-0258
- **File:** `apps/sanitation/services.py:222`
- **Function/Class:** `add_sanitation_scope`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0259

- **ID:** MC-0259
- **File:** `apps/sanitation/services.py:289`
- **Function/Class:** `create_chemical_reference`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0260

- **ID:** MC-0260
- **File:** `apps/sanitation/services.py:323`
- **Function/Class:** `link_chemical_to_version`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0261

- **ID:** MC-0261
- **File:** `apps/scheduling/applicability.py:500`
- **Function/Class:** `create_checklist_applicability_rule`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0262

- **ID:** MC-0262
- **File:** `apps/scheduling/batch_events.py:281`
- **Function/Class:** `_get_or_create_receipt`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0263

- **ID:** MC-0263
- **File:** `apps/scheduling/generation.py:398`
- **Function/Class:** `upsert_occurrence_task`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0264

- **ID:** MC-0264
- **File:** `apps/scheduling/services.py:206`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0265

- **ID:** MC-0265
- **File:** `tests/test_phase07e_recurring_schedules.py:569`
- **Function/Class:** `test_shift_missed_and_skip_policies_and_integrity_race`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0266

- **ID:** MC-0266
- **File:** `apps/supplier_quality/services.py:93`
- **Function/Class:** `create_supplier_quality_profile`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0267

- **ID:** MC-0267
- **File:** `apps/supplier_quality/services.py:94`
- **Function/Class:** `create_supplier_quality_profile`
- **Token:** `IntegrityError` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0268

- **ID:** MC-0268
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:37`
- **Function/Class:** `<text>`
- **Token:** `loaddata` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0269

- **ID:** MC-0269
- **File:** `apps/access_control/models.py:32`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0270

- **ID:** MC-0270
- **File:** `apps/access_control/models.py:38`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0271

- **ID:** MC-0271
- **File:** `apps/access_control/models.py:76`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0272

- **ID:** MC-0272
- **File:** `apps/access_control/models.py:82`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0273

- **ID:** MC-0273
- **File:** `apps/accounts/models.py:40`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0274

- **ID:** MC-0274
- **File:** `apps/accounts/models.py:46`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0275

- **ID:** MC-0275
- **File:** `apps/batch_genealogy/models.py:74`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0276

- **ID:** MC-0276
- **File:** `apps/capa/models.py:152`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0277

- **ID:** MC-0277
- **File:** `apps/change_control/models.py:145`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0278

- **ID:** MC-0278
- **File:** `apps/changeover/models.py:93`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0279

- **ID:** MC-0279
- **File:** `apps/checklists/models.py:199`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0280

- **ID:** MC-0280
- **File:** `apps/checklists/models.py:209`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0281

- **ID:** MC-0281
- **File:** `apps/checklists/models.py:521`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0282

- **ID:** MC-0282
- **File:** `apps/checklists/models.py:1121`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0283

- **ID:** MC-0283
- **File:** `apps/checklists/proposal_loader.py:440`
- **Function/Class:** `_get_org_template`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0284

- **ID:** MC-0284
- **File:** `apps/compliance_mapping/models.py:164`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0285

- **ID:** MC-0285
- **File:** `apps/compliance_mapping/models.py:232`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0286

- **ID:** MC-0286
- **File:** `apps/customer_complaints/models.py:162`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0287

- **ID:** MC-0287
- **File:** `apps/customer_complaints/models.py:236`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0288

- **ID:** MC-0288
- **File:** `apps/dispatch/models.py:160`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0289

- **ID:** MC-0289
- **File:** `apps/document_control/models.py:97`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0290

- **ID:** MC-0290
- **File:** `apps/document_control/models.py:183`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0291

- **ID:** MC-0291
- **File:** `apps/environmental/models.py:115`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0292

- **ID:** MC-0292
- **File:** `apps/environmental/models.py:173`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0293

- **ID:** MC-0293
- **File:** `apps/environmental/models.py:210`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0294

- **ID:** MC-0294
- **File:** `apps/foreign_body/models.py:100`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0295

- **ID:** MC-0295
- **File:** `apps/foreign_body/models.py:166`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0296

- **ID:** MC-0296
- **File:** `apps/haccp/models.py:95`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0297

- **ID:** MC-0297
- **File:** `apps/haccp/models.py:185`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0298

- **ID:** MC-0298
- **File:** `apps/haccp/models.py:215`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0299

- **ID:** MC-0299
- **File:** `apps/haccp/models.py:244`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0300

- **ID:** MC-0300
- **File:** `apps/haccp/models.py:293`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0301

- **ID:** MC-0301
- **File:** `apps/instruments/models.py:127`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0302

- **ID:** MC-0302
- **File:** `apps/instruments/models.py:141`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0303

- **ID:** MC-0303
- **File:** `apps/ipqc/models.py:131`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0304

- **ID:** MC-0304
- **File:** `apps/iqc/models.py:96`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0305

- **ID:** MC-0305
- **File:** `apps/iqc/models.py:97`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0306

- **ID:** MC-0306
- **File:** `apps/laboratory/models.py:91`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0307

- **ID:** MC-0307
- **File:** `apps/laboratory/models.py:159`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0308

- **ID:** MC-0308
- **File:** `apps/laboratory/models.py:274`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0309

- **ID:** MC-0309
- **File:** `apps/laboratory/models.py:332`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0310

- **ID:** MC-0310
- **File:** `apps/master_data/models.py:99`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0311

- **ID:** MC-0311
- **File:** `apps/master_data/models.py:104`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0312

- **ID:** MC-0312
- **File:** `apps/master_data/models.py:123`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0313

- **ID:** MC-0313
- **File:** `apps/master_data/models.py:125`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0314

- **ID:** MC-0314
- **File:** `apps/master_data/models.py:196`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0315

- **ID:** MC-0315
- **File:** `apps/master_data/models.py:206`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0316

- **ID:** MC-0316
- **File:** `apps/master_data/models.py:373`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0317

- **ID:** MC-0317
- **File:** `apps/master_data/models.py:379`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0318

- **ID:** MC-0318
- **File:** `apps/nonconformance/models.py:182`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0319

- **ID:** MC-0319
- **File:** `apps/nonconformance/models.py:309`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0320

- **ID:** MC-0320
- **File:** `apps/notifications/models.py:154`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0321

- **ID:** MC-0321
- **File:** `apps/organizations/models.py:29`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0322

- **ID:** MC-0322
- **File:** `apps/organizations/models.py:35`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0323

- **ID:** MC-0323
- **File:** `apps/organizations/models.py:64`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0324

- **ID:** MC-0324
- **File:** `apps/organizations/models.py:71`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0325

- **ID:** MC-0325
- **File:** `apps/organizations/models.py:113`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0326

- **ID:** MC-0326
- **File:** `apps/organizations/models.py:119`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0327

- **ID:** MC-0327
- **File:** `apps/organizations/models.py:128`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0328

- **ID:** MC-0328
- **File:** `apps/organizations/models.py:191`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0329

- **ID:** MC-0329
- **File:** `apps/organizations/models.py:220`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0330

- **ID:** MC-0330
- **File:** `apps/packaging/models.py:77`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0331

- **ID:** MC-0331
- **File:** `apps/packaging/models.py:268`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0332

- **ID:** MC-0332
- **File:** `apps/process_fmea/models.py:84`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0333

- **ID:** MC-0333
- **File:** `apps/process_fmea/models.py:224`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0334

- **ID:** MC-0334
- **File:** `apps/process_fmea/models.py:260`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0335

- **ID:** MC-0335
- **File:** `apps/product_returns/models.py:127`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0336

- **ID:** MC-0336
- **File:** `apps/product_returns/models.py:128`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0337

- **ID:** MC-0337
- **File:** `apps/quality_audits/models.py:147`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0338

- **ID:** MC-0338
- **File:** `apps/quality_audits/models.py:272`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0339

- **ID:** MC-0339
- **File:** `apps/quality_quarantine/models.py:101`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0340

- **ID:** MC-0340
- **File:** `apps/quality_risks/models.py:146`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0341

- **ID:** MC-0341
- **File:** `apps/quality_risks/models.py:204`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0342

- **ID:** MC-0342
- **File:** `apps/rca/models.py:115`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0343

- **ID:** MC-0343
- **File:** `apps/recall/models.py:161`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0344

- **ID:** MC-0344
- **File:** `apps/recall/models.py:263`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0345

- **ID:** MC-0345
- **File:** `apps/recall/models.py:301`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0346

- **ID:** MC-0346
- **File:** `apps/recall/models.py:642`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0347

- **ID:** MC-0347
- **File:** `apps/receiving/models.py:109`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0348

- **ID:** MC-0348
- **File:** `apps/receiving/models.py:155`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0349

- **ID:** MC-0349
- **File:** `apps/receiving/models.py:371`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0350

- **ID:** MC-0350
- **File:** `apps/sampling/models.py:73`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0351

- **ID:** MC-0351
- **File:** `apps/sampling/models.py:188`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0352

- **ID:** MC-0352
- **File:** `apps/sanitation/models.py:87`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0353

- **ID:** MC-0353
- **File:** `apps/sanitation/models.py:226`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0354

- **ID:** MC-0354
- **File:** `apps/sanitation/models.py:348`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0355

- **ID:** MC-0355
- **File:** `apps/supplier_quality/models.py:78`
- **Function/Class:** `Meta`
- **Token:** `Lower` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0356

- **ID:** MC-0356
- **File:** `apps/checklists/selectors.py:112`
- **Function/Class:** `list_checklist_templates`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0357

- **ID:** MC-0357
- **File:** `apps/checklists/services.py:208`
- **Function/Class:** `_next_section_position`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0358

- **ID:** MC-0358
- **File:** `apps/checklists/services.py:219`
- **Function/Class:** `_next_item_position`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0359

- **ID:** MC-0359
- **File:** `apps/checklists/services.py:822`
- **Function/Class:** `_allocate_next_version_number`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0360

- **ID:** MC-0360
- **File:** `apps/checklists/services.py:893`
- **Function/Class:** `_next_option_position`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0361

- **ID:** MC-0361
- **File:** `apps/mongo_poc/services.py:90`
- **Function/Class:** `allocate_version_number`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0362

- **ID:** MC-0362
- **File:** `apps/mongo_poc/services.py:112`
- **Function/Class:** `submit_immutable_snapshot`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0363

- **ID:** MC-0363
- **File:** `apps/process_fmea/services.py:415`
- **Function/Class:** `record_failure_mode_assessment`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0364

- **ID:** MC-0364
- **File:** `apps/process_fmea/services.py:805`
- **Function/Class:** `revise_process_fmea`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0365

- **ID:** MC-0365
- **File:** `apps/quality_risks/selectors.py:91`
- **Function/Class:** `report_high_rated_risks`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0366

- **ID:** MC-0366
- **File:** `apps/quality_risks/services.py:375`
- **Function/Class:** `record_risk_assessment`
- **Token:** `Max` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0367

- **ID:** MC-0367
- **File:** `apps/quality/selectors.py:51`
- **Function/Class:** `list_qa_reviewable_submissions`
- **Token:** `OuterRef` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0368

- **ID:** MC-0368
- **File:** `apps/reviews/selectors.py:49`
- **Function/Class:** `_base_pending_queryset`
- **Token:** `OuterRef` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0369

- **ID:** MC-0369
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:34`
- **Function/Class:** `<text>`
- **Token:** `pg_dump` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0370

- **ID:** MC-0370
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:178`
- **Function/Class:** `<text>`
- **Token:** `pg_dump` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0371

- **ID:** MC-0371
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:180`
- **Function/Class:** `<text>`
- **Token:** `pg_dump` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0372

- **ID:** MC-0372
- **File:** `scripts/ops/restore_drill.py:205`
- **Function/Class:** `<text>`
- **Token:** `pg_dump` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0373

- **ID:** MC-0373
- **File:** `scripts/ops/restore_drill.py:227`
- **Function/Class:** `<text>`
- **Token:** `pg_dump` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0374

- **ID:** MC-0374
- **File:** `scripts/migration/generate_full_compatibility_inventory.py:35`
- **Function/Class:** `<text>`
- **Token:** `pg_restore` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0375

- **ID:** MC-0375
- **File:** `scripts/ops/restore_drill.py:213`
- **Function/Class:** `<text>`
- **Token:** `pg_restore` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0376

- **ID:** MC-0376
- **File:** `scripts/ops/restore_drill.py:232`
- **Function/Class:** `<text>`
- **Token:** `pg_restore` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0377

- **ID:** MC-0377
- **File:** `apps/access_control/governance_services.py:226`
- **Function/Class:** `apply_role_template_to_role`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0378

- **ID:** MC-0378
- **File:** `apps/access_control/services.py:34`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0379

- **ID:** MC-0379
- **File:** `apps/batch_dossier/selectors.py:158`
- **Function/Class:** `lab_samples_for_batch`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0380

- **ID:** MC-0380
- **File:** `apps/batch_dossier/selectors.py:219`
- **Function/Class:** `dispatch_for_batch`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0381

- **ID:** MC-0381
- **File:** `apps/batch_dossier/selectors.py:300`
- **Function/Class:** `submissions_with_device_traces`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0382

- **ID:** MC-0382
- **File:** `apps/checklists/proposal_loader.py:394`
- **Function/Class:** `version_structure_fingerprint`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0383

- **ID:** MC-0383
- **File:** `apps/checklists/selectors.py:185`
- **Function/Class:** `get_version_with_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0384

- **ID:** MC-0384
- **File:** `apps/checklists/selectors.py:191`
- **Function/Class:** `get_version_with_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0385

- **ID:** MC-0385
- **File:** `apps/checklists/selectors.py:194`
- **Function/Class:** `get_version_with_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0386

- **ID:** MC-0386
- **File:** `apps/checklists/services.py:594`
- **Function/Class:** `set_checklist_calculation_operands`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0387

- **ID:** MC-0387
- **File:** `apps/checklists/services.py:616`
- **Function/Class:** `set_checklist_calculation_operands`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0388

- **ID:** MC-0388
- **File:** `apps/checklists/services.py:915`
- **Function/Class:** `_clone_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0389

- **ID:** MC-0389
- **File:** `apps/checklists/services.py:993`
- **Function/Class:** `_clone_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0390

- **ID:** MC-0390
- **File:** `apps/checklists/services.py:1858`
- **Function/Class:** `_validate_publish_structure`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0391

- **ID:** MC-0391
- **File:** `apps/checklists/views.py:564`
- **Function/Class:** `item_edit`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0392

- **ID:** MC-0392
- **File:** `apps/core/checklist_workflow.py:308`
- **Function/Class:** `prefetch_workflow_graph`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0393

- **ID:** MC-0393
- **File:** `apps/quality/selectors.py:139`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0394

- **ID:** MC-0394
- **File:** `apps/quality/selectors.py:143`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0395

- **ID:** MC-0395
- **File:** `apps/recall/services.py:85`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0396

- **ID:** MC-0396
- **File:** `apps/recording/correction_services.py:507`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0397

- **ID:** MC-0397
- **File:** `apps/recording/daily_selectors.py:75`
- **Function/Class:** `_with_latest_submission`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0398

- **ID:** MC-0398
- **File:** `apps/recording/daily_selectors.py:195`
- **Function/Class:** `monthly_pack_context`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0399

- **ID:** MC-0399
- **File:** `apps/recording/selectors.py:57`
- **Function/Class:** `list_recordable_checklist_tasks`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0400

- **ID:** MC-0400
- **File:** `apps/recording/selectors.py:165`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0401

- **ID:** MC-0401
- **File:** `apps/recording/selectors.py:169`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0402

- **ID:** MC-0402
- **File:** `apps/recording/selectors.py:177`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0403

- **ID:** MC-0403
- **File:** `apps/recording/services.py:358`
- **Function/Class:** `collect_submission_completeness`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0404

- **ID:** MC-0404
- **File:** `apps/recording/services.py:723`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0405

- **ID:** MC-0405
- **File:** `apps/recording/services.py:983`
- **Function/Class:** `submit_checklist_record`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0406

- **ID:** MC-0406
- **File:** `tests/test_phase06i_calculated_fields.py:426`
- **Function/Class:** `test_snapshot_render_includes_calculated_context`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0407

- **ID:** MC-0407
- **File:** `apps/reviews/selectors.py:223`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0408

- **ID:** MC-0408
- **File:** `apps/reviews/selectors.py:227`
- **Function/Class:** `_load_sections`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0409

- **ID:** MC-0409
- **File:** `apps/sampling/engine.py:140`
- **Function/Class:** `_effective_versions`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0410

- **ID:** MC-0410
- **File:** `apps/sanitation/services.py:413`
- **Function/Class:** `bind_checklist_template_to_sanitation_program`
- **Token:** `prefetch_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0411

- **ID:** MC-0411
- **File:** `scripts/ops/restore_drill.py:7`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0412

- **ID:** MC-0412
- **File:** `scripts/ops/restore_drill.py:23`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0413

- **ID:** MC-0413
- **File:** `scripts/ops/restore_drill.py:120`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0414

- **ID:** MC-0414
- **File:** `scripts/ops/restore_drill.py:124`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0415

- **ID:** MC-0415
- **File:** `scripts/ops/restore_drill.py:141`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0416

- **ID:** MC-0416
- **File:** `scripts/ops/restore_drill.py:154`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0417

- **ID:** MC-0417
- **File:** `scripts/ops/restore_drill.py:169`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0418

- **ID:** MC-0418
- **File:** `scripts/ops/restore_drill.py:188`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0419

- **ID:** MC-0419
- **File:** `scripts/ops/restore_drill.py:245`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0420

- **ID:** MC-0420
- **File:** `scripts/ops/restore_drill.py:282`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0421

- **ID:** MC-0421
- **File:** `scripts/ops/restore_drill.py:298`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0422

- **ID:** MC-0422
- **File:** `scripts/ops/restore_drill.py:318`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0423

- **ID:** MC-0423
- **File:** `scripts/ops/restore_drill.py:319`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0424

- **ID:** MC-0424
- **File:** `scripts/ops/restore_drill.py:323`
- **Function/Class:** `<text>`
- **Token:** `psql` (TEXT)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0425

- **ID:** MC-0425
- **File:** `apps/access_control/services.py:35`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0426

- **ID:** MC-0426
- **File:** `apps/access_control/services.py:35`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0427

- **ID:** MC-0427
- **File:** `apps/access_control/services.py:36`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0428

- **ID:** MC-0428
- **File:** `apps/access_control/services.py:36`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0429

- **ID:** MC-0429
- **File:** `apps/access_control/services.py:248`
- **Function/Class:** `get_accessible_sites`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0430

- **ID:** MC-0430
- **File:** `apps/access_control/services.py:248`
- **Function/Class:** `get_accessible_sites`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0431

- **ID:** MC-0431
- **File:** `apps/access_control/services.py:299`
- **Function/Class:** `get_accessible_departments`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0432

- **ID:** MC-0432
- **File:** `apps/access_control/services.py:299`
- **Function/Class:** `get_accessible_departments`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0433

- **ID:** MC-0433
- **File:** `apps/access_control/services.py:299`
- **Function/Class:** `get_accessible_departments`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0434

- **ID:** MC-0434
- **File:** `apps/accounts/backends.py:45`
- **Function/Class:** `authenticate`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0435

- **ID:** MC-0435
- **File:** `apps/batch_dossier/selectors.py:258`
- **Function/Class:** `evidence_for_linked_targets`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0436

- **ID:** MC-0436
- **File:** `apps/batch_dossier/selectors.py:260`
- **Function/Class:** `evidence_for_linked_targets`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0437

- **ID:** MC-0437
- **File:** `apps/checklists/effective_version.py:141`
- **Function/Class:** `eligible_published_versions_at`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0438

- **ID:** MC-0438
- **File:** `apps/checklists/effective_version.py:141`
- **Function/Class:** `eligible_published_versions_at`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0439

- **ID:** MC-0439
- **File:** `apps/checklists/effective_version.py:142`
- **Function/Class:** `eligible_published_versions_at`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0440

- **ID:** MC-0440
- **File:** `apps/checklists/effective_version.py:142`
- **Function/Class:** `eligible_published_versions_at`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0441

- **ID:** MC-0441
- **File:** `apps/checklists/selectors.py:130`
- **Function/Class:** `list_checklist_templates`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0442

- **ID:** MC-0442
- **File:** `apps/checklists/selectors.py:130`
- **Function/Class:** `list_checklist_templates`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0443

- **ID:** MC-0443
- **File:** `apps/document_control/selectors.py:53`
- **Function/Class:** `list_effective_documents`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0444

- **ID:** MC-0444
- **File:** `apps/document_control/selectors.py:53`
- **Function/Class:** `list_effective_documents`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0445

- **ID:** MC-0445
- **File:** `apps/document_control/selectors.py:78`
- **Function/Class:** `get_effective_version`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0446

- **ID:** MC-0446
- **File:** `apps/document_control/selectors.py:78`
- **Function/Class:** `get_effective_version`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0447

- **ID:** MC-0447
- **File:** `apps/haccp/selectors.py:67`
- **Function/Class:** `_effective_window_q`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0448

- **ID:** MC-0448
- **File:** `apps/haccp/selectors.py:68`
- **Function/Class:** `_effective_window_q`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0449

- **ID:** MC-0449
- **File:** `apps/haccp/selectors.py:68`
- **Function/Class:** `_effective_window_q`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0450

- **ID:** MC-0450
- **File:** `apps/haccp/selectors.py:69`
- **Function/Class:** `_effective_window_q`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0451

- **ID:** MC-0451
- **File:** `apps/haccp/selectors.py:69`
- **Function/Class:** `_effective_window_q`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0452

- **ID:** MC-0452
- **File:** `apps/instruments/models.py:212`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0453

- **ID:** MC-0453
- **File:** `apps/instruments/models.py:212`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0454

- **ID:** MC-0454
- **File:** `apps/instruments/selectors.py:86`
- **Function/Class:** `list_equipment`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0455

- **ID:** MC-0455
- **File:** `apps/instruments/selectors.py:86`
- **Function/Class:** `list_equipment`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0456

- **ID:** MC-0456
- **File:** `apps/instruments/selectors.py:86`
- **Function/Class:** `list_equipment`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0457

- **ID:** MC-0457
- **File:** `apps/integrations/reconciliation.py:40`
- **Function/Class:** `reconcile_external_batch_events`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0458

- **ID:** MC-0458
- **File:** `apps/integrations/reconciliation.py:40`
- **Function/Class:** `reconcile_external_batch_events`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0459

- **ID:** MC-0459
- **File:** `apps/master_data/models.py:106`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0460

- **ID:** MC-0460
- **File:** `apps/master_data/models.py:111`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0461

- **ID:** MC-0461
- **File:** `apps/master_data/models.py:112`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0462

- **ID:** MC-0462
- **File:** `apps/master_data/models.py:113`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0463

- **ID:** MC-0463
- **File:** `apps/master_data/models.py:288`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0464

- **ID:** MC-0464
- **File:** `apps/master_data/models.py:289`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0465

- **ID:** MC-0465
- **File:** `apps/master_data/models.py:290`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0466

- **ID:** MC-0466
- **File:** `apps/master_data/selectors.py:106`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0467

- **ID:** MC-0467
- **File:** `apps/master_data/selectors.py:107`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0468

- **ID:** MC-0468
- **File:** `apps/master_data/selectors.py:108`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0469

- **ID:** MC-0469
- **File:** `apps/master_data/selectors.py:109`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0470

- **ID:** MC-0470
- **File:** `apps/master_data/selectors.py:110`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0471

- **ID:** MC-0471
- **File:** `apps/master_data/selectors.py:111`
- **Function/Class:** `list_fg_products`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0472

- **ID:** MC-0472
- **File:** `apps/organizations/selectors.py:150`
- **Function/Class:** `list_shifts_for_actor`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0473

- **ID:** MC-0473
- **File:** `apps/organizations/selectors.py:150`
- **Function/Class:** `list_shifts_for_actor`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0474

- **ID:** MC-0474
- **File:** `apps/recall/services.py:86`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0475

- **ID:** MC-0475
- **File:** `apps/recall/services.py:86`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0476

- **ID:** MC-0476
- **File:** `apps/recall/services.py:87`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0477

- **ID:** MC-0477
- **File:** `apps/recall/services.py:87`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0478

- **ID:** MC-0478
- **File:** `apps/recording/models.py:250`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0479

- **ID:** MC-0479
- **File:** `apps/recording/models.py:251`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0480

- **ID:** MC-0480
- **File:** `apps/recording/models.py:252`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0481

- **ID:** MC-0481
- **File:** `apps/recording/models.py:253`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0482

- **ID:** MC-0482
- **File:** `apps/recording/models.py:256`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0483

- **ID:** MC-0483
- **File:** `apps/recording/models.py:257`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0484

- **ID:** MC-0484
- **File:** `apps/recording/models.py:258`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0485

- **ID:** MC-0485
- **File:** `apps/recording/models.py:259`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0486

- **ID:** MC-0486
- **File:** `apps/recording/models.py:262`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0487

- **ID:** MC-0487
- **File:** `apps/recording/models.py:263`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0488

- **ID:** MC-0488
- **File:** `apps/recording/models.py:264`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0489

- **ID:** MC-0489
- **File:** `apps/recording/models.py:265`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0490

- **ID:** MC-0490
- **File:** `apps/recording/models.py:268`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0491

- **ID:** MC-0491
- **File:** `apps/recording/models.py:269`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0492

- **ID:** MC-0492
- **File:** `apps/recording/models.py:270`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0493

- **ID:** MC-0493
- **File:** `apps/recording/models.py:271`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0494

- **ID:** MC-0494
- **File:** `apps/recording/models.py:500`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0495

- **ID:** MC-0495
- **File:** `apps/recording/models.py:501`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0496

- **ID:** MC-0496
- **File:** `apps/recording/models.py:502`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0497

- **ID:** MC-0497
- **File:** `apps/recording/models.py:503`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0498

- **ID:** MC-0498
- **File:** `apps/recording/models.py:506`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0499

- **ID:** MC-0499
- **File:** `apps/recording/models.py:507`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0500

- **ID:** MC-0500
- **File:** `apps/recording/models.py:508`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0501

- **ID:** MC-0501
- **File:** `apps/recording/models.py:509`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0502

- **ID:** MC-0502
- **File:** `apps/recording/models.py:512`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0503

- **ID:** MC-0503
- **File:** `apps/recording/models.py:513`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0504

- **ID:** MC-0504
- **File:** `apps/recording/models.py:514`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0505

- **ID:** MC-0505
- **File:** `apps/recording/models.py:515`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0506

- **ID:** MC-0506
- **File:** `apps/recording/models.py:518`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0507

- **ID:** MC-0507
- **File:** `apps/recording/models.py:519`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0508

- **ID:** MC-0508
- **File:** `apps/recording/models.py:520`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0509

- **ID:** MC-0509
- **File:** `apps/recording/models.py:521`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0510

- **ID:** MC-0510
- **File:** `apps/sampling/engine.py:137`
- **Function/Class:** `_effective_versions`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0511

- **ID:** MC-0511
- **File:** `apps/sampling/engine.py:137`
- **Function/Class:** `_effective_versions`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0512

- **ID:** MC-0512
- **File:** `apps/sampling/engine.py:138`
- **Function/Class:** `_effective_versions`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0513

- **ID:** MC-0513
- **File:** `apps/sampling/engine.py:138`
- **Function/Class:** `_effective_versions`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0514

- **ID:** MC-0514
- **File:** `apps/scheduling/applicability.py:265`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0515

- **ID:** MC-0515
- **File:** `apps/scheduling/applicability.py:265`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0516

- **ID:** MC-0516
- **File:** `apps/scheduling/applicability.py:266`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0517

- **ID:** MC-0517
- **File:** `apps/scheduling/applicability.py:266`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0518

- **ID:** MC-0518
- **File:** `apps/scheduling/applicability.py:278`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0519

- **ID:** MC-0519
- **File:** `apps/scheduling/applicability.py:278`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0520

- **ID:** MC-0520
- **File:** `apps/scheduling/applicability.py:280`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0521

- **ID:** MC-0521
- **File:** `apps/scheduling/applicability.py:280`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0522

- **ID:** MC-0522
- **File:** `apps/scheduling/applicability.py:282`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0523

- **ID:** MC-0523
- **File:** `apps/scheduling/applicability.py:282`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0524

- **ID:** MC-0524
- **File:** `apps/scheduling/applicability.py:284`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0525

- **ID:** MC-0525
- **File:** `apps/scheduling/applicability.py:284`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0526

- **ID:** MC-0526
- **File:** `apps/scheduling/models.py:270`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0527

- **ID:** MC-0527
- **File:** `apps/scheduling/models.py:501`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0528

- **ID:** MC-0528
- **File:** `apps/scheduling/models.py:502`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0529

- **ID:** MC-0529
- **File:** `apps/scheduling/models.py:503`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0530

- **ID:** MC-0530
- **File:** `apps/scheduling/models.py:698`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0531

- **ID:** MC-0531
- **File:** `apps/scheduling/models.py:698`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0532

- **ID:** MC-0532
- **File:** `apps/scheduling/models.py:867`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0533

- **ID:** MC-0533
- **File:** `apps/scheduling/models.py:872`
- **Function/Class:** `Meta`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0534

- **ID:** MC-0534
- **File:** `apps/scheduling/selectors.py:234`
- **Function/Class:** `_apply_due_state_filter`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0535

- **ID:** MC-0535
- **File:** `apps/scheduling/selectors.py:234`
- **Function/Class:** `_apply_due_state_filter`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0536

- **ID:** MC-0536
- **File:** `apps/scheduling/selectors.py:237`
- **Function/Class:** `_apply_due_state_filter`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0537

- **ID:** MC-0537
- **File:** `apps/scheduling/selectors.py:237`
- **Function/Class:** `_apply_due_state_filter`
- **Token:** `Q` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0538

- **ID:** MC-0538
- **File:** `apps/access_control/governance_services.py:92`
- **Function/Class:** `set_role_permissions`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0539

- **ID:** MC-0539
- **File:** `apps/access_control/governance_services.py:179`
- **Function/Class:** `update_role_template_permissions`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0540

- **ID:** MC-0540
- **File:** `apps/access_control/governance_services.py:235`
- **Function/Class:** `apply_role_template_to_role`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0541

- **ID:** MC-0541
- **File:** `apps/accounts/services.py:218`
- **Function/Class:** `record_failed_login`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0542

- **ID:** MC-0542
- **File:** `apps/accounts/services.py:252`
- **Function/Class:** `record_successful_login`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0543

- **ID:** MC-0543
- **File:** `apps/accounts/services.py:364`
- **Function/Class:** `unlock_account`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0544

- **ID:** MC-0544
- **File:** `apps/batch_dossier/services.py:147`
- **Function/Class:** `upsert_batch_dossier_policy`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0545

- **ID:** MC-0545
- **File:** `apps/batch_genealogy/services.py:150`
- **Function/Class:** `upsert_genealogy_policy`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0546

- **ID:** MC-0546
- **File:** `apps/capa/services.py:153`
- **Function/Class:** `transition_capa_status`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0547

- **ID:** MC-0547
- **File:** `apps/capa/services.py:199`
- **Function/Class:** `record_capa_verification`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0548

- **ID:** MC-0548
- **File:** `apps/capa/services.py:260`
- **Function/Class:** `record_capa_effectiveness_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0549

- **ID:** MC-0549
- **File:** `apps/capa/services.py:322`
- **Function/Class:** `add_capa_action_item`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0550

- **ID:** MC-0550
- **File:** `apps/capa/services.py:370`
- **Function/Class:** `complete_capa_action_item`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0551

- **ID:** MC-0551
- **File:** `apps/capa/services.py:408`
- **Function/Class:** `close_corrective_action`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0552

- **ID:** MC-0552
- **File:** `apps/checklists/effective_version.py:324`
- **Function/Class:** `set_checklist_version_effectivity`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0553

- **ID:** MC-0553
- **File:** `apps/checklists/services.py:197`
- **Function/Class:** `_lock_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0554

- **ID:** MC-0554
- **File:** `apps/checklists/services.py:648`
- **Function/Class:** `_swap_positions`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0555

- **ID:** MC-0555
- **File:** `apps/checklists/services.py:725`
- **Function/Class:** `update_checklist_template`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0556

- **ID:** MC-0556
- **File:** `apps/checklists/services.py:781`
- **Function/Class:** `activate_checklist_template`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0557

- **ID:** MC-0557
- **File:** `apps/checklists/services.py:802`
- **Function/Class:** `deactivate_checklist_template`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0558

- **ID:** MC-0558
- **File:** `apps/checklists/services.py:819`
- **Function/Class:** `_allocate_next_version_number`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0559

- **ID:** MC-0559
- **File:** `apps/checklists/services.py:899`
- **Function/Class:** `_lock_item`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0560

- **ID:** MC-0560
- **File:** `apps/checklists/services.py:1089`
- **Function/Class:** `create_checklist_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0561

- **ID:** MC-0561
- **File:** `apps/checklists/services.py:1198`
- **Function/Class:** `update_checklist_section`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0562

- **ID:** MC-0562
- **File:** `apps/checklists/services.py:1226`
- **Function/Class:** `remove_checklist_section`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0563

- **ID:** MC-0563
- **File:** `apps/checklists/services.py:1256`
- **Function/Class:** `move_checklist_section`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0564

- **ID:** MC-0564
- **File:** `apps/checklists/services.py:1306`
- **Function/Class:** `add_checklist_item`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0565

- **ID:** MC-0565
- **File:** `apps/checklists/services.py:1325`
- **Function/Class:** `add_checklist_item`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0566

- **ID:** MC-0566
- **File:** `apps/checklists/services.py:1741`
- **Function/Class:** `update_checklist_item_option`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0567

- **ID:** MC-0567
- **File:** `apps/checklists/services.py:1786`
- **Function/Class:** `remove_checklist_item_option`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0568

- **ID:** MC-0568
- **File:** `apps/checklists/services.py:1821`
- **Function/Class:** `move_checklist_item_option`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0569

- **ID:** MC-0569
- **File:** `apps/customer_complaints/services.py:101`
- **Function/Class:** `upsert_complaint_policy`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0570

- **ID:** MC-0570
- **File:** `apps/dispatch/services.py:248`
- **Function/Class:** `update_dispatch_quality_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0571

- **ID:** MC-0571
- **File:** `apps/dispatch/services.py:330`
- **Function/Class:** `link_vehicle_inspection`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0572

- **ID:** MC-0572
- **File:** `apps/dispatch/services.py:377`
- **Function/Class:** `link_qa_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0573

- **ID:** MC-0573
- **File:** `apps/dispatch/services.py:423`
- **Function/Class:** `record_cold_chain_temperature`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0574

- **ID:** MC-0574
- **File:** `apps/dispatch/services.py:487`
- **Function/Class:** `set_dispatch_quantity_line`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0575

- **ID:** MC-0575
- **File:** `apps/dispatch/services.py:502`
- **Function/Class:** `set_dispatch_quantity_line`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0576

- **ID:** MC-0576
- **File:** `apps/dispatch/services.py:614`
- **Function/Class:** `complete_dispatch_quality_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0577

- **ID:** MC-0577
- **File:** `apps/dispatch/services.py:709`
- **Function/Class:** `cancel_dispatch_quality_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0578

- **ID:** MC-0578
- **File:** `apps/document_control/services.py:358`
- **Function/Class:** `make_version_effective`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0579

- **ID:** MC-0579
- **File:** `apps/environmental/services.py:229`
- **Function/Class:** `create_draft_spec_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0580

- **ID:** MC-0580
- **File:** `apps/environmental/services.py:269`
- **Function/Class:** `add_limit_rule`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0581

- **ID:** MC-0581
- **File:** `apps/environmental/services.py:306`
- **Function/Class:** `approve_spec_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0582

- **ID:** MC-0582
- **File:** `apps/environmental/services.py:336`
- **Function/Class:** `retire_spec_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0583

- **ID:** MC-0583
- **File:** `apps/evidence/services.py:262`
- **Function/Class:** `retire_evidence_attachment`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0584

- **ID:** MC-0584
- **File:** `apps/foreign_body/services.py:304`
- **Function/Class:** `verify_challenge_test`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0585

- **ID:** MC-0585
- **File:** `apps/foreign_body/services.py:348`
- **Function/Class:** `void_challenge_test`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0586

- **ID:** MC-0586
- **File:** `apps/haccp/services.py:175`
- **Function/Class:** `create_draft_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0587

- **ID:** MC-0587
- **File:** `apps/haccp/services.py:536`
- **Function/Class:** `approve_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0588

- **ID:** MC-0588
- **File:** `apps/haccp/services.py:595`
- **Function/Class:** `retire_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0589

- **ID:** MC-0589
- **File:** `apps/instruments/services.py:179`
- **Function/Class:** `update_equipment`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0590

- **ID:** MC-0590
- **File:** `apps/instruments/services.py:247`
- **Function/Class:** `set_equipment_operational_status`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0591

- **ID:** MC-0591
- **File:** `apps/instruments/services.py:273`
- **Function/Class:** `activate_equipment`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0592

- **ID:** MC-0592
- **File:** `apps/instruments/services.py:292`
- **Function/Class:** `deactivate_equipment`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0593

- **ID:** MC-0593
- **File:** `apps/instruments/services.py:364`
- **Function/Class:** `update_calibration_certificate_metadata`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0594

- **ID:** MC-0594
- **File:** `apps/integrations/services.py:299`
- **Function/Class:** `mark_attempt_dead_letter`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0595

- **ID:** MC-0595
- **File:** `apps/laboratory/services.py:172`
- **Function/Class:** `transition_lab_sample`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0596

- **ID:** MC-0596
- **File:** `apps/laboratory/services.py:217`
- **Function/Class:** `create_lab_test`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0597

- **ID:** MC-0597
- **File:** `apps/laboratory/services.py:361`
- **Function/Class:** `verify_lab_result`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0598

- **ID:** MC-0598
- **File:** `apps/laboratory/services.py:394`
- **Function/Class:** `finalize_lab_result`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0599

- **ID:** MC-0599
- **File:** `apps/laboratory/services.py:440`
- **Function/Class:** `amend_lab_result`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0600

- **ID:** MC-0600
- **File:** `apps/master_data/services.py:224`
- **Function/Class:** `update_fg_product`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0601

- **ID:** MC-0601
- **File:** `apps/master_data/services.py:285`
- **Function/Class:** `activate_fg_product`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0602

- **ID:** MC-0602
- **File:** `apps/master_data/services.py:304`
- **Function/Class:** `deactivate_fg_product`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0603

- **ID:** MC-0603
- **File:** `apps/master_data/specification_services.py:243`
- **Function/Class:** `create_specification_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0604

- **ID:** MC-0604
- **File:** `apps/master_data/specification_services.py:290`
- **Function/Class:** `update_draft_specification_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0605

- **ID:** MC-0605
- **File:** `apps/master_data/specification_services.py:356`
- **Function/Class:** `upsert_specification_parameter`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0606

- **ID:** MC-0606
- **File:** `apps/master_data/specification_services.py:376`
- **Function/Class:** `upsert_specification_parameter`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0607

- **ID:** MC-0607
- **File:** `apps/master_data/specification_services.py:441`
- **Function/Class:** `remove_specification_parameter`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0608

- **ID:** MC-0608
- **File:** `apps/master_data/specification_services.py:476`
- **Function/Class:** `approve_specification_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0609

- **ID:** MC-0609
- **File:** `apps/master_data/specification_services.py:517`
- **Function/Class:** `retire_specification_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0610

- **ID:** MC-0610
- **File:** `apps/nonconformance/services.py:188`
- **Function/Class:** `update_nonconformance_case_fields`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0611

- **ID:** MC-0611
- **File:** `apps/nonconformance/services.py:258`
- **Function/Class:** `transition_nonconformance_status`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0612

- **ID:** MC-0612
- **File:** `apps/nonconformance/services.py:308`
- **Function/Class:** `close_nonconformance`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0613

- **ID:** MC-0613
- **File:** `apps/nonconformance/services.py:435`
- **Function/Class:** `close_hold_case`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0614

- **ID:** MC-0614
- **File:** `apps/notifications/services.py:242`
- **Function/Class:** `mark_notification_read`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0615

- **ID:** MC-0615
- **File:** `apps/notifications/tasks.py:36`
- **Function/Class:** `deliver_notification_email`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0616

- **ID:** MC-0616
- **File:** `apps/organizations/services.py:221`
- **Function/Class:** `update_organization`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0617

- **ID:** MC-0617
- **File:** `apps/organizations/services.py:347`
- **Function/Class:** `update_site`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0618

- **ID:** MC-0618
- **File:** `apps/organizations/services.py:477`
- **Function/Class:** `update_department`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0619

- **ID:** MC-0619
- **File:** `apps/organizations/services.py:685`
- **Function/Class:** `update_shift`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0620

- **ID:** MC-0620
- **File:** `apps/organizations/services.py:752`
- **Function/Class:** `activate_shift`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0621

- **ID:** MC-0621
- **File:** `apps/organizations/services.py:771`
- **Function/Class:** `deactivate_shift`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0622

- **ID:** MC-0622
- **File:** `apps/quality/services.py:97`
- **Function/Class:** `create_qa_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0623

- **ID:** MC-0623
- **File:** `apps/quality/services.py:147`
- **Function/Class:** `create_qa_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0624

- **ID:** MC-0624
- **File:** `apps/quality/services.py:170`
- **Function/Class:** `create_qa_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0625

- **ID:** MC-0625
- **File:** `apps/quality_quarantine/services.py:174`
- **Function/Class:** `update_quarantine_quantity`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0626

- **ID:** MC-0626
- **File:** `apps/quality_quarantine/services.py:230`
- **Function/Class:** `release_quarantine_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0627

- **ID:** MC-0627
- **File:** `apps/quality_quarantine/services.py:290`
- **Function/Class:** `cancel_quarantine_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0628

- **ID:** MC-0628
- **File:** `apps/quality_quarantine/services.py:329`
- **Function/Class:** `record_erp_sync_status`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0629

- **ID:** MC-0629
- **File:** `apps/rca/services.py:93`
- **Function/Class:** `_locked_rca`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0630

- **ID:** MC-0630
- **File:** `apps/rca/services.py:110`
- **Function/Class:** `_locked_cause`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0631

- **ID:** MC-0631
- **File:** `apps/rca/services.py:426`
- **Function/Class:** `add_rca_evidence`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0632

- **ID:** MC-0632
- **File:** `apps/recording/correction_services.py:241`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0633

- **ID:** MC-0633
- **File:** `apps/recording/correction_services.py:257`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0634

- **ID:** MC-0634
- **File:** `apps/recording/correction_services.py:278`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0635

- **ID:** MC-0635
- **File:** `apps/recording/correction_services.py:442`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0636

- **ID:** MC-0636
- **File:** `apps/recording/correction_services.py:468`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0637

- **ID:** MC-0637
- **File:** `apps/recording/correction_services.py:517`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0638

- **ID:** MC-0638
- **File:** `apps/recording/services.py:164`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0639

- **ID:** MC-0639
- **File:** `apps/recording/services.py:694`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0640

- **ID:** MC-0640
- **File:** `apps/recording/services.py:730`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0641

- **ID:** MC-0641
- **File:** `apps/recording/services.py:939`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0642

- **ID:** MC-0642
- **File:** `apps/recording/services.py:993`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0643

- **ID:** MC-0643
- **File:** `apps/reports/services.py:268`
- **Function/Class:** `execute_report_run_by_id`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0644

- **ID:** MC-0644
- **File:** `apps/reviews/governance.py:205`
- **Function/Class:** `upsert_supervisor_review_governance_policy`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0645

- **ID:** MC-0645
- **File:** `apps/reviews/services.py:89`
- **Function/Class:** `create_supervisor_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0646

- **ID:** MC-0646
- **File:** `apps/reviews/services.py:140`
- **Function/Class:** `create_supervisor_review`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0647

- **ID:** MC-0647
- **File:** `apps/rework/services.py:208`
- **Function/Class:** `authorize_rework_case`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0648

- **ID:** MC-0648
- **File:** `apps/rework/services.py:234`
- **Function/Class:** `start_rework_case`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0649

- **ID:** MC-0649
- **File:** `apps/rework/services.py:318`
- **Function/Class:** `complete_rework_case`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0650

- **ID:** MC-0650
- **File:** `apps/rework/services.py:390`
- **Function/Class:** `cancel_rework_case`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0651

- **ID:** MC-0651
- **File:** `apps/rework/services.py:425`
- **Function/Class:** `open_rework_reinspection`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0652

- **ID:** MC-0652
- **File:** `apps/sampling/services.py:124`
- **Function/Class:** `create_draft_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0653

- **ID:** MC-0653
- **File:** `apps/sampling/services.py:288`
- **Function/Class:** `approve_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0654

- **ID:** MC-0654
- **File:** `apps/sampling/services.py:344`
- **Function/Class:** `retire_plan_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0655

- **ID:** MC-0655
- **File:** `apps/sanitation/services.py:141`
- **Function/Class:** `create_draft_program_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0656

- **ID:** MC-0656
- **File:** `apps/sanitation/services.py:196`
- **Function/Class:** `add_sanitation_scope`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0657

- **ID:** MC-0657
- **File:** `apps/sanitation/services.py:239`
- **Function/Class:** `add_schedule_link`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0658

- **ID:** MC-0658
- **File:** `apps/sanitation/services.py:303`
- **Function/Class:** `link_chemical_to_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0659

- **ID:** MC-0659
- **File:** `apps/sanitation/services.py:336`
- **Function/Class:** `approve_program_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0660

- **ID:** MC-0660
- **File:** `apps/sanitation/services.py:377`
- **Function/Class:** `retire_program_version`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0661

- **ID:** MC-0661
- **File:** `apps/sanitation/services.py:413`
- **Function/Class:** `bind_checklist_template_to_sanitation_program`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0662

- **ID:** MC-0662
- **File:** `apps/scheduling/applicability.py:537`
- **Function/Class:** `update_checklist_applicability_rule`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0663

- **ID:** MC-0663
- **File:** `apps/scheduling/applicability.py:604`
- **Function/Class:** `deactivate_checklist_applicability_rule`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0664

- **ID:** MC-0664
- **File:** `apps/scheduling/assignment.py:278`
- **Function/Class:** `assign_checklist_task`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0665

- **ID:** MC-0665
- **File:** `apps/scheduling/assignment.py:354`
- **Function/Class:** `unassign_checklist_task`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0666

- **ID:** MC-0666
- **File:** `apps/scheduling/batch_events.py:337`
- **Function/Class:** `process_external_batch_event`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0667

- **ID:** MC-0667
- **File:** `apps/scheduling/due.py:229`
- **Function/Class:** `set_checklist_task_due_window`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0668

- **ID:** MC-0668
- **File:** `apps/scheduling/generation.py:636`
- **Function/Class:** `deactivate_checklist_schedule`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0669

- **ID:** MC-0669
- **File:** `apps/scheduling/services.py:292`
- **Function/Class:** `cancel_checklist_task`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0670

- **ID:** MC-0670
- **File:** `apps/supplier_quality/services.py:127`
- **Function/Class:** `update_supplier_quality_profile`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0671

- **ID:** MC-0671
- **File:** `apps/supplier_quality/services.py:208`
- **Function/Class:** `verify_supplier_certificate`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0672

- **ID:** MC-0672
- **File:** `apps/training/services.py:267`
- **Function/Class:** `update_training_record`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0673

- **ID:** MC-0673
- **File:** `apps/training/services.py:334`
- **Function/Class:** `set_training_record_status`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0674

- **ID:** MC-0674
- **File:** `apps/training/services.py:384`
- **Function/Class:** `set_training_enforcement_policy`
- **Token:** `select_for_update` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Row lock unsupported on Mongo — redesign concurrency
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0675

- **ID:** MC-0675
- **File:** `apps/access_control/governance_services.py:54`
- **Function/Class:** `_resolve_permission_codenames`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0676

- **ID:** MC-0676
- **File:** `apps/access_control/governance_services.py:99`
- **Function/Class:** `set_role_permissions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0677

- **ID:** MC-0677
- **File:** `apps/access_control/governance_services.py:186`
- **Function/Class:** `update_role_template_permissions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0678

- **ID:** MC-0678
- **File:** `apps/access_control/governance_services.py:242`
- **Function/Class:** `apply_role_template_to_role`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0679

- **ID:** MC-0679
- **File:** `apps/access_control/selectors.py:27`
- **Function/Class:** `list_active_assignments_for_user`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0680

- **ID:** MC-0680
- **File:** `apps/access_control/services.py:34`
- **Function/Class:** `_active_assignments_qs`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0681

- **ID:** MC-0681
- **File:** `apps/access_control/services.py:183`
- **Function/Class:** `get_effective_permissions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0682

- **ID:** MC-0682
- **File:** `apps/batch_dossier/selectors.py:44`
- **Function/Class:** `tasks_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0683

- **ID:** MC-0683
- **File:** `apps/batch_dossier/selectors.py:63`
- **Function/Class:** `submissions_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0684

- **ID:** MC-0684
- **File:** `apps/batch_dossier/selectors.py:82`
- **Function/Class:** `corrections_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0685

- **ID:** MC-0685
- **File:** `apps/batch_dossier/selectors.py:101`
- **Function/Class:** `supervisor_reviews_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0686

- **ID:** MC-0686
- **File:** `apps/batch_dossier/selectors.py:117`
- **Function/Class:** `qa_reviews_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0687

- **ID:** MC-0687
- **File:** `apps/batch_dossier/selectors.py:136`
- **Function/Class:** `ipqc_cases_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0688

- **ID:** MC-0688
- **File:** `apps/batch_dossier/selectors.py:158`
- **Function/Class:** `lab_samples_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0689

- **ID:** MC-0689
- **File:** `apps/batch_dossier/selectors.py:190`
- **Function/Class:** `holds_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0690

- **ID:** MC-0690
- **File:** `apps/batch_dossier/selectors.py:205`
- **Function/Class:** `capas_for_batch_ncrs`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0691

- **ID:** MC-0691
- **File:** `apps/batch_dossier/selectors.py:233`
- **Function/Class:** `external_batch_events_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0692

- **ID:** MC-0692
- **File:** `apps/batch_dossier/selectors.py:262`
- **Function/Class:** `evidence_for_linked_targets`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0693

- **ID:** MC-0693
- **File:** `apps/batch_dossier/selectors.py:277`
- **Function/Class:** `audit_events_for_batch`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0694

- **ID:** MC-0694
- **File:** `apps/batch_dossier/selectors.py:305`
- **Function/Class:** `submissions_with_device_traces`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0695

- **ID:** MC-0695
- **File:** `apps/batch_genealogy/selectors.py:34`
- **Function/Class:** `edges_from_node`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0696

- **ID:** MC-0696
- **File:** `apps/batch_genealogy/selectors.py:42`
- **Function/Class:** `edges_to_node`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0697

- **ID:** MC-0697
- **File:** `apps/batch_genealogy/selectors.py:49`
- **Function/Class:** `edges_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0698

- **ID:** MC-0698
- **File:** `apps/batch_genealogy/services.py:515`
- **Function/Class:** `_trace`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0699

- **ID:** MC-0699
- **File:** `apps/batch_genealogy/services.py:524`
- **Function/Class:** `_trace`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0700

- **ID:** MC-0700
- **File:** `apps/capa/selectors.py:38`
- **Function/Class:** `list_corrective_actions_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0701

- **ID:** MC-0701
- **File:** `apps/capa/selectors.py:54`
- **Function/Class:** `list_corrective_actions_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0702

- **ID:** MC-0702
- **File:** `apps/capa/selectors.py:61`
- **Function/Class:** `list_capa_history`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0703

- **ID:** MC-0703
- **File:** `apps/capa/services.py:370`
- **Function/Class:** `complete_capa_action_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0704

- **ID:** MC-0704
- **File:** `apps/capa/views.py:47`
- **Function/Class:** `_load`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0705

- **ID:** MC-0705
- **File:** `apps/capa/views.py:123`
- **Function/Class:** `capa_detail`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0706

- **ID:** MC-0706
- **File:** `apps/change_control/services.py:130`
- **Function/Class:** `start_change_assessment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0707

- **ID:** MC-0707
- **File:** `apps/change_control/services.py:167`
- **Function/Class:** `record_change_impact_assessment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0708

- **ID:** MC-0708
- **File:** `apps/change_control/services.py:229`
- **Function/Class:** `add_affected_link`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0709

- **ID:** MC-0709
- **File:** `apps/change_control/services.py:291`
- **Function/Class:** `approve_quality_change`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0710

- **ID:** MC-0710
- **File:** `apps/change_control/services.py:339`
- **Function/Class:** `start_change_implementation`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0711

- **ID:** MC-0711
- **File:** `apps/change_control/services.py:373`
- **Function/Class:** `record_implementation_link`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0712

- **ID:** MC-0712
- **File:** `apps/change_control/services.py:431`
- **Function/Class:** `submit_change_for_verification`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0713

- **ID:** MC-0713
- **File:** `apps/change_control/services.py:466`
- **Function/Class:** `verify_and_close_quality_change`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0714

- **ID:** MC-0714
- **File:** `apps/checklists/effective_version.py:122`
- **Function/Class:** `published_versions_queryset`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0715

- **ID:** MC-0715
- **File:** `apps/checklists/effective_version.py:161`
- **Function/Class:** `resolve_effective_checklist_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0716

- **ID:** MC-0716
- **File:** `apps/checklists/effective_version.py:324`
- **Function/Class:** `set_checklist_version_effectivity`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0717

- **ID:** MC-0717
- **File:** `apps/checklists/proposal_loader.py:439`
- **Function/Class:** `_get_org_template`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0718

- **ID:** MC-0718
- **File:** `apps/checklists/proposal_loader.py:449`
- **Function/Class:** `_latest_draft`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0719

- **ID:** MC-0719
- **File:** `apps/checklists/selectors.py:83`
- **Function/Class:** `products_for_checklist_manage`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0720

- **ID:** MC-0720
- **File:** `apps/checklists/selectors.py:108`
- **Function/Class:** `list_checklist_templates`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0721

- **ID:** MC-0721
- **File:** `apps/checklists/selectors.py:136`
- **Function/Class:** `get_checklist_template`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0722

- **ID:** MC-0722
- **File:** `apps/checklists/selectors.py:164`
- **Function/Class:** `get_checklist_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0723

- **ID:** MC-0723
- **File:** `apps/checklists/selectors.py:185`
- **Function/Class:** `get_version_with_structure`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0724

- **ID:** MC-0724
- **File:** `apps/checklists/services.py:197`
- **Function/Class:** `_lock_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0725

- **ID:** MC-0725
- **File:** `apps/checklists/services.py:415`
- **Function/Class:** `set_checklist_item_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0726

- **ID:** MC-0726
- **File:** `apps/checklists/services.py:594`
- **Function/Class:** `set_checklist_calculation_operands`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0727

- **ID:** MC-0727
- **File:** `apps/checklists/services.py:616`
- **Function/Class:** `set_checklist_calculation_operands`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0728

- **ID:** MC-0728
- **File:** `apps/checklists/services.py:632`
- **Function/Class:** `ordered_operands_for_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0729

- **ID:** MC-0729
- **File:** `apps/checklists/services.py:725`
- **Function/Class:** `update_checklist_template`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0730

- **ID:** MC-0730
- **File:** `apps/checklists/services.py:899`
- **Function/Class:** `_lock_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0731

- **ID:** MC-0731
- **File:** `apps/checklists/services.py:993`
- **Function/Class:** `_clone_structure`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0732

- **ID:** MC-0732
- **File:** `apps/checklists/services.py:1003`
- **Function/Class:** `_clone_structure`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0733

- **ID:** MC-0733
- **File:** `apps/checklists/services.py:1089`
- **Function/Class:** `create_checklist_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0734

- **ID:** MC-0734
- **File:** `apps/checklists/services.py:1101`
- **Function/Class:** `create_checklist_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0735

- **ID:** MC-0735
- **File:** `apps/checklists/services.py:1198`
- **Function/Class:** `update_checklist_section`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0736

- **ID:** MC-0736
- **File:** `apps/checklists/services.py:1226`
- **Function/Class:** `remove_checklist_section`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0737

- **ID:** MC-0737
- **File:** `apps/checklists/services.py:1256`
- **Function/Class:** `move_checklist_section`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0738

- **ID:** MC-0738
- **File:** `apps/checklists/services.py:1306`
- **Function/Class:** `add_checklist_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0739

- **ID:** MC-0739
- **File:** `apps/checklists/services.py:1741`
- **Function/Class:** `update_checklist_item_option`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0740

- **ID:** MC-0740
- **File:** `apps/checklists/services.py:1786`
- **Function/Class:** `remove_checklist_item_option`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0741

- **ID:** MC-0741
- **File:** `apps/checklists/services.py:1821`
- **Function/Class:** `move_checklist_item_option`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0742

- **ID:** MC-0742
- **File:** `tests/test_checklist_governance.py:362`
- **Function/Class:** `test_admin_blocks_immutable_mutations`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0743

- **ID:** MC-0743
- **File:** `tests/test_checklist_governance.py:363`
- **Function/Class:** `test_admin_blocks_immutable_mutations`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0744

- **ID:** MC-0744
- **File:** `tests/test_checklist_response_schema.py:323`
- **Function/Class:** `test_admin_and_query_bounds_with_options`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0745

- **ID:** MC-0745
- **File:** `apps/checklists/views.py:151`
- **Function/Class:** `_template_form`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0746

- **ID:** MC-0746
- **File:** `apps/checklists/views.py:175`
- **Function/Class:** `template_list`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0747

- **ID:** MC-0747
- **File:** `apps/checklists/views.py:439`
- **Function/Class:** `section_edit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0748

- **ID:** MC-0748
- **File:** `apps/checklists/views.py:472`
- **Function/Class:** `section_delete`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0749

- **ID:** MC-0749
- **File:** `apps/checklists/views.py:495`
- **Function/Class:** `section_move`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0750

- **ID:** MC-0750
- **File:** `apps/checklists/views.py:518`
- **Function/Class:** `item_add`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0751

- **ID:** MC-0751
- **File:** `apps/checklists/views.py:564`
- **Function/Class:** `item_edit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0752

- **ID:** MC-0752
- **File:** `apps/checklists/views.py:623`
- **Function/Class:** `item_delete`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0753

- **ID:** MC-0753
- **File:** `apps/checklists/views.py:648`
- **Function/Class:** `item_move`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0754

- **ID:** MC-0754
- **File:** `apps/checklists/views.py:673`
- **Function/Class:** `option_add`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0755

- **ID:** MC-0755
- **File:** `apps/checklists/views.py:707`
- **Function/Class:** `option_edit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0756

- **ID:** MC-0756
- **File:** `apps/checklists/views.py:745`
- **Function/Class:** `option_delete`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0757

- **ID:** MC-0757
- **File:** `apps/checklists/views.py:772`
- **Function/Class:** `option_move`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0758

- **ID:** MC-0758
- **File:** `apps/compliance_mapping/selectors.py:61`
- **Function/Class:** `list_control_mappings`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0759

- **ID:** MC-0759
- **File:** `apps/compliance_mapping/selectors.py:76`
- **Function/Class:** `list_open_gaps`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0760

- **ID:** MC-0760
- **File:** `apps/compliance_mapping/services.py:268`
- **Function/Class:** `add_source_edition`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0761

- **ID:** MC-0761
- **File:** `apps/compliance_mapping/services.py:335`
- **Function/Class:** `update_edition_applicability`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0762

- **ID:** MC-0762
- **File:** `apps/compliance_mapping/services.py:371`
- **Function/Class:** `withdraw_source_edition`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0763

- **ID:** MC-0763
- **File:** `apps/compliance_mapping/services.py:408`
- **Function/Class:** `create_control_mapping`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0764

- **ID:** MC-0764
- **File:** `apps/compliance_mapping/services.py:457`
- **Function/Class:** `transition_mapping_status`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0765

- **ID:** MC-0765
- **File:** `apps/compliance_mapping/services.py:493`
- **Function/Class:** `verify_control_mapping`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0766

- **ID:** MC-0766
- **File:** `apps/compliance_mapping/services.py:533`
- **Function/Class:** `link_mapping_evidence`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0767

- **ID:** MC-0767
- **File:** `apps/compliance_mapping/services.py:579`
- **Function/Class:** `record_compliance_gap`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0768

- **ID:** MC-0768
- **File:** `apps/compliance_mapping/services.py:640`
- **Function/Class:** `link_gap_action`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0769

- **ID:** MC-0769
- **File:** `apps/compliance_mapping/services.py:839`
- **Function/Class:** `close_compliance_gap`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0770

- **ID:** MC-0770
- **File:** `apps/core/checklist_workflow.py:308`
- **Function/Class:** `prefetch_workflow_graph`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0771

- **ID:** MC-0771
- **File:** `apps/core/checklist_workflow.py:316`
- **Function/Class:** `prefetch_workflow_graph`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0772

- **ID:** MC-0772
- **File:** `apps/customer_complaints/selectors.py:38`
- **Function/Class:** `list_complaints_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0773

- **ID:** MC-0773
- **File:** `apps/customer_complaints/selectors.py:48`
- **Function/Class:** `get_complaint_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0774

- **ID:** MC-0774
- **File:** `apps/customer_complaints/selectors.py:65`
- **Function/Class:** `timeline_for_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0775

- **ID:** MC-0775
- **File:** `apps/customer_complaints/views.py:40`
- **Function/Class:** `_load`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0776

- **ID:** MC-0776
- **File:** `apps/dispatch/selectors.py:42`
- **Function/Class:** `list_dispatch_records_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0777

- **ID:** MC-0777
- **File:** `apps/dispatch/selectors.py:49`
- **Function/Class:** `list_dispatch_history`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0778

- **ID:** MC-0778
- **File:** `apps/dispatch/selectors.py:62`
- **Function/Class:** `list_dispatch_records_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0779

- **ID:** MC-0779
- **File:** `apps/dispatch/views.py:40`
- **Function/Class:** `_load`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0780

- **ID:** MC-0780
- **File:** `apps/document_control/selectors.py:92`
- **Function/Class:** `list_controlled_versions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0781

- **ID:** MC-0781
- **File:** `apps/document_control/selectors.py:106`
- **Function/Class:** `list_record_document_links`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0782

- **ID:** MC-0782
- **File:** `apps/document_control/services.py:157`
- **Function/Class:** `create_document_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0783

- **ID:** MC-0783
- **File:** `apps/document_control/services.py:206`
- **Function/Class:** `update_draft_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0784

- **ID:** MC-0784
- **File:** `apps/document_control/services.py:246`
- **Function/Class:** `submit_version_for_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0785

- **ID:** MC-0785
- **File:** `apps/document_control/services.py:272`
- **Function/Class:** `return_version_to_draft`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0786

- **ID:** MC-0786
- **File:** `apps/document_control/services.py:303`
- **Function/Class:** `approve_document_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0787

- **ID:** MC-0787
- **File:** `apps/document_control/services.py:352`
- **Function/Class:** `make_version_effective`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0788

- **ID:** MC-0788
- **File:** `apps/document_control/services.py:430`
- **Function/Class:** `retire_document_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0789

- **ID:** MC-0789
- **File:** `apps/document_control/services.py:492`
- **Function/Class:** `acknowledge_document_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0790

- **ID:** MC-0790
- **File:** `apps/document_control/services.py:538`
- **Function/Class:** `link_quality_record_to_document_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0791

- **ID:** MC-0791
- **File:** `apps/environmental/selectors.py:20`
- **Function/Class:** `points_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0792

- **ID:** MC-0792
- **File:** `apps/environmental/selectors.py:57`
- **Function/Class:** `readings_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0793

- **ID:** MC-0793
- **File:** `apps/environmental/services.py:269`
- **Function/Class:** `add_limit_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0794

- **ID:** MC-0794
- **File:** `apps/environmental/services.py:306`
- **Function/Class:** `approve_spec_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0795

- **ID:** MC-0795
- **File:** `apps/environmental/services.py:336`
- **Function/Class:** `retire_spec_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0796

- **ID:** MC-0796
- **File:** `apps/environmental/services.py:400`
- **Function/Class:** `_resolve_approved_limit_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0797

- **ID:** MC-0797
- **File:** `apps/environmental/services.py:409`
- **Function/Class:** `_resolve_approved_limit_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0798

- **ID:** MC-0798
- **File:** `apps/environmental/services.py:419`
- **Function/Class:** `_resolve_approved_limit_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0799

- **ID:** MC-0799
- **File:** `apps/evidence/linking.py:118`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0800

- **ID:** MC-0800
- **File:** `apps/evidence/linking.py:139`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0801

- **ID:** MC-0801
- **File:** `apps/evidence/linking.py:158`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0802

- **ID:** MC-0802
- **File:** `apps/evidence/linking.py:178`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0803

- **ID:** MC-0803
- **File:** `apps/evidence/linking.py:247`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0804

- **ID:** MC-0804
- **File:** `apps/evidence/linking.py:285`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0805

- **ID:** MC-0805
- **File:** `apps/evidence/linking.py:394`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0806

- **ID:** MC-0806
- **File:** `apps/evidence/linking.py:412`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0807

- **ID:** MC-0807
- **File:** `apps/evidence/linking.py:426`
- **Function/Class:** `resolve_linked_target`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0808

- **ID:** MC-0808
- **File:** `apps/evidence/selectors.py:45`
- **Function/Class:** `list_evidence_for_link`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0809

- **ID:** MC-0809
- **File:** `apps/evidence/selectors.py:59`
- **Function/Class:** `get_evidence_attachment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0810

- **ID:** MC-0810
- **File:** `apps/evidence/services.py:172`
- **Function/Class:** `authorize_evidence_download`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0811

- **ID:** MC-0811
- **File:** `apps/foreign_body/selectors.py:29`
- **Function/Class:** `challenge_tests_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0812

- **ID:** MC-0812
- **File:** `apps/foreign_body/services.py:304`
- **Function/Class:** `verify_challenge_test`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0813

- **ID:** MC-0813
- **File:** `apps/haccp/selectors.py:34`
- **Function/Class:** `plans_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0814

- **ID:** MC-0814
- **File:** `apps/haccp/selectors.py:48`
- **Function/Class:** `control_points_for_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0815

- **ID:** MC-0815
- **File:** `apps/haccp/selectors.py:64`
- **Function/Class:** `approved_versions_effective_on`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0816

- **ID:** MC-0816
- **File:** `apps/haccp/services.py:229`
- **Function/Class:** `add_process_step`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0817

- **ID:** MC-0817
- **File:** `apps/haccp/services.py:272`
- **Function/Class:** `add_hazard`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0818

- **ID:** MC-0818
- **File:** `apps/haccp/services.py:310`
- **Function/Class:** `add_control_measure`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0819

- **ID:** MC-0819
- **File:** `apps/haccp/services.py:350`
- **Function/Class:** `add_control_point`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0820

- **ID:** MC-0820
- **File:** `apps/haccp/services.py:419`
- **Function/Class:** `set_critical_limit_reference`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0821

- **ID:** MC-0821
- **File:** `apps/haccp/services.py:464`
- **Function/Class:** `set_monitoring_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0822

- **ID:** MC-0822
- **File:** `apps/haccp/services.py:499`
- **Function/Class:** `set_corrective_action_reference`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0823

- **ID:** MC-0823
- **File:** `apps/haccp/services.py:536`
- **Function/Class:** `approve_plan_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0824

- **ID:** MC-0824
- **File:** `apps/haccp/services.py:595`
- **Function/Class:** `retire_plan_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0825

- **ID:** MC-0825
- **File:** `apps/haccp/services.py:641`
- **Function/Class:** `bind_checklist_item_to_control_point`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0826

- **ID:** MC-0826
- **File:** `apps/haccp/services.py:654`
- **Function/Class:** `bind_checklist_item_to_control_point`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0827

- **ID:** MC-0827
- **File:** `apps/haccp/services.py:669`
- **Function/Class:** `bind_checklist_item_to_control_point`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0828

- **ID:** MC-0828
- **File:** `apps/haccp/snapshots.py:33`
- **Function/Class:** `snapshot_for_checklist_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0829

- **ID:** MC-0829
- **File:** `apps/haccp/views.py:49`
- **Function/Class:** `haccp_plan_detail`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0830

- **ID:** MC-0830
- **File:** `apps/instruments/selectors.py:45`
- **Function/Class:** `get_equipment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0831

- **ID:** MC-0831
- **File:** `apps/instruments/selectors.py:69`
- **Function/Class:** `list_equipment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0832

- **ID:** MC-0832
- **File:** `apps/instruments/selectors.py:100`
- **Function/Class:** `list_calibration_records`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0833

- **ID:** MC-0833
- **File:** `apps/instruments/services.py:179`
- **Function/Class:** `update_equipment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0834

- **ID:** MC-0834
- **File:** `apps/instruments/services.py:326`
- **Function/Class:** `create_calibration_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0835

- **ID:** MC-0835
- **File:** `apps/instruments/services.py:364`
- **Function/Class:** `update_calibration_certificate_metadata`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0836

- **ID:** MC-0836
- **File:** `apps/integrations/reconciliation.py:37`
- **Function/Class:** `reconcile_external_batch_events`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0837

- **ID:** MC-0837
- **File:** `apps/ipqc/selectors.py:72`
- **Function/Class:** `cases_due`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0838

- **ID:** MC-0838
- **File:** `apps/ipqc/selectors.py:91`
- **Function/Class:** `cases_overdue`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0839

- **ID:** MC-0839
- **File:** `apps/ipqc/selectors.py:107`
- **Function/Class:** `cases_with_failure`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0840

- **ID:** MC-0840
- **File:** `apps/iqc/services.py:498`
- **Function/Class:** `ingest_incoming_receipt_event`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0841

- **ID:** MC-0841
- **File:** `apps/laboratory/selectors.py:34`
- **Function/Class:** `samples_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0842

- **ID:** MC-0842
- **File:** `apps/laboratory/selectors.py:41`
- **Function/Class:** `samples_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0843

- **ID:** MC-0843
- **File:** `apps/laboratory/selectors.py:48`
- **Function/Class:** `latest_results_for_sample`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0844

- **ID:** MC-0844
- **File:** `apps/laboratory/services.py:269`
- **Function/Class:** `enter_lab_result`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0845

- **ID:** MC-0845
- **File:** `apps/laboratory/views.py:52`
- **Function/Class:** `lab_sample_detail`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0846

- **ID:** MC-0846
- **File:** `apps/master_data/selectors.py:61`
- **Function/Class:** `get_fg_product`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0847

- **ID:** MC-0847
- **File:** `apps/master_data/selectors.py:84`
- **Function/Class:** `list_fg_products`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0848

- **ID:** MC-0848
- **File:** `apps/master_data/selectors.py:155`
- **Function/Class:** `get_product_specification`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0849

- **ID:** MC-0849
- **File:** `apps/master_data/selectors.py:181`
- **Function/Class:** `list_product_specifications`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0850

- **ID:** MC-0850
- **File:** `apps/master_data/selectors.py:197`
- **Function/Class:** `get_specification_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0851

- **ID:** MC-0851
- **File:** `apps/master_data/services.py:224`
- **Function/Class:** `update_fg_product`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0852

- **ID:** MC-0852
- **File:** `apps/master_data/specification_services.py:243`
- **Function/Class:** `create_specification_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0853

- **ID:** MC-0853
- **File:** `apps/master_data/specification_services.py:290`
- **Function/Class:** `update_draft_specification_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0854

- **ID:** MC-0854
- **File:** `apps/master_data/specification_services.py:356`
- **Function/Class:** `upsert_specification_parameter`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0855

- **ID:** MC-0855
- **File:** `apps/master_data/specification_services.py:441`
- **Function/Class:** `remove_specification_parameter`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0856

- **ID:** MC-0856
- **File:** `apps/master_data/specification_services.py:476`
- **Function/Class:** `approve_specification_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0857

- **ID:** MC-0857
- **File:** `apps/master_data/specification_services.py:517`
- **Function/Class:** `retire_specification_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0858

- **ID:** MC-0858
- **File:** `apps/master_data/specification_services.py:551`
- **Function/Class:** `clone_specification_version_as_draft`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0859

- **ID:** MC-0859
- **File:** `apps/nonconformance/selectors.py:42`
- **Function/Class:** `list_nonconformances_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0860

- **ID:** MC-0860
- **File:** `apps/nonconformance/selectors.py:58`
- **Function/Class:** `list_nonconformances_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0861

- **ID:** MC-0861
- **File:** `apps/nonconformance/selectors.py:73`
- **Function/Class:** `list_hold_cases_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0862

- **ID:** MC-0862
- **File:** `apps/nonconformance/selectors.py:85`
- **Function/Class:** `list_case_history`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0863

- **ID:** MC-0863
- **File:** `apps/nonconformance/views.py:47`
- **Function/Class:** `_load`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0864

- **ID:** MC-0864
- **File:** `apps/nonconformance/views.py:131`
- **Function/Class:** `ncr_detail`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0865

- **ID:** MC-0865
- **File:** `apps/notifications/selectors.py:16`
- **Function/Class:** `notifications_for_recipient`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0866

- **ID:** MC-0866
- **File:** `apps/notifications/tasks.py:36`
- **Function/Class:** `deliver_notification_email`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0867

- **ID:** MC-0867
- **File:** `apps/organizations/hierarchy_import.py:537`
- **Function/Class:** `import_organization_hierarchy`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0868

- **ID:** MC-0868
- **File:** `apps/organizations/hierarchy_import.py:540`
- **Function/Class:** `import_organization_hierarchy`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0869

- **ID:** MC-0869
- **File:** `apps/organizations/selectors.py:38`
- **Function/Class:** `get_site_by_id`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0870

- **ID:** MC-0870
- **File:** `apps/organizations/selectors.py:49`
- **Function/Class:** `list_sites_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0871

- **ID:** MC-0871
- **File:** `apps/organizations/selectors.py:54`
- **Function/Class:** `get_department_by_id`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0872

- **ID:** MC-0872
- **File:** `apps/organizations/selectors.py:66`
- **Function/Class:** `list_departments_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0873

- **ID:** MC-0873
- **File:** `apps/organizations/selectors.py:77`
- **Function/Class:** `list_departments_for_site`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0874

- **ID:** MC-0874
- **File:** `apps/organizations/selectors.py:110`
- **Function/Class:** `get_shift_by_id`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0875

- **ID:** MC-0875
- **File:** `apps/organizations/selectors.py:134`
- **Function/Class:** `list_shifts_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0876

- **ID:** MC-0876
- **File:** `apps/organizations/selectors.py:159`
- **Function/Class:** `list_shifts_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0877

- **ID:** MC-0877
- **File:** `apps/organizations/services.py:347`
- **Function/Class:** `update_site`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0878

- **ID:** MC-0878
- **File:** `apps/organizations/services.py:477`
- **Function/Class:** `update_department`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0879

- **ID:** MC-0879
- **File:** `apps/organizations/services.py:685`
- **Function/Class:** `update_shift`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0880

- **ID:** MC-0880
- **File:** `apps/packaging/services.py:320`
- **Function/Class:** `bind_checklist_item_to_artwork`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0881

- **ID:** MC-0881
- **File:** `apps/packaging/services.py:373`
- **Function/Class:** `create_line_clearance_hook`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0882

- **ID:** MC-0882
- **File:** `apps/packaging/services.py:440`
- **Function/Class:** `record_artwork_verification`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0883

- **ID:** MC-0883
- **File:** `apps/packaging/snapshots.py:39`
- **Function/Class:** `snapshot_for_checklist_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0884

- **ID:** MC-0884
- **File:** `apps/process_fmea/selectors.py:45`
- **Function/Class:** `list_failure_modes`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0885

- **ID:** MC-0885
- **File:** `apps/process_fmea/services.py:244`
- **Function/Class:** `add_process_step`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0886

- **ID:** MC-0886
- **File:** `apps/process_fmea/services.py:279`
- **Function/Class:** `add_failure_mode`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0887

- **ID:** MC-0887
- **File:** `apps/process_fmea/services.py:313`
- **Function/Class:** `add_failure_effect`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0888

- **ID:** MC-0888
- **File:** `apps/process_fmea/services.py:326`
- **Function/Class:** `add_potential_cause`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0889

- **ID:** MC-0889
- **File:** `apps/process_fmea/services.py:343`
- **Function/Class:** `add_current_control`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0890

- **ID:** MC-0890
- **File:** `apps/process_fmea/services.py:368`
- **Function/Class:** `record_failure_mode_assessment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0891

- **ID:** MC-0891
- **File:** `apps/process_fmea/services.py:471`
- **Function/Class:** `add_recommended_action`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0892

- **ID:** MC-0892
- **File:** `apps/process_fmea/services.py:580`
- **Function/Class:** `link_process_fmea`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0893

- **ID:** MC-0893
- **File:** `apps/process_fmea/services.py:676`
- **Function/Class:** `apply_scoring_policy_to_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0894

- **ID:** MC-0894
- **File:** `apps/process_fmea/services.py:689`
- **Function/Class:** `approve_process_fmea_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0895

- **ID:** MC-0895
- **File:** `apps/process_fmea/services.py:721`
- **Function/Class:** `withdraw_process_fmea_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0896

- **ID:** MC-0896
- **File:** `apps/product_returns/services.py:216`
- **Function/Class:** `start_return_inspection`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0897

- **ID:** MC-0897
- **File:** `apps/quality/mongo_spike.py:50`
- **Function/Class:** `create_qa_review_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0898

- **ID:** MC-0898
- **File:** `apps/quality/mongo_spike.py:155`
- **Function/Class:** `create_qa_review_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0899

- **ID:** MC-0899
- **File:** `apps/quality/selectors.py:57`
- **Function/Class:** `list_qa_reviewable_submissions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0900

- **ID:** MC-0900
- **File:** `apps/quality/selectors.py:83`
- **Function/Class:** `get_checklist_submission_for_qa`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0901

- **ID:** MC-0901
- **File:** `apps/quality/selectors.py:110`
- **Function/Class:** `get_qa_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0902

- **ID:** MC-0902
- **File:** `apps/quality/selectors.py:171`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0903

- **ID:** MC-0903
- **File:** `apps/quality/selectors.py:178`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0904

- **ID:** MC-0904
- **File:** `apps/quality/selectors.py:183`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0905

- **ID:** MC-0905
- **File:** `apps/quality/selectors.py:190`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0906

- **ID:** MC-0906
- **File:** `apps/quality/selectors.py:195`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0907

- **ID:** MC-0907
- **File:** `apps/quality/selectors.py:200`
- **Function/Class:** `load_qa_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0908

- **ID:** MC-0908
- **File:** `apps/quality/services.py:97`
- **Function/Class:** `create_qa_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0909

- **ID:** MC-0909
- **File:** `apps/quality/services.py:204`
- **Function/Class:** `create_qa_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0910

- **ID:** MC-0910
- **File:** `apps/quality/services.py:226`
- **Function/Class:** `create_qa_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0911

- **ID:** MC-0911
- **File:** `apps/quality_audits/selectors.py:46`
- **Function/Class:** `list_findings_for_audit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0912

- **ID:** MC-0912
- **File:** `apps/quality_audits/selectors.py:59`
- **Function/Class:** `report_open_findings`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0913

- **ID:** MC-0913
- **File:** `apps/quality_audits/selectors.py:82`
- **Function/Class:** `report_overdue_findings`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0914

- **ID:** MC-0914
- **File:** `apps/quality_audits/selectors.py:107`
- **Function/Class:** `report_capa_links`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0915

- **ID:** MC-0915
- **File:** `apps/quality_audits/services.py:156`
- **Function/Class:** `add_audit_participant`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0916

- **ID:** MC-0916
- **File:** `apps/quality_audits/services.py:218`
- **Function/Class:** `bind_audit_checklist`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0917

- **ID:** MC-0917
- **File:** `apps/quality_audits/services.py:234`
- **Function/Class:** `bind_audit_checklist`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0918

- **ID:** MC-0918
- **File:** `apps/quality_audits/services.py:257`
- **Function/Class:** `start_quality_audit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0919

- **ID:** MC-0919
- **File:** `apps/quality_audits/services.py:290`
- **Function/Class:** `create_audit_finding`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0920

- **ID:** MC-0920
- **File:** `apps/quality_audits/services.py:361`
- **Function/Class:** `complete_finding_action`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0921

- **ID:** MC-0921
- **File:** `apps/quality_audits/services.py:392`
- **Function/Class:** `verify_audit_finding`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0922

- **ID:** MC-0922
- **File:** `apps/quality_audits/services.py:421`
- **Function/Class:** `close_audit_finding`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0923

- **ID:** MC-0923
- **File:** `apps/quality_audits/services.py:461`
- **Function/Class:** `link_finding_quality_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0924

- **ID:** MC-0924
- **File:** `apps/quality_audits/services.py:551`
- **Function/Class:** `cancel_quality_audit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0925

- **ID:** MC-0925
- **File:** `apps/quality_audits/services.py:577`
- **Function/Class:** `reopen_finding_action`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0926

- **ID:** MC-0926
- **File:** `apps/quality_audits/services.py:596`
- **Function/Class:** `close_quality_audit`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0927

- **ID:** MC-0927
- **File:** `apps/quality_quarantine/selectors.py:34`
- **Function/Class:** `list_quarantines_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0928

- **ID:** MC-0928
- **File:** `apps/quality_quarantine/selectors.py:73`
- **Function/Class:** `events_for_quarantine`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0929

- **ID:** MC-0929
- **File:** `apps/quality_quarantine/views.py:44`
- **Function/Class:** `_load`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0930

- **ID:** MC-0930
- **File:** `apps/quality_risks/services.py:229`
- **Function/Class:** `open_quality_risk`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0931

- **ID:** MC-0931
- **File:** `apps/quality_risks/services.py:254`
- **Function/Class:** `accept_quality_risk`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0932

- **ID:** MC-0932
- **File:** `apps/quality_risks/services.py:291`
- **Function/Class:** `close_quality_risk`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0933

- **ID:** MC-0933
- **File:** `apps/quality_risks/services.py:316`
- **Function/Class:** `cancel_quality_risk`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0934

- **ID:** MC-0934
- **File:** `apps/quality_risks/services.py:352`
- **Function/Class:** `record_risk_assessment`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0935

- **ID:** MC-0935
- **File:** `apps/quality_risks/services.py:423`
- **Function/Class:** `record_risk_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0936

- **ID:** MC-0936
- **File:** `apps/quality_risks/services.py:467`
- **Function/Class:** `link_quality_risk`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0937

- **ID:** MC-0937
- **File:** `apps/quality_risks/services.py:524`
- **Function/Class:** `add_risk_mitigation`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0938

- **ID:** MC-0938
- **File:** `apps/rca/selectors.py:41`
- **Function/Class:** `list_rcas_for_actor`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0939

- **ID:** MC-0939
- **File:** `apps/rca/services.py:93`
- **Function/Class:** `_locked_rca`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0940

- **ID:** MC-0940
- **File:** `apps/rca/services.py:110`
- **Function/Class:** `_locked_cause`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0941

- **ID:** MC-0941
- **File:** `apps/rca/views.py:181`
- **Function/Class:** `rca_detail`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0942

- **ID:** MC-0942
- **File:** `apps/rca/views.py:326`
- **Function/Class:** `rca_support_cause`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0943

- **ID:** MC-0943
- **File:** `apps/rca/views.py:353`
- **Function/Class:** `rca_confirm_cause`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0944

- **ID:** MC-0944
- **File:** `apps/rca/views.py:380`
- **Function/Class:** `rca_link_capa`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0945

- **ID:** MC-0945
- **File:** `apps/recall/mock_services.py:528`
- **Function/Class:** `link_mock_finding_to_ncr`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0946

- **ID:** MC-0946
- **File:** `apps/recall/mock_services.py:588`
- **Function/Class:** `link_mock_finding_to_capa`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0947

- **ID:** MC-0947
- **File:** `apps/recall/mock_services.py:647`
- **Function/Class:** `create_mock_improvement_action`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0948

- **ID:** MC-0948
- **File:** `apps/recall/selectors.py:18`
- **Function/Class:** `get_recall_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0949

- **ID:** MC-0949
- **File:** `apps/recall/selectors.py:37`
- **Function/Class:** `timeline_for_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0950

- **ID:** MC-0950
- **File:** `apps/recall/services.py:85`
- **Function/Class:** `user_has_explicit_scoped_permission`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0951

- **ID:** MC-0951
- **File:** `apps/recall/services.py:968`
- **Function/Class:** `serialize_recall_case`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0952

- **ID:** MC-0952
- **File:** `apps/recording/calculation_runtime.py:23`
- **Function/Class:** `ordered_operands`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0953

- **ID:** MC-0953
- **File:** `apps/recording/condition_runtime.py:57`
- **Function/Class:** `load_rules_for_items`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0954

- **ID:** MC-0954
- **File:** `apps/recording/correction_services.py:57`
- **Function/Class:** `get_active_correction_for_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0955

- **ID:** MC-0955
- **File:** `apps/recording/correction_services.py:197`
- **Function/Class:** `_clone_working_responses_from_snapshot`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0956

- **ID:** MC-0956
- **File:** `apps/recording/correction_services.py:241`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0957

- **ID:** MC-0957
- **File:** `apps/recording/correction_services.py:257`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0958

- **ID:** MC-0958
- **File:** `apps/recording/correction_services.py:304`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0959

- **ID:** MC-0959
- **File:** `apps/recording/correction_services.py:317`
- **Function/Class:** `start_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0960

- **ID:** MC-0960
- **File:** `apps/recording/correction_services.py:442`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0961

- **ID:** MC-0961
- **File:** `apps/recording/correction_services.py:468`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0962

- **ID:** MC-0962
- **File:** `apps/recording/correction_services.py:507`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0963

- **ID:** MC-0963
- **File:** `apps/recording/correction_services.py:517`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0964

- **ID:** MC-0964
- **File:** `apps/recording/correction_services.py:638`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0965

- **ID:** MC-0965
- **File:** `apps/recording/correction_services.py:654`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0966

- **ID:** MC-0966
- **File:** `apps/recording/daily_selectors.py:63`
- **Function/Class:** `controlled_records_qs`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0967

- **ID:** MC-0967
- **File:** `apps/recording/daily_selectors.py:78`
- **Function/Class:** `_with_latest_submission`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0968

- **ID:** MC-0968
- **File:** `apps/recording/daily_selectors.py:148`
- **Function/Class:** `print_record_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0969

- **ID:** MC-0969
- **File:** `apps/recording/daily_selectors.py:153`
- **Function/Class:** `print_record_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0970

- **ID:** MC-0970
- **File:** `apps/recording/daily_selectors.py:195`
- **Function/Class:** `monthly_pack_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0971

- **ID:** MC-0971
- **File:** `apps/recording/daily_selectors.py:209`
- **Function/Class:** `monthly_pack_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0972

- **ID:** MC-0972
- **File:** `apps/recording/evaluation_runtime.py:24`
- **Function/Class:** `load_evaluation_rules`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0973

- **ID:** MC-0973
- **File:** `apps/recording/mongo_spike.py:37`
- **Function/Class:** `start_checklist_recording_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0974

- **ID:** MC-0974
- **File:** `apps/recording/mongo_spike.py:52`
- **Function/Class:** `start_checklist_recording_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0975

- **ID:** MC-0975
- **File:** `apps/recording/mongo_spike.py:101`
- **Function/Class:** `start_checklist_recording_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0976

- **ID:** MC-0976
- **File:** `apps/recording/selectors.py:57`
- **Function/Class:** `list_recordable_checklist_tasks`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0977

- **ID:** MC-0977
- **File:** `apps/recording/selectors.py:66`
- **Function/Class:** `list_recordable_checklist_tasks`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0978

- **ID:** MC-0978
- **File:** `apps/recording/selectors.py:83`
- **Function/Class:** `get_recordable_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0979

- **ID:** MC-0979
- **File:** `apps/recording/selectors.py:102`
- **Function/Class:** `get_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0980

- **ID:** MC-0980
- **File:** `apps/recording/selectors.py:126`
- **Function/Class:** `get_checklist_submission`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0981

- **ID:** MC-0981
- **File:** `apps/recording/selectors.py:156`
- **Function/Class:** `get_latest_checklist_submission_for_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0982

- **ID:** MC-0982
- **File:** `apps/recording/selectors.py:169`
- **Function/Class:** `_load_sections`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0983

- **ID:** MC-0983
- **File:** `apps/recording/selectors.py:211`
- **Function/Class:** `load_record_editor_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0984

- **ID:** MC-0984
- **File:** `apps/recording/selectors.py:253`
- **Function/Class:** `load_submitted_record_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0985

- **ID:** MC-0985
- **File:** `apps/recording/selectors.py:265`
- **Function/Class:** `load_submitted_record_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0986

- **ID:** MC-0986
- **File:** `apps/recording/selectors.py:284`
- **Function/Class:** `get_checklist_correction`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0987

- **ID:** MC-0987
- **File:** `apps/recording/selectors.py:326`
- **Function/Class:** `load_correction_editor_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0988

- **ID:** MC-0988
- **File:** `apps/recording/selectors.py:347`
- **Function/Class:** `load_correction_editor_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0989

- **ID:** MC-0989
- **File:** `apps/recording/selectors.py:384`
- **Function/Class:** `load_record_history_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0990

- **ID:** MC-0990
- **File:** `apps/recording/selectors.py:391`
- **Function/Class:** `load_record_history_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0991

- **ID:** MC-0991
- **File:** `apps/recording/selectors.py:397`
- **Function/Class:** `load_record_history_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0992

- **ID:** MC-0992
- **File:** `apps/recording/selectors.py:411`
- **Function/Class:** `load_record_history_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0993

- **ID:** MC-0993
- **File:** `apps/recording/selectors.py:440`
- **Function/Class:** `load_returned_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0994

- **ID:** MC-0994
- **File:** `apps/recording/selectors.py:445`
- **Function/Class:** `load_returned_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0995

- **ID:** MC-0995
- **File:** `apps/recording/selectors.py:453`
- **Function/Class:** `load_returned_submission_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0996

- **ID:** MC-0996
- **File:** `apps/recording/services.py:133`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0997

- **ID:** MC-0997
- **File:** `apps/recording/services.py:148`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0998

- **ID:** MC-0998
- **File:** `apps/recording/services.py:164`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-0999

- **ID:** MC-0999
- **File:** `apps/recording/services.py:178`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1000

- **ID:** MC-1000
- **File:** `apps/recording/services.py:206`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1001

- **ID:** MC-1001
- **File:** `apps/recording/services.py:220`
- **Function/Class:** `start_checklist_recording`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1002

- **ID:** MC-1002
- **File:** `apps/recording/services.py:358`
- **Function/Class:** `collect_submission_completeness`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1003

- **ID:** MC-1003
- **File:** `apps/recording/services.py:366`
- **Function/Class:** `collect_submission_completeness`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1004

- **ID:** MC-1004
- **File:** `apps/recording/services.py:694`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1005

- **ID:** MC-1005
- **File:** `apps/recording/services.py:723`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1006

- **ID:** MC-1006
- **File:** `apps/recording/services.py:849`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1007

- **ID:** MC-1007
- **File:** `apps/recording/services.py:939`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1008

- **ID:** MC-1008
- **File:** `apps/recording/services.py:962`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1009

- **ID:** MC-1009
- **File:** `apps/recording/services.py:983`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1010

- **ID:** MC-1010
- **File:** `apps/recording/services.py:993`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1011

- **ID:** MC-1011
- **File:** `apps/recording/services.py:1099`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1012

- **ID:** MC-1012
- **File:** `apps/recording/services.py:1110`
- **Function/Class:** `submit_checklist_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1013

- **ID:** MC-1013
- **File:** `tests/test_phase06i_calculated_fields.py:452`
- **Function/Class:** `test_clone_preserves_calculation_operands`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1014

- **ID:** MC-1014
- **File:** `apps/reports/queries.py:111`
- **Function/Class:** `query_batch_checklist`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1015

- **ID:** MC-1015
- **File:** `apps/reports/queries.py:159`
- **Function/Class:** `query_submission_history`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1016

- **ID:** MC-1016
- **File:** `apps/reports/queries.py:215`
- **Function/Class:** `query_supervisor_reviews`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1017

- **ID:** MC-1017
- **File:** `apps/reports/queries.py:264`
- **Function/Class:** `query_qa_dispositions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1018

- **ID:** MC-1018
- **File:** `apps/reports/queries.py:312`
- **Function/Class:** `query_corrections`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1019

- **ID:** MC-1019
- **File:** `apps/reports/queries.py:416`
- **Function/Class:** `query_overdue_tasks`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1020

- **ID:** MC-1020
- **File:** `apps/reviews/governance.py:342`
- **Function/Class:** `revoke_temporary_supervisor_review_delegation`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1021

- **ID:** MC-1021
- **File:** `apps/reviews/mongo_spike.py:50`
- **Function/Class:** `create_supervisor_review_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1022

- **ID:** MC-1022
- **File:** `apps/reviews/mongo_spike.py:149`
- **Function/Class:** `create_supervisor_review_cas`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1023

- **ID:** MC-1023
- **File:** `apps/reviews/selectors.py:54`
- **Function/Class:** `_base_pending_queryset`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1024

- **ID:** MC-1024
- **File:** `apps/reviews/selectors.py:169`
- **Function/Class:** `get_checklist_submission_for_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1025

- **ID:** MC-1025
- **File:** `apps/reviews/selectors.py:196`
- **Function/Class:** `get_supervisor_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1026

- **ID:** MC-1026
- **File:** `apps/reviews/selectors.py:255`
- **Function/Class:** `load_submission_review_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1027

- **ID:** MC-1027
- **File:** `apps/reviews/selectors.py:262`
- **Function/Class:** `load_submission_review_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1028

- **ID:** MC-1028
- **File:** `apps/reviews/services.py:89`
- **Function/Class:** `create_supervisor_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1029

- **ID:** MC-1029
- **File:** `apps/reviews/services.py:178`
- **Function/Class:** `create_supervisor_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1030

- **ID:** MC-1030
- **File:** `apps/reviews/services.py:199`
- **Function/Class:** `create_supervisor_review`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1031

- **ID:** MC-1031
- **File:** `apps/rework/selectors.py:13`
- **Function/Class:** `list_cases_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1032

- **ID:** MC-1032
- **File:** `apps/rework/selectors.py:30`
- **Function/Class:** `get_case_for_org`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1033

- **ID:** MC-1033
- **File:** `apps/sampling/engine.py:140`
- **Function/Class:** `_effective_versions`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1034

- **ID:** MC-1034
- **File:** `apps/sampling/engine.py:200`
- **Function/Class:** `resolve_sampling_requirement`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1035

- **ID:** MC-1035
- **File:** `apps/sampling/selectors.py:21`
- **Function/Class:** `rules_for_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1036

- **ID:** MC-1036
- **File:** `apps/sampling/services.py:186`
- **Function/Class:** `add_sampling_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1037

- **ID:** MC-1037
- **File:** `apps/sampling/services.py:244`
- **Function/Class:** `set_sample_requirement`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1038

- **ID:** MC-1038
- **File:** `apps/sampling/services.py:288`
- **Function/Class:** `approve_plan_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1039

- **ID:** MC-1039
- **File:** `apps/sampling/services.py:344`
- **Function/Class:** `retire_plan_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1040

- **ID:** MC-1040
- **File:** `apps/sampling/services.py:383`
- **Function/Class:** `bind_checklist_item_to_sampling_plan`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1041

- **ID:** MC-1041
- **File:** `apps/sampling/services.py:397`
- **Function/Class:** `bind_checklist_item_to_sampling_plan`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1042

- **ID:** MC-1042
- **File:** `apps/sampling/snapshots.py:13`
- **Function/Class:** `snapshot_for_checklist_item`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1043

- **ID:** MC-1043
- **File:** `apps/sanitation/selectors.py:13`
- **Function/Class:** `programs_for_organization`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1044

- **ID:** MC-1044
- **File:** `apps/sanitation/services.py:196`
- **Function/Class:** `add_sanitation_scope`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1045

- **ID:** MC-1045
- **File:** `apps/sanitation/services.py:239`
- **Function/Class:** `add_schedule_link`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1046

- **ID:** MC-1046
- **File:** `apps/sanitation/services.py:303`
- **Function/Class:** `link_chemical_to_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1047

- **ID:** MC-1047
- **File:** `apps/sanitation/services.py:336`
- **Function/Class:** `approve_program_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1048

- **ID:** MC-1048
- **File:** `apps/sanitation/services.py:377`
- **Function/Class:** `retire_program_version`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1049

- **ID:** MC-1049
- **File:** `apps/sanitation/services.py:413`
- **Function/Class:** `bind_checklist_template_to_sanitation_program`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1050

- **ID:** MC-1050
- **File:** `apps/sanitation/snapshots.py:13`
- **Function/Class:** `snapshot_for_checklist_template`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1051

- **ID:** MC-1051
- **File:** `apps/sanitation/snapshots.py:61`
- **Function/Class:** `build_frozen_sanitation_context`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1052

- **ID:** MC-1052
- **File:** `apps/scheduling/applicability.py:261`
- **Function/Class:** `candidate_applicability_rules`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1053

- **ID:** MC-1053
- **File:** `apps/scheduling/applicability.py:537`
- **Function/Class:** `update_checklist_applicability_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1054

- **ID:** MC-1054
- **File:** `apps/scheduling/applicability.py:604`
- **Function/Class:** `deactivate_checklist_applicability_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1055

- **ID:** MC-1055
- **File:** `apps/scheduling/assignment.py:278`
- **Function/Class:** `assign_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1056

- **ID:** MC-1056
- **File:** `apps/scheduling/assignment.py:332`
- **Function/Class:** `assign_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1057

- **ID:** MC-1057
- **File:** `apps/scheduling/assignment.py:354`
- **Function/Class:** `unassign_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1058

- **ID:** MC-1058
- **File:** `apps/scheduling/assignment.py:399`
- **Function/Class:** `unassign_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1059

- **ID:** MC-1059
- **File:** `apps/scheduling/assignment.py:438`
- **Function/Class:** `list_assignment_history`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1060

- **ID:** MC-1060
- **File:** `apps/scheduling/batch_events.py:217`
- **Function/Class:** `_resolve_org_mapping`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1061

- **ID:** MC-1061
- **File:** `apps/scheduling/batch_events.py:236`
- **Function/Class:** `_resolve_scoped_mapping`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1062

- **ID:** MC-1062
- **File:** `apps/scheduling/batch_events.py:337`
- **Function/Class:** `process_external_batch_event`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1063

- **ID:** MC-1063
- **File:** `apps/scheduling/due.py:229`
- **Function/Class:** `set_checklist_task_due_window`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1064

- **ID:** MC-1064
- **File:** `apps/scheduling/generation.py:366`
- **Function/Class:** `upsert_occurrence_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1065

- **ID:** MC-1065
- **File:** `apps/scheduling/generation.py:433`
- **Function/Class:** `generate_for_schedule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1066

- **ID:** MC-1066
- **File:** `apps/scheduling/generation.py:507`
- **Function/Class:** `run_active_schedule_generation`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1067

- **ID:** MC-1067
- **File:** `apps/scheduling/generation.py:636`
- **Function/Class:** `deactivate_checklist_schedule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1068

- **ID:** MC-1068
- **File:** `apps/scheduling/generation.py:675`
- **Function/Class:** `create_manual_schedule_occurrence`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1069

- **ID:** MC-1069
- **File:** `apps/scheduling/selectors.py:130`
- **Function/Class:** `templates_for_task_manage`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1070

- **ID:** MC-1070
- **File:** `apps/scheduling/selectors.py:149`
- **Function/Class:** `published_versions_for_template`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1071

- **ID:** MC-1071
- **File:** `apps/scheduling/selectors.py:175`
- **Function/Class:** `list_checklist_tasks`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1072

- **ID:** MC-1072
- **File:** `apps/scheduling/selectors.py:230`
- **Function/Class:** `_apply_due_state_filter`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1073

- **ID:** MC-1073
- **File:** `apps/scheduling/selectors.py:318`
- **Function/Class:** `get_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1074

- **ID:** MC-1074
- **File:** `apps/scheduling/selectors.py:346`
- **Function/Class:** `get_checklist_applicability_rule`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1075

- **ID:** MC-1075
- **File:** `apps/scheduling/selectors.py:378`
- **Function/Class:** `list_checklist_applicability_rules`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1076

- **ID:** MC-1076
- **File:** `apps/scheduling/services.py:104`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1077

- **ID:** MC-1077
- **File:** `apps/scheduling/services.py:127`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1078

- **ID:** MC-1078
- **File:** `apps/scheduling/services.py:153`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1079

- **ID:** MC-1079
- **File:** `apps/scheduling/services.py:165`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1080

- **ID:** MC-1080
- **File:** `apps/scheduling/services.py:208`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1081

- **ID:** MC-1081
- **File:** `apps/scheduling/services.py:220`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1082

- **ID:** MC-1082
- **File:** `apps/scheduling/services.py:244`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1083

- **ID:** MC-1083
- **File:** `apps/scheduling/services.py:292`
- **Function/Class:** `cancel_checklist_task`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1084

- **ID:** MC-1084
- **File:** `apps/scheduling/views.py:166`
- **Function/Class:** `task_list`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1085

- **ID:** MC-1085
- **File:** `apps/supplier_quality/services.py:208`
- **Function/Class:** `verify_supplier_certificate`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1086

- **ID:** MC-1086
- **File:** `apps/training/selectors.py:43`
- **Function/Class:** `get_training_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1087

- **ID:** MC-1087
- **File:** `apps/training/selectors.py:78`
- **Function/Class:** `list_training_records`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1088

- **ID:** MC-1088
- **File:** `apps/training/services.py:267`
- **Function/Class:** `update_training_record`
- **Token:** `select_related` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1089

- **ID:** MC-1089
- **File:** `apps/quality/selectors.py:71`
- **Function/Class:** `list_qa_reviewable_submissions`
- **Token:** `Subquery` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1090

- **ID:** MC-1090
- **File:** `apps/reviews/selectors.py:62`
- **Function/Class:** `_base_pending_queryset`
- **Token:** `Subquery` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** HIGH
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** HIGH
- **Required redesign:** Unsupported / unproven query or schema feature
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1091

- **ID:** MC-1091
- **File:** `apps/access_control/governance_services.py:80`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1092

- **ID:** MC-1092
- **File:** `apps/access_control/governance_services.py:121`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1093

- **ID:** MC-1093
- **File:** `apps/access_control/governance_services.py:167`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1094

- **ID:** MC-1094
- **File:** `apps/access_control/governance_services.py:210`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1095

- **ID:** MC-1095
- **File:** `apps/access_control/services.py:308`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1096

- **ID:** MC-1096
- **File:** `apps/access_control/services.py:326`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1097

- **ID:** MC-1097
- **File:** `apps/access_control/services.py:404`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1098

- **ID:** MC-1098
- **File:** `apps/accounts/services.py:212`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1099

- **ID:** MC-1099
- **File:** `apps/accounts/services.py:248`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1100

- **ID:** MC-1100
- **File:** `apps/accounts/services.py:289`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1101

- **ID:** MC-1101
- **File:** `apps/accounts/services.py:323`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1102

- **ID:** MC-1102
- **File:** `apps/accounts/services.py:354`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1103

- **ID:** MC-1103
- **File:** `apps/accounts/services.py:384`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1104

- **ID:** MC-1104
- **File:** `apps/accounts/services.py:391`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1105

- **ID:** MC-1105
- **File:** `apps/ai_assistance/services.py:114`
- **Function/Class:** `run_ai_assistance`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1106

- **ID:** MC-1106
- **File:** `apps/batch_dossier/services.py:136`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1107

- **ID:** MC-1107
- **File:** `apps/batch_dossier/services.py:999`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1108

- **ID:** MC-1108
- **File:** `apps/batch_genealogy/services.py:138`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1109

- **ID:** MC-1109
- **File:** `apps/batch_genealogy/services.py:178`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1110

- **ID:** MC-1110
- **File:** `apps/batch_genealogy/services.py:337`
- **Function/Class:** `ingest_erp_genealogy_edge`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1111

- **ID:** MC-1111
- **File:** `apps/capa/services.py:82`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1112

- **ID:** MC-1112
- **File:** `apps/capa/services.py:144`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1113

- **ID:** MC-1113
- **File:** `apps/capa/services.py:190`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1114

- **ID:** MC-1114
- **File:** `apps/capa/services.py:251`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1115

- **ID:** MC-1115
- **File:** `apps/capa/services.py:312`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1116

- **ID:** MC-1116
- **File:** `apps/capa/services.py:362`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1117

- **ID:** MC-1117
- **File:** `apps/capa/services.py:399`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1118

- **ID:** MC-1118
- **File:** `apps/change_control/services.py:74`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1119

- **ID:** MC-1119
- **File:** `apps/change_control/services.py:128`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1120

- **ID:** MC-1120
- **File:** `apps/change_control/services.py:154`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1121

- **ID:** MC-1121
- **File:** `apps/change_control/services.py:219`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1122

- **ID:** MC-1122
- **File:** `apps/change_control/services.py:284`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1123

- **ID:** MC-1123
- **File:** `apps/change_control/services.py:337`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1124

- **ID:** MC-1124
- **File:** `apps/change_control/services.py:363`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1125

- **ID:** MC-1125
- **File:** `apps/change_control/services.py:429`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1126

- **ID:** MC-1126
- **File:** `apps/change_control/services.py:459`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1127

- **ID:** MC-1127
- **File:** `apps/changeover/services.py:81`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1128

- **ID:** MC-1128
- **File:** `apps/changeover/services.py:117`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1129

- **ID:** MC-1129
- **File:** `apps/changeover/services.py:164`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1130

- **ID:** MC-1130
- **File:** `apps/changeover/services.py:187`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1131

- **ID:** MC-1131
- **File:** `apps/changeover/services.py:308`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1132

- **ID:** MC-1132
- **File:** `apps/changeover/services.py:347`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1133

- **ID:** MC-1133
- **File:** `apps/changeover/services.py:429`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1134

- **ID:** MC-1134
- **File:** `apps/checklists/effective_version.py:306`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1135

- **ID:** MC-1135
- **File:** `apps/checklists/proposal_loader.py:499`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1136

- **ID:** MC-1136
- **File:** `apps/checklists/services.py:381`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1137

- **ID:** MC-1137
- **File:** `apps/checklists/services.py:446`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1138

- **ID:** MC-1138
- **File:** `apps/checklists/services.py:465`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1139

- **ID:** MC-1139
- **File:** `apps/checklists/services.py:547`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1140

- **ID:** MC-1140
- **File:** `apps/checklists/services.py:574`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1141

- **ID:** MC-1141
- **File:** `apps/checklists/services.py:672`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1142

- **ID:** MC-1142
- **File:** `apps/checklists/services.py:713`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1143

- **ID:** MC-1143
- **File:** `apps/checklists/services.py:778`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1144

- **ID:** MC-1144
- **File:** `apps/checklists/services.py:797`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1145

- **ID:** MC-1145
- **File:** `apps/checklists/services.py:1074`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1146

- **ID:** MC-1146
- **File:** `apps/checklists/services.py:1120`
- **Function/Class:** `create_checklist_version`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1147

- **ID:** MC-1147
- **File:** `apps/checklists/services.py:1159`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1148

- **ID:** MC-1148
- **File:** `apps/checklists/services.py:1188`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1149

- **ID:** MC-1149
- **File:** `apps/checklists/services.py:1222`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1150

- **ID:** MC-1150
- **File:** `apps/checklists/services.py:1247`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1151

- **ID:** MC-1151
- **File:** `apps/checklists/services.py:1275`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1152

- **ID:** MC-1152
- **File:** `apps/checklists/services.py:1414`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1153

- **ID:** MC-1153
- **File:** `apps/checklists/services.py:1648`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1154

- **ID:** MC-1154
- **File:** `apps/checklists/services.py:1664`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1155

- **ID:** MC-1155
- **File:** `apps/checklists/services.py:1690`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1156

- **ID:** MC-1156
- **File:** `apps/checklists/services.py:1731`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1157

- **ID:** MC-1157
- **File:** `apps/checklists/services.py:1782`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1158

- **ID:** MC-1158
- **File:** `apps/checklists/services.py:1812`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1159

- **ID:** MC-1159
- **File:** `apps/checklists/services.py:2063`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1160

- **ID:** MC-1160
- **File:** `apps/checklists/services.py:2087`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1161

- **ID:** MC-1161
- **File:** `apps/compliance_mapping/services.py:183`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1162

- **ID:** MC-1162
- **File:** `apps/compliance_mapping/services.py:256`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1163

- **ID:** MC-1163
- **File:** `apps/compliance_mapping/services.py:326`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1164

- **ID:** MC-1164
- **File:** `apps/compliance_mapping/services.py:369`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1165

- **ID:** MC-1165
- **File:** `apps/compliance_mapping/services.py:396`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1166

- **ID:** MC-1166
- **File:** `apps/compliance_mapping/services.py:453`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1167

- **ID:** MC-1167
- **File:** `apps/compliance_mapping/services.py:491`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1168

- **ID:** MC-1168
- **File:** `apps/compliance_mapping/services.py:524`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1169

- **ID:** MC-1169
- **File:** `apps/compliance_mapping/services.py:577`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1170

- **ID:** MC-1170
- **File:** `apps/compliance_mapping/services.py:620`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1171

- **ID:** MC-1171
- **File:** `apps/compliance_mapping/services.py:801`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1172

- **ID:** MC-1172
- **File:** `apps/compliance_mapping/services.py:837`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1173

- **ID:** MC-1173
- **File:** `apps/core/optimistic_transition.py:131`
- **Function/Class:** `create_immutable_unique`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1174

- **ID:** MC-1174
- **File:** `apps/customer_complaints/services.py:90`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1175

- **ID:** MC-1175
- **File:** `apps/customer_complaints/services.py:124`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1176

- **ID:** MC-1176
- **File:** `apps/customer_complaints/services.py:175`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1177

- **ID:** MC-1177
- **File:** `apps/customer_complaints/services.py:242`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1178

- **ID:** MC-1178
- **File:** `apps/customer_complaints/services.py:270`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1179

- **ID:** MC-1179
- **File:** `apps/customer_complaints/services.py:310`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1180

- **ID:** MC-1180
- **File:** `apps/customer_complaints/services.py:420`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1181

- **ID:** MC-1181
- **File:** `apps/customer_complaints/services.py:467`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1182

- **ID:** MC-1182
- **File:** `apps/customer_complaints/services.py:585`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1183

- **ID:** MC-1183
- **File:** `apps/customer_complaints/services.py:686`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1184

- **ID:** MC-1184
- **File:** `apps/dispatch/services.py:147`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1185

- **ID:** MC-1185
- **File:** `apps/dispatch/services.py:228`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1186

- **ID:** MC-1186
- **File:** `apps/dispatch/services.py:320`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1187

- **ID:** MC-1187
- **File:** `apps/dispatch/services.py:369`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1188

- **ID:** MC-1188
- **File:** `apps/dispatch/services.py:410`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1189

- **ID:** MC-1189
- **File:** `apps/dispatch/services.py:470`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1190

- **ID:** MC-1190
- **File:** `apps/dispatch/services.py:569`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1191

- **ID:** MC-1191
- **File:** `apps/dispatch/services.py:612`
- **Function/Class:** `complete_dispatch_quality_record`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1192

- **ID:** MC-1192
- **File:** `apps/dispatch/services.py:700`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1193

- **ID:** MC-1193
- **File:** `apps/dispatch/services.py:701`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1194

- **ID:** MC-1194
- **File:** `apps/document_control/services.py:82`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1195

- **ID:** MC-1195
- **File:** `apps/document_control/services.py:149`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1196

- **ID:** MC-1196
- **File:** `apps/document_control/services.py:195`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1197

- **ID:** MC-1197
- **File:** `apps/document_control/services.py:244`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1198

- **ID:** MC-1198
- **File:** `apps/document_control/services.py:270`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1199

- **ID:** MC-1199
- **File:** `apps/document_control/services.py:296`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1200

- **ID:** MC-1200
- **File:** `apps/document_control/services.py:345`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1201

- **ID:** MC-1201
- **File:** `apps/document_control/services.py:428`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1202

- **ID:** MC-1202
- **File:** `apps/document_control/services.py:485`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1203

- **ID:** MC-1203
- **File:** `apps/document_control/services.py:528`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1204

- **ID:** MC-1204
- **File:** `apps/environmental/services.py:96`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1205

- **ID:** MC-1205
- **File:** `apps/environmental/services.py:147`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1206

- **ID:** MC-1206
- **File:** `apps/environmental/services.py:183`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1207

- **ID:** MC-1207
- **File:** `apps/environmental/services.py:221`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1208

- **ID:** MC-1208
- **File:** `apps/environmental/services.py:254`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1209

- **ID:** MC-1209
- **File:** `apps/environmental/services.py:298`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1210

- **ID:** MC-1210
- **File:** `apps/environmental/services.py:328`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1211

- **ID:** MC-1211
- **File:** `apps/environmental/services.py:356`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1212

- **ID:** MC-1212
- **File:** `apps/environmental/services.py:432`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1213

- **ID:** MC-1213
- **File:** `apps/environmental/services.py:574`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1214

- **ID:** MC-1214
- **File:** `apps/evidence/services.py:71`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1215

- **ID:** MC-1215
- **File:** `apps/evidence/services.py:249`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1216

- **ID:** MC-1216
- **File:** `apps/evidence/services.py:304`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1217

- **ID:** MC-1217
- **File:** `apps/foreign_body/services.py:100`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1218

- **ID:** MC-1218
- **File:** `apps/foreign_body/services.py:142`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1219

- **ID:** MC-1219
- **File:** `apps/foreign_body/services.py:194`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1220

- **ID:** MC-1220
- **File:** `apps/foreign_body/services.py:296`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1221

- **ID:** MC-1221
- **File:** `apps/foreign_body/services.py:339`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1222

- **ID:** MC-1222
- **File:** `apps/foreign_body/services.py:378`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1223

- **ID:** MC-1223
- **File:** `apps/haccp/services.py:127`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1224

- **ID:** MC-1224
- **File:** `apps/haccp/services.py:165`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1225

- **ID:** MC-1225
- **File:** `apps/haccp/services.py:218`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1226

- **ID:** MC-1226
- **File:** `apps/haccp/services.py:260`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1227

- **ID:** MC-1227
- **File:** `apps/haccp/services.py:299`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1228

- **ID:** MC-1228
- **File:** `apps/haccp/services.py:337`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1229

- **ID:** MC-1229
- **File:** `apps/haccp/services.py:403`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1230

- **ID:** MC-1230
- **File:** `apps/haccp/services.py:450`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1231

- **ID:** MC-1231
- **File:** `apps/haccp/services.py:486`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1232

- **ID:** MC-1232
- **File:** `apps/haccp/services.py:525`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1233

- **ID:** MC-1233
- **File:** `apps/haccp/services.py:591`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1234

- **ID:** MC-1234
- **File:** `apps/haccp/services.py:626`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1235

- **ID:** MC-1235
- **File:** `apps/instruments/services.py:99`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1236

- **ID:** MC-1236
- **File:** `apps/instruments/services.py:162`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1237

- **ID:** MC-1237
- **File:** `apps/instruments/services.py:239`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1238

- **ID:** MC-1238
- **File:** `apps/instruments/services.py:270`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1239

- **ID:** MC-1239
- **File:** `apps/instruments/services.py:289`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1240

- **ID:** MC-1240
- **File:** `apps/instruments/services.py:308`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1241

- **ID:** MC-1241
- **File:** `apps/instruments/services.py:353`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1242

- **ID:** MC-1242
- **File:** `tests/test_phase05d_equipment_calibration.py:372`
- **Function/Class:** `test_authorization_and_validation_coverage_edges`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1243

- **ID:** MC-1243
- **File:** `apps/integrations/services.py:89`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1244

- **ID:** MC-1244
- **File:** `apps/integrations/services.py:291`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1245

- **ID:** MC-1245
- **File:** `apps/ipqc/services.py:152`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1246

- **ID:** MC-1246
- **File:** `apps/ipqc/services.py:183`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1247

- **ID:** MC-1247
- **File:** `apps/ipqc/services.py:281`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1248

- **ID:** MC-1248
- **File:** `apps/ipqc/services.py:409`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1249

- **ID:** MC-1249
- **File:** `apps/ipqc/services.py:451`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1250

- **ID:** MC-1250
- **File:** `apps/ipqc/services.py:500`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1251

- **ID:** MC-1251
- **File:** `apps/ipqc/services.py:557`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1252

- **ID:** MC-1252
- **File:** `apps/ipqc/services.py:620`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1253

- **ID:** MC-1253
- **File:** `apps/ipqc/services.py:661`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1254

- **ID:** MC-1254
- **File:** `apps/ipqc/services.py:691`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1255

- **ID:** MC-1255
- **File:** `apps/ipqc/services.py:754`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1256

- **ID:** MC-1256
- **File:** `apps/ipqc/services.py:799`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1257

- **ID:** MC-1257
- **File:** `apps/ipqc/services.py:841`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1258

- **ID:** MC-1258
- **File:** `apps/ipqc/services.py:861`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1259

- **ID:** MC-1259
- **File:** `apps/iqc/services.py:102`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1260

- **ID:** MC-1260
- **File:** `apps/iqc/services.py:136`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1261

- **ID:** MC-1261
- **File:** `apps/iqc/services.py:177`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1262

- **ID:** MC-1262
- **File:** `apps/iqc/services.py:243`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1263

- **ID:** MC-1263
- **File:** `apps/iqc/services.py:284`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1264

- **ID:** MC-1264
- **File:** `apps/iqc/services.py:324`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1265

- **ID:** MC-1265
- **File:** `apps/iqc/services.py:383`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1266

- **ID:** MC-1266
- **File:** `apps/iqc/services.py:465`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1267

- **ID:** MC-1267
- **File:** `apps/laboratory/services.py:93`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1268

- **ID:** MC-1268
- **File:** `apps/laboratory/services.py:163`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1269

- **ID:** MC-1269
- **File:** `apps/laboratory/services.py:206`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1270

- **ID:** MC-1270
- **File:** `apps/laboratory/services.py:258`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1271

- **ID:** MC-1271
- **File:** `apps/laboratory/services.py:358`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1272

- **ID:** MC-1272
- **File:** `apps/laboratory/services.py:391`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1273

- **ID:** MC-1273
- **File:** `apps/laboratory/services.py:425`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1274

- **ID:** MC-1274
- **File:** `apps/laboratory/services.py:502`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1275

- **ID:** MC-1275
- **File:** `apps/laboratory/services.py:527`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1276

- **ID:** MC-1276
- **File:** `apps/laboratory/services.py:573`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1277

- **ID:** MC-1277
- **File:** `apps/laboratory/services.py:622`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1278

- **ID:** MC-1278
- **File:** `apps/master_data/product_import.py:323`
- **Function/Class:** `import_fg_products`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1279

- **ID:** MC-1279
- **File:** `apps/master_data/services.py:144`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1280

- **ID:** MC-1280
- **File:** `apps/master_data/services.py:202`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1281

- **ID:** MC-1281
- **File:** `apps/master_data/services.py:282`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1282

- **ID:** MC-1282
- **File:** `apps/master_data/services.py:301`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1283

- **ID:** MC-1283
- **File:** `apps/master_data/specification_services.py:166`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1284

- **ID:** MC-1284
- **File:** `apps/master_data/specification_services.py:231`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1285

- **ID:** MC-1285
- **File:** `apps/master_data/specification_services.py:278`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1286

- **ID:** MC-1286
- **File:** `apps/master_data/specification_services.py:329`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1287

- **ID:** MC-1287
- **File:** `apps/master_data/specification_services.py:433`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1288

- **ID:** MC-1288
- **File:** `apps/master_data/specification_services.py:462`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1289

- **ID:** MC-1289
- **File:** `apps/master_data/specification_services.py:509`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1290

- **ID:** MC-1290
- **File:** `apps/master_data/specification_services.py:539`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1291

- **ID:** MC-1291
- **File:** `apps/nonconformance/services.py:93`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1292

- **ID:** MC-1292
- **File:** `apps/nonconformance/services.py:173`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1293

- **ID:** MC-1293
- **File:** `apps/nonconformance/services.py:248`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1294

- **ID:** MC-1294
- **File:** `apps/nonconformance/services.py:299`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1295

- **ID:** MC-1295
- **File:** `apps/nonconformance/services.py:350`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1296

- **ID:** MC-1296
- **File:** `apps/nonconformance/services.py:426`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1297

- **ID:** MC-1297
- **File:** `apps/notifications/services.py:74`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1298

- **ID:** MC-1298
- **File:** `apps/notifications/services.py:120`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1299

- **ID:** MC-1299
- **File:** `apps/notifications/services.py:239`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1300

- **ID:** MC-1300
- **File:** `apps/notifications/tasks.py:34`
- **Function/Class:** `deliver_notification_email`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1301

- **ID:** MC-1301
- **File:** `apps/organizations/hierarchy_import.py:530`
- **Function/Class:** `import_organization_hierarchy`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1302

- **ID:** MC-1302
- **File:** `apps/organizations/services.py:169`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1303

- **ID:** MC-1303
- **File:** `apps/organizations/services.py:212`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1304

- **ID:** MC-1304
- **File:** `apps/organizations/services.py:254`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1305

- **ID:** MC-1305
- **File:** `apps/organizations/services.py:277`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1306

- **ID:** MC-1306
- **File:** `apps/organizations/services.py:303`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1307

- **ID:** MC-1307
- **File:** `apps/organizations/services.py:337`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1308

- **ID:** MC-1308
- **File:** `apps/organizations/services.py:384`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1309

- **ID:** MC-1309
- **File:** `apps/organizations/services.py:399`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1310

- **ID:** MC-1310
- **File:** `apps/organizations/services.py:419`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1311

- **ID:** MC-1311
- **File:** `apps/organizations/services.py:466`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1312

- **ID:** MC-1312
- **File:** `apps/organizations/services.py:529`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1313

- **ID:** MC-1313
- **File:** `apps/organizations/services.py:559`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1314

- **ID:** MC-1314
- **File:** `apps/organizations/services.py:613`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1315

- **ID:** MC-1315
- **File:** `apps/organizations/services.py:669`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1316

- **ID:** MC-1316
- **File:** `apps/organizations/services.py:749`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1317

- **ID:** MC-1317
- **File:** `apps/organizations/services.py:768`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1318

- **ID:** MC-1318
- **File:** `apps/packaging/services.py:77`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1319

- **ID:** MC-1319
- **File:** `apps/packaging/services.py:133`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1320

- **ID:** MC-1320
- **File:** `apps/packaging/services.py:184`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1321

- **ID:** MC-1321
- **File:** `apps/packaging/services.py:234`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1322

- **ID:** MC-1322
- **File:** `apps/packaging/services.py:280`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1323

- **ID:** MC-1323
- **File:** `apps/packaging/services.py:308`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1324

- **ID:** MC-1324
- **File:** `apps/packaging/services.py:358`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1325

- **ID:** MC-1325
- **File:** `apps/packaging/services.py:412`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1326

- **ID:** MC-1326
- **File:** `apps/process_fmea/services.py:180`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1327

- **ID:** MC-1327
- **File:** `apps/process_fmea/services.py:235`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1328

- **ID:** MC-1328
- **File:** `apps/process_fmea/services.py:275`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1329

- **ID:** MC-1329
- **File:** `apps/process_fmea/services.py:309`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1330

- **ID:** MC-1330
- **File:** `apps/process_fmea/services.py:322`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1331

- **ID:** MC-1331
- **File:** `apps/process_fmea/services.py:335`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1332

- **ID:** MC-1332
- **File:** `apps/process_fmea/services.py:357`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1333

- **ID:** MC-1333
- **File:** `apps/process_fmea/services.py:456`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1334

- **ID:** MC-1334
- **File:** `apps/process_fmea/services.py:571`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1335

- **ID:** MC-1335
- **File:** `apps/process_fmea/services.py:620`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1336

- **ID:** MC-1336
- **File:** `apps/process_fmea/services.py:674`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1337

- **ID:** MC-1337
- **File:** `apps/process_fmea/services.py:687`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1338

- **ID:** MC-1338
- **File:** `apps/process_fmea/services.py:719`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1339

- **ID:** MC-1339
- **File:** `apps/process_fmea/services.py:791`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1340

- **ID:** MC-1340
- **File:** `apps/product_returns/services.py:81`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1341

- **ID:** MC-1341
- **File:** `apps/product_returns/services.py:143`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1342

- **ID:** MC-1342
- **File:** `apps/product_returns/services.py:187`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1343

- **ID:** MC-1343
- **File:** `apps/product_returns/services.py:248`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1344

- **ID:** MC-1344
- **File:** `apps/product_returns/services.py:273`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1345

- **ID:** MC-1345
- **File:** `apps/product_returns/services.py:325`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1346

- **ID:** MC-1346
- **File:** `apps/quality/services.py:95`
- **Function/Class:** `create_qa_review`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1347

- **ID:** MC-1347
- **File:** `tests/test_phase10a_qa_review.py:530`
- **Function/Class:** `_decide`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1348

- **ID:** MC-1348
- **File:** `apps/quality_audits/services.py:91`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1349

- **ID:** MC-1349
- **File:** `apps/quality_audits/services.py:152`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1350

- **ID:** MC-1350
- **File:** `apps/quality_audits/services.py:180`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1351

- **ID:** MC-1351
- **File:** `apps/quality_audits/services.py:210`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1352

- **ID:** MC-1352
- **File:** `apps/quality_audits/services.py:255`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1353

- **ID:** MC-1353
- **File:** `apps/quality_audits/services.py:278`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1354

- **ID:** MC-1354
- **File:** `apps/quality_audits/services.py:359`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1355

- **ID:** MC-1355
- **File:** `apps/quality_audits/services.py:390`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1356

- **ID:** MC-1356
- **File:** `apps/quality_audits/services.py:419`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1357

- **ID:** MC-1357
- **File:** `apps/quality_audits/services.py:448`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1358

- **ID:** MC-1358
- **File:** `apps/quality_audits/services.py:549`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1359

- **ID:** MC-1359
- **File:** `apps/quality_audits/services.py:575`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1360

- **ID:** MC-1360
- **File:** `apps/quality_audits/services.py:594`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1361

- **ID:** MC-1361
- **File:** `apps/quality_audits/services.py:620`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1362

- **ID:** MC-1362
- **File:** `apps/quality_quarantine/services.py:83`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1363

- **ID:** MC-1363
- **File:** `apps/quality_quarantine/services.py:165`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1364

- **ID:** MC-1364
- **File:** `apps/quality_quarantine/services.py:222`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1365

- **ID:** MC-1365
- **File:** `apps/quality_quarantine/services.py:282`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1366

- **ID:** MC-1366
- **File:** `apps/quality_quarantine/services.py:318`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1367

- **ID:** MC-1367
- **File:** `apps/quality_quarantine/services.py:373`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1368

- **ID:** MC-1368
- **File:** `apps/quality_risks/services.py:160`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1369

- **ID:** MC-1369
- **File:** `apps/quality_risks/services.py:227`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1370

- **ID:** MC-1370
- **File:** `apps/quality_risks/services.py:250`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1371

- **ID:** MC-1371
- **File:** `apps/quality_risks/services.py:289`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1372

- **ID:** MC-1372
- **File:** `apps/quality_risks/services.py:314`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1373

- **ID:** MC-1373
- **File:** `apps/quality_risks/services.py:339`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1374

- **ID:** MC-1374
- **File:** `apps/quality_risks/services.py:415`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1375

- **ID:** MC-1375
- **File:** `apps/quality_risks/services.py:458`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1376

- **ID:** MC-1376
- **File:** `apps/quality_risks/services.py:506`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1377

- **ID:** MC-1377
- **File:** `apps/quality_risks/services.py:648`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1378

- **ID:** MC-1378
- **File:** `apps/quality_risks/services.py:676`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1379

- **ID:** MC-1379
- **File:** `apps/rca/services.py:171`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1380

- **ID:** MC-1380
- **File:** `apps/rca/services.py:238`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1381

- **ID:** MC-1381
- **File:** `apps/rca/services.py:261`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1382

- **ID:** MC-1382
- **File:** `apps/rca/services.py:292`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1383

- **ID:** MC-1383
- **File:** `apps/rca/services.py:328`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1384

- **ID:** MC-1384
- **File:** `apps/rca/services.py:366`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1385

- **ID:** MC-1385
- **File:** `apps/rca/services.py:412`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1386

- **ID:** MC-1386
- **File:** `apps/rca/services.py:463`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1387

- **ID:** MC-1387
- **File:** `apps/rca/services.py:505`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1388

- **ID:** MC-1388
- **File:** `apps/rca/services.py:565`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1389

- **ID:** MC-1389
- **File:** `apps/rca/services.py:604`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1390

- **ID:** MC-1390
- **File:** `apps/rca/services.py:669`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1391

- **ID:** MC-1391
- **File:** `apps/rca/services.py:694`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1392

- **ID:** MC-1392
- **File:** `apps/recall/mock_services.py:94`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1393

- **ID:** MC-1393
- **File:** `apps/recall/mock_services.py:167`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1394

- **ID:** MC-1394
- **File:** `apps/recall/mock_services.py:209`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1395

- **ID:** MC-1395
- **File:** `apps/recall/mock_services.py:292`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1396

- **ID:** MC-1396
- **File:** `apps/recall/mock_services.py:361`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1397

- **ID:** MC-1397
- **File:** `apps/recall/mock_services.py:473`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1398

- **ID:** MC-1398
- **File:** `apps/recall/mock_services.py:514`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1399

- **ID:** MC-1399
- **File:** `apps/recall/mock_services.py:573`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1400

- **ID:** MC-1400
- **File:** `apps/recall/mock_services.py:633`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1401

- **ID:** MC-1401
- **File:** `apps/recall/services.py:142`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1402

- **ID:** MC-1402
- **File:** `apps/recall/services.py:176`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1403

- **ID:** MC-1403
- **File:** `apps/recall/services.py:261`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1404

- **ID:** MC-1404
- **File:** `apps/recall/services.py:300`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1405

- **ID:** MC-1405
- **File:** `apps/recall/services.py:344`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1406

- **ID:** MC-1406
- **File:** `apps/recall/services.py:404`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1407

- **ID:** MC-1407
- **File:** `apps/recall/services.py:530`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1408

- **ID:** MC-1408
- **File:** `apps/recall/services.py:613`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1409

- **ID:** MC-1409
- **File:** `apps/recall/services.py:839`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1410

- **ID:** MC-1410
- **File:** `apps/receiving/services.py:90`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1411

- **ID:** MC-1411
- **File:** `apps/receiving/services.py:129`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1412

- **ID:** MC-1412
- **File:** `apps/receiving/services.py:167`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1413

- **ID:** MC-1413
- **File:** `apps/receiving/services.py:204`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1414

- **ID:** MC-1414
- **File:** `apps/receiving/services.py:231`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1415

- **ID:** MC-1415
- **File:** `apps/receiving/services.py:347`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1416

- **ID:** MC-1416
- **File:** `apps/receiving/services.py:404`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1417

- **ID:** MC-1417
- **File:** `apps/receiving/services.py:436`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1418

- **ID:** MC-1418
- **File:** `apps/recording/correction_services.py:239`
- **Function/Class:** `start_checklist_correction`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1419

- **ID:** MC-1419
- **File:** `apps/recording/correction_services.py:440`
- **Function/Class:** `resubmit_checklist_correction`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1420

- **ID:** MC-1420
- **File:** `apps/recording/services.py:162`
- **Function/Class:** `start_checklist_recording`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1421

- **ID:** MC-1421
- **File:** `apps/recording/services.py:692`
- **Function/Class:** `save_checklist_draft_responses`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1422

- **ID:** MC-1422
- **File:** `apps/recording/services.py:937`
- **Function/Class:** `submit_checklist_record`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1423

- **ID:** MC-1423
- **File:** `apps/recording/synthetic_demo.py:106`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1424

- **ID:** MC-1424
- **File:** `tests/test_phase08a_draft_recording.py:470`
- **Function/Class:** `_start`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1425

- **ID:** MC-1425
- **File:** `tests/test_phase08b_submission.py:411`
- **Function/Class:** `_submit`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1426

- **ID:** MC-1426
- **File:** `tests/test_phase09b_correction.py:590`
- **Function/Class:** `_start`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1427

- **ID:** MC-1427
- **File:** `tests/test_phase09b_correction.py:619`
- **Function/Class:** `_resubmit`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1428

- **ID:** MC-1428
- **File:** `apps/reports/services.py:153`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1429

- **ID:** MC-1429
- **File:** `apps/reports/services.py:267`
- **Function/Class:** `execute_report_run_by_id`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1430

- **ID:** MC-1430
- **File:** `apps/reviews/governance.py:176`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1431

- **ID:** MC-1431
- **File:** `apps/reviews/governance.py:265`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1432

- **ID:** MC-1432
- **File:** `apps/reviews/governance.py:333`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1433

- **ID:** MC-1433
- **File:** `apps/reviews/mongo_spike.py:48`
- **Function/Class:** `create_supervisor_review_cas`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1434

- **ID:** MC-1434
- **File:** `apps/reviews/services.py:87`
- **Function/Class:** `create_supervisor_review`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1435

- **ID:** MC-1435
- **File:** `tests/test_mongo_supervisor_concurrency_spike.py:151`
- **Function/Class:** `test_network_retry_same_decision_after_commit`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1436

- **ID:** MC-1436
- **File:** `tests/test_phase09a_supervisor_review.py:495`
- **Function/Class:** `_run`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1437

- **ID:** MC-1437
- **File:** `tests/test_phase09c_supervisor_governance.py:475`
- **Function/Class:** `_run`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1438

- **ID:** MC-1438
- **File:** `apps/rework/services.py:135`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1439

- **ID:** MC-1439
- **File:** `apps/rework/services.py:205`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1440

- **ID:** MC-1440
- **File:** `apps/rework/services.py:231`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1441

- **ID:** MC-1441
- **File:** `apps/rework/services.py:308`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1442

- **ID:** MC-1442
- **File:** `apps/rework/services.py:385`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1443

- **ID:** MC-1443
- **File:** `apps/rework/services.py:416`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1444

- **ID:** MC-1444
- **File:** `apps/rework/services.py:472`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1445

- **ID:** MC-1445
- **File:** `apps/sampling/services.py:74`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1446

- **ID:** MC-1446
- **File:** `apps/sampling/services.py:114`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1447

- **ID:** MC-1447
- **File:** `apps/sampling/services.py:167`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1448

- **ID:** MC-1448
- **File:** `apps/sampling/services.py:229`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1449

- **ID:** MC-1449
- **File:** `apps/sampling/services.py:278`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1450

- **ID:** MC-1450
- **File:** `apps/sampling/services.py:340`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1451

- **ID:** MC-1451
- **File:** `apps/sampling/services.py:374`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1452

- **ID:** MC-1452
- **File:** `apps/sanitation/services.py:86`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1453

- **ID:** MC-1453
- **File:** `apps/sanitation/services.py:132`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1454

- **ID:** MC-1454
- **File:** `apps/sanitation/services.py:180`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1455

- **ID:** MC-1455
- **File:** `apps/sanitation/services.py:227`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1456

- **ID:** MC-1456
- **File:** `apps/sanitation/services.py:262`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1457

- **ID:** MC-1457
- **File:** `apps/sanitation/services.py:293`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1458

- **ID:** MC-1458
- **File:** `apps/sanitation/services.py:328`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1459

- **ID:** MC-1459
- **File:** `apps/sanitation/services.py:369`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1460

- **ID:** MC-1460
- **File:** `apps/sanitation/services.py:404`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1461

- **ID:** MC-1461
- **File:** `apps/sanitation/services.py:450`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1462

- **ID:** MC-1462
- **File:** `apps/scheduling/applicability.py:451`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1463

- **ID:** MC-1463
- **File:** `apps/scheduling/applicability.py:513`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1464

- **ID:** MC-1464
- **File:** `apps/scheduling/applicability.py:595`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1465

- **ID:** MC-1465
- **File:** `apps/scheduling/assignment.py:256`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1466

- **ID:** MC-1466
- **File:** `apps/scheduling/assignment.py:342`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1467

- **ID:** MC-1467
- **File:** `apps/scheduling/batch_events.py:270`
- **Function/Class:** `_get_or_create_receipt`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1468

- **ID:** MC-1468
- **File:** `apps/scheduling/batch_events.py:335`
- **Function/Class:** `process_external_batch_event`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1469

- **ID:** MC-1469
- **File:** `apps/scheduling/due.py:214`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1470

- **ID:** MC-1470
- **File:** `apps/scheduling/generation.py:343`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1471

- **ID:** MC-1471
- **File:** `apps/scheduling/generation.py:554`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1472

- **ID:** MC-1472
- **File:** `apps/scheduling/generation.py:630`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1473

- **ID:** MC-1473
- **File:** `apps/scheduling/generation.py:664`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1474

- **ID:** MC-1474
- **File:** `apps/scheduling/services.py:189`
- **Function/Class:** `create_batch_checklist_task`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1475

- **ID:** MC-1475
- **File:** `apps/scheduling/services.py:290`
- **Function/Class:** `cancel_checklist_task`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1476

- **ID:** MC-1476
- **File:** `tests/test_batch_checklist_task.py:383`
- **Function/Class:** `_create`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1477

- **ID:** MC-1477
- **File:** `apps/security_audit/services.py:60`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1478

- **ID:** MC-1478
- **File:** `apps/supplier_quality/services.py:66`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1479

- **ID:** MC-1479
- **File:** `apps/supplier_quality/services.py:116`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1480

- **ID:** MC-1480
- **File:** `apps/supplier_quality/services.py:158`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1481

- **ID:** MC-1481
- **File:** `apps/supplier_quality/services.py:199`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1482

- **ID:** MC-1482
- **File:** `apps/supplier_quality/services.py:233`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1483

- **ID:** MC-1483
- **File:** `apps/training/services.py:176`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1484

- **ID:** MC-1484
- **File:** `apps/training/services.py:247`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1485

- **ID:** MC-1485
- **File:** `apps/training/services.py:326`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1486

- **ID:** MC-1486
- **File:** `apps/training/services.py:361`
- **Function/Class:** `<module>`
- **Token:** `transaction.atomic` (ATTR)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Verify Mongo transaction API / nesting
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1487

- **ID:** MC-1487
- **File:** `apps/mongo_poc/models.py:20`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1488

- **ID:** MC-1488
- **File:** `apps/mongo_poc/models.py:35`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1489

- **ID:** MC-1489
- **File:** `apps/mongo_poc/models.py:51`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1490

- **ID:** MC-1490
- **File:** `apps/mongo_poc/models.py:67`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1491

- **ID:** MC-1491
- **File:** `apps/mongo_poc/models.py:86`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1492

- **ID:** MC-1492
- **File:** `apps/mongo_poc/models.py:116`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1493

- **ID:** MC-1493
- **File:** `apps/mongo_poc/models.py:137`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1494

- **ID:** MC-1494
- **File:** `apps/mongo_poc/models.py:180`
- **Function/Class:** `Meta`
- **Token:** `UniqueConstraint` (NAME)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** LOW-MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** LOW-MEDIUM
- **Required redesign:** Review for Mongo semantics
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1495

- **ID:** MC-1495
- **File:** `apps/changeover/services.py:440`
- **Function/Class:** `upsert_allergen_risk_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1496

- **ID:** MC-1496
- **File:** `apps/environmental/services.py:585`
- **Function/Class:** `upsert_environmental_excursion_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1497

- **ID:** MC-1497
- **File:** `apps/foreign_body/services.py:411`
- **Function/Class:** `assess_and_persist_containment`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1498

- **ID:** MC-1498
- **File:** `apps/haccp/services.py:432`
- **Function/Class:** `set_critical_limit_reference`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1499

- **ID:** MC-1499
- **File:** `apps/haccp/services.py:472`
- **Function/Class:** `set_monitoring_rule`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1500

- **ID:** MC-1500
- **File:** `apps/haccp/services.py:512`
- **Function/Class:** `set_corrective_action_reference`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1501

- **ID:** MC-1501
- **File:** `apps/haccp/services.py:676`
- **Function/Class:** `bind_checklist_item_to_control_point`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1502

- **ID:** MC-1502
- **File:** `apps/ipqc/services.py:163`
- **Function/Class:** `upsert_ipqc_workflow_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1503

- **ID:** MC-1503
- **File:** `apps/iqc/services.py:114`
- **Function/Class:** `upsert_iqc_workflow_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1504

- **ID:** MC-1504
- **File:** `apps/packaging/services.py:332`
- **Function/Class:** `bind_checklist_item_to_artwork`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1505

- **ID:** MC-1505
- **File:** `apps/recall/services.py:154`
- **Function/Class:** `upsert_recall_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1506

- **ID:** MC-1506
- **File:** `apps/recall/services.py:564`
- **Function/Class:** `upsert_quantity_reconciliation`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1507

- **ID:** MC-1507
- **File:** `apps/rework/policy.py:62`
- **Function/Class:** `upsert_policy_stub`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1508

- **ID:** MC-1508
- **File:** `apps/rework/services.py:482`
- **Function/Class:** `upsert_rework_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1509

- **ID:** MC-1509
- **File:** `apps/sampling/services.py:412`
- **Function/Class:** `bind_checklist_item_to_sampling_plan`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1510

- **ID:** MC-1510
- **File:** `apps/sanitation/services.py:426`
- **Function/Class:** `bind_checklist_template_to_sanitation_program`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN

### MC-1511

- **ID:** MC-1511
- **File:** `apps/sanitation/services.py:462`
- **Function/Class:** `upsert_sanitation_fail_policy`
- **Token:** `update_or_create` (CALL)
- **Current PostgreSQL behavior:** uses Django ORM/SQL feature above
- **Mongo compatibility:** MEDIUM
- **Business invariant:** preserve existing domain semantics; do not weaken
- **Risk:** MEDIUM
- **Required redesign:** Race / uniqueness semantics must be proven
- **Test required:** yes — Mongo + regression on PostgreSQL during migration
- **Status:** OPEN


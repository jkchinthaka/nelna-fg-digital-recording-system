# Operational Permission Matrix (Phase 03C)

**Document status:** Technical inventory — **TECHNICALLY SUPPORTED** only  
**Not:** company-approved role chart  
**Code catalogue:** `apps/access_control/permission_catalogue.py`

## Capability × permission

| Capability bucket | Permission | Org | Site | Dept | System-wide | Business mapping |
| --- | --- | --- | --- | --- | --- | --- |
| view | `scheduling.view_checklisttask` | Y | Y | Y | — | APPROVAL REQUIRED |
| view | `checklists.view_checklisttemplate` | Y | — | — | Y | APPROVAL REQUIRED |
| view | `master_data.view_fgproduct` | Y | — | — | Y | APPROVAL REQUIRED |
| view | `organizations.view_shift` | Y | Y | Y | — | APPROVAL REQUIRED |
| view | `reviews.view_supervisorreview` | Y | Y | Y | — | APPROVAL REQUIRED |
| manage | `scheduling.manage_checklisttask` | Y | Y | Y | — | APPROVAL REQUIRED |
| manage | `capa.manage_capa` | Y | Y | Y | — | APPROVAL REQUIRED |
| manage | `nonconformance.manage_nonconformance` | Y | Y | Y | — | APPROVAL REQUIRED |
| manage | `supplier_quality.manage_supplierquality_qa` | Y | — | — | Y | APPROVAL REQUIRED |
| checklist_publish | `checklists.manage_checklist` | Y | — | — | Y | APPROVAL REQUIRED |
| master_data | `master_data.manage_fgproduct` | Y | Y | — | — | APPROVAL REQUIRED |
| master_data | `organizations.manage_shift` | Y | Y | — | — | APPROVAL REQUIRED |
| record | `scheduling.record_checklisttask` | Y | Y | Y | — | APPROVAL REQUIRED (APR-007) |
| submit | `scheduling.record_checklisttask` (same) | Y | Y | Y | — | APPROVAL REQUIRED |
| correction | `scheduling.record_checklisttask` (same) | Y | Y | Y | — | APPROVAL REQUIRED |
| supervisor_review | `reviews.review_checklistsubmission` | Y | Y | Y | — | APPROVAL REQUIRED (APR-008) |
| qa_review | `quality.qa_review_checklistsubmission` | Y | Y | Y | — | APPROVAL REQUIRED (APR-009) |
| audit_access | `security_audit.view_securityauditevent` | — | — | — | Y | APPROVAL REQUIRED |
| system_administration | Django `is_superuser` (not a Permission row) | — | — | — | Y | Break-glass only |

## Separation reminders

| Must not auto-imply | |
| --- | --- |
| manage → record | No |
| record → Supervisor review | No |
| Supervisor review → QA review | No |
| System Admin → business QA | No (pending APR-010 / SOD-04) |

## Approved business mappings found

**None.** Recorder / Supervisor / QA category → Role mappings remain empty configuration worksheets.

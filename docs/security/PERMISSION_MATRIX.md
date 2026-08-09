# Permission Matrix — Technical vs Business

**Document status:** Technical catalogue companion (Phase 03C)
**Authority:** Code permissions + `apps/access_control/permission_catalogue.py`
**Rule:** TECHNICALLY SUPPORTED ≠ BUSINESS APPROVED. Silence is not approval.

## Vocabulary

| Label | Meaning |
| --- | --- |
| TECHNICALLY SUPPORTED | Permission/codename exists and is enforceable via scoped RBAC |
| BUSINESS APPROVED | Named owner mapping of permission → business responsibility with APR evidence |
| APPROVAL REQUIRED | No written owner mapping yet |

## Capability separation (non-negotiable technical)

- `manage_*` does **not** imply `record_checklisttask`
- `record_checklisttask` does **not** imply Supervisor or QA review
- `review_checklistsubmission` does **not** imply QA or record
- `qa_review_checklistsubmission` does **not** imply Supervisor or record
- Submit and correction use the **record** permission (documented as separate capability buckets)

## Matrix

| Catalogue key | Permission | Bucket | Object scopes | Technical | Business mapping |
| --- | --- | --- | --- | --- | --- |
| view_checklisttask | `scheduling.view_checklisttask` | view | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| view_checklisttemplate | `checklists.view_checklisttemplate` | view | Organization / system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| view_checklistsubmission | `reviews.view_supervisorreview` | view | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_checklisttask | `scheduling.manage_checklisttask` | manage | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_checklist | `checklists.manage_checklist` | checklist_publish | Organization / system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_fgproduct | `master_data.manage_fgproduct` | master_data | Organization / Site | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_shift | `organizations.manage_shift` | master_data | Organization / Site | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_capa | `capa.manage_capa` | manage | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_nonconformance | `nonconformance.manage_nonconformance` | manage | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| manage_supplierquality_qa | `supplier_quality.manage_supplierquality_qa` | manage | Organization / system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| view_supplierquality_procurement | `supplier_quality.view_supplierquality_procurement` | view | Organization / system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| record_checklisttask | `scheduling.record_checklisttask` | record | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED (APR-007) |
| submit_via_record | `scheduling.record_checklisttask` | submit | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| correction_via_record | `scheduling.record_checklisttask` | correction | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| review_checklistsubmission | `reviews.review_checklistsubmission` | supervisor_review | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED (APR-008) |
| qa_review_checklistsubmission | `quality.qa_review_checklistsubmission` | qa_review | Organization / Site / Department | TECHNICALLY SUPPORTED | APPROVAL REQUIRED (APR-009) |
| audit_event_view | `security_audit.view_securityauditevent` | audit_access | system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED |
| system_administration_superuser | Django `is_superuser` | system_administration | system-wide | TECHNICALLY SUPPORTED | APPROVAL REQUIRED (break-glass only) |

## Approved business mappings found

**None.** APR-007 / APR-008 / APR-009 / APR-010 remain **EVIDENCE REQUIRED**.

## Related

- [PHASE_03C_ROLE_GOVERNANCE.md](../governance/PHASE_03C_ROLE_GOVERNANCE.md)
- [SOD_DECISION_REGISTER.md](../governance/SOD_DECISION_REGISTER.md)
- [ADR-007-SCOPED-RBAC.md](../architecture/ADR-007-SCOPED-RBAC.md)
- [CHECKLIST_RECORDER_ROLE_MAPPING.md](../business/CHECKLIST_RECORDER_ROLE_MAPPING.md)

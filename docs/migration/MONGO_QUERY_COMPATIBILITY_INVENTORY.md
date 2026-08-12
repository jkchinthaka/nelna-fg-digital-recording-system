# Mongo Query Compatibility Inventory

**Generated (UTC):** 2026-08-12T09:55:18Z  

Static scan of unsupported / high-risk Django ORM patterns for MongoDB cutover.
Counts are occurrence sites (AST), not unique business operations.

## Pattern summary

| Pattern | Occurrences | Mongo risk |
| --- | ---: | --- |
| prefetch_related | 34 | HIGH — unsupported / rewrite |
| OuterRef | 2 | HIGH — unproven / rewrite |
| Subquery | 2 | HIGH — unproven / rewrite |
| Exists | 0 | MEDIUM — verify |
| select_for_update | 137 | BLOCKER — replace with CAS |
| annotate | 8 | MEDIUM — case-by-case |
| aggregate | 16 | MEDIUM — case-by-case |
| Lower/Upper/Coalesce/Case/When | 87 | MEDIUM — expressions |
| select_related | 410 | LOW-MEDIUM — often OK as joins/lookups |
| RawSQL / extra | 36 | HIGH if present |

## Core operator path priority

Prove these before optional modules:

```text
Login → Daily Record → Save → Submit → Supervisor → Return/Approve
→ Correction/Resubmit → QA Release/Hold/Reject → History → Print
Then: NCR → RCA → CAPA
```

| Core page | Related apps / hints |
| --- | --- |
| Login | accounts, login, auth |
| Dashboard | dashboard, workspace |
| Daily Records | recording, scheduling |
| History | history, recording |
| Recorder task | recording |
| Supervisor queue | reviews |
| QA queue | quality |
| Printing | print, reports, batch_dossier |
| RCA | rca |
| CAPA | capa |
| NCR | nonconformance |
| Reports | reports |

## Occurrences by pattern

### `Case` (0)


### `Coalesce` (0)


### `Exists` (0)


### `Lower` (87)

- `apps/access_control/models.py:32`
- `apps/access_control/models.py:38`
- `apps/access_control/models.py:76`
- `apps/access_control/models.py:82`
- `apps/accounts/models.py:40`
- `apps/accounts/models.py:46`
- `apps/batch_genealogy/models.py:74`
- `apps/capa/models.py:152`
- `apps/change_control/models.py:145`
- `apps/changeover/models.py:93`
- `apps/checklists/models.py:199`
- `apps/checklists/models.py:209`
- `apps/checklists/models.py:521`
- `apps/checklists/models.py:1121`
- `apps/checklists/proposal_loader.py:440`
- `apps/compliance_mapping/models.py:164`
- `apps/compliance_mapping/models.py:232`
- `apps/customer_complaints/models.py:162`
- `apps/customer_complaints/models.py:236`
- `apps/dispatch/models.py:160`
- `apps/document_control/models.py:97`
- `apps/document_control/models.py:183`
- `apps/environmental/models.py:115`
- `apps/environmental/models.py:173`
- `apps/environmental/models.py:210`
- `apps/foreign_body/models.py:100`
- `apps/foreign_body/models.py:166`
- `apps/haccp/models.py:95`
- `apps/haccp/models.py:185`
- `apps/haccp/models.py:215`
- `apps/haccp/models.py:244`
- `apps/haccp/models.py:293`
- `apps/instruments/models.py:127`
- `apps/instruments/models.py:141`
- `apps/ipqc/models.py:131`
- `apps/iqc/models.py:96`
- `apps/iqc/models.py:97`
- `apps/laboratory/models.py:91`
- `apps/laboratory/models.py:159`
- `apps/laboratory/models.py:274`
- `apps/laboratory/models.py:332`
- `apps/master_data/models.py:99`
- `apps/master_data/models.py:104`
- `apps/master_data/models.py:123`
- `apps/master_data/models.py:125`
- `apps/master_data/models.py:196`
- `apps/master_data/models.py:206`
- `apps/master_data/models.py:373`
- `apps/master_data/models.py:379`
- `apps/nonconformance/models.py:182`
- `apps/nonconformance/models.py:309`
- `apps/notifications/models.py:154`
- `apps/organizations/models.py:29`
- `apps/organizations/models.py:35`
- `apps/organizations/models.py:64`
- `apps/organizations/models.py:71`
- `apps/organizations/models.py:113`
- `apps/organizations/models.py:119`
- `apps/organizations/models.py:128`
- `apps/organizations/models.py:191`
- `apps/organizations/models.py:220`
- `apps/packaging/models.py:77`
- `apps/packaging/models.py:268`
- `apps/process_fmea/models.py:84`
- `apps/process_fmea/models.py:224`
- `apps/process_fmea/models.py:260`
- `apps/product_returns/models.py:127`
- `apps/product_returns/models.py:128`
- `apps/quality_audits/models.py:147`
- `apps/quality_audits/models.py:272`
- `apps/quality_quarantine/models.py:101`
- `apps/quality_risks/models.py:146`
- `apps/quality_risks/models.py:204`
- `apps/rca/models.py:115`
- `apps/recall/models.py:161`
- `apps/recall/models.py:263`
- `apps/recall/models.py:301`
- `apps/recall/models.py:642`
- `apps/receiving/models.py:109`
- `apps/receiving/models.py:155`
- `apps/receiving/models.py:371`
- `apps/sampling/models.py:73`
- `apps/sampling/models.py:188`
- `apps/sanitation/models.py:87`
- `apps/sanitation/models.py:226`
- `apps/sanitation/models.py:348`
- `apps/supplier_quality/models.py:78`

### `OuterRef` (2)

- `apps/quality/selectors.py:51`
- `apps/reviews/selectors.py:49`

### `RawSQL` (0)


### `Subquery` (2)

- `apps/quality/selectors.py:71`
- `apps/reviews/selectors.py:62`

### `Upper` (0)


### `When` (0)


### `aggregate` (16)

- `apps/checklists/services.py:208`
- `apps/checklists/services.py:219`
- `apps/checklists/services.py:822`
- `apps/checklists/services.py:893`
- `apps/mongo_poc/services.py:89`
- `apps/mongo_poc/services.py:112`
- `apps/process_fmea/services.py:415`
- `apps/process_fmea/services.py:805`
- `apps/quality_risks/services.py:375`
- `apps/recording/correction_services.py:539`
- `apps/scheduling/generation.py:519`
- `apps/scheduling/generation.py:526`
- `apps/scheduling/generation.py:527`
- `apps/scheduling/generation.py:528`
- `apps/scheduling/generation.py:529`
- `apps/scheduling/generation.py:531`

### `annotate` (8)

- `apps/checklists/proposal_loader.py:439`
- `apps/checklists/selectors.py:108`
- `apps/checklists/selectors.py:153`
- `apps/compliance_mapping/selectors.py:87`
- `apps/quality_audits/selectors.py:96`
- `apps/quality_audits/selectors.py:119`
- `apps/quality_risks/selectors.py:89`
- `apps/reviews/selectors.py:54`

### `extra` (36)

- `apps/capa/admin.py:23`
- `apps/checklists/admin.py:22`
- `apps/checklists/admin.py:42`
- `apps/checklists/admin.py:77`
- `apps/checklists/evaluation.py:282`
- `apps/checklists/evaluation.py:290`
- `apps/checklists/evaluation.py:294`
- `apps/checklists/services.py:124`
- `apps/checklists/services.py:125`
- `apps/compliance_mapping/tests/test_phase46_compliance_mapping.py:491`
- `apps/compliance_mapping/tests/test_phase46_compliance_mapping.py:506`
- `apps/compliance_mapping/tests/test_phase46_compliance_mapping.py:513`
- `apps/compliance_mapping/tests/test_phase46_compliance_mapping.py:691`
- `apps/compliance_mapping/tests/test_phase46_compliance_mapping.py:694`
- `apps/dispatch/admin.py:29`
- `apps/dispatch/admin.py:36`
- `apps/ipqc/services.py:584`
- `apps/ipqc/services.py:589`
- `apps/master_data/admin.py:55`
- `apps/master_data/specification_services.py:70`
- `apps/master_data/specification_services.py:71`
- `apps/master_data/specification_services.py:93`
- `apps/master_data/specification_services.py:94`
- `apps/master_data/tests/test_phase06o_product_specifications.py:174`
- `apps/master_data/tests/test_phase06o_product_specifications.py:177`
- `apps/rca/services.py:472`
- `apps/rca/services.py:473`
- `apps/rca/services.py:474`
- `apps/recording/admin.py:19`
- `apps/recording/admin.py:133`
- `apps/recording/synthetic_demo.py:90`
- `apps/recording/synthetic_demo.py:91`
- `apps/scheduling/applicability.py:421`
- `apps/scheduling/applicability.py:422`
- `apps/scheduling/assignment.py:86`
- `apps/scheduling/batch_events.py:97`

### `prefetch_related` (34)

- `apps/access_control/governance_services.py:226`
- `apps/access_control/services.py:34`
- `apps/batch_dossier/selectors.py:158`
- `apps/batch_dossier/selectors.py:219`
- `apps/batch_dossier/selectors.py:300`
- `apps/checklists/proposal_loader.py:394`
- `apps/checklists/selectors.py:185`
- `apps/checklists/selectors.py:191`
- `apps/checklists/selectors.py:194`
- `apps/checklists/services.py:594`
- `apps/checklists/services.py:616`
- `apps/checklists/services.py:915`
- `apps/checklists/services.py:993`
- `apps/checklists/services.py:1858`
- `apps/checklists/views.py:564`
- `apps/core/checklist_workflow.py:308`
- `apps/quality/selectors.py:139`
- `apps/quality/selectors.py:143`
- `apps/recall/services.py:85`
- `apps/recording/correction_services.py:507`
- `apps/recording/daily_selectors.py:75`
- `apps/recording/daily_selectors.py:195`
- `apps/recording/selectors.py:57`
- `apps/recording/selectors.py:165`
- `apps/recording/selectors.py:169`
- `apps/recording/selectors.py:177`
- `apps/recording/services.py:358`
- `apps/recording/services.py:723`
- `apps/recording/services.py:983`
- `apps/recording/tests/test_phase06i_calculated_fields.py:426`
- `apps/reviews/selectors.py:223`
- `apps/reviews/selectors.py:227`
- `apps/sampling/engine.py:140`
- `apps/sanitation/services.py:413`

### `select_for_update` (137)

- `apps/access_control/governance_services.py:92`
- `apps/access_control/governance_services.py:179`
- `apps/access_control/governance_services.py:235`
- `apps/accounts/services.py:218`
- `apps/accounts/services.py:252`
- `apps/accounts/services.py:364`
- `apps/batch_dossier/services.py:147`
- `apps/batch_genealogy/services.py:150`
- `apps/capa/services.py:153`
- `apps/capa/services.py:199`
- `apps/capa/services.py:260`
- `apps/capa/services.py:322`
- `apps/capa/services.py:370`
- `apps/capa/services.py:408`
- `apps/checklists/effective_version.py:324`
- `apps/checklists/services.py:197`
- `apps/checklists/services.py:648`
- `apps/checklists/services.py:725`
- `apps/checklists/services.py:781`
- `apps/checklists/services.py:802`
- `apps/checklists/services.py:819`
- `apps/checklists/services.py:899`
- `apps/checklists/services.py:1089`
- `apps/checklists/services.py:1198`
- `apps/checklists/services.py:1226`
- `apps/checklists/services.py:1256`
- `apps/checklists/services.py:1306`
- `apps/checklists/services.py:1325`
- `apps/checklists/services.py:1741`
- `apps/checklists/services.py:1786`
- `apps/checklists/services.py:1821`
- `apps/customer_complaints/services.py:101`
- `apps/dispatch/services.py:248`
- `apps/dispatch/services.py:330`
- `apps/dispatch/services.py:377`
- `apps/dispatch/services.py:423`
- `apps/dispatch/services.py:487`
- `apps/dispatch/services.py:502`
- `apps/dispatch/services.py:614`
- `apps/dispatch/services.py:709`
- `apps/document_control/services.py:358`
- `apps/environmental/services.py:229`
- `apps/environmental/services.py:269`
- `apps/environmental/services.py:306`
- `apps/environmental/services.py:336`
- `apps/evidence/services.py:262`
- `apps/foreign_body/services.py:304`
- `apps/foreign_body/services.py:348`
- `apps/haccp/services.py:175`
- `apps/haccp/services.py:536`
- `apps/haccp/services.py:595`
- `apps/instruments/services.py:179`
- `apps/instruments/services.py:247`
- `apps/instruments/services.py:273`
- `apps/instruments/services.py:292`
- `apps/instruments/services.py:364`
- `apps/integrations/services.py:299`
- `apps/laboratory/services.py:172`
- `apps/laboratory/services.py:217`
- `apps/laboratory/services.py:361`
- `apps/laboratory/services.py:394`
- `apps/laboratory/services.py:440`
- `apps/master_data/services.py:224`
- `apps/master_data/services.py:285`
- `apps/master_data/services.py:304`
- `apps/master_data/specification_services.py:243`
- `apps/master_data/specification_services.py:290`
- `apps/master_data/specification_services.py:356`
- `apps/master_data/specification_services.py:376`
- `apps/master_data/specification_services.py:441`
- `apps/master_data/specification_services.py:476`
- `apps/master_data/specification_services.py:517`
- `apps/nonconformance/services.py:188`
- `apps/nonconformance/services.py:258`
- `apps/nonconformance/services.py:308`
- `apps/nonconformance/services.py:435`
- `apps/notifications/services.py:242`
- `apps/notifications/tasks.py:36`
- `apps/organizations/services.py:221`
- `apps/organizations/services.py:347`
- `apps/organizations/services.py:477`
- `apps/organizations/services.py:685`
- `apps/organizations/services.py:752`
- `apps/organizations/services.py:771`
- `apps/quality/services.py:97`
- `apps/quality/services.py:147`
- `apps/quality/services.py:170`
- `apps/quality_quarantine/services.py:174`
- `apps/quality_quarantine/services.py:230`
- `apps/quality_quarantine/services.py:290`
- `apps/quality_quarantine/services.py:329`
- `apps/rca/services.py:93`
- `apps/rca/services.py:110`
- `apps/rca/services.py:426`
- `apps/recording/correction_services.py:241`
- `apps/recording/correction_services.py:257`
- `apps/recording/correction_services.py:278`
- `apps/recording/correction_services.py:442`
- `apps/recording/correction_services.py:468`
- `apps/recording/correction_services.py:517`
- `apps/recording/services.py:164`
- `apps/recording/services.py:694`
- `apps/recording/services.py:730`
- `apps/recording/services.py:939`
- `apps/recording/services.py:993`
- `apps/reports/services.py:268`
- `apps/reviews/governance.py:205`
- `apps/reviews/services.py:89`
- `apps/reviews/services.py:140`
- `apps/rework/services.py:208`
- `apps/rework/services.py:234`
- `apps/rework/services.py:318`
- `apps/rework/services.py:390`
- `apps/rework/services.py:425`
- `apps/sampling/services.py:124`
- `apps/sampling/services.py:288`
- `apps/sampling/services.py:344`
- `apps/sanitation/services.py:141`
- `apps/sanitation/services.py:196`
- `apps/sanitation/services.py:239`
- `apps/sanitation/services.py:303`
- `apps/sanitation/services.py:336`
- `apps/sanitation/services.py:377`
- `apps/sanitation/services.py:413`
- `apps/scheduling/applicability.py:537`
- `apps/scheduling/applicability.py:604`
- `apps/scheduling/assignment.py:278`
- `apps/scheduling/assignment.py:354`
- `apps/scheduling/batch_events.py:337`
- `apps/scheduling/due.py:229`
- `apps/scheduling/generation.py:636`
- `apps/scheduling/services.py:292`
- `apps/supplier_quality/services.py:127`
- `apps/supplier_quality/services.py:208`
- `apps/training/services.py:267`
- `apps/training/services.py:334`
- `apps/training/services.py:384`

### `select_related` (410)

- `apps/access_control/governance_services.py:54`
- `apps/access_control/governance_services.py:99`
- `apps/access_control/governance_services.py:186`
- `apps/access_control/governance_services.py:242`
- `apps/access_control/selectors.py:27`
- `apps/access_control/services.py:34`
- `apps/access_control/services.py:183`
- `apps/batch_dossier/selectors.py:44`
- `apps/batch_dossier/selectors.py:63`
- `apps/batch_dossier/selectors.py:82`
- `apps/batch_dossier/selectors.py:101`
- `apps/batch_dossier/selectors.py:117`
- `apps/batch_dossier/selectors.py:136`
- `apps/batch_dossier/selectors.py:158`
- `apps/batch_dossier/selectors.py:190`
- `apps/batch_dossier/selectors.py:205`
- `apps/batch_dossier/selectors.py:233`
- `apps/batch_dossier/selectors.py:262`
- `apps/batch_dossier/selectors.py:277`
- `apps/batch_dossier/selectors.py:305`
- `apps/batch_genealogy/selectors.py:34`
- `apps/batch_genealogy/selectors.py:42`
- `apps/batch_genealogy/selectors.py:49`
- `apps/batch_genealogy/services.py:515`
- `apps/batch_genealogy/services.py:524`
- `apps/capa/selectors.py:38`
- `apps/capa/selectors.py:54`
- `apps/capa/selectors.py:61`
- `apps/capa/services.py:370`
- `apps/capa/views.py:47`
- `apps/capa/views.py:123`
- `apps/change_control/services.py:130`
- `apps/change_control/services.py:167`
- `apps/change_control/services.py:229`
- `apps/change_control/services.py:291`
- `apps/change_control/services.py:339`
- `apps/change_control/services.py:373`
- `apps/change_control/services.py:431`
- `apps/change_control/services.py:466`
- `apps/checklists/effective_version.py:122`
- `apps/checklists/effective_version.py:161`
- `apps/checklists/effective_version.py:324`
- `apps/checklists/proposal_loader.py:439`
- `apps/checklists/proposal_loader.py:449`
- `apps/checklists/selectors.py:83`
- `apps/checklists/selectors.py:108`
- `apps/checklists/selectors.py:136`
- `apps/checklists/selectors.py:164`
- `apps/checklists/selectors.py:185`
- `apps/checklists/services.py:197`
- `apps/checklists/services.py:415`
- `apps/checklists/services.py:594`
- `apps/checklists/services.py:616`
- `apps/checklists/services.py:632`
- `apps/checklists/services.py:725`
- `apps/checklists/services.py:899`
- `apps/checklists/services.py:993`
- `apps/checklists/services.py:1003`
- `apps/checklists/services.py:1089`
- `apps/checklists/services.py:1101`
- `apps/checklists/services.py:1198`
- `apps/checklists/services.py:1226`
- `apps/checklists/services.py:1256`
- `apps/checklists/services.py:1306`
- `apps/checklists/services.py:1741`
- `apps/checklists/services.py:1786`
- `apps/checklists/services.py:1821`
- `apps/checklists/tests/test_checklist_governance.py:362`
- `apps/checklists/tests/test_checklist_governance.py:363`
- `apps/checklists/tests/test_checklist_response_schema.py:323`
- `apps/checklists/views.py:151`
- `apps/checklists/views.py:175`
- `apps/checklists/views.py:439`
- `apps/checklists/views.py:472`
- `apps/checklists/views.py:495`
- `apps/checklists/views.py:518`
- `apps/checklists/views.py:564`
- `apps/checklists/views.py:623`
- `apps/checklists/views.py:648`
- `apps/checklists/views.py:673`
- `apps/checklists/views.py:707`
- `apps/checklists/views.py:745`
- `apps/checklists/views.py:772`
- `apps/compliance_mapping/selectors.py:61`
- `apps/compliance_mapping/selectors.py:76`
- `apps/compliance_mapping/services.py:268`
- `apps/compliance_mapping/services.py:335`
- `apps/compliance_mapping/services.py:371`
- `apps/compliance_mapping/services.py:408`
- `apps/compliance_mapping/services.py:457`
- `apps/compliance_mapping/services.py:493`
- `apps/compliance_mapping/services.py:533`
- `apps/compliance_mapping/services.py:579`
- `apps/compliance_mapping/services.py:640`
- `apps/compliance_mapping/services.py:839`
- `apps/core/checklist_workflow.py:308`
- `apps/core/checklist_workflow.py:316`
- `apps/customer_complaints/selectors.py:38`
- `apps/customer_complaints/selectors.py:48`
- `apps/customer_complaints/selectors.py:65`
- `apps/customer_complaints/views.py:40`
- `apps/dispatch/selectors.py:42`
- `apps/dispatch/selectors.py:49`
- `apps/dispatch/selectors.py:62`
- `apps/dispatch/views.py:40`
- `apps/document_control/selectors.py:92`
- `apps/document_control/selectors.py:106`
- `apps/document_control/services.py:157`
- `apps/document_control/services.py:206`
- `apps/document_control/services.py:246`
- `apps/document_control/services.py:272`
- `apps/document_control/services.py:303`
- `apps/document_control/services.py:352`
- `apps/document_control/services.py:430`
- `apps/document_control/services.py:492`
- `apps/document_control/services.py:538`
- `apps/environmental/selectors.py:20`
- `apps/environmental/selectors.py:57`
- `apps/environmental/services.py:269`
- `apps/environmental/services.py:306`
- `apps/environmental/services.py:336`
- `apps/environmental/services.py:400`
- `apps/environmental/services.py:409`
- `apps/environmental/services.py:419`
- `apps/evidence/linking.py:118`
- `apps/evidence/linking.py:139`
- `apps/evidence/linking.py:158`
- `apps/evidence/linking.py:178`
- `apps/evidence/linking.py:247`
- `apps/evidence/linking.py:285`
- `apps/evidence/linking.py:394`
- `apps/evidence/linking.py:412`
- `apps/evidence/linking.py:426`
- `apps/evidence/selectors.py:45`
- `apps/evidence/selectors.py:59`
- `apps/evidence/services.py:172`
- `apps/foreign_body/selectors.py:29`
- `apps/foreign_body/services.py:304`
- `apps/haccp/selectors.py:34`
- `apps/haccp/selectors.py:48`
- `apps/haccp/selectors.py:64`
- `apps/haccp/services.py:229`
- `apps/haccp/services.py:272`
- `apps/haccp/services.py:310`
- `apps/haccp/services.py:350`
- `apps/haccp/services.py:419`
- `apps/haccp/services.py:464`
- `apps/haccp/services.py:499`
- `apps/haccp/services.py:536`
- `apps/haccp/services.py:595`
- `apps/haccp/services.py:641`
- `apps/haccp/services.py:654`
- `apps/haccp/services.py:669`
- `apps/haccp/snapshots.py:33`
- `apps/haccp/views.py:49`
- `apps/instruments/selectors.py:45`
- `apps/instruments/selectors.py:69`
- `apps/instruments/selectors.py:100`
- `apps/instruments/services.py:179`
- `apps/instruments/services.py:326`
- `apps/instruments/services.py:364`
- `apps/integrations/reconciliation.py:37`
- `apps/ipqc/selectors.py:72`
- `apps/ipqc/selectors.py:91`
- `apps/ipqc/selectors.py:107`
- `apps/iqc/services.py:498`
- `apps/laboratory/selectors.py:34`
- `apps/laboratory/selectors.py:41`
- `apps/laboratory/selectors.py:48`
- `apps/laboratory/services.py:269`
- `apps/laboratory/views.py:52`
- `apps/master_data/selectors.py:61`
- `apps/master_data/selectors.py:84`
- `apps/master_data/selectors.py:155`
- `apps/master_data/selectors.py:181`
- `apps/master_data/selectors.py:197`
- `apps/master_data/services.py:224`
- `apps/master_data/specification_services.py:243`
- `apps/master_data/specification_services.py:290`
- `apps/master_data/specification_services.py:356`
- `apps/master_data/specification_services.py:441`
- `apps/master_data/specification_services.py:476`
- `apps/master_data/specification_services.py:517`
- `apps/master_data/specification_services.py:551`
- `apps/nonconformance/selectors.py:42`
- `apps/nonconformance/selectors.py:58`
- `apps/nonconformance/selectors.py:73`
- `apps/nonconformance/selectors.py:85`
- `apps/nonconformance/views.py:47`
- `apps/nonconformance/views.py:131`
- `apps/notifications/selectors.py:16`
- `apps/notifications/tasks.py:36`
- `apps/organizations/hierarchy_import.py:537`
- `apps/organizations/hierarchy_import.py:540`
- `apps/organizations/selectors.py:38`
- `apps/organizations/selectors.py:49`
- `apps/organizations/selectors.py:54`
- `apps/organizations/selectors.py:66`
- `apps/organizations/selectors.py:77`
- `apps/organizations/selectors.py:110`
- … 210 more

## M2M / through / cascades

See `docs/migration/FG_MONGODB_COLLECTION_MANIFEST.md` and `docs/migration/MONGODB_PRIMARY_KEY_PLAN.md` for through-model and PK review.
Delete cascades and M2M must be validated per relationship on Mongo POC — do not assume PostgreSQL ON DELETE behavior.

## Classification

```text
MONGODB SAME-DATABASE CUTOVER BLOCKED — CONTINUING COMPATIBILITY ENGINEERING
```


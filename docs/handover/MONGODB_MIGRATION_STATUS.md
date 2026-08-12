# MongoDB Migration Status

## Executive status

```text
STARTING_BRANCH=feature/mongodb-same-maintainpro-db
STARTING_SHA=d8682b7
MAIN_SHA=d5a4460
ORIGIN_MAIN_SHA=d5a4460
```

PostgreSQL remains the authoritative system of record on `main`.

```text
MONGODB SAME-DATABASE CUTOVER BLOCKED — CONTINUING COMPATIBILITY ENGINEERING
```

Exact classification for this checkpoint:

```text
CONTINUATION REQUIRED — MONGODB FUNCTIONAL PARITY MIGRATION CHECKPOINT CREATED
```

---

## Production target (unchanged)

```text
Host route: via MONGODB_URI (do not hard-code 127.0.0.1:27018 in Python)
Logical database: mgintginpro_prod
FG namespace: fg_
Isolated POC only: fg_same_db_poc
Company Mongo writes: NONE
MaintainPro impact: NONE
main merged: NO
```

---

## Checkpoint progress

| Item | Status |
| --- | --- |
| Persistence facade | Done — `apps/core/persistence/` (vendor, atomic, CAS, lock_queryset, latest_ids) |
| Supervisor production path | Done — unique insert, no `select_for_update` |
| QA production path | Done — unique insert, no `select_for_update` |
| Recording start production | Done — unique(task) insert |
| Recording draft save | Done — `lock_queryset` + draft_version CAS |
| Recording submit / correction | Done — `lock_queryset` + unique IntegrityError |
| RCA close/cancel | Done — CAS status + mutable guard; `@atomic_fn` |
| Supervisor/QA queue OuterRef/Subquery | Done — `latest_ids_by_parent` |
| Supervisor/QA section prefetch | Done — batched `load_sections_with_items_and_options` |
| Full Mongo pytest suite | Not run |
| Live company read-only audit | Script ready — not executed |

---

## Exact inventory highlights (this generation)

| Token | Count |
| --- | ---: |
| select_for_update | 118 (was 137) |
| prefetch_related | 30 (was 34) |
| OuterRef / Subquery (core queues) | 0 remaining in reviews/quality selectors |
| transaction.atomic | 372 |
| IntegrityError | 110 |
| Lower | 87 |

---

## Next continuation module

1. Remaining `select_for_update` in checklists versioning, scheduling, CAPA, NCR, laboratory, HACCP, master_data (~118 sites)
2. Remaining `prefetch_related` in checklists selectors/services
3. Isolated Mongo POC: migrate + subset pytest under `mongo_same_db_poc`
4. Contrib Mongo AppConfig activation (POC only)
5. FG-only backup/restore for `fg_*` collections

---

## References

- [../migration/MONGO_FULL_COMPATIBILITY_INVENTORY.md](../migration/MONGO_FULL_COMPATIBILITY_INVENTORY.md)
- [../migration/MONGO_CONCURRENCY_PATTERN.md](../migration/MONGO_CONCURRENCY_PATTERN.md)
- [../migration/FG_COLLECTION_MANIFEST.md](../migration/FG_COLLECTION_MANIFEST.md)
- [../migration/DJANGO_CONTRIB_MONGO_CONFIG.md](../migration/DJANGO_CONTRIB_MONGO_CONFIG.md)
- [../migration/MONGO_PRIMARY_KEY_MATRIX.md](../migration/MONGO_PRIMARY_KEY_MATRIX.md)

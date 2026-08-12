# MongoDB Migration Status

## Executive status

```text
STARTING_BRANCH=feature/mongodb-same-maintainpro-db
STARTING_SHA=aa4c789
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
| Full compatibility inventory | Done — `MONGO_FULL_COMPATIBILITY_INVENTORY.md` (exact AST scan) |
| Persistence facade | Done — `apps/core/persistence/` (vendor detect, atomic, CAS) |
| Permanent `fg_` naming + manifests | Done |
| Primary key matrix | Done |
| Contrib Mongo config plan | Documented — not activated on main |
| Supervisor CAS spike | PASS |
| QA CAS spike | PASS (this batch) |
| Recording start CAS spike | PASS (this batch) |
| Recording submit/correction spike | **NEXT** |
| RCA / CAPA / NCR spikes | Not started |
| prefetch / Subquery rewrites | Inventory only |
| Full Mongo pytest suite | Not run |
| Live company read-only audit | Script ready — not executed |

---

## Exact inventory highlights (this generation)

| Token | Count |
| --- | ---: |
| select_for_update | 137 |
| prefetch_related | 34 |
| OuterRef | 2 |
| transaction.atomic | 396 |
| IntegrityError | 113 |
| Lower | 87 |

---

## Next continuation module

1. **Recording submit + draft + correction CAS spikes** (`apps/recording/services.py`)
2. Replace production Supervisor/QA paths to call persistence facade behind feature flag / backend detection
3. RCA close/cancel concurrency spike
4. Begin prefetch_related rewrites for Supervisor/QA queues
5. Isolated Mongo POC migrate + subset pytest under `mongo_same_db_poc`

---

## References

- [../migration/MONGO_FULL_COMPATIBILITY_INVENTORY.md](../migration/MONGO_FULL_COMPATIBILITY_INVENTORY.md)
- [../migration/MONGO_CONCURRENCY_PATTERN.md](../migration/MONGO_CONCURRENCY_PATTERN.md)
- [../migration/FG_COLLECTION_MANIFEST.md](../migration/FG_COLLECTION_MANIFEST.md)
- [../migration/DJANGO_CONTRIB_MONGO_CONFIG.md](../migration/DJANGO_CONTRIB_MONGO_CONFIG.md)
- [../migration/MONGO_PRIMARY_KEY_MATRIX.md](../migration/MONGO_PRIMARY_KEY_MATRIX.md)

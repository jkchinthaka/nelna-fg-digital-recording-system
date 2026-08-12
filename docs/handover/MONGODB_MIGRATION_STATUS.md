# MongoDB Migration Status

## Executive status

PostgreSQL remains the authoritative system of record on `main`. MongoDB same-database cutover with MaintainPro in **`mgintginpro_prod`** is **blocked** — continuing compatibility engineering on `feature/mongodb-same-maintainpro-db`.

```text
MONGODB SAME-DATABASE CUTOVER BLOCKED — CONTINUING COMPATIBILITY ENGINEERING
```

Static collection collision audit (231 FG `fg_*` vs 114 MaintainPro Prisma collections): **SAFE — NO COLLISION** (0 exact matches). Live read-only inventory on company MongoDB still required before any write.

---

## Checkpoint (this branch)

| Item | Status |
| --- | --- |
| Safety boundary commit | Done |
| Permanent `fg_` naming contract | Done (`apps/core/db_namespace.py` + manifest) |
| Primary key audit | Done — 220 UUID SAFE; 6 through; 4 contrib; 1 other |
| `select_for_update` inventory | **137** sites documented |
| Concurrency pattern | Optimistic CAS / unique insert (`optimistic_transition`) |
| Supervisor Mongo spike | PASS on PostgreSQL race harness (6 tests) |
| QA / Recording / RCA spikes | Not started |
| Full Mongo POC pytest | Not run |
| Company Mongo writes | **NONE** |
| `main` merged | **NO** |

---

## Production target (confirmed)

```text
Host: 127.0.0.1
Port: 27018
Database: mgintginpro_prod
FG namespace: fg_
```

Isolated POC only: `fg_same_db_poc` on local replica set port 27027.

---

## References

- [../migration/SAME_DATABASE_MONGODB_CUTOVER_AUDIT.md](../migration/SAME_DATABASE_MONGODB_CUTOVER_AUDIT.md)
- [../migration/FG_MONGODB_COLLECTION_MANIFEST.md](../migration/FG_MONGODB_COLLECTION_MANIFEST.md)
- [../migration/MONGODB_PRIMARY_KEY_PLAN.md](../migration/MONGODB_PRIMARY_KEY_PLAN.md)
- [../migration/MONGO_CONCURRENCY_INVENTORY.md](../migration/MONGO_CONCURRENCY_INVENTORY.md)
- [../migration/MONGO_CONCURRENCY_PATTERN.md](../migration/MONGO_CONCURRENCY_PATTERN.md)
- [../migration/MONGO_QUERY_COMPATIBILITY_INVENTORY.md](../migration/MONGO_QUERY_COMPATIBILITY_INVENTORY.md)
- [../migration/MONGO_TEST_STRATEGY.md](../migration/MONGO_TEST_STRATEGY.md)
- [../migration/FG_MONGO_DBA_USER_INSTRUCTIONS.md](../migration/FG_MONGO_DBA_USER_INSTRUCTIONS.md)

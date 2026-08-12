# MongoDB Migration Status

## Executive status

PostgreSQL remains the authoritative system of record on `main`. MongoDB same-database cutover with MaintainPro in **`mgintginpro_prod`** is **blocked** — see [../migration/SAME_DATABASE_MONGODB_CUTOVER_AUDIT.md](../migration/SAME_DATABASE_MONGODB_CUTOVER_AUDIT.md) and [../migration/COLLECTION_COLLISION_AUDIT.md](../migration/COLLECTION_COLLISION_AUDIT.md).

Static collection collision audit (231 FG `fg_*` vs 114 MaintainPro Prisma collections): **SAFE — NO COLLISION** (0 exact matches). Live read-only inventory on company MongoDB still required before any write.

Exact gate status from the MongoDB POC results:

```text
STATUS: MONGODB POC PARTIAL — ISOLATED INVARIANTS PASSED; FULL APPLICATION NOT PROVEN — DO NOT MIGRATE
```

Exact cutover status from the same document:

```text
STATUS: MONGODB POC FAILED FOR CUTOVER — DO NOT MIGRATE
```

## Handover blocker statement

MongoDB cutover must be treated as professionally blocked at handover time because:

- the POC proved only isolated mirror-model invariants
- full application compatibility was not demonstrated
- the default application path still targets PostgreSQL
- the required owner decision `APR-020` is still outstanding

## Specific technical blockers cited in the repo

- `select_for_update` parity not proven
- nested savepoint behavior unsupported
- `prefetch_related` unsupported for the assessed backend path
- `OuterRef` / `Subquery` production selectors not fully proven
- stock Django `auth.User` AutoField compatibility not proven for cutover
- full application pytest suite on MongoDB not completed

## Safe handover language

Use one of these statements:

- PostgreSQL is the current system of record.
- MongoDB was evaluated through an isolated POC.
- MongoDB cutover is blocked and must not be presented as the migration path.

Do not say:

- MongoDB is approved
- MongoDB passed cutover
- the application has migrated

## References

- [../migration/MONGODB_POC_RESULTS.md](../migration/MONGODB_POC_RESULTS.md)
- [../architecture/ADR-018-DATABASE-PLATFORM-MONGODB-ASSESSMENT.md](../architecture/ADR-018-DATABASE-PLATFORM-MONGODB-ASSESSMENT.md)
- [DATABASE.md](DATABASE.md)

# Backup / restore / DR

PostgreSQL is the system of record. MongoDB is not.

## Non-production drill

Run `python scripts/ops/restore_drill.py` on an approved non-production workstation.

- Host tools: `psql` / `pg_dump` / `pg_restore` on PATH, or
- Docker: `RESTORE_DRILL_DOCKER_SERVICE=postgres`

The script writes `docs/operations/RESTORE_DRILL_EVIDENCE.md`.  
RPO/RTO remain **COMPANY DECISION REQUIRED**.

## Attachments

Evidence files live in object storage (MinIO locally; S3-compatible in production).  
Object-store backup/restore is a separate operator procedure. Do not assume database restore includes photos.

## Production

Do not run the scratch-DB drill against production. Production backup ownership is unassigned until IT names it.

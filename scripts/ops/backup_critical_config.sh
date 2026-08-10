#!/usr/bin/env bash
# Phase 19 — critical config inventory export (no secrets).
# Captures approved non-secret settings keys for ops custody. Secrets stay in vault.
set -euo pipefail
: "${BACKUP_DIR:?}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="${BACKUP_DIR}/nelna_fg_critical_config_${STAMP}.txt"
mkdir -p "${BACKUP_DIR}"
{
  echo "# Nelna FG critical config inventory (no secret values)"
  echo "# Generated (UTC): ${STAMP}"
  echo "# Operator must pair this with vault-held secrets under company custody."
  echo
  echo "Required production env keys (values omitted):"
  cat <<'KEYS'
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
DJANGO_CSRF_TRUSTED_ORIGINS
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
REDIS_URL
SECURE_SSL_REDIRECT
SECURE_HSTS_SECONDS
SESSION_COOKIE_AGE
EVIDENCE_STORAGE_ROOT
KEYS
  if [[ -f ".env.example" ]]; then
    echo
    echo "--- .env.example snapshot (placeholders only) ---"
    # Strip obvious secret-bearing assignment lines by redacting values after '='.
    sed -E 's/^(DJANGO_SECRET_KEY|POSTGRES_PASSWORD|REDIS_URL|MONGODB_URI)=.*/\1=[REDACTED]/' .env.example
  fi
} > "${OUT}"
sha256sum "${OUT}" > "${OUT}.sha256"
echo "Wrote ${OUT}"

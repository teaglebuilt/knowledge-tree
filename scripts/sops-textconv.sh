#!/usr/bin/env bash
# git textconv filter: render sops-encrypted markdown as plaintext in diffs.
# Wired up by .gitattributes (diff=sops) + `make secrets-hooks`.
# Falls back to cat so a not-yet-encrypted file still diffs normally.
set -euo pipefail
if head -c 200 "$1" | grep -q '"data": "ENC\[AES256_GCM'; then
  # Committed ciphertext holds ${AWS_ACCOUNT_ID} in its KMS ARN; sops needs the
  # real digits to reach KMS. Mirrors kb.secrets._sops.
  acct="${AWS_ACCOUNT_ID:-$(aws sts get-caller-identity --query Account --output text)}"
  tmp=$(mktemp)
  trap 'rm -f "$tmp"' EXIT
  sed "s/\${AWS_ACCOUNT_ID}/$acct/" "$1" > "$tmp"
  sops -d --input-type binary --output-type binary "$tmp"
else
  cat "$1"
fi

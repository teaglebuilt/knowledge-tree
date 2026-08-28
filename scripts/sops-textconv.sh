#!/usr/bin/env bash
# git textconv filter: render sops-encrypted markdown as plaintext in diffs.
# Wired up by .gitattributes (diff=sops) + `make secrets-git-config`.
# Falls back to cat so a not-yet-encrypted file still diffs normally.
set -euo pipefail
if head -c 200 "$1" | grep -q '"data": "ENC\[AES256_GCM'; then
  sops -d --input-type binary --output-type binary "$1"
else
  cat "$1"
fi

from __future__ import annotations

import functools
import os
import re
import subprocess
import tempfile
from pathlib import Path

import yaml

from . import config

# A sops binary-store file is JSON whose payload is a single ENC[...] blob.
_MARKER = b"ENC[AES256_GCM"

# Neither .sops.yaml nor a committed ciphertext carries the AWS account id --
# both hold ${AWS_ACCOUNT_ID} in the account field of the KMS ARN. sops does no
# interpolation of its own (it rejects the placeholder as a malformed ARN), so
# _sops() expands it on the way in and templates it back out on the way out.
# Only the account field of an arn:aws:kms: string is touched, never arbitrary
# document text.
_ACCOUNT_VAR = "${AWS_ACCOUNT_ID}"
_ARN_REAL = re.compile(r"(arn:aws:kms:[a-z0-9-]+:)(\d{12})(:)")
_ARN_VAR = re.compile(r"(arn:aws:kms:[a-z0-9-]+:)\$\{AWS_ACCOUNT_ID\}(:)")


@functools.lru_cache(maxsize=1)
def account_id() -> str:
    """Resolve the AWS account id: $AWS_ACCOUNT_ID, else the caller's identity.

    Cached, so a batch encrypt does one sts call rather than one per file and
    cannot half-succeed if that call is flaky.
    """
    acct = os.environ.get("AWS_ACCOUNT_ID")
    if acct:
        return acct
    proc = subprocess.run(
        ["aws", "sts", "get-caller-identity", "--query", "Account", "--output", "text"],
        capture_output=True,
        text=True,
    )
    acct = proc.stdout.strip()
    if proc.returncode != 0 or not acct.isdigit():
        raise SystemExit(
            "cannot resolve the AWS account id -- set AWS_ACCOUNT_ID, or make\n"
            "`aws sts get-caller-identity` work (e.g. `aws sso login`)."
        )
    return acct


def expand(text: str, acct: str) -> str:
    """${AWS_ACCOUNT_ID} -> digits, in KMS ARNs only."""
    return _ARN_VAR.sub(rf"\g<1>{acct}\g<2>", text)


def templatize(text: str, acct: str) -> str:
    """Digits -> ${AWS_ACCOUNT_ID}, in KMS ARNs only."""
    return _ARN_REAL.sub(rf"\g<1>{_ACCOUNT_VAR}\g<3>", text)


# --------------------------------------------------------------------------- #
# policy
# --------------------------------------------------------------------------- #

def load_policy() -> dict:
    if not config.BRANCHES_PATH.exists():
        raise FileNotFoundError(f"{config.BRANCHES_PATH} not found")
    return yaml.safe_load(config.BRANCHES_PATH.read_text()) or {}


def wants_encryption(rel: str | Path, policy: dict) -> bool:
    """Deepest `encrypted:` declaration on the path's ancestry wins."""
    parts = Path(rel).parts
    if not parts or parts[0] != config.TREE_DIR:
        return False

    encrypted = False
    node = policy
    for segment in parts[1:-1]:  # directory segments below tree/
        if not isinstance(node, dict) or segment not in node:
            break
        node = node[segment] or {}
        if "encrypted" in node:
            encrypted = bool(node["encrypted"])
        node = node.get("branches") or {}
    return encrypted


def is_encrypted(data: bytes) -> bool:
    return data.lstrip()[:1] == b"{" and _MARKER in data[:4096]


# --------------------------------------------------------------------------- #
# file discovery
# --------------------------------------------------------------------------- #

def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=config.ROOT, capture_output=True, check=False
    )


def _markdown(paths: list[str] | None) -> list[Path]:
    """Tracked + untracked-but-not-ignored markdown, repo-relative."""
    out = _git(
        "ls-files", "--cached", "--others", "--exclude-standard", "-z",
        "--", *(paths or [config.TREE_DIR]),
    )
    return [Path(p) for p in out.stdout.decode().split("\0") if p.endswith(".md")]


def resolve(paths: list[str] | None = None) -> list[tuple[Path, bool]]:
    """[(repo-relative path, should-be-encrypted)], deduped and sorted."""
    policy = load_policy()
    return sorted({(f, wants_encryption(f, policy)) for f in _markdown(paths)})


def _staged(rel: Path) -> bytes | None:
    out = _git("show", f":{rel.as_posix()}")
    return out.stdout if out.returncode == 0 else None


def encrypted_paths() -> set[str]:
    """Repo-relative paths of files that are ciphertext on disk right now.

    Used by the ingest pipeline so encrypted notes never reach the index.
    """
    out = set()
    for rel, _ in resolve():
        fp = config.ROOT / rel
        if fp.exists() and is_encrypted(fp.read_bytes()):
            out.add(str(rel))
    return out


# --------------------------------------------------------------------------- #
# commands
# --------------------------------------------------------------------------- #

def status(paths: list[str] | None = None, show_all: bool = False) -> int:
    """Report files the policy covers. Plaintext-by-default files are the vast
    majority of the tree and are only listed under --all."""
    shown = mismatched = 0
    for rel, want in resolve(paths):
        have = is_encrypted((config.ROOT / rel).read_bytes())
        bad = have != want
        mismatched += bad
        if not (want or bad or show_all):
            continue
        shown += 1
        flag = "  <-- MISMATCH" if bad else ""
        print(
            f"want={'encrypted' if want else 'plaintext':<9} "
            f"on-disk={'encrypted' if have else 'plaintext':<9} {rel}{flag}"
        )
    print(f"\n{shown} file(s) shown, {mismatched} out of policy")
    return 0


def check(paths: list[str] | None = None, staged: bool = False) -> int:
    """Exit non-zero if any file's state disagrees with branches.yaml."""
    bad: list[tuple[Path, bool]] = []
    for rel, want in resolve(paths):
        data = _staged(rel) if staged else None
        if data is None:
            fp = config.ROOT / rel
            if not fp.exists():
                continue
            data = fp.read_bytes()
        if is_encrypted(data) != want:
            bad.append((rel, want))

    for rel, want in bad:
        if want:
            print(f"PLAINTEXT, but branches.yaml says encrypted:  {rel}")
        else:
            print(f"ENCRYPTED, but branches.yaml says plaintext:  {rel}")

    if bad:
        print(
            "\nReconcile with `make secrets-encrypt` (or `make secrets-decrypt`), "
            "or change the policy in tree/branches.yaml."
        )
        return 1
    return 0


def _sops(flag: str, rel: Path) -> bool:
    """Run `sops -i` with ${AWS_ACCOUNT_ID} resolved on both inputs it reads.

    sops is handed a temp copy of .sops.yaml with real digits (`--config`), and
    for a decrypt the file's own `sops:` metadata is expanded first -- that ARN
    is load-bearing, KMS rejects the call without the right account. After an
    encrypt the account id sops just wrote into the metadata is templated back
    out, so what lands in git stays free of it. The MAC covers the payload, not
    the key metadata, so rewriting that string does not invalidate the file.

    A plaintext body is never rewritten, only ciphertext metadata, so a
    document may contain the literal string ${AWS_ACCOUNT_ID} unharmed.
    """
    acct = account_id()
    fp = config.ROOT / rel
    original = fp.read_bytes()

    if flag == "-d":
        expanded = expand(original.decode(), acct).encode()
        if expanded != original:
            fp.write_bytes(expanded)

    # The temp config MUST live in the repo root: sops resolves path_regex
    # relative to the directory holding the config file, so a /tmp copy makes
    # every ^tree/... rule miss ("no matching creation rules found").
    fd, cfg = tempfile.mkstemp(dir=config.ROOT, prefix=".sops-", suffix=".yaml")
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(expand(config.SOPS_CONFIG_PATH.read_text(), acct))
        ok = subprocess.run(
            ["sops", "--config", Path(cfg).name, flag, "-i", rel.as_posix()],
            cwd=config.ROOT,
        ).returncode == 0
    finally:
        os.unlink(cfg)

    if not ok:
        if fp.read_bytes() != original:
            fp.write_bytes(original)  # undo the expansion
        return False

    if flag == "-e":
        out = fp.read_bytes()
        fp.write_bytes(templatize(out.decode(), acct).encode())
    return True


def encrypt(paths: list[str] | None = None) -> int:
    """Encrypt every file the policy marks encrypted. Idempotent.

    sops <3.9 has no already-encrypted guard and will silently wrap a file
    twice, so the on-disk check here is load-bearing.
    """
    rc = 0
    for rel, want in resolve(paths):
        if not want:
            continue
        if is_encrypted((config.ROOT / rel).read_bytes()):
            print(f"  = {rel}")
        elif _sops("-e", rel):
            print(f"  + encrypted  {rel}")
        else:
            rc = 1
    return rc


def decrypt(paths: list[str] | None = None) -> int:
    """Decrypt in place so Obsidian and `kb ingest` can read the files.

    Decrypts anything currently ciphertext, including files the policy says
    should be plaintext -- that is how you unwind a mistaken encrypt.
    """
    rc = 0
    for rel, _want in resolve(paths):
        if not is_encrypted((config.ROOT / rel).read_bytes()):
            continue
        if _sops("-d", rel):
            print(f"  - decrypted  {rel}")
        else:
            rc = 1
    return rc


def _render_sops_config(kms: str | None = None) -> tuple[str, list[str]]:
    """Build .sops.yaml content from branches.yaml.

    Go's RE2 has no negative lookahead, so one recursive regex cannot express
    an `encrypted: false` override. Emitting a non-recursive rule per concrete
    directory makes sops itself reject the excluded subtrees, rather than
    leaning on this module to remember not to touch them.
    """
    path = config.SOPS_CONFIG_PATH
    if not kms:
        existing = yaml.safe_load(path.read_text()) if path.exists() else {}
        for rule in (existing or {}).get("creation_rules", []):
            if rule.get("kms"):
                kms = rule["kms"]
                break
    if not kms:
        raise SystemExit(f"no KMS ARN in {path.name}; pass --kms")
    # Never let real digits reach the tracked file, whatever --kms was given.
    kms = templatize(kms, "")

    dirs = sorted({rel.parent.as_posix() for rel, want in resolve() if want})
    lines = [
        "# GENERATED from tree/branches.yaml -- do not edit by hand.",
        "# Regenerate with `make secrets-config` after changing branches.yaml.",
        "#",
        "# One non-recursive rule per directory holding encrypted markdown, so",
        "# `encrypted: false` subtrees genuinely match no rule at all.",
        "creation_rules:",
    ]
    for d in dirs:
        lines.append(f"  - path_regex: ^{d}/[^/]+\\.md$")
        lines.append(f"    kms: {kms}")
    return "\n".join(lines) + "\n", dirs


def gen_sops_config(kms: str | None = None, check_only: bool = False) -> int:
    """Regenerate .sops.yaml from branches.yaml, or verify it is current."""
    path = config.SOPS_CONFIG_PATH
    content, dirs = _render_sops_config(kms)

    if check_only:
        if path.exists() and path.read_text() == content:
            return 0
        print(
            f"{path.name} is stale — branches.yaml adds or removes encrypted "
            f"directories.\nRun `make secrets-config` and commit the result."
        )
        return 1

    path.write_text(content)
    print(f"{path.name}: {len(dirs)} rule(s)")
    for d in dirs:
        print(f"  {d}/")
    return 0

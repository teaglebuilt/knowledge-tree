"""Encryption policy for the knowledge tree, declared in tree/branches.yaml.

branches.yaml mirrors the directory layout under tree/. A node may set
`encrypted: true|false`; that value applies to every file beneath it until a
deeper node overrides it. Anything undeclared defaults to plaintext.

    networking:
      branches:
        censorship:
          encrypted: true         # tree/networking/censorship/** is encrypted
          branches:
            hardware:
              encrypted: false    # ...except this subtree

sops does the actual crypto; this module decides *which* files it runs on and
keeps .sops.yaml generated from the same source of truth. `check()` never
shells out to sops, so the pre-commit hook works without AWS credentials.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import yaml

from . import config

# A sops binary-store file is JSON whose payload is a single ENC[...] blob.
_MARKER = b"ENC[AES256_GCM"


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
    return subprocess.run(
        ["sops", flag, "-i", rel.as_posix()], cwd=config.ROOT
    ).returncode == 0


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

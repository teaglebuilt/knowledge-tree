from __future__ import annotations

import datetime as _dt
import hashlib
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import NamedTuple
from urllib.parse import unquote

import yaml

from . import config
from .chunk import _FRONTMATTER

BINARY_SUFFIXES = {".epub", ".pdf"}
_ZLIB_NOISE = re.compile(
    r"\(?\s*(?:z-?librar(?:y)?\.?sk|1lib\.?sk|z-?lib\.?sk|z-librarysk|1libsk)\s*[,)]*",
    re.IGNORECASE,
)
BUCKETS = ("books", "pdf", "epub")


class Decl(NamedTuple):
    slug: str
    bucket: str
    domain: tuple[str, ...]
    declared: str

    @property
    def target(self) -> Path:
        tree_root = config.ROOT / config.KNOWLEDGE_DIRS[0].strip()
        return tree_root.joinpath(*self.domain, self.bucket, f"{self.slug}.md")

    @property
    def kind(self) -> str:
        return "book" if self.bucket in ("books", "epub") else "paper"

    def resolve(self) -> Path:
        p = Path(self.declared).expanduser()
        if p.is_absolute():
            return p
        if not config.SOURCE_VOLUME:
            raise ValueError(
                f"{self.declared!r} is relative but KNOWLEDGE_VOLUME_PATH is unset"
            )
        return config.SOURCE_VOLUME / p


def _is_bundle(p: Path) -> bool:
    """Books.app stores epubs exploded — a .epub directory, not a zip."""
    return p.suffix.lower() == ".epub" and p.is_dir()


def _feed(h, f: Path) -> None:
    with f.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    if _is_bundle(p):
        # hash (relpath, bytes) pairs so the digest is stable across machines
        for f in sorted(x for x in p.rglob("*") if x.is_file()):
            h.update(str(f.relative_to(p)).encode() + b"\0")
            _feed(h, f)
        return h.hexdigest()
    _feed(h, p)
    return h.hexdigest()


def _clean_title(stem: str) -> str:
    s = _ZLIB_NOISE.sub("", stem)
    s = re.sub(r"\(\s*\)", "", s)            # drop parens emptied by noise removal
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" -,·—") or stem          # keep balanced parens intact


def _slug(stem: str) -> str:
    s = _ZLIB_NOISE.sub("", stem)
    s = re.sub(r"[^\w\s-]", " ", s)          # drop punctuation
    s = re.sub(r"\s+", "-", s.strip().lower())
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:70].rstrip("-") or "source"


def _collapse_blank(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _epub_to_md(path: Path) -> str:
    import ebooklib
    from ebooklib import epub

    book = epub.read_epub(str(path))

    items = []
    try:
        for entry in book.spine:
            idref = entry[0] if isinstance(entry, (tuple, list)) else entry
            it = book.get_item_with_id(idref)
            if it is not None:
                items.append(it)
    except Exception:
        items = []
    if not items:
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    parts: list[str] = []
    for item in items:
        if getattr(item, "get_type", lambda: None)() != ebooklib.ITEM_DOCUMENT:
            continue
        text = _xhtml_to_md(item.get_content().decode("utf-8", errors="replace"))
        if text:
            parts.append(text)
    return _collapse_blank("\n\n".join(parts))


_XML_PROLOG = re.compile(r"<\?xml[^>]*\?>")
_EPUB_NS = {
    "c": "urn:oasis:names:tc:opendocument:xmlns:container",
    "opf": "http://www.idpf.org/2007/opf",
}


def _xhtml_to_md(html: str) -> str:
    from markdownify import markdownify as md

    html = _XML_PROLOG.sub("", html)  # drop XML prolog (else it leaks as text)
    return md(html, heading_style="ATX", strip=["script", "style"]).strip()


def _epub_dir_to_md(path: Path) -> str:
    """Read an unzipped epub: container.xml -> OPF -> manifest/spine order."""
    container = ET.parse(path / "META-INF" / "container.xml").getroot()
    rootfile = container.find("./c:rootfiles/c:rootfile", _EPUB_NS)
    if rootfile is None or not rootfile.get("full-path"):
        raise ValueError("no rootfile in META-INF/container.xml")

    opf_path = path / unquote(rootfile.get("full-path"))
    opf = ET.parse(opf_path).getroot()
    base = opf_path.parent

    href = {
        it.get("id"): it.get("href")
        for it in opf.findall("./opf:manifest/opf:item", _EPUB_NS)
        if it.get("id") and it.get("href")
    }

    parts: list[str] = []
    for ref in opf.findall("./opf:spine/opf:itemref", _EPUB_NS):
        target = href.get(ref.get("idref"))
        if not target:
            continue
        doc = base / unquote(target.split("#", 1)[0])
        if not doc.is_file():
            continue
        text = _xhtml_to_md(doc.read_text(encoding="utf-8", errors="replace"))
        if text:
            parts.append(text)
    return _collapse_blank("\n\n".join(parts))


def _pdf_to_md(path: Path) -> str:
    import pymupdf4llm

    try:
        pymupdf4llm.use_layout(False)
    except Exception:
        pass
    return _collapse_blank(pymupdf4llm.to_markdown(str(path), show_progress=False))


def _convert(path: Path) -> str:
    if path.suffix.lower() == ".epub":
        return _epub_dir_to_md(path) if path.is_dir() else _epub_to_md(path)
    return _pdf_to_md(path)


def _walk(node: dict, domain: tuple[str, ...], out: list[Decl]) -> None:
    if not isinstance(node, dict):
        return
    for bucket in BUCKETS:
        for slug, declared in (node.get(bucket) or {}).items():
            if declared:                       # '' means "known, path not filled in yet"
                out.append(Decl(str(slug), bucket, domain, str(declared)))
    for name, child in (node.get("branches") or {}).items():
        _walk(child or {}, (*domain, str(name)), out)


def declarations() -> list[Decl]:
    policy = yaml.safe_load(config.BRANCHES_PATH.read_text()) or {}
    out: list[Decl] = []
    for name, child in policy.items():
        _walk(child or {}, (str(name),), out)
    return sorted(out, key=lambda d: (d.domain, d.bucket, d.slug))


def _existing_source_hash(md_path: Path) -> str | None:
    if not md_path.exists():
        return None
    m = _FRONTMATTER.match(md_path.read_text(encoding="utf-8", errors="replace"))
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    h = fm.get("source_hash")
    return str(h) if h else None


def _frontmatter(decl: Decl, source: Path, source_hash: str) -> str:
    fm = {
        "title": _clean_title(source.stem),
        "source": decl.declared,               # portable: no absolute host path
        "source_type": decl.kind,
        "source_hash": source_hash,
        "tags": list(dict.fromkeys([*decl.domain, decl.kind])),
        "extracted": _dt.date.today().isoformat(),
    }
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"


def run(force: bool = False) -> dict:
    extracted = skipped = failed = missing = 0

    for decl in declarations():
        label = "/".join((*decl.domain, decl.bucket, decl.slug))
        try:
            src = decl.resolve()
        except ValueError as e:
            print(f"  ! {label}: {e}")
            failed += 1
            continue

        if not (src.is_file() or _is_bundle(src)):
            print(f"  ? {label}: source not found at {decl.declared}")
            missing += 1
            continue

        target = decl.target
        try:
            src_hash = _sha256(src)
        except OSError as e:  # unreadable mount, permissions, vanished file
            print(f"  ! {label}: cannot read source ({e.strerror})")
            failed += 1
            continue

        if not force and _existing_source_hash(target) == src_hash:
            skipped += 1
            continue

        try:
            body = _convert(src)
        except Exception as e:  # a bad file shouldn't sink the whole run
            print(f"  ! {label}: {type(e).__name__}: {e}")
            failed += 1
            continue

        if not body.strip():
            print(f"  ! {label}: empty extraction")
            failed += 1
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(_frontmatter(decl, src, src_hash) + body + "\n", encoding="utf-8")
        extracted += 1
        print(f"  + {target.relative_to(config.ROOT)}  <- {decl.declared}")

    print(
        f"\nextract: {extracted} converted, {skipped} unchanged, "
        f"{missing} missing, {failed} failed"
    )
    return {"extracted": extracted, "skipped": skipped,
            "missing": missing, "failed": failed}

from __future__ import annotations

import datetime as _dt
import hashlib
import re
from pathlib import Path

import yaml

from . import config
from .chunk import _FRONTMATTER

BINARY_SUFFIXES = {".epub", ".pdf"}

# z-library / 1lib download-site noise that litters the filenames.
_ZLIB_NOISE = re.compile(
    r"\(?\s*(?:z-?librar(?:y)?\.?sk|1lib\.?sk|z-?lib\.?sk|z-librarysk|1libsk)\s*[,)]*",
    re.IGNORECASE,
)


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
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


# --- converters (imports are lazy so the base pipeline needs no epub/pdf deps) --

def _epub_to_md(path: Path) -> str:
    import ebooklib
    from ebooklib import epub
    from markdownify import markdownify as md

    book = epub.read_epub(str(path))

    # Prefer spine order (reading order); fall back to document order.
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
        html = item.get_content().decode("utf-8", errors="replace")
        html = re.sub(r"<\?xml[^>]*\?>", "", html)  # drop XML prolog (else it leaks as text)
        text = md(html, heading_style="ATX", strip=["script", "style"]).strip()
        if text:
            parts.append(text)
    return _collapse_blank("\n\n".join(parts))


def _pdf_to_md(path: Path) -> str:
    import pymupdf4llm

    # These are born-digital text PDFs (books/papers), not scans. Disable the
    # per-page layout GNN + Tesseract OCR that newer pymupdf4llm enables by
    # default — it's minutes-slow and buys nothing here. The legacy text path
    # derives headings from font sizes, which the header-aware chunker wants.
    try:
        pymupdf4llm.use_layout(False)
    except Exception:
        pass
    return _collapse_blank(pymupdf4llm.to_markdown(str(path), show_progress=False))


def _convert(path: Path) -> str:
    if path.suffix.lower() == ".epub":
        return _epub_to_md(path)
    return _pdf_to_md(path)


# --- provenance / target mapping --------------------------------------------

def _tags_for(rel: Path, kind: str) -> list[str]:
    # rel = ai/books/x.epub -> domain segments minus the {books,pdf} bucket + file
    segs = [s for s in rel.parts[:-1] if s not in {"books", "pdf"}]
    return list(dict.fromkeys([*segs, kind]))  # dedup, keep order


def _target(source: Path) -> Path:
    rel = source.relative_to(config.SOURCES_DIR)
    tree_root = config.ROOT / config.KNOWLEDGE_DIRS[0].strip()
    return tree_root / rel.parent / f"{_slug(source.stem)}.md"


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


def _frontmatter(source: Path, source_hash: str) -> str:
    rel = source.relative_to(config.SOURCES_DIR)
    kind = "book" if (source.suffix.lower() == ".epub" or "books" in rel.parts) else "paper"
    fm = {
        "title": _clean_title(source.stem),
        "source": str(source.relative_to(config.ROOT)),
        "source_type": kind,
        "source_hash": source_hash,
        "tags": _tags_for(rel, kind),
        "extracted": _dt.date.today().isoformat(),
    }
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"


def _iter_binaries() -> list[Path]:
    if not config.SOURCES_DIR.exists():
        return []
    return sorted(
        p for p in config.SOURCES_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in BINARY_SUFFIXES
    )


def run(force: bool = False) -> dict:
    extracted = skipped = failed = 0
    for src in _iter_binaries():
        target = _target(src)
        src_hash = _sha256(src)

        if not force and _existing_source_hash(target) == src_hash:
            skipped += 1
            continue

        try:
            body = _convert(src)
        except Exception as e:  # a bad file shouldn't sink the whole run
            print(f"  ! {src.relative_to(config.SOURCES_DIR)}: {type(e).__name__}: {e}")
            failed += 1
            continue

        if not body.strip():
            print(f"  ! {src.relative_to(config.SOURCES_DIR)}: empty extraction")
            failed += 1
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(_frontmatter(src, src_hash) + body + "\n", encoding="utf-8")
        extracted += 1
        print(f"  + {target.relative_to(config.ROOT)}  <- {src.relative_to(config.SOURCES_DIR)}")

    print(
        f"\nextract: {extracted} converted, {skipped} unchanged, {failed} failed"
    )
    return {"extracted": extracted, "skipped": skipped, "failed": failed}

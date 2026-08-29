# Translation rules — edge cases

Read this when a file doesn't fit the straightforward cases in SKILL.md. The
governing question is always the same: **will a reader or the embedding index
see this text?** English if yes; untouched if it's a machine identifier.

## Mixed-language files

Common in technical corpora: English headings with source-language body, or
English body with source-language comments in code. Don't decide per file —
`lang_scan.py` reports per line and per category, so work from its output
rather than from an impression of the file.

A file scanning as `TRACE` (under 5% of lines) is usually one of:

- a stray untranslated bullet left over from an earlier partial pass
- a proper noun that has no English form — legitimate, see below
- a quoted error message or log line — see below

All three need a decision, not a blanket skip.

## Text that should stay in the source language

These are real, and forcing them to English makes the document worse:

- **Quoted terminal output, log lines, and error messages** produced by a
  localized tool. The reader needs to match what their screen shows. Translate
  the surrounding explanation; leave the quoted string, and add a bracketed
  English gloss after it if the meaning matters.
- **Proper nouns with no established English form** — a company, a product, a
  domestic standard. Use the official English name if one exists; otherwise
  transliterate and put the original in parentheses on first use.
- **Deliberate examples of source-language input** — a document about CJK text
  handling needs its CJK sample data intact.

Put these inside inline code or a fenced block where the format allows. That
moves them into a `WARN` category rather than `BLOCK`, so the gate surfaces
them for review instead of failing the file. If a genuine case can't be marked
that way, note it in the collection report so a human can confirm.

## Inline code containing source-language text

Ambiguous, and worth slowing down for. Two cases:

```
`kubectl get pods`          <- a command. Never translate.
`安全组`                     <- a term someone wrapped in backticks for emphasis.
                               Translate it, and consider whether it should be
                               bold rather than code.
```

Rule of thumb: if it would be typed into a terminal or appear in source code,
it's code. If it's a concept being named, it's prose that was formatted wrong.

## Code blocks

Translate comments. Leave everything else:

```yaml
# 传统方式：长期 Token 存储在 Secret 中      <- translate this line
apiVersion: v1
kind: Secret
metadata:
  name: default-token-xxx                  <- never touch
```

Two traps:

- **String literals that are user-facing.** A `message: "操作失败"` in an example
  config is a judgement call — translating it makes the example clearer,
  leaving it keeps the example faithful. Prefer translating, since these are
  illustrative rather than executable, and note it if the example is copied
  from a real system.
- **The info string.** ` ```yaml ` is a language identifier. `verify_translation.py`
  compares the full sequence of info strings before and after and fails on any
  change, because a translated info string breaks highlighting everywhere it
  appears.

## Heading anchors and tables of contents

The most common silent breakage. A TOC entry has two halves that behave
differently:

```
[概述](#1-概述)
 ^^^^  ^^^^^^^^
 prose  derived identifier
```

Translate the first, **regenerate** the second from the final English heading
using GitHub slug rules:

1. Strip markdown formatting (`**bold**`, `` `code` ``, links → their text)
2. Lowercase
3. Remove everything that isn't a word character, space, or hyphen
4. Spaces → hyphens
5. Duplicate slugs get `-1`, `-2`, … appended in document order

`mdlang.slugify()` implements exactly this, and `verify_translation.py` fails
the file if any anchor doesn't resolve to a heading that exists. Never
hand-guess an anchor; derive it.

## Wikilinks

```
[[domain-05-security/README.md|返回目录]]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^
  target — a path              alias — reader-visible
```

Translate the alias (`返回目录` → `Back to index`). The target is a path:

- If the referenced document is also being collected, **remap** the target to
  its new location under `tree/`
- If it isn't, the link will dangle. Flag it in the report rather than leaving
  a broken edge or deleting the link silently — a dangling wikilink is a valid
  marker of something worth collecting later, but only if someone knows it's there.

A bare `[[Kubernetes|Kubernetes]]` with no path refers to a tree note by title;
leave those alone unless the tree uses a different title.

## Frontmatter

Any human-readable value must be English, because `title`, `description` and
`summary` are what get embedded — untranslated values there degrade retrieval
for every future query, not just for the file they're in.

| Field kind | Examples | Action |
|---|---|---|
| Human-readable | `title`, `description`, `summary`, `abstract`, `audience`, `intent_queries` | Translate |
| Slug / enum | `tags`, `category`, `tier`, `difficulty`, `reading_level` | Leave |
| Date / version | `created`, `last_updated`, `k8s_versions` | Leave |
| Provenance | `source_path`, `original_language`, `authors` | Leave; add if missing |

Unknown keys default to *must be translated*. A corpus you haven't seen before
is far more likely to hide untranslated prose behind an unfamiliar key than to
hold deliberate source-language text there. To exempt a key, add it to
`preserve_frontmatter` in a config file and pass `--config`.

`trigger_keywords` and `keywords` are a mixed case: usually English technical
terms already, but any source-language entries in them should be translated,
since they exist to be matched against English queries.

## Tuning the checks for a different corpus

Everything is config-driven. Write a JSON file with only the keys you're
changing and pass `--config` to either script:

```json
{
  "preserve_frontmatter": ["tags", "category", "author_native_name"],
  "warn_categories": ["inline_code", "code", "code_comment"],
  "max_chunk_lines": 250,
  "line_delta_tolerance": 0.25
}
```

Useful adjustments:

- **`preserve_frontmatter`** — add keys that legitimately hold source-language
  values, such as a native-script author name.
- **Move `code_comment` from blocking to warning** for a corpus where code
  comments are quoted from external sources and shouldn't be rewritten.
- **Lower `max_chunk_lines`** if translations are drifting or losing content;
  smaller chunks are more reliable and cost more passes.
- **Raise `line_delta_tolerance`** for language pairs with large length
  differences. Chinese → English typically *grows* line count slightly when
  prose reflows; a large negative delta is still a red flag in any pair.

## When the gate keeps failing

Re-run the failing file through `lang_scan.py --show 30` to see exactly which
lines remain. In order of likelihood:

1. **Frontmatter was skipped.** The most common miss by a wide margin — the
   body reads as English and the file looks done.
2. **The tail of a long file.** Attention drifted near the end. Re-translate
   the last chunks specifically rather than the whole file.
3. **Code comments.** Easy to read past when scanning a fenced block.
4. **Anchors.** Headings became English and the TOC didn't follow.
5. **Structure counts off by a few.** Usually a table row or list item dropped
   at a chunk boundary — check the seams between chunks first.

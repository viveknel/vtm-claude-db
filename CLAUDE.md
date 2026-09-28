# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A searchable library of *Vampire: The Masquerade* sourcebooks, built with
Anthropic's `book-indexer` skill. Each book was read once from its source PDF
and turned into a self-contained bundle: a thematic Markdown index plus a
SQLite full-text-search database of paragraph-level chunks. A top-level
`library_index.md` synthesizes themes, agreements, and disagreements across
all 26 books. There is no application code here — this is a research/RAG
corpus, and the only "development" work is querying it, indexing new books
into it, or maintaining the synthesis layer.

Read `README.md` first — it explains the three game lines/editions this
library spans (V20, classic Revised Edition, classic Dark Ages) and five
things to know before treating any claim as consistent across books. Read
`library_index.md` for the actual cross-book synthesis (themes, points of
agreement, points of disagreement). Do not re-derive that context; it's
already written out in those two files.

## Commands

Requires only Python 3 stdlib (`sqlite3` built in — nothing to install).

Query a single book's chunk database:
```bash
python3 <book-folder>/scripts/query_chunks.py <book-folder>/book_chunks.db "search terms"
python3 <book-folder>/scripts/query_chunks.py <book-folder>/book_chunks.db --page 42
python3 <book-folder>/scripts/query_chunks.py <book-folder>/book_chunks.db --chapter "Chapter One"
python3 <book-folder>/scripts/query_chunks.py <book-folder>/book_chunks.db --range 40 45
```

Query multiple books' databases at once (results grouped and ranked per book,
not merged):
```bash
python3 scripts/query_library.py <book1>/book_chunks.db <book2>/book_chunks.db "search terms"
```

Full-text search (both scripts) is SQLite FTS5: supports phrase queries
(`"exact phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`),
and prefix matching (`term*`). FTS5 treats hyphens specially — a literal
hyphenated term (e.g. `Dur-An-Ki`) can error or return nothing; search a
distinctive un-hyphenated word instead (e.g. `ashipu`).

Every `query_chunks.py` is an identical copy across all 26 book folders — the
script itself never needs per-book editing.

## Architecture

```
<book-folder>/
├── book_index.md      ← thematic index (chapter summaries, themes, key
│                          terms) — small enough to read in full; answers
│                          most broad/thematic questions without querying
├── book_chunks.db      ← SQLite: chunks(chunk_id, page, chapter, text) +
│                          an FTS5 virtual table chunks_fts over it
├── README.md           ← per-book usage instructions
└── scripts/
    └── query_chunks.py ← thin CLI wrapper around the two tables above
```

Every book folder is fully self-contained and can be copied out and used on
its own. `dark-ages-inquisitor/` additionally has
`dark-ages-inquisitor-v20-conversion.md`, a fan analysis of running that
book's classic-line rules at a V20 table.

**Query pattern for answering questions:**
1. Broad/thematic question about one book → read that book's `book_index.md`
   in full.
2. Exact quote, figure, or page lookup → query that book's `book_chunks.db`
   via `query_chunks.py`. Cite the returned page number — it's the audit
   trail back to the source PDF.
3. Question spanning multiple books → read `library_index.md` first (it
   likely already covers the cross-reference), then use
   `scripts/query_library.py` against the specific books it names if exact
   wording is needed.
4. Only fall back to the original PDF (not stored in this repo) for things
   text extraction can't capture, like charts or layout — and only after
   both of the above fail.

**Mechanically dense chapters** (character creation, Discipline/power
catalogs, combat rules) are deliberately *not* summarized power-by-power in
`book_index.md` files — they're flagged as reference material, so go straight
to `book_chunks.db` for specific rules text.

## Editorial conventions to preserve when touching these files

- **Three separate canons, not one continuity**: V20 (2011-2016
  retrospective), classic Revised Edition (c. 1998-2002 modern-nights
  clanbooks), and classic Dark Ages (late 1990s/early 2000s). Don't silently
  merge facts across lines when answering a question or editing the index —
  note which line a claim comes from.
- **Deliberate in-book unreliability is a feature, not a gap.** Several books
  are narrated by biased in-character voices that contradict each other or
  themselves on purpose (e.g. `secrets-of-thaumaturgy-revised`'s narrator is
  later revealed to be a non-Tremere impersonator). Don't flatten this into a
  single "correct" account when summarizing.
- **`library_index.md` explicitly calls out unresolved disagreements**
  (Carthage's destruction, the Assamite blood curse's status, the
  Telyavic/Telyavelic Tremere's fate, Cappadocians/Giovanni active-vs-
  destroyed, Saulot's diablerie from both sides, etc.) rather than picking a
  winner. When adding new source material that touches these threads, add to
  the existing disagreement writeup instead of resolving it one way.
- Chunk databases and thematic indexes contain **summaries and short
  paragraph-level excerpts for search/citation, not full book text** — this
  library assumes the user already owns the source PDFs.

## Adding a new book to the library

Per `README.md`'s "Adding another related book later": bring the new PDF
plus `library_index.md` and each existing book's `book_index.md` (chunk
databases and original PDFs aren't needed again). Run the book-indexer
workflow on just the new book to produce its own `<slug>/` bundle
(`book_index.md`, `book_chunks.db`, `README.md`, `scripts/query_chunks.py`),
then update `library_index.md`'s synthesis sections — themes, points of
agreement/disagreement, and which product line/edition the new book belongs
to — to fold in what it adds, confirms, or complicates. Also add the new book
to `README.md`'s table and tree listing.

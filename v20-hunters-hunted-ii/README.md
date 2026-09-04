# The Hunters Hunted II — Searchable Index Bundle

This bundle lets Claude answer questions about this book without
re-reading the original PDF.

## Files

- **`book_index.md`** — thematic index: chapter summaries, themes, key
  terms, cross-cutting arguments. Read this first, in full, for any
  broad/thematic question.
- **`book_chunks.db`** — SQLite database of paragraph-level chunks with
  full-text search, for precise fact lookup, exact figures, or quote
  verification. Query it, don't load it in full.
- **`scripts/query_chunks.py`** — command-line helper for querying the DB.

Book: *The Hunters Hunted II* (V20, 2013) — 185 pages, indexed 2026-09-04.

## A note on page numbers

Page numbers throughout `book_index.md` and in `book_chunks.db`'s
`page` column are **PDF page numbers** (page 1 = the front cover), not
the book's own printed folio numbers. The printed number visible in
each page's footer runs **one lower** than the PDF page number used
here (e.g. PDF page 16 is footer-numbered "15"). `--page N` below
always means the PDF page number.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 142
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Six: Organizations and Resources"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`). Chapter names must match exactly as tagged; see
   `book_index.md`'s section headers for the exact strings (e.g.
   `"Chapter One: Alone in the Night"`, `"Here Goes Everything"`,
   `"Appendix: Template Characters"`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

## Part of a library

This book is one bundle in a larger *Vampire: The Masquerade* library.
If you were handed this folder alongside a top-level `library_index.md`
and other book folders, read that file first for cross-book synthesis
— it specifically connects this book to `dark-ages-inquisitor` (a
shared character, Leopold of Murnau) and to `v20-core` (this book
resolves an open mystery from that book's "Criminals" section). If
this bundle was provided standalone, those connections are also noted
in this file's own `book_index.md` under "Cross-cutting themes," for
reference even without the wider library on hand.

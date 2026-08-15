# Vampire: The Dark Ages 20th Anniversary Edition — Searchable Index Bundle

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

Book: Vampire: The Dark Ages 20th Anniversary Edition — 489 pages,
indexed 2026-08-15.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 412
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two: The Clans of Caine"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

Note: Chapters Four through Eight are primarily game mechanics
(character creation, Discipline power catalogs, combat/dice rules,
Storyteller advice) with little narrative content — `book_index.md`
flags these as such rather than padding out a power-by-power summary.
Query `book_chunks.db` directly for specific mechanical rules text.

## Part of a library

This book is part of a related four-book V20 library. See
`../library_index.md` at the top of the library directory for
cross-book synthesis and themes shared across all four books, and
`../scripts/query_library.py` to search across all four chunk databases
at once.

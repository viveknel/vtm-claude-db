# Rites of the Blood — Searchable Index Bundle

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

Book: Rites of the Blood (CCP hf/Onyx Path, 2014; V20 modern-nights line)
— 172 pages, indexed 2026-09-13.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 36
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two: The Sword of Caine"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

## Note on this book's relationship to continuity

This book's own introduction states it deliberately departs from strict
V20 metaplot in places (see `book_index.md`'s "Cross-cutting themes") —
most notably a surviving Telyavelic Tremere lineage that complicates
`v20-core`'s claim that bloodline was destroyed by the 16th century, and
a still-active True Black Hand (Tal'Mahe'Ra). Treat these as this book's
own take rather than assuming automatic consistency with other books in
this library, while still citing them as relevant alternate data points.

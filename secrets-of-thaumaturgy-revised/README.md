# Blood Magic: Secrets of Thaumaturgy — Searchable Index Bundle

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

Book: Blood Magic: Secrets of Thaumaturgy (White Wolf, 2000; classic
Revised Edition line) — 145 pages, indexed 2026-09-13.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 142
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two: The Rites of Blood"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

## Note on this book's narration

Every chapter is written by a different unreliable in-character narrator
(see `book_index.md`'s "Cross-cutting themes"), and Chapters One and Two
both carry a second layer of hostile in-universe editorial marginalia
contradicting the narrator in real time. When quoting a claim from this
book, note *which* narrator's voice it comes from — the book does not
present a single trustworthy account of Tremere history, and its own
byline reveals the first-person "Tremere" narrator of Chapters One-Two to
be a non-Tremere impersonator.

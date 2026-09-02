# V20 Dark Ages Companion — Searchable Index Bundle

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

Book: V20 Dark Ages Companion — 133 pages, indexed 2026-08-30.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 78
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Four: The Domain of Constantinople"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
   Page numbers in this database match the book's own printed page
   numbers, not the PDF's raw page index.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

Note: Chapters Seven ("Building a Domain") and Eight ("Art of the
Battlefield") are primarily game mechanics (feudal Background rules,
weapon/armor tables, a streamlined combat system) with limited
narrative content beyond their closing Clan Apocrypha sections —
`book_index.md` flags these as such rather than padding out a
rule-by-rule summary. Query `book_chunks.db` directly for specific
mechanical text (Background costs, Merit ratings, weapon stats, ritual
systems).

## Part of a library

This book is part of a related 21-book Vampire: The Masquerade/Dark
Ages library, and specifically belongs to the V20 line alongside
`v20-core`, `v20-lore-clans`, `v20-lore-bloodlines`, and `v20-dark-ages`
(this book is a domain-and-Apocrypha companion to `v20-dark-ages`
specifically). See `../library_index.md` at the top of the library
directory for cross-book synthesis and themes shared across the whole
collection, and `../scripts/query_library.py` to search across
multiple books' chunk databases at once.

# Blood Sacrifice: The Thaumaturgy Companion — Searchable Index Bundle

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

Book: Blood Sacrifice: The Thaumaturgy Companion (White Wolf, 2002;
classic Revised Edition line) — 101 pages, indexed 2026-09-15.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 40
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two: Dur-An-Ki — The Demon-Haunted World"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`). **Caveat:** FTS5 treats hyphens specially, so querying the
   literal term `Dur-An-Ki` can error out or return nothing — search a
   distinctive un-hyphenated word instead (e.g. `ashipu`, `Sadhana`,
   `wangateur`, `kalif`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

## Note on this book's relationship to other books in the library

This is the direct classic-era companion to `secrets-of-thaumaturgy-
revised` (also in this library, if bundled together) — it literally
patches an omission from that book (a missing Level Five Setite Sorcery
power) and is best read as its sequel. It is also the primary source
for much of `v20-rites-of-the-blood`'s Setite/Assamite Sorcery material
(Typhon's Brew, the Ladder of Heaven, kalif, Papa Zombie of the Samedi
bloodline all appear in both, in fuller form here). See `book_index.md`'s
"Cross-cutting themes" for a fuller account of these connections,
including a genuine, unresolved contradiction with `v20-rites-of-the-
blood` over whether the Assamite blood curse has ever been broken.

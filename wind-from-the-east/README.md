# Wind from the East — Searchable Index Bundle

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

Book: *Wind from the East* — 98 pages, indexed 2026-08-15.

**Important — this book spans two game lines and two libraries:**
This is a *Vampire: The Dark Ages* sourcebook (fitting alongside the
other Dark Ages material in this library), but roughly half its content
is *Kindred of the East* material (Wan Kuei, the Five August Courts,
etc.) covering the same Mongol-era setting from the Eastern vampire
side. The user has indicated they will also build a separate *Kindred
of the East* library, and this same book will be bundled into that
library too, since it's equally relevant there. When working from either
library, this bundle's `book_index.md` and `book_chunks.db` cover the
**entire book** (both the Dark Ages/Cainite material and the Kindred of
the East/Wan Kuei material) — there's no need to treat the two halves
separately or to re-derive Kindred of the East content from scratch;
it's already indexed here.

See the top-level `README.md` for how this fits into the broader
library structure.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 42
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter One: Empire of the World-Conqueror"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

# Dark Ages: Inquisitor — Searchable Index Bundle

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

Book: Dark Ages: Inquisitor — 245 pages, indexed 2026-08-25.

## Before you use this bundle: which edition it belongs to

This is a sourcebook for the **original, classic-line** *Vampire: The
Dark Ages* (2002) — it explicitly requires that book's core rules to
play — not for *Vampire: The Dark Ages 20th Anniversary Edition*
(`v20-dark-ages` in the wider library this bundle may be part of). It
uses the classic Storyteller System (Attributes/Abilities, Virtues 1-5,
Willpower) throughout, including a full set of book-specific mechanics
(Superior Virtues, Conviction, Piety, Callousness, Curses) that have no
direct V20 equivalent. If this bundle is being used inside the larger
`v20-lib` library, treat it as part of that library's **Classic Dark
Ages** line, alongside `clanbook-salubri` and `wind-from-the-east` —
related in setting and broad chronology to `v20-dark-ages`, but not a
rules-compatible or continuity-guaranteed match to it.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 142
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two: Call to Arms"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured — this is a
   heavily illustrated book, and interior art is not captured in the
   chunk database).

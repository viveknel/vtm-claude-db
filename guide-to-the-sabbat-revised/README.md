# Guide to the Sabbat (Revised) — Searchable Index Bundle

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

Book: *Guide to the Sabbat* (WW2303) — 226 pages, indexed 2026-09-29.

Note: this is a **classic Revised Edition** sourcebook (1999/2000), a
different game line/era from the V20 books and Dark Ages books elsewhere
in this library — see the top-level `README.md` for how the different game
lines/editions relate. It predates V20 by over a decade, but was checked
directly against `v20-core` and found to generally agree with it (Code of
Milan text, sect titles/hierarchy, Black Hand, several auctoritas ritae,
and the Salubri antitribu leader Adonai all correspond, with no outright
contradiction found) — see `book_index.md`'s edition note for specifics.
Treat this book's sect canon as generally holding unless a V20 book
explicitly contradicts something here; V20 takes priority in that case.

Page numbers in `book_chunks.db` are the PDF's own page index (1–226),
**not** the book's printed page footer numbers — the two run one apart
throughout (PDF page = printed footer number + 1, since the cover/fiction/
credits/TOC occupy unnumbered PDF pages 1–5 before the printed numbering
starts at "1" on PDF page 6). `book_index.md` cites PDF page numbers
throughout for consistency with the database.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 152
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Five: Codes of the Night"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured).

Note: Chapter Two's clan/bloodline catalog (pp. 52-81), Chapter Three's
character-creation walkthrough (pp. 82-97), Chapter Four's high-level
Discipline/Dark Thaumaturgy catalog (pp. 98-127), and the Appendix's NPC
stat blocks, ghoul/revenant templates and weapons tables (pp. 206-222) are
dense character-option/rules text rather than narrative — `book_index.md`
names what each section covers rather than describing every entry
individually. Query `book_chunks.db` directly for a specific clan's
Disciplines, an NPC's full Traits, or a weapon's exact stats.

## Part of a library

This book is part of a related library of *Vampire: The Masquerade*
sourcebooks. See `../library_index.md` at the top of the library directory
for cross-book synthesis and themes shared across the whole collection, and
`../scripts/query_library.py` to search across multiple books' chunk
databases at once.

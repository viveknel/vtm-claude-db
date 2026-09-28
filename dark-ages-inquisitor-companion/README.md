# Dark Ages: Inquisitor Companion — Searchable Index Bundle

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

Book: Dark Ages: Inquisitor Companion — 143 pages, indexed 2026-09-28.

## Before you use this bundle: it's a companion volume, not standalone

This book is a direct companion/expansion to `dark-ages-inquisitor`,
covering the same classic, pre-V20 *Vampire: The Dark Ages* shadow
Inquisition setting and requiring that book's core rules and cosmology.
It assumes — and doesn't reintroduce — the base book's premise, named
leadership (Cardinal Marzone, Gauthier de Dampiere, Aignen le Libraire,
Rodrigue de Navarre), and core mechanics (Superior Virtues, Conviction,
Piety, Callousness, Curses). For founding history, the Crimson
Curia/Cainite Heresy plot, or core mechanic definitions, check
`../dark-ages-inquisitor/book_index.md` first — this bundle covers what
that one doesn't: order-by-order recruitment/politics/chapter-houses, the
medieval Church's own structure and the Marzonian Rule governing mixed
cells, a large new catalog of Blessings/Curses/Merits/Flaws, rules for
un-empowered (non-order) inquisitor characters, and six new antagonists.
`book_index.md`'s own opening section spells this relationship out in
more detail, including the two threads (the Pale Brother; the Sicae Dei's
origin) that connect directly to the base book.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 118
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Three: The Ways of the Faithful"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
   Page numbers in this database match the book's own printed page
   numbers (verified against the printed footer on every page), not the
   PDF's raw page index (which runs 2 higher throughout, since the front
   and back cover images are unnumbered PDF pages 1-2).
4. Only fall back to the original PDF if both files fail to answer the
   question (e.g. the question is about a figure, chart, or visual
   layout that text extraction wouldn't have captured — this is a
   heavily illustrated book, and interior art is not captured in the
   chunk database).

Note: Chapter Three's Blessings/Curses/Merits-and-Flaws catalog entries
(pp. 98-127) are dense character-option text rather than narrative —
`book_index.md` names every new trait by category and page range rather
than describing each one individually. Query `book_chunks.db` directly
for a specific trait's full system text.

## Part of a library

This book is part of a related library of *Vampire: The Masquerade*/
*Dark Ages* sourcebooks, and belongs to that library's **Classic Dark
Ages** line alongside `clanbook-salubri`, `wind-from-the-east`, and its
own direct companion `dark-ages-inquisitor`. See `../library_index.md`
at the top of the library directory for cross-book synthesis and themes
shared across the whole collection, and `../scripts/query_library.py`
to search across multiple books' chunk databases at once.

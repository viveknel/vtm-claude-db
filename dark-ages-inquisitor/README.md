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
- **`dark-ages-inquisitor-v20-conversion.md`** — a fan conversion guide analyzing where this
  book's classic-line rules genuinely conflict with V20, where they
  already line up, and a practical house-rule package for running this
  book at a V20 Dark Ages table. Not part of the original source PDF;
  added separately as a derived analysis. See "About v20-conversion.md"
  below before treating it the same way as the other two files.

Book: Dark Ages: Inquisitor — 245 pages, indexed 2026-08-25.
`v20-conversion.md` added 2026-08-25 (same day, as a follow-on document).

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

The edition dependency above describes the *source material as written*.
`v20-conversion.md` (see next section) narrows that gap for anyone
actually wanting to run this book at a V20 table, but it doesn't change
what edition the original PDF targets — don't cite it as evidence that
the book is natively V20-compatible.

## About `v20-conversion.md`

This file is a derived fan analysis, not sourcebook content, and it
should be read differently from `book_index.md`:

- `book_index.md` and `book_chunks.db` describe **what the book says**.
  `v20-conversion.md` describes **how to run what the book says under a
  different rules edition** — it's a conversion/compatibility layer, not
  a summary of source content, and shouldn't be cited as if it were
  printed material from the original PDF.
- It corrects an initial pass that mis-compared this book's mortal-tier
  chargen numbers (Attributes 6/4/3, Abilities 11/7/4, 21 freebie points)
  against V20's *full-vampire* chargen budget. Checked instead against
  V20's own mortal/ghoul creation rules, the numbers already match
  exactly — that specific "incompatibility" doesn't exist. If a question
  touches chargen budgets, `v20-conversion.md`'s corrected analysis
  should be preferred over any earlier assumption that the two editions'
  point totals diverge.
- It identifies what *does* still need reconciling: the Superior
  Virtues/Conviction/Piety/Curses subsystem (a gap, since V20 has no
  hunter subsystem to compare it against), True Faith overlapping with
  Superior Virtues if both are left active, and Merits & Flaws catalog
  drift between the classic and V20 editions.
- Treat its proposed house rules (chargen budget usage, True Faith
  handling, Merits & Flaws verification step) as one workable option, not
  as settled rules text — it says as much itself ("a fan conversion, not
  an official one").
- If this bundle is used alongside `v20-dark-ages` for a question
  spanning both books, `v20-conversion.md` is the right file to check
  first for any rules-mechanical question; `book_index.md`'s existing
  "Crimson Curia" / "Cainite Heresy" cross-reference (see that file's
  "Cross-cutting themes" section) remains the right file for lore
  questions instead.

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
5. For a V20-compatibility or conversion question specifically, read
   `v20-conversion.md` directly rather than trying to derive a conversion
   from `book_index.md` alone — the analysis and correction work has
   already been done there.

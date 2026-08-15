# V20 Searchable Library

A searchable index of four *Vampire: The Masquerade 20th Anniversary
Edition* sourcebooks, built so that questions about the setting can be
answered without re-reading the original PDFs. Each book has its own
self-contained bundle (thematic index + full-text search database), and
a top-level synthesis layer ties themes together across all four.

Built with Anthropic's [book-indexer skill](https://github.com/anthropics/skills)
(Claude reads each source PDF once, extracts and tags its text, then
writes a thematic index and a queryable chunk database from it).

## What's in here

| Book | Folder | Pages |
|---|---|---|
| Vampire: The Masquerade 20th Anniversary Edition (core rulebook) | `v20-core/` | 528 |
| V20 Lore of the Clans | `v20-lore-clans/` | 309 |
| V20 Lore of the Bloodlines | `v20-lore-bloodlines/` | 103 |
| Vampire: The Dark Ages 20th Anniversary Edition | `v20-dark-ages/` | 489 |

```
.
├── README.md              ← you are here
├── library_index.md        ← cross-book synthesis: themes, agreements,
│                              disagreements, and how the four books relate
├── scripts/
│   └── query_library.py    ← search all four books' databases at once
├── v20-core/
│   ├── book_index.md       ← thematic index (read this for broad questions)
│   ├── book_chunks.db      ← full-text search database (query for exact facts/quotes)
│   ├── README.md           ← usage instructions for this book's bundle
│   └── scripts/
│       └── query_chunks.py ← search this book's database alone
├── v20-lore-clans/
│   └── (same four items)
├── v20-lore-bloodlines/
│   └── (same four items)
└── v20-dark-ages/
    └── (same four items)
```

Every book folder is a complete, self-contained bundle — any one of
them (e.g. `v20-lore-clans/`) can be copied out and used entirely on
its own, with its own README explaining how.

## Quick start

**Broad or thematic question about one book** ("what does Lore of the
Clans say about the Tremere?") — read that book's `book_index.md`
directly; it's small enough to load in full and answers most questions
without any querying.

**Exact quote, precise fact, or page-number lookup** — query that
book's chunk database:

```bash
python3 v20-lore-clans/scripts/query_chunks.py v20-lore-clans/book_chunks.db "Tremere pyramid hierarchy"
python3 v20-lore-clans/scripts/query_chunks.py v20-lore-clans/book_chunks.db --page 212
python3 v20-lore-clans/scripts/query_chunks.py v20-lore-clans/book_chunks.db --chapter "The Tremere"
```

**Question that spans multiple books** ("how do the Dark Ages and
modern books describe the Salubri differently?") — read
`library_index.md` first, then search across books at once if you need
exact wording:

```bash
python3 scripts/query_library.py v20-lore-clans/book_chunks.db v20-dark-ages/book_chunks.db "Saulot"
```

Full-text search (both scripts) supports phrase queries (`"exact
phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`),
and prefix matching (`term*`).

## Requirements

Python 3 with the standard library only (`sqlite3` is built in — no
extra packages to install).

## Notes on scope

- These bundles contain **summaries and short paragraph-level
  excerpts** for search/citation purposes, not the original books'
  full text. They're a research aid for someone who already owns the
  source PDFs, not a substitute for them.
- Mechanically dense chapters (character creation, Discipline/power
  catalogs, combat rules) are noted in each `book_index.md` as
  reference material rather than summarized power-by-power — query the
  relevant `book_chunks.db` directly for specific rules text.
- Where the four books genuinely disagree with each other (e.g.
  Carthage's portrayal, or the Cappadocians' status as an active vs.
  destroyed Clan), `library_index.md` calls this out explicitly rather
  than silently picking one version — see its "Points of disagreement
  or tension" section.

## Adding another related book later

Bring the new PDF plus this repo's `library_index.md` and each existing
book's `book_index.md` (chunk databases and original PDFs aren't
needed again). Run the indexing workflow on just the new book to
produce its own `<slug>/` bundle, then update `library_index.md`'s
synthesis sections to fold in what the new book adds, confirms, or
complicates.

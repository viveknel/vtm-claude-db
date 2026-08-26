# Vampire: The Masquerade Searchable Library

A searchable index of 20 *Vampire: The Masquerade* sourcebooks, spanning
three product lines/editions, built so that questions about the setting
can be answered without re-reading the original PDFs. Each book has its
own self-contained bundle (thematic index + full-text search database),
and a top-level synthesis layer ties themes together across all of them.

Built with Anthropic's [book-indexer skill](https://github.com/anthropics/skills)
(Claude reads each source PDF once, extracts and tags its text, then
writes a thematic index and a queryable chunk database from it).

## Three things to know before using this library

**1. This library spans three different editions/product lines, not one
continuity.** See `library_index.md`'s "A note on editions and game
lines" section for the full explanation, but briefly:
- **V20** (`v20-core`, `v20-lore-clans`, `v20-lore-bloodlines`,
  `v20-dark-ages`) — the 2011-2015 *20th Anniversary Edition*, a later
  retrospective/updated presentation of the game.
- **Classic Revised Edition** (the 13 `clanbook-*-revised` books) — the
  *original* modern-nights clanbook line, published c. 1998-2000,
  predating V20 by over a decade. V20's modern-nights material is a
  later, edited retelling of much of what these books cover — expect
  broad agreement on core clan identity but real differences in
  specific historical claims and details.
- **Classic Dark Ages** (`clanbook-salubri`, `wind-from-the-east`,
  `dark-ages-inquisitor`) — the *original*, pre-V20 Dark Ages product
  line, also from the late 1990s/early 2000s. `v20-dark-ages` is a
  later, updated edition of this same period-setting line, not a direct
  reprint.

Treat these as related but separate canons. When a question could be
answered from more than one line, check which one the person actually
wants (or note the split) rather than silently picking one.

**2. `wind-from-the-east` is a crossover book relevant to a second,
separate library.** It's a *Vampire: The Dark Ages* sourcebook (so it
belongs here), but roughly half its content is *Kindred of the East*
material (Wan Kuei, the Five August Courts) covering the same Mongol-era
setting from the Eastern-vampire side. The person building this library
has said they'll also build a separate Kindred of the East library, and
this same book will be bundled there too, since it's equally relevant to
both. Its `book_index.md` and `book_chunks.db` here cover the entire
book (both halves) — no need to treat the two halves separately or to
look elsewhere for its Kindred of the East content.

**3. `dark-ages-inquisitor` is a rules-dependent hunters'-side book, not
a Kindred sourcebook — but its bundle also includes a V20 conversion
guide.** Every other book in this library describes the setting from a
vampire's-eye view. `dark-ages-inquisitor` is the shadow Inquisition's
own sourcebook — the mortal hunters who fight Cainites — and it
explicitly requires the *original* *Dark Ages: Vampire* core rulebook to
play (classic Storyteller System, not V20's revised traits). Don't
assume its game mechanics are compatible with `v20-dark-ages` without
checking; and expect its narrators to often describe vampires without
fully recognizing them as such — that's a deliberate feature of the book,
not a gap in this bundle's indexing.

That "don't assume compatible" caution is about the source PDF as
written, not the last word on the subject: the `dark-ages-inquisitor`
bundle also contains `v20-conversion.md`, a fan analysis that works out
specifically where this book's rules do and don't line up with V20 and
gives a house-rule package for running it at a V20 table. Its headline
finding is that the gap is smaller than the disclaimer suggests — core
mechanics and this book's mortal-tier chargen numbers already match V20
(against V20's own mortal/ghoul rules, not the full-vampire budget); the
real gaps are the book's own Superior Virtues/Conviction/Piety/Curses
subsystem (nothing in V20 to check it against), True Faith overlap, and
Merits & Flaws catalog drift. For any V20-compatibility question, go to
that file rather than this README's summary.

## What's in here

**V20 line:**

| Book | Folder | Pages |
|---|---|---|
| Vampire: The Masquerade 20th Anniversary Edition (core rulebook) | `v20-core/` | 528 |
| V20 Lore of the Clans | `v20-lore-clans/` | 309 |
| V20 Lore of the Bloodlines | `v20-lore-bloodlines/` | 103 |
| Vampire: The Dark Ages 20th Anniversary Edition | `v20-dark-ages/` | 489 |

**Classic Dark Ages line:**

| Book | Folder | Pages |
|---|---|---|
| Clanbook: Salubri | `clanbook-salubri/` | 74 |
| Wind from the East (Dark Ages / Kindred of the East crossover) | `wind-from-the-east/` | 98 |
| Dark Ages: Inquisitor (hunters'-side sourcebook, classic-line rules; bundle also includes a V20 conversion guide) | `dark-ages-inquisitor/` | 245 |

**Classic Revised Edition line:**

| Book | Folder | Pages |
|---|---|---|
| Clanbook: Brujah | `clanbook-brujah-revised/` | 106 |
| Clanbook: Gangrel | `clanbook-gangrel-revised/` | 106 |
| Clanbook: Malkavian | `clanbook-malkavian-revised/` | 106 |
| Clanbook: Nosferatu | `clanbook-nosferatu-revised/` | 106 |
| Clanbook: Toreador | `clanbook-toreador-revised/` | 106 |
| Clanbook: Tremere | `clanbook-tremere-revised/` | 106 |
| Clanbook: Ventrue | `clanbook-ventrue-revised/` | 106 |
| Clanbook: Assamite | `clanbook-assamite-revised/` | 106 |
| Clanbook: Followers of Set | `clanbook-followers-of-set-revised/` | 106 |
| Clanbook: Tzimisce | `clanbook-tzimisce-revised/` | 106 |
| Clanbook: Lasombra | `clanbook-lasombra-revised/` | 106 |
| Clanbook: Giovanni | `clanbook-giovanni-revised/` | 106 |
| Clanbook: Ravnos | `clanbook-ravnos-revised/` | 106 |

```
.
├── README.md                ← you are here
├── library_index.md          ← cross-book synthesis: editions, themes,
│                                agreements, and disagreements across all 20 books
├── scripts/
│   └── query_library.py      ← search several books' databases at once
├── v20-core/
│   ├── book_index.md         ← thematic index (read this for broad questions)
│   ├── book_chunks.db        ← full-text search database (query for exact facts/quotes)
│   ├── README.md             ← usage instructions for this book's bundle
│   └── scripts/
│       └── query_chunks.py   ← search this book's database alone
├── v20-lore-clans/
├── v20-lore-bloodlines/
├── v20-dark-ages/
├── clanbook-salubri/
├── wind-from-the-east/
├── dark-ages-inquisitor/
├── clanbook-brujah-revised/
├── clanbook-gangrel-revised/
├── clanbook-malkavian-revised/
├── clanbook-nosferatu-revised/
├── clanbook-toreador-revised/
├── clanbook-tremere-revised/
├── clanbook-ventrue-revised/
├── clanbook-assamite-revised/
├── clanbook-followers-of-set-revised/
├── clanbook-tzimisce-revised/
├── clanbook-lasombra-revised/
├── clanbook-giovanni-revised/
└── clanbook-ravnos-revised/
    (each of the above folders has the same four items as v20-core/,
    except dark-ages-inquisitor/, which has a fifth: v20-conversion.md —
    see that folder's own README.md)
```

Every book folder is a complete, self-contained bundle — any one of
them (e.g. `clanbook-tremere-revised/`) can be copied out and used
entirely on its own, with its own README explaining how.

## Quick start

**Broad or thematic question about one book** ("what does Clanbook:
Tremere say about the Council of Seven?") — read that book's
`book_index.md` directly; it's small enough to load in full and answers
most questions without any querying.

**Exact quote, precise fact, or page-number lookup** — query that
book's chunk database:

```bash
python3 clanbook-tremere-revised/scripts/query_chunks.py clanbook-tremere-revised/book_chunks.db "Council of Seven"
python3 clanbook-tremere-revised/scripts/query_chunks.py clanbook-tremere-revised/book_chunks.db --page 42
python3 clanbook-tremere-revised/scripts/query_chunks.py clanbook-tremere-revised/book_chunks.db --chapter "Chapter One: The Price of Immortality"
```

**Question that spans multiple books** ("how do the Dark Ages and
modern books describe the Salubri differently?", "how did the Tremere
and the Salubri each describe Saulot's diablerie?") — read
`library_index.md` first, then search across the specific books it
names if you need exact wording:

```bash
python3 scripts/query_library.py clanbook-salubri/book_chunks.db clanbook-tremere-revised/book_chunks.db "Saulot diablerie"
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
- Where books genuinely disagree with each other (e.g. Carthage's
  portrayal, the Cappadocians'/Salubri's status as active vs. destroyed
  across timelines, or the Tremere's and Salubri's opposing accounts of
  Saulot's diablerie), `library_index.md` calls this out explicitly
  rather than silently picking one version — see its "Points of
  disagreement or tension" section.
- See "Three things to know before using this library" above before
  treating any claim as consistent across the whole collection.

## Adding another related book later

Bring the new PDF plus this repo's `library_index.md` and each existing
book's `book_index.md` (chunk databases and original PDFs aren't
needed again). Run the indexing workflow on just the new book to
produce its own `<slug>/` bundle, then update `library_index.md`'s
synthesis sections to fold in what the new book adds, confirms, or
complicates — including, if relevant, which product line/edition it
belongs to.

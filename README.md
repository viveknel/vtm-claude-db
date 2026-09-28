# Vampire: The Masquerade Searchable Library

A searchable index of 27 *Vampire: The Masquerade* sourcebooks, spanning
three product lines/editions, built so that questions about the setting
can be answered without re-reading the original PDFs. Each book has its
own self-contained bundle (thematic index + full-text search database),
and a top-level synthesis layer ties themes together across all of them.

Built with Anthropic's [book-indexer skill](https://github.com/anthropics/skills)
(Claude reads each source PDF once, extracts and tags its text, then
writes a thematic index and a queryable chunk database from it).

## Five things to know before using this library

**1. This library spans three different editions/product lines, not one
continuity.** See `library_index.md`'s "A note on editions and game
lines" section for the full explanation, but briefly:
- **V20** (`v20-core`, `v20-lore-clans`, `v20-lore-bloodlines`,
  `v20-dark-ages`, `v20-dark-ages-companion`, `v20-hunters-hunted-ii`,
  `v20-tome-of-secrets`, `v20-rites-of-the-blood`) —
  the 2011-2016 *20th Anniversary Edition*, a later retrospective/updated
  presentation of the game. `v20-dark-ages-companion` and
  `v20-tome-of-secrets` are both direct expansions of `v20-dark-ages`
  (domains/Storyteller toolkit for the former, blood-sorcery material
  and connected serial fiction for the latter), not independent setting
  books. `v20-hunters-hunted-ii` is the modern-nights mortal-hunters
  sourcebook — see point 4 below for its direct link to
  `dark-ages-inquisitor`. `v20-rites-of-the-blood` is a modern-nights
  blood-magic sourcebook whose own introduction admits it deliberately
  departs from strict metaplot continuity in places — see point 5 below.
- **Classic Revised Edition** (the 13 `clanbook-*-revised` books, plus
  the Discipline-focused `secrets-of-thaumaturgy-revised` and its direct
  sequel `blood-sacrifice-revised`) — the *original* modern-nights
  clanbook line, published c. 1998-2002, predating V20 by over a decade.
  V20's modern-nights material is a later, edited retelling of much of
  what these books cover — expect broad agreement on core clan identity
  but real differences in specific historical claims and details.
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
guide, and it has its own direct companion volume.** Every other book in
this library describes the setting from a vampire's-eye view.
`dark-ages-inquisitor` is the shadow Inquisition's own sourcebook — the
mortal hunters who fight Cainites — and it explicitly requires the
*original* *Dark Ages: Vampire* core rulebook to play (classic
Storyteller System, not V20's revised traits). Don't assume its game
mechanics are compatible with `v20-dark-ages` without checking; and
expect its narrators to often describe vampires without fully
recognizing them as such — that's a deliberate feature of the book, not
a gap in this bundle's indexing.

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

`dark-ages-inquisitor-companion/` (2004) is a separate bundle that
expands directly on `dark-ages-inquisitor` — same classic-line rules and
setting, no new edition dependency — covering the five orders' internal
politics/recruitment/chapter-houses in depth, the Marzonian Rule
governing mixed cells, a large new catalog of Blessings/Curses/Merits &
Flaws, rules for non-order "outside the orders" inquisitor characters,
and six new antagonists, two of which (the Pale Brother; the Sicae Dei's
founding) tie directly into plot threads the base book leaves open. Read
it after `dark-ages-inquisitor`, not standalone — its own README and
`book_index.md` assume the base book's premise and named leadership
rather than re-explaining them.

**4. `v20-hunters-hunted-ii` is this library's other hunters'-side
book, and it connects back to `dark-ages-inquisitor` and `v20-core` in
ways worth knowing before treating it as a standalone modern-nights
sourcebook.** Like `dark-ages-inquisitor`, it's written from the
mortal-hunter vantage point rather than the Kindred's. Two specific
connections matter:
- Its central hunter organization, the Society of Leopold, reveres a
  founding martyr named "Leopold of Murnau" — almost certainly the same
  **Leopold von Murnau** who appears as a living, struggling 13th-century
  inquisitor in `dark-ages-inquisitor` (whose own book leaves his fate
  open). Treat the two as one figure across eras, not a coincidental
  name reuse — see `library_index.md`'s "The modern view from the
  other side" section.
- Its Chapter Six **resolves an open mystery from `v20-core`**: that
  book's brief "Criminals" sidebar mentions unidentified Caitiff
  informants inciting American gang wars against vampire-run crime and
  calls it "an open mystery." `v20-hunters-hunted-ii` names them (the
  Kerberos coterie) and tells the full story. If a question concerns
  that mystery, this book is the answer, not a separate account.

**5. The four blood-magic books (`secrets-of-thaumaturgy-revised`,
`blood-sacrifice-revised`, `v20-tome-of-secrets`, `v20-rites-of-the-
blood`) add rich cross-book material, but two things are worth knowing
before treating their claims as settled.** First, `v20-rites-of-the-
blood` is an unusually explicit case of intentional non-continuity. Its
own introduction states it deliberately "moves around the metaplot" to
explore its themes, citing the Tremere antitribu and the True Black
Hand's continued existence as examples. Concretely: this library's
`v20-core` bundle states the Telyavic Tremere bloodline's remnants were
"reported destroyed by the 16th century," but `v20-rites-of-the-blood`
depicts a hidden Telyavelic Tremere lineage surviving into the modern
nights within the Sabbat — and `v20-core`'s own antitribu material sits
ambiguously between the two, describing Tremere antitribu who still
"out" hidden Telyavic infiltrators today. Don't silently resolve this in
either direction; present it as an open question across the three
sources — see `library_index.md`'s "The Telyavic/Telyavelic Tremere"
section for the full three-way read. The same caution applies more
mildly to `secrets-of-thaumaturgy-revised`, whose every chapter is
narrated by a different unreliable in-character voice (one later
revealed, by its own byline, to be a non-Tremere impersonator) — see
that book's own README for how to handle quotes from it. Second, the
Assamite blood curse's status is a genuine four-way unresolved question
across this whole group of books — `secrets-of-thaumaturgy-revised` and
`blood-sacrifice-revised` (2000 and 2002) both treat it as already
broken, while `v20-lore-clans` (three competing explanations) and
`v20-rites-of-the-blood` (still unbroken, actively being fought over)
give two more, later positions. See `library_index.md`'s "The Assamite
blood curse" section.

## What's in here

**V20 line:**

| Book | Folder | Pages |
|---|---|---|
| Vampire: The Masquerade 20th Anniversary Edition (core rulebook) | `v20-core/` | 528 |
| V20 Lore of the Clans | `v20-lore-clans/` | 309 |
| V20 Lore of the Bloodlines | `v20-lore-bloodlines/` | 103 |
| Vampire: The Dark Ages 20th Anniversary Edition | `v20-dark-ages/` | 489 |
| V20 Dark Ages Companion (companion to the above — six domains, Storyteller toolkit) | `v20-dark-ages-companion/` | 133 |
| The Hunters Hunted II (modern-nights mortal hunters — companion in spirit to `dark-ages-inquisitor`) | `v20-hunters-hunted-ii/` | 185 |
| Tome of Secrets (companion to `v20-dark-ages` — blood sorcery, feudalism/warfare toolkit, connected serial fiction) | `v20-tome-of-secrets/` | 119 |
| Rites of the Blood (modern-nights blood magic across every faction; see point 5 above on its intentional metaplot divergence) | `v20-rites-of-the-blood/` | 172 |

**Classic Dark Ages line:**

| Book | Folder | Pages |
|---|---|---|
| Clanbook: Salubri | `clanbook-salubri/` | 74 |
| Wind from the East (Dark Ages / Kindred of the East crossover) | `wind-from-the-east/` | 98 |
| Dark Ages: Inquisitor (hunters'-side sourcebook, classic-line rules; bundle also includes a V20 conversion guide) | `dark-ages-inquisitor/` | 245 |
| Dark Ages: Inquisitor Companion (direct companion to the above — order-by-order detail, new Blessings/Curses/Merits & Flaws, new antagonists) | `dark-ages-inquisitor-companion/` | 143 |

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
| Blood Magic: Secrets of Thaumaturgy | `secrets-of-thaumaturgy-revised/` | 145 |
| Blood Sacrifice: The Thaumaturgy Companion (direct sequel to the above) | `blood-sacrifice-revised/` | 101 |

```
.
├── README.md                ← you are here
├── library_index.md          ← cross-book synthesis: editions, themes,
│                                agreements, and disagreements across all 27 books
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
├── v20-dark-ages-companion/
├── v20-hunters-hunted-ii/
├── v20-tome-of-secrets/
├── v20-rites-of-the-blood/
├── clanbook-salubri/
├── wind-from-the-east/
├── dark-ages-inquisitor/
├── dark-ages-inquisitor-companion/
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
├── clanbook-ravnos-revised/
├── secrets-of-thaumaturgy-revised/
└── blood-sacrifice-revised/
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
```bash
python3 scripts/query_library.py dark-ages-inquisitor/book_chunks.db v20-hunters-hunted-ii/book_chunks.db "Leopold"
```
```bash
python3 scripts/query_library.py dark-ages-inquisitor/book_chunks.db dark-ages-inquisitor-companion/book_chunks.db "Pale Brother"
```
```bash
python3 scripts/query_library.py v20-core/book_chunks.db v20-rites-of-the-blood/book_chunks.db "Telyav"
```
```bash
python3 scripts/query_library.py blood-sacrifice-revised/book_chunks.db v20-rites-of-the-blood/book_chunks.db "wangateur"
```

Full-text search (both scripts) supports phrase queries (`"exact
phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`),
and prefix matching (`term*`). Note: FTS5 treats hyphens specially, so
querying a literal hyphenated term like `Dur-An-Ki` can error out or
return nothing — search a distinctive un-hyphenated word instead (e.g.
`ashipu`).

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
  across timelines, the Tremere's and Salubri's opposing accounts of
  Saulot's diablerie, the Telyavic/Telyavelic Tremere's fate, or the
  Assamite blood curse's status), `library_index.md` calls this out
  explicitly rather than silently picking one version — see its "Points
  of disagreement or tension" section.
- See "Five things to know before using this library" above before
  treating any claim as consistent across the whole collection.

## Adding another related book later

Bring the new PDF plus this repo's `library_index.md` and each existing
book's `book_index.md` (chunk databases and original PDFs aren't
needed again). Run the indexing workflow on just the new book to
produce its own `<slug>/` bundle, then update `library_index.md`'s
synthesis sections to fold in what the new book adds, confirms, or
complicates — including, if relevant, which product line/edition it
belongs to.

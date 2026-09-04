# Vampire: The Masquerade — Cross-Book Index

## Books in this collection

**V20 line** (20th Anniversary Edition, modern retrospective/reboot, published ~2011-2015):
- `v20-core/` — Vampire: The Masquerade 20th Anniversary Edition (core rulebook), 528 pages
- `v20-lore-clans/` — V20 Lore of the Clans, 309 pages
- `v20-lore-bloodlines/` — V20 Lore of the Bloodlines, 103 pages
- `v20-dark-ages/` — Vampire: The Dark Ages 20th Anniversary Edition, 489 pages
- `v20-dark-ages-companion/` — V20 Dark Ages Companion (six domain profiles —
  Rome, Bath, Bjarkarey, Constantinople, Mogadishu, Mangaluru — plus
  Storyteller domain-building and combat rules; a direct companion to
  `v20-dark-ages`, not a standalone setting book), 133 pages
- `v20-hunters-hunted-ii/` — The Hunters Hunted II (modern-nights mortal
  hunters: character creation, tactics, Numina powers, and detailed
  hunter-organization write-ups — the modern-day counterpart to
  `dark-ages-inquisitor`'s classic-line hunters), 185 pages

**Classic Dark Ages line** (original, pre-V20, published ~1996-2002):
- `clanbook-salubri/` — Clanbook: Salubri, 74 pages
- `wind-from-the-east/` — Wind from the East (Dark Ages/Mongol-era supplement, also relevant to Kindred of the East — see its own README), 98 pages
- `dark-ages-inquisitor/` — Dark Ages: Inquisitor (a *hunters'*-side sourcebook — the shadow Inquisition that fights Cainites — for the original, pre-V20 *Dark Ages: Vampire*, which it explicitly requires to play), 245 pages. Bundle also includes `dark-ages-inquisitor-v20-conversion.md`, a fan analysis/house-rule package for running this book at a V20 table — see "A note on editions and game lines" below and that bundle's own README.

**Classic Revised Edition line** (original, pre-V20, modern nights, published ~1998-2000):
- `clanbook-brujah-revised/`, `clanbook-gangrel-revised/`, `clanbook-malkavian-revised/`,
  `clanbook-nosferatu-revised/`, `clanbook-toreador-revised/`, `clanbook-tremere-revised/`,
  `clanbook-ventrue-revised/`, `clanbook-assamite-revised/`, `clanbook-followers-of-set-revised/`,
  `clanbook-tzimisce-revised/`, `clanbook-lasombra-revised/`, `clanbook-giovanni-revised/`,
  `clanbook-ravnos-revised/` — 106 pages each

## How to use this file
This file synthesizes themes across all 21 books above. For details on
any single book, read that book's own `book_index.md` in its
subdirectory. For exact quotes/facts, query that book's `book_chunks.db`,
or use `scripts/query_library.py` to search across several databases at
once (see usage below).

## A note on editions and game lines — read this before cross-referencing

This library spans **three distinct editions/product lines** of
*Vampire: The Masquerade*, and they are not simply the same continuity
at different dates — they're separate publication lines with their own
internal consistency, written years apart by different (though
overlapping) teams. Treat material from different lines as separate
canons that happen to share cosmology, not as strictly compatible facts.

1. **V20** (`v20-core`, `v20-lore-clans`, `v20-lore-bloodlines`,
   `v20-dark-ages`, `v20-dark-ages-companion`, `v20-hunters-hunted-ii`)
   is a 2011-2015 *20th Anniversary retrospective* line: a consolidated,
   updated re-presentation of the game aimed at both new and returning
   players, published as two internally consistent sub-pairs — one for
   "modern nights" (present day) and one for the Dark Ages period (1242
   CE), each roughly 750 years apart in fictional time but written and
   edited as a matched pair. `v20-dark-ages-companion` is not a third,
   independent sub-pair member — it's a direct expansion of
   `v20-dark-ages` specifically (six new domains plus Storyteller
   toolkit), sharing that book's exact setting-date and cosmology
   rather than adding a new one. `v20-hunters-hunted-ii` sits within the
   modern-nights sub-pair (it expands directly on `v20-core`'s brief
   "Witch-Hunters" section) but flips perspective to the mortals hunting
   Kindred rather than the Kindred themselves — the modern-nights
   counterpart to the classic-line `dark-ages-inquisitor`, discussed
   further below.
2. **The classic Revised Edition line** (`clanbook-brujah-revised`
   through `clanbook-ravnos-revised`, 13 books) is the *original*
   modern-nights clanbook series, published c. 1998-2000, predating V20
   by over a decade. These are the primary-source books V20's modern-
   nights material was later distilled and updated from — expect V20 to
   be broadly consistent with them at the level of core clan identity,
   but with real differences in specific historical claims, elder
   names, and plot details (V20 openly rewrites, prunes, and sometimes
   contradicts classic-line specifics; it does not claim to be a
   word-for-word update).
3. **The classic Dark Ages line** (`clanbook-salubri`,
   `wind-from-the-east`, `dark-ages-inquisitor`) is the *original*,
   pre-V20 Dark Ages product line, also from the late 1990s/early 2000s.
   `v20-dark-ages` is explicitly a later, updated edition of this same
   period-setting line — but it is not a direct reprint. Where
   `clanbook-salubri` or `wind-from-the-east` and `v20-dark-ages`
   describe the same character, event, or Clan, expect broad agreement
   on the big picture and real divergence on detail; neither supersedes
   the other for research purposes, and both are worth checking.
   `dark-ages-inquisitor` carries the strongest edition dependency of
   the three: it explicitly states it is not a complete game and
   requires the *original* *Dark Ages: Vampire* core rulebook to play,
   using that book's classic Storyteller System rather than V20's
   revised traits. Treat it as tied to the classic-line rules, not to
   `v20-dark-ages`, even though both cover the same broad historical
   period.

   That said, the practical gap for anyone wanting to *run* the book at
   a V20 table is narrower than the disclaimer implies. The
   `dark-ages-inquisitor` bundle includes `v20-conversion.md`, which
   finds that core resolution mechanics (dice pools, difficulty 6,
   Virtues, Willpower, Health) and this book's mortal-tier character
   creation numbers already match V20 as written — the chargen figures
   line up with V20's own ghoul/mortal creation rules, not the
   higher full-vampire budget some might expect to compare them against.
   What doesn't carry over cleanly is this book's own hunter-specific
   subsystem (Superior Virtues, Conviction, Piety, Curses, Cocytus),
   which has no V20 counterpart to reconcile against and has to be
   imported as-is, plus True Faith handling and some Merits & Flaws
   catalog drift. For any question specifically about running this book
   under V20 rules, prefer `v20-conversion.md` over inferring an answer
   from the edition-dependency framing here.

**Practical implication:** if a question is about "the Salubri," "the
Tremere," or any other topic covered by both a classic-line book and a
V20 book, check which line's portrayal the person actually wants (or
present both, flagged by line) rather than silently picking one. The
"Points of disagreement or tension" section below calls out the sharpest
examples.

Within each line, all books describing the same setting-time are
substantially consistent with one another, though (especially in the
classic-line clanbooks) each is narrated by unreliable in-character
voices who sometimes contradict each other on purpose — see "Unreliable,
plural history" below.

## Cross-cutting themes

### Unreliable, plural history as a deliberate design principle
All four books use in-character, biased narrators and explicitly refuse
to settle on one "true" account of contested events.
- **v20-lore-bloodlines** and **v20-lore-clans** are structured entirely
  as oral history dictated by named (or implied) elder narrators to a
  childe, with each chapter flagging its own unreliability up front —
  see especially the Malkavian chapter's "everything I say here is a
  lie" (lore-clans, Ch. Malkavians) and the multiple competing origin
  myths given for the Daughters of Cacophony and Samedi (lore-bloodlines).
- **v20-core** frames this at the cosmological level: the Book of Nod
  itself is described as having "any number of editions of varying
  reliability" (v20-core, Ch. One, p.27-28), and Generation/Antediluvian
  lore is presented as rumor rather than fact throughout.
- **v20-dark-ages** goes furthest with this device, presenting entire
  chapters as literal letter exchanges between named in-fiction
  correspondents who openly dispute each other's claims (Appendix B:
  Apocrypha of the Clans is built almost entirely from this format —
  see the Brujah "Letters from Carthage" and the Cappadocian theological
  correspondence).

### Carthage as the Brujah/Ventrue founding wound — and a live example of the disagreement problem
Every book that touches Brujah or Ventrue history references Carthage's
destruction, and no two accounts agree on the details, which makes it a
useful test case for how this library handles contradiction.
- **v20-lore-clans** (Ch. Brujah) frames Carthage as a genuine
  philosopher-king utopia under Troile, destroyed by Ventrue treachery —
  "the original wound."
- **v20-lore-clans** (Ch. Ventrue) flatly rejects that framing in the
  same book: Carthage was "a horrific death-cult city" and its
  destruction was "delenda est" — a monstrous place that had to be
  destroyed, not a lost golden age.
- **v20-dark-ages** (Appendix B) adds a third, in-period layer: letters
  from a Cainite named Zamra transcribe a Carthage-era account of
  Troile's origin that is gentler than the standard diablerie narrative
  (Troile is Embraced as an equal after a loyalty test, not simply as a
  betrayer), while a companion letter shows the last Carthaginian prince
  as a coward whose defiant last stand was pure propaganda — undercutting
  *both* modern versions.
No single book is "right" here — treat this as the library's clearest
demonstration that in-character sourcing is deliberately unreliable
throughout, not a research gap to resolve.

### Founding-atrocity guilt and the Tremere/Salubri destruction
The Tremere's seizure of Clan status via violence against the Salubri is
referenced in all four books, but its *status* — recent scandal vs.
settled ancient history vs. still-unfolding — differs by timeline.
- **v20-dark-ages** (Ch. Two: Assamites entry, and Ch. Two: Bloodlines
  framing) places the event as very recent and ongoing: the Tremere
  "created the first Gargoyles" in 1121 against the Tzimisce, and the
  Salubri's founder Saulot was destroyed by Tremere sorcerers in 1133 —
  within living memory of the 1242 setting, with the Salubri caste
  system still fractured but not yet destroyed as a people.
- **v20-lore-clans** (Ch. Tremere, Ch. Salubri context via Baali/Kiasyd
  entries) and **v20-lore-bloodlines** (Ch. Salubri) treat this same
  event — dated consistently to 1291 in the modern books, a further
  ~150 years after the Dark Ages setting — as ancient, settled history:
  the Salubri are now a nearly extinct bloodline rather than an active
  Clan, hunted rather than merely diminished.
- **v20-dark-ages** (Appendix B: Salubri) makes the timeline gap
  explicit with a speculative "what if" sidebar imagining a Storyteller
  choosing to have the three Salubri castes reunify before 1291 and
  avoid the Clan's near-total destruction — openly telling the table
  that the modern books' outcome is one branch among several, not
  foreordained.

### The Cappadocians and Giovanni: active Clan vs. historical footnote
This is the single largest structural difference between the Dark Ages
book and the other three, and worth flagging clearly for anyone
switching between them.
- **v20-core**, **v20-lore-clans**, and **v20-lore-bloodlines** all
  describe the Cappadocians as destroyed — Augustus Giovanni's "the
  Bite" campaign wiped out the Clan over roughly two centuries, and any
  survivors (Premascines) are treated as dangerous rumors. The Giovanni
  are a fully independent, self-sufficient Clan with their own
  Disciplines, controlling Venice under a secret 1528 Promise with the
  Camarilla.
- **v20-dark-ages** depicts the *opposite* stage of this relationship:
  the Cappadocians are a fully active Clan (Ch. Two) with their own
  decennial gathering at Erciyes, and the "Young Ones" (Giovanni) are
  still a junior, secretive family within Cappadocian society, not yet
  an independent Clan. Appendix B's Giovanni section includes an
  explicit designer sidebar ("Giovani Through the Ages") telling
  Storytellers outright that the modern-book outcome (Augustus's plan
  succeeding, the Cappadocians' destruction) is not guaranteed from the
  Dark Ages starting point — it's presented as a live possibility for a
  long-running chronicle to decide, not backstory already written.
- Consequence for research: if a question is about "the Cappadocians"
  or "the Giovanni" without specifying an era, check which timeline is
  meant before answering — the two source sets describe them as
  occupying opposite ends of the same historical arc.

### The Beast as a patient, intelligent adversary
All four books reject a simple "animal urge" framing of vampiric
monstrosity in favor of the Beast as a strategic, patient force that
wins through small escalating victories.
- **v20-core** (Ch. One) states this most directly: the Beast "knows
  that the war against the Man is one that, given time, it will
  inevitably win," and is "often a savvy creature" in young vampires.
- **v20-dark-ages** develops this furthest with an extended second-person
  literary set-piece (Introduction) walking through the full
  Hunger→Hunt→Feeding→Denouement cycle as the one experience every
  vampire shares regardless of Clan, era, or politics — and introduces
  "Wassail" (Ch. One) as this era's term for the Beast's final,
  irreversible total victory over a vampire's remaining self.
- **v20-lore-clans** and **v20-lore-bloodlines** show the Beast's
  patience playing out at Clan scale rather than individual scale —
  e.g. the Tzimisce chapter's anxious philosophical fragment
  (dark-ages, Appendix B) about whether the demon Kupala has slowly
  corrupted the entire Clan's psychology over centuries mirrors the same
  "small losses compound" logic applied to a whole people rather than
  one vampire.

### Morality systems: Paths of Enlightenment (modern) vs. Roads (Dark Ages)
Both eras use structurally identical game systems (a Humanity-equivalent
plus alternative moral codes, each with a Hierarchy of Sins) but
different terminology and different specific codes.
- **v20-core** (Ch. Seven) presents eleven Paths of Enlightenment
  (Blood, Bones, Caine, Cathari, Feral Heart, Honorable Accord, Lilith,
  Metamorphosis, Night, Paradox, Power and the Inner Voice) alongside
  default Humanity.
- **v20-dark-ages** (Ch. Three) presents five major "Roads" (Beast,
  Heaven, Humanity, Kings, Bones) plus minor Roads (Yasa), organized
  differently — Road of Heaven, for instance, is explicitly the whole
  spectrum of period mortal religions (Christian, Muslim, Jewish,
  Druidic, Roman pagan) practiced through a vampiric lens, which has no
  single equivalent Path in the modern book.
- Several Path/Road names carry over with continuity: **Road of Bones**
  (dark-ages) and **Path of the Bones** (v20-core) are the same
  Cappadocian-originated death-scholarship code under slightly different
  names in each era; **Road of Paradox**/"Asura" (dark-ages, Appendix B)
  and **Path of Paradox**/"Shilmulo" (v20-core, and cross-referenced in
  v20-lore-clans' Ravnos chapter) are likewise the same Ravnos philosophy
  across both eras, with consistent core tenets (svadharma, maya,
  samsara) despite the different names for adherents.

### Regional/cultural specificity over generic "medieval Europe" or "the West"
All four V20 books push back against a monolithic default setting, but this
is most sustained in the Dark Ages book — and the classic-line clanbooks
extend this same instinct further still.
- **v20-lore-clans** and **v20-lore-bloodlines** work non-European
  history and cultures into individual Clan/bloodline chapters (the
  Assamites' Islamic and Jewish religious diversity, the Ravnos's Indian
  caste system, the Tzimisce's Carpathian specificity, several African
  and Asian bloodlines in Lore of the Bloodlines).
- **v20-dark-ages** Chapter Nine ("The Dark Medieval World") goes
  furthest among the V20 books, devoting extensive space to real
  1241-42 history outside Western Europe — the Mongol invasion of
  Hungary and Rus, Lithuania's pagan holdout status, Georgia's Golden
  Age, the Steppe peoples — and Chapter Eight's Storyteller advice
  explicitly instructs "set your chronicle in a non-Western European
  country" as a deliberate design suggestion, not an afterthought.
- **wind-from-the-east** is effectively a book-length expansion of that
  same instinct: the entire book is built around the Mongol Empire and
  its collision with both Cainite and Wan Kuei (Kindred of the East)
  society, treating the two cosmologies as equally important rather
  than centering one.
- Individual classic-line clanbooks push the same instinct further than
  their V20 counterparts in places: **clanbook-nosferatu-revised**
  devotes a substantial, historiographically pointed section to African
  Nosferatu kingdoms (explicitly naming and rejecting the "Hamitic
  Hypothesis"), and **clanbook-followers-of-set-revised** gives real
  narrative weight to Mesoamerican (Tlacique), West African (Damballan),
  and Indian (Naktanchara) bloodline variants rather than treating them
  as footnotes to an Egypt/Europe-centered main line.

### Saulot's diablerie: three genuinely different treatments, now including the Tremere's own voice
The Tremere's diablerie of the Salubri founder Saulot — already tracked
above as a Dark Ages/modern-books timeline difference — gets a third,
starkly different treatment once the classic-line clanbooks are added,
because two of them are written from the opposing sides of the same
event.
- **clanbook-salubri** (classic Dark Ages) is the victims'-eye account:
  the clan is being actively exterminated by "the Usurpers," and the
  book's own closing twist (Appendix Two) goes further than any other
  book in the library by surfacing a disputed ancient tablet suggesting
  Saulot himself may have inadvertently created the Baali — undermining
  even the Salubri's own sympathetic self-narrative.
- **clanbook-tremere-revised** (classic Revised) is the perpetrators'-
  eye account, and treats the same act matter-of-factly, even
  approvingly: a sidebar states plainly that Tremere "discovered" and
  diablerized Saulot and calls it "a boon to all Kindred," dismissing
  rumors that Saulot orchestrated his own death as "misguided
  propaganda."
- **v20-lore-clans** and **v20-dark-ages** (see "Founding-atrocity guilt"
  above) treat the event more ambivalently and place it on a timeline —
  neither book endorses the Tremere's self-justification the way
  clanbook-tremere-revised does.
Reading clanbook-salubri and clanbook-tremere-revised back to back is
the single clearest demonstration in this library of how differently
two clanbooks can frame the identical historical act depending on whose
voice is narrating.

### The Week of Nightmares: a Ravnos catastrophe felt clan-wide
Three classic Revised-line clanbooks reference the same present-day
cataclysm — the death of the Ravnos Antediluvian — from progressively
more distant vantage points, and reading them together reconstructs the
full event better than any single book does.
- **clanbook-ravnos-revised** (Ch. One) is the epicenter account: a
  first-person narrator physically visits the Bangladesh site where the
  Antediluvian Zapathasura/Ravana died (apparently to something like
  nuclear-scale force), describes the clan-wide four-night psychic rage
  that swept every Ravnos simultaneously, and states outright that
  "nearly all" the eldest Ravnos, especially in Asia, were destroyed —
  explicitly framing the event as "the first battlefield of Gehenna."
- **clanbook-malkavian-revised** (Ch. One) registers the same event
  ("the Week of Nightmares") as an unexplained clan-wide sensory/
  emotional catastrophe coinciding with the sudden failure of the
  Malkavians' own decades-old Convention of Thorns conditioning (**the
  Reawakening**) — the Malkavian narrator explicitly wonders whether
  "Ravnos' death-scream was so sharp that it reached back through time
  to caress us all," without fully understanding the cause.
- **clanbook-gangrel-revised** (Ch. One) references the same period more
  obliquely: Justicar Xaviar's still-unexplained, terror-driven decision
  to withdraw the entire Gangrel clan from the Camarilla is left
  deliberately unresolved in that book, but its timing and the Gehenna-
  adjacent unease it provokes line up with the same moment.
None of these three books cross-references the others by name (each
clanbook is written to stand alone), but a Storyteller or researcher
working across all three gets a substantially richer picture of a
single shared event than any one book provides — a useful example of
this library's value over reading any single sourcebook in isolation.

### Carthage, again: a fourth, fifth, and sixth telling
The Carthage disagreement already tracked above (Brujah utopia vs.
death-cult vs. neither, across the V20 books) gets still more entries
once the classic-line clanbooks are added, reinforcing that this is a
deliberately, permanently unresolved point across the entire line no
matter how many books are consulted.
- **clanbook-brujah-revised** gives the fullest classic-line Brujah
  account: an idealized but real port city undone as much by internal
  decadence (Baalist rites) as by Ventrue-linked betrayal, with the
  reformist **Promethians** faction offered as a partial counterweight
  to the "lost golden age" framing.
- **clanbook-toreador-revised** treats Carthage as a case study in why
  no lesser Cainite should attempt Mycenae-style direct rule, told from
  the Ventrue-allied Toreador side of the same war.
- **clanbook-nosferatu-revised**, true to that clan's outsider stance,
  is openly skeptical of the Brujah/Ventrue fixation on Carthage,
  suggesting the emotional weight both clans put on it says more about
  them than about the actual historical stakes.

### A shared name across game lines: Zao-lat and the Wu Zao
A specific, easy-to-miss but genuine cross-line connection: **v20-dark-
ages**' Salubri "Watcher" caste material describes their founder as
**Zao-lat**, a trickster who stole enlightenment from "the Ten Thousand
Demons" in "the Middle Kingdom" and whose followers operate in East Asia
as the "Wu Zao" (feared/mocked by the Wan Kuei). **wind-from-the-east**
independently describes a Wan Kuei group called the **Wu Zao**, holding
that they descend from a barbarian figure also named **Zao-lat**. This
is very likely the same figure/lineage referenced from two different
angles (V20's Dark Ages Salubri material and the classic-line Mongol-era
supplement) rather than a coincidence — worth flagging explicitly if a
question touches either the Salubri Watcher caste or the Wu Zao, since
neither book cross-references the other directly.

### The view from the other side: Dark Ages: Inquisitor's hunters
Every other book in this library is written from a Kindred (or, in
wind-from-the-east's case, partly Wan Kuei) point of view — even their
unreliable narrators are vampires disagreeing with other vampires.
**dark-ages-inquisitor** is the library's only book narrated by the
people hunting Cainites rather than by Cainites themselves, and it adds
a genuinely new kind of unreliability on top of the library's existing
"plural history" pattern: its narrators often don't know they're looking
at a vampire at all. Its Prelude has an Oculi Dei "Eye" watch a "night-
devil" feed on a girl without being able to name what he's seeing; its
Chapter One bestiary folds vampires into a broader "Demons of Flesh"
category alongside monstrous swamp-creatures and werewolves, with
"blood-drinking horror" as only a passing aside rather than a
headline distinction. Anyone answering a question like "how did
contemporaries understand vampires" should check this book specifically
— it is the library's only source written from genuine mortal ignorance
rather than after-the-fact Kindred hindsight.

### The modern view from the other side: The Hunters Hunted II, and a direct link to Dark Ages: Inquisitor
`v20-hunters-hunted-ii` is this library's second (and only modern-nights)
book narrated from the hunters' side rather than the Kindred's, and it
extends the "view from the other side" pattern established by
`dark-ages-inquisitor` into the present day — its own Chapter One is
told entirely as an experienced hunter's in-voice monologue to a
newly-made hunter, deliberately withholding V20 terminology (Clans,
Sects) the way `dark-ages-inquisitor`'s narrators withhold the word
"vampire" itself.

More than a thematic echo, the two books share a **specific named
character across eras**: `dark-ages-inquisitor`'s Prelude introduces
**Brother Leopold von Murnau**, a 13th-century Dominican inquisitor of
the House of Murnau, last seen in that book confronting his own
corrupted cousin with his ultimate fate left open. `v20-hunters-hunted-
ii`'s central modern hunter organization, the **Society of Leopold**,
reveres a **"Leopold of Murnau"** as its founding figure — author of
"The Testament of Leopold," killed by a vampire, and commemorated in a
named relic made from his bones ("The Keys of Leopold"). Neither book
states outright that these are the same continuity event narrated
twice, but the name, order, era, and cause of death all match: read
together, the two books supply a beginning (a living, struggling
13th-century inquisitor) and an end/legacy (a martyred founder-saint
venerated 700+ years later) for the same figure. Treat this as a
genuine intentional throughline rather than coincidental reuse of a
name, and prefer citing both books together for any question
specifically about Leopold.

`v20-hunters-hunted-ii` is also **directly and non-contradictorily
consistent** with `v20-core`'s own brief "Witch-Hunters" sidebar (Ch.
Nine): both agree that the Society of Leopold's current Inquisitor
General is Ingrid Bauer ("the Iron Maiden"), that she succeeded a
Monsignor Amelio Vittore, and that her regime has reinstated torture
and opened combat colleges. Unlike the Dark Ages/modern-books
relationships tracked elsewhere in this file, this is a case of one
book expanding on another within the *same* sub-pair without
introducing any divergence — see "Points of agreement" below.

### An open mystery resolved: who's behind the American gang wars?
`v20-core`'s "Criminals" sidebar (Ch. Nine) mentions mysterious
informants — who all self-identify as "Caitiff" — feeding intelligence
to organized crime and inciting gang wars against vampire-controlled
criminal networks in Detroit, Miami, Los Angeles, and Chicago, and
states outright that their true identity and motive is "an open
mystery." `v20-hunters-hunted-ii`'s Chapter Six answers this in full:
the informants are **Kerberos**, a coterie of five Caitiff vampires
secretly created and led by a Tzimisce elder, **Nevesa "Zek"
Zekistraya**, who deliberately botched her own childer's Embraces to
disguise them (and herself) as ordinary Caitiff, working through
Detroit cartel boss Santos "Sapa Inca" de Sanza. This is a rarer kind
of cross-book relationship in this library than the disagreements
tracked elsewhere — not a contradiction or a different vantage point on
the same event, but a straightforward answer to a question the earlier
book poses and deliberately leaves open. If a question concerns that
specific `v20-core` mystery, treat `v20-hunters-hunted-ii` as the
definitive follow-up rather than searching for another explanation.

### The Cainite Heresy: the same name, two different emphases, in two different lines
dark-ages-inquisitor's central ongoing plot hook — the **Cainite
Heresy**, a cult that treats Cainites as blessed or angelic beings
descended from Cain, run in this book through the **Crimson Curia** (a
secret conspiracy of Cainites embedded within the Church hierarchy
itself) — is not a one-off invention specific to this book. **v20-
dark-ages** (Ch. Two: Clans of Caine, Lasombra entry, p.51) independently
describes its own "Cainite Heresy": a cult "dominated by Lasombra
priests and bishops" who believe "Cainites, having been marked by God,
are akin to angelic beings," treated as blasphemy by orthodox Lasombra
and a driver of the clan's internal Shadow Reconquista schism. Neither
book names the other's specific machinery (v20-dark-ages never mentions
a "Crimson Curia"; dark-ages-inquisitor never names the Lasombra as the
Heresy's source), but both independently arrive at the same core claim —
that vampirism itself can be preached as a mark of divine favor rather
than a curse — from opposite vantage points: v20-dark-ages frames it as
an *internal* Lasombra theological schism, while dark-ages-inquisitor
frames it as a mortal-facing recruiting cult that inquisitors partially
uncover from the outside. Read together, they suggest the Heresy is
bigger and more decentralized than either book alone implies — worth
flagging explicitly rather than picking one book's framing as the
complete picture. None of dark-ages-inquisitor's other named Cainites
(Xalbador, the Pale Brother, Ulfila/"St. Amanda," Radovan Istvic, the
Genoese d'Agostino family) currently appear in any other book in this
library.

**v20-dark-ages-companion** adds a third, individual-level data point
that complicates the "Lasombra schism" framing specifically: **Bethany
of Ely**, an Eighth Generation *Salubri* Healer (not a Lasombra), is
described as having "led the Cainite Heresy's believers in Ely" in
England before Tremere persecution broke her faith and drove her into
Mithraist exile in Bath (v20-dark-ages-companion, Ch. Two: The Domain
of Bath, p.29-30; she resurfaces via a letter to an exiled friend in
Ch. Six's Salubri Apocrypha, p.99). Her account is a convert's-eye
view of leaving the Heresy, not an institutional description of
running or hunting it, and her Clan membership shows the Heresy
recruited outside Lasombra ranks — neither v20-dark-ages nor
dark-ages-inquisitor rules this out, but neither depicts it either.
Treat Bethany as evidence the Heresy was more doctrinally porous than
its Lasombra-clergy reputation suggests, not as a contradiction of
either book's framing.

### The Dream of Constantinople: a Methuselah v20-dark-ages only mentions in passing, now fully realized
v20-dark-ages' Appendix B briefly describes the Obertus Tzimisce as
"fostered by the Methuselah Dracon" and notes they were "scattered,
temporarily rudderless" once Constantinople fell and "Dracon was cast
out" (v20-dark-ages, Appendix B, Tzimisce revenant-families entry,
p.455) — a single-paragraph aside with no further explanation of who
the Dracon was or what happened in Constantinople. **v20-dark-ages-companion**'s entire Chapter Four is
built around exactly this event: the Dracon, the Toreador Methuselah
Michael the Patriarch, and the Ventrue Antonius once ruled
Constantinople together as "the Dream," a Cainite-kine utopia that
collapsed when Michael's madness, the Dracon's disappearance, and the
1204 sack unraveled it (v20-dark-ages-companion, Ch. Four, p.58-59).
Nothing in the fuller account contradicts v20-dark-ages' aside — the
Companion is simply the library's only source that develops it, and
should be treated as the primary reference for any question about the
Dracon, Michael, or the Obertus' pre-scattering history.

### Single throwaway lines elsewhere, fully worked out in the Companion
Beyond Constantinople, v20-dark-ages-companion has a recurring habit of
taking a sentence-length mention from an earlier book in this library
and building an entire subsystem around it, without contradicting the
source:
- **v20-lore-clans** notes in passing that some Assamites practice
  "Zoroastrianism" among several religions the Clan tolerates (v20-lore-
  clans, The Assamites, p.19). **v20-dark-ages-companion**'s Assamite
  Apocrypha (Ch. Five, p.83-85) turns this into a full dual **Road of
  Zarathustra** system (Road of Angra Mainyu / Road of Ahura Mazda,
  with a one-time free switch between them) plus its own internal
  history (Zarathustra, the martyr Tehmina, the elder Ur-Shulgi).
- **clanbook-ravnos-revised** mentions in passing that "among the most
  traditional Ravnos, mortal lineage" — **jati** — "is at least as
  important as Kindred" (clanbook-ravnos-revised, Ch. Two, p.41), without
  naming any specific jati. **v20-dark-ages-companion**'s Ravnos
  Apocrypha (Ch. Six, p.100-103) names several (Alexandrites,
  Phaedymites, Bashirites, Sybarites, Yoryari, Phuri Dae) and builds out
  the **Sadhana** blood-magic tradition (Blood Nectar, the five-level
  Power of Karma) two of these jati are said to practice.
For any question about Zoroastrian Cainites or Ravnos jati structure,
prefer the Companion's fuller treatment; for the Clan-level context
those details sit inside, the original books remain the right source.

### The Salubri's fortunes vary sharply by region within the same 1242 setting
This is a different kind of variation from the "Salubri as Clan vs.
bloodline" timeline question below — it's not a disagreement between
books, but a detail that only becomes visible once v20-dark-ages-
companion is added: even within a single shared setting-date (1242
CE), the Salubri's circumstances differ drastically by domain.
v20-dark-ages-companion's Mangaluru chapter (Ch. Six) depicts a still-
unified, openly ruling Salubri caste-triumvirate member, consistent
with v20-dark-ages' broader claim that the Clan is "waning" rather than
already destroyed in the Dark Ages — but its Bath chapter (Ch. Two)
depicts persecuted Salubri refugees sheltering under a foreign Prince's
mercy, and its Constantinople chapter (Ch. Four) depicts a lone Salubri
(Rakhama) hiding her identity while secretly hunting the Skull of
Saulot. Read together, the three domains suggest a Clan whose global
decline (agreed upon across the V20 line) was locally uneven rather
than uniform — Mangaluru as a still-thriving stronghold, Bath and
Constantinople as evidence of the diaspora already underway elsewhere.

## Points of agreement
- **Core cosmology is stable across all four books**: Caine's curse,
  the Second/Third Generation Antediluvian structure, Gehenna as
  looming and unconfirmed, Golconda as a rumored and possibly
  Antediluvian-suppressed transcendent state, and the basic mechanics
  of the Embrace, frenzy, and diablerie/Amaranth are consistent whether
  the book is set in 1242 or the present day.
- **The Tzimisce/Kupala relationship** is consistent across
  v20-lore-clans and v20-dark-ages: both describe a buried, ancient
  entity granting the Clan its land-based sorcery at an unspecified but
  real cost to the Clan's collective psychology, and both treat Kupala's
  true nature as deliberately unresolved.
- **Antitribu/dissident-faction framing recurs structurally**: the
  modern books' Sabbat antitribu (v20-lore-clans, Appendix II) and the
  Dark Ages book's internal Clan schisms (the Lasombra's Shadow
  Reconquista, the Salubri caste split, the Setite Priests/Warriors/
  Witches division) both use the device of giving a dissenting internal
  faction its own unfiltered voice to complicate the "official" Clan
  narrative — this is a consistent authorial technique across the whole
  line, not just a modern-books habit.
- **dark-ages-inquisitor's outsider theology matches the insiders'
  cosmology**: the Cainite Heresy's account of vampires as "Cain's
  heirs," sustained by the "shining blood" and organized around the "See
  of Nod," lines up with Caine's curse and Book of Nod material as
  described from the inside by every other book in the library, even
  though dark-ages-inquisitor's narrators never have full or reliable
  access to that inside view themselves.
- **The Society of Leopold's modern leadership is consistent between
  v20-core and v20-hunters-hunted-ii**: both name Ingrid Bauer ("the
  Iron Maiden") as the current Inquisitor General following Monsignor
  Amelio Vittore's incapacitation, and v20-hunters-hunted-ii's fuller
  treatment (sub-orders, sects, Theurgy) reads as a direct expansion of
  v20-core's sketch rather than a divergent account — see "The modern
  view from the other side" above.

## Points of disagreement or tension
- **Carthage** (Brujah utopia vs. death-cult vs. neither vs. Ventrue-
  scale-obsession vs. outsider skepticism — see above, the single most
  heavily and permanently contested topic in the library, spanning
  every game line).
- **Cappadocians/Giovanni status** (active Clan vs. destroyed — a
  timeline artifact, not a contradiction, but one that will confuse
  answers if not flagged — see above). **clanbook-giovanni-revised**
  adds a classic-line account of the founding coup itself (told from the
  Giovanni's own gloating perspective), which the V20 books' "settled
  history" framing doesn't include in comparable narrative detail.
- **Salubri as Clan vs. bloodline** (still-unified three-caste Clan in
  1242 vs. nearly-extinct bloodline in the modern setting — see above).
  **clanbook-salubri** adds a third data point: a classic-line, Dark
  Ages-era account that is *more* pessimistic in tone than v20-dark-
  ages' version, treating the clan as already on the edge of
  extinction rather than merely "waning."
- **Saulot's diablerie — victim's account vs. perpetrator's account**
  (clanbook-salubri vs. clanbook-tremere-revised — see above, the
  clearest example in the library of two books narrating the identical
  event from opposing in-universe sides).
- **Gargoyle creation timeline**: v20-dark-ages dates Tremere Gargoyle
  creation to 1121 and depicts active Tremere/Tzimisce war over it as
  current events; the modern books (v20-lore-clans, v20-lore-bloodlines,
  and classic-line **clanbook-tremere-revised** and
  **clanbook-gangrel-revised**) treat the Montmartre Pact (1489) ending
  that practice as settled history, consistent with the gap between the
  two eras' settings. clanbook-gangrel-revised additionally frames the
  Gargoyles' creation as a direct atrocity against captured Gangrel
  (not just Tzimisce), a detail not emphasized in the V20 Tremere
  material.
- **Malkavian founding-myth details** differ sharply not just in
  emphasis but in basic narrative structure across the three tellings
  now in this library: v20-lore-clans' "Caine's birthday party" parable
  treats Malkav's nature as an enigmatic in-joke with Caine himself;
  v20-dark-ages ties Malkavian persecution more directly to the real
  medieval Church's shifting theology of mental illness; and classic-
  line **clanbook-malkavian-revised** gives the most elaborate and
  different account of all three — Malkav as one of several childer who
  drank "the hoarded blood of the Three" and was physically torn apart
  near Petra, with the entire modern clan's psychic hive-mind
  ("the Cobweb") originating from his scattered blood/mind. These three
  versions are not reconcilable as a single continuity; treat them as
  three separate tellings, per the edition note at the top of this file.
- **The "Watchers"/third-caste Salubri question**: v20-dark-ages
  presents the Wu Zao/Watcher caste relatively matter-of-factly as an
  established (if secretive) third caste; **clanbook-salubri**, an
  earlier and differently-scoped treatment, presents the very existence
  of a third caste as unconfirmed rumor within its own narrative, with
  a planted letter raising the alternative possibility that "watchers"
  are Tremere infiltrators or a manipulative internal faction rather
  than a genuine caste. Don't treat the Watchers'/Wu Zao's existence and
  nature as settled fact across the whole library.
- **The Cainite Heresy's source** (an internal Lasombra clergy schism in
  v20-dark-ages vs. a Church-wide Crimson Curia conspiracy in
  dark-ages-inquisitor — see above; not a contradiction so much as two
  books each describing one piece of a larger, decentralized movement
  neither fully maps). **v20-dark-ages-companion** adds a third,
  individual data point: Bethany of Ely, a Salubri (not Lasombra) who
  led Heresy believers in England before renouncing the faith — evidence
  the movement recruited outside Lasombra ranks.
- **Editions generally**: beyond the specific points above, expect many
  smaller factual mismatches (elder names, exact dates, minor plot
  details) between the classic Revised-line clanbooks and V20's modern-
  nights material covering the same clans, since V20 is a retrospective
  rewrite rather than a reprint — see the edition note at the top of
  this file before treating any single specific claim as cross-line
  consensus.

## Chronology / influence
Reading order for someone new to this whole library: start with
whichever **line** matches the setting-time you actually care about
(see the edition note near the top of this file) rather than mixing
lines together by default.

- **New to V20 specifically**: `v20-core` first (it defines the
  baseline modern-nights cosmology, Sects, and full game system that the
  two Lore books assume you already know), then `v20-lore-clans` and
  `v20-lore-bloodlines` in either order, then `v20-dark-ages` last if
  the goal is to see how the setting's deep history diverges from what
  the other three books describe as settled fact. `v20-dark-ages` is a
  fully standalone rulebook and works fine read first if the Dark
  Medieval period is the primary interest. Read `v20-dark-ages-companion`
  after `v20-dark-ages`, not before or standalone — it assumes the core
  book's cosmology, Roads, and rules and adds domains/Apocrypha on top
  rather than re-explaining the setting. Read `v20-hunters-hunted-ii`
  after `v20-core` specifically — it directly expands `v20-core`'s
  "Witch-Hunters" sidebar and resolves that book's open "Caitiff
  informants" mystery, so reading order matters more here than for the
  other modern-nights books; it's otherwise self-contained and doesn't
  require the two Lore books first.
- **New to the classic Revised-line modern-nights clanbooks**: each of
  the 13 (`clanbook-brujah-revised` through `clanbook-ravnos-revised`)
  is fully standalone — there's no dependency chain. If tracing the
  "Week of Nightmares"/Antediluvian-death thread specifically, read
  `clanbook-ravnos-revised` first (the epicenter account) before
  `clanbook-malkavian-revised` and `clanbook-gangrel-revised` (which
  reference it more obliquely).
- **New to the classic Dark Ages line**: `clanbook-salubri` and
  `wind-from-the-east` are both standalone; read them before or after
  `v20-dark-ages` as suits the question — they cover overlapping ground
  from an earlier, differently-scoped product line rather than serving
  as prerequisites for it. `dark-ages-inquisitor` is also standalone for
  research purposes (its own book_index.md doesn't require the others),
  but remember it's a rules supplement to the *original* Dark Ages:
  Vampire specifically — if a question is about game mechanics rather
  than setting lore, don't mix its answers with `v20-dark-ages`. If the
  question is specifically about running this book's mechanics *under*
  V20, read `dark-ages-inquisitor/v20-conversion.md` instead of
  reasoning about compatibility from first principles.
- **Researching how mortals/hunters perceived Cainites**:
  `dark-ages-inquisitor` and `v20-hunters-hunted-ii` are the two books
  in the library written from that vantage point — the former for the
  Dark Ages, the latter for modern nights. Read them together for the
  Leopold von Murnau throughline (see "The modern view from the other
  side" above); either stands alone for a single-era question.
- **Cross-line research** (e.g. "how does the Salubri/Tremere conflict
  differ across every book that covers it?"): read this file's relevant
  synthesis section first, then pull the specific books it names.

## Cross-book query examples
```bash
python3 scripts/query_library.py v20-core/book_chunks.db v20-lore-clans/book_chunks.db v20-lore-bloodlines/book_chunks.db v20-dark-ages/book_chunks.db "Carthage"
```
```bash
python3 scripts/query_library.py v20-lore-clans/book_chunks.db v20-dark-ages/book_chunks.db clanbook-salubri/book_chunks.db clanbook-tremere-revised/book_chunks.db "Saulot"
```
```bash
python3 scripts/query_library.py v20-core/book_chunks.db v20-dark-ages/book_chunks.db "Golconda"
```
```bash
python3 scripts/query_library.py clanbook-ravnos-revised/book_chunks.db clanbook-malkavian-revised/book_chunks.db clanbook-gangrel-revised/book_chunks.db "Week of Nightmares"
```
```bash
python3 scripts/query_library.py v20-dark-ages/book_chunks.db wind-from-the-east/book_chunks.db "Zao-lat"
```
```bash
python3 scripts/query_library.py dark-ages-inquisitor/book_chunks.db v20-dark-ages/book_chunks.db "Cainite Heresy"
```
```bash
python3 scripts/query_library.py v20-dark-ages/book_chunks.db v20-dark-ages-companion/book_chunks.db "Dracon"
```
```bash
python3 scripts/query_library.py v20-lore-clans/book_chunks.db v20-dark-ages-companion/book_chunks.db "Zoroastrian"
```
```bash
python3 scripts/query_library.py clanbook-ravnos-revised/book_chunks.db v20-dark-ages-companion/book_chunks.db "jati"
```
```bash
python3 scripts/query_library.py dark-ages-inquisitor/book_chunks.db v20-hunters-hunted-ii/book_chunks.db "Leopold"
```
```bash
python3 scripts/query_library.py v20-core/book_chunks.db v20-hunters-hunted-ii/book_chunks.db "Kerberos"
```
(Replace the slug paths with whichever subset of books is relevant to
the question — the slug names shown above are what appears in the
grouped results, so use them as written. With 22 books in the library,
prefer naming only the 2-5 books actually relevant to a question rather
than querying all of them at once.)

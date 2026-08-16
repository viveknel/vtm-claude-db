# Vampire: The Masquerade — Cross-Book Index

## Books in this collection

**V20 line** (20th Anniversary Edition, modern retrospective/reboot, published ~2011-2015):
- `v20-core/` — Vampire: The Masquerade 20th Anniversary Edition (core rulebook), 528 pages
- `v20-lore-clans/` — V20 Lore of the Clans, 309 pages
- `v20-lore-bloodlines/` — V20 Lore of the Bloodlines, 103 pages
- `v20-dark-ages/` — Vampire: The Dark Ages 20th Anniversary Edition, 489 pages

**Classic Dark Ages line** (original, pre-V20, published ~1996-2002):
- `clanbook-salubri/` — Clanbook: Salubri, 74 pages
- `wind-from-the-east/` — Wind from the East (Dark Ages/Mongol-era supplement, also relevant to Kindred of the East — see its own README), 98 pages

**Classic Revised Edition line** (original, pre-V20, modern nights, published ~1998-2000):
- `clanbook-brujah-revised/`, `clanbook-gangrel-revised/`, `clanbook-malkavian-revised/`,
  `clanbook-nosferatu-revised/`, `clanbook-toreador-revised/`, `clanbook-tremere-revised/`,
  `clanbook-ventrue-revised/`, `clanbook-assamite-revised/`, `clanbook-followers-of-set-revised/`,
  `clanbook-tzimisce-revised/`, `clanbook-lasombra-revised/`, `clanbook-giovanni-revised/`,
  `clanbook-ravnos-revised/` — 106 pages each

## How to use this file
This file synthesizes themes across all 19 books above. For details on
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
   `v20-dark-ages`) is a 2011-2015 *20th Anniversary retrospective*
   line: a consolidated, updated re-presentation of the game aimed at
   both new and returning players, published as two internally
   consistent sub-pairs — one for "modern nights" (present day) and one
   for the Dark Ages period (1242 CE), each roughly 750 years apart in
   fictional time but written and edited as a matched pair.
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
   `wind-from-the-east`) is the *original*, pre-V20 Dark Ages product
   line, also from the late 1990s/early 2000s. `v20-dark-ages` is
   explicitly a later, updated edition of this same period-setting line
   — but it is not a direct reprint. Where `clanbook-salubri` or `wind
   from-the-east` and `v20-dark-ages` describe the same character,
   event, or Clan, expect broad agreement on the big picture and real
   divergence on detail; neither supersedes the other for research
   purposes, and both are worth checking.

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
  Medieval period is the primary interest.
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
  as prerequisites for it.
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
(Replace the slug paths with whichever subset of books is relevant to
the question — the slug names shown above are what appears in the
grouped results, so use them as written. With 19 books in the library,
prefer naming only the 2-5 books actually relevant to a question rather
than querying all of them at once.)

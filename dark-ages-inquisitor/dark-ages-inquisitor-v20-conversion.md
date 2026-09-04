# Running *Dark Ages: Inquisitor* with V20

*Dark Ages: Inquisitor* (White Wolf, 2002) says outright that it "is not a
complete game" and requires the *original* *Dark Ages: Vampire* core
rulebook — classic Storyteller System, not V20's revised trait set. In
practice, though, the real gaps are narrower than that disclaimer
suggests. Below is what's actually incompatible, what already lines up
fine, and a conversion package to make the book playable at a V20 Dark
Ages table. Where relevant, this also draws on *The Hunters Hunted II*
(2013) — V20's own modern-nights mortal-hunter sourcebook, indexed in
this library as `v20-hunters-hunted-ii` — since it's the closest thing
V20 has to an official answer for several of the gaps below.

## The good news: the core engine hasn't moved much

Before listing conflicts, it's worth being clear about how much *didn't*
change between the classic-line rules Inquisitor assumes and V20:

- **Dice pools and difficulty** — both use d10 pools against a
  Storyteller-set difficulty (baseline 6), no "10-again," no target-number
  system swap.
- **Virtues** — both use the same three, on the same 1–5 scale:
  Conscience, Self-Control, Courage.
- **Willpower** — both use a 1–10 permanent-rating/spendable-pool split,
  and both set starting Willpower from the Courage Virtue.
- **Health** — the same seven-level track (Bruised → Incapacitated) with
  identical dice-pool penalties.
- **Abilities** — both use the Talents/Skills/Knowledges three-category
  structure.
- **Mortal-tier character creation** — V20's own rules for creating
  ghouls (and, by extension, other mortals) in the Appendix use
  Attributes 6/4/3, Abilities 11/7/4, 21 freebie points at 5/dot
  Attributes and 2/dot Abilities, 7 dots for Virtues, and 5 dots for
  Backgrounds. Those are exactly Inquisitor's chargen numbers. V20 kept
  the classic-line mortal-tier budget unchanged and only increased the
  numbers for full vampire PCs (7/5/3 Attributes, 13/9/5 Abilities, 15
  freebie points) — a different reference class that inquisitors, being
  mortals, were never meant to be measured against. So Inquisitor's
  character creation chapter is already V20-compliant as printed; no
  conversion is needed there at all.

**A wrinkle worth knowing about:** *The Hunters Hunted II* doesn't use
this same ghoul/mortal budget for its own hunters. Its Attribute spread
matches (6/4/3, with an optional 7/5/3 for "more potent" chronicles),
but its Ability spread is 13/9/5 — the *vampire* PC budget, not the
mortal/ghoul one — with 21 freebie points as usual. V20 canon now
contains two different "how tough should a mortal hunter be" answers:
*Dark Ages: Vampire*'s ghoul-tier numbers (which Inquisitor matches as
printed) and *Hunters Hunted II*'s own, more generous Ability budget.
Neither is wrong; they reflect different design goals (Inquisitor
assumes hunters are meant to be fragile relative to Cainites; *Hunters
Hunted II* explicitly calibrates for hunters who can go a few more
rounds). Pick one deliberately for your table rather than assuming
there's a single settled V20 answer — the conversion package below
gives both as explicit options.

This matters practically: it means Inquisitor's core resolution
mechanics — combat, Virtue rolls, Willpower spends, and chargen itself —
don't need to be rebuilt. The real incompatibilities are narrower than
they first look, and concentrated in one entirely book-specific
subsystem V20 has no equivalent for, plus a couple of smaller frictions.

## Where they actually conflict

### 1. Superior Virtues, Conviction, Piety, and Curses still have no V20 equivalent — even with *Hunters Hunted II* on the shelf

Inquisitor's entire Chapter Four/Five mechanical spine — Superior Virtues
(Faith/Wisdom/Zeal extending Conscience/Self-Control/Courage from a 5-dot
cap to 10), Conviction (a 1–10 fuel resource for Blessings), Piety (a
Road-like moral-standing score), Callousness (triggered when Conviction
exceeds Piety), and the five Curse categories culminating in Cocytus —
is a bespoke system built for the classic line. It's tempting to assume
this gap closed once V20 got its own hunter sourcebook, but it didn't:
*Hunters Hunted II*'s "Numina" system (Hedge Magic, Psychic Phenomena,
True Faith) is built entirely differently — Willpower-fueled activation
rolls with no Virtue-extension mechanic, no Road-analog moral-standing
score, and nothing resembling the five Curse categories or a
Cocytus-style total-collapse state. The closest thing it has is True
Faith's own hypocrisy check (a Conscience roll to avoid losing a dot if
the character acts against their faith), which is a pale echo at best.
So this remains a genuine gap, not merely an incompatibility: there's
still nothing in official V20 material to reconcile Superior
Virtues/Conviction/Piety/Curses against, and the whole subsystem still
has to be imported wholesale rather than converted piecemeal.

### 2. True Faith is now handled three different ways

V20 core gives **True Faith** as a Storyteller-controlled Trait (rated
1–5, mechanical effects escalating by dot, from warding off vampires at
Faith 1 up to forcing a vampire to flee at Faith 5) — it's explicitly rare
and not normally player-purchasable. Inquisitor deliberately *doesn't*
use this Trait for player characters; instead it builds Superior
Virtues/Piety as True Faith's in-fiction replacement and gives a sidebar
conversion for translating between the two systems (Servant = True Faith
1, Acolyte = 2, Advocate = 3, Judge = 4 — the book deliberately never
reaches True Faith 5 through this route, on the grounds that such
holiness "cannot easily be quantified by any means").

*Hunters Hunted II* adds a third model on top of these two: a **True
Faith Numina Path**, player-purchasable but capped at 1 dot at character
creation and growable only through sustained in-story devotion at the
Storyteller's discretion — structurally closer to V20 core's escalating
1–5 progression (repel vampires → sense their presence → resist
mind-affecting powers → immunity to ghouling/Presence → inspire
Rötschreck-like fear, plus rare, unleveled Miracles) than to Inquisitor's
Superior Virtue substitute. If you run Inquisitor unmodified inside a
V20 game, you now have three parallel "resist the supernatural through
faith" systems that could plausibly sit at the same table — V20 core's
True Faith for NPCs, Inquisitor's Superior Virtues/Piety for PC
inquisitors, and *Hunters Hunted II*'s capped Path for any other mortal
PC who isn't a card-carrying inquisitor — which is workable, but needs
an explicit ruling for which applies to whom. The conversion package
below gives one.

### 3. The Merits & Flaws catalog has drifted — with at least two confirmed direct collisions

Inquisitor's "Disallowed" list and its own roughly twenty new
Merits/Flaws are keyed to the *classic* core Vampire Merits & Flaws
catalog (it explicitly disallows things like *13th Generation*, *Prey
Exclusion*, *Blood Madness* — all classic-line entries). V20 reorganized
and partly rewrote its Merits & Flaws chapter. Some names, costs, and
even the existence of specific entries differ between the two editions.

This isn't just a theoretical risk — two of Inquisitor's own new Merits
share a name with a Merit in *Hunters Hunted II*, with the mechanics
having drifted in the intervening (in-fiction) centuries:
- **Holy Aura** is a 2-pt Merit in both books, but does different
  things. Inquisitor (p. 171): marks the character as touched by
  God — the devout are drawn to them, the wicked avoid them, and anyone
  attempting to lie to or conceal something from them faces +2
  difficulty. *Hunters Hunted II* (p. 125): grants -1 difficulty on all
  social interaction rolls, and supernatural creatures (especially
  Kindred) notice and may react with hostility rather than avoidance.
- **Ecstatic** appears in both — as a **2-pt Flaw** in Inquisitor
  (p. 171: powerful Blessing use can trigger glossolalia or prophetic
  fits, requiring a Willpower roll to avoid losing control) and as a
  **2-pt Merit** in *Hunters Hunted II* (p. 125: the same
  stigmata/glossolalia/trance phenomenon, but reframed as "a Merit of
  dubious benefit" — a Social bonus among the faithful that offsets the
  stigma of appearing unstable).

Neither collision breaks anything by itself, but a table running both
books (or converting one using the other for inspiration) should decide
explicitly which version — or a merged version — applies, rather than
defaulting to whichever a player happens to remember. None of this
breaks Inquisitor's *other* new Merits/Flaws (those remain
self-contained), but the disallowed list and any cross-references to
"standard Vampire Merits/Flaws" still need a line-by-line check against
V20's actual catalog rather than an assumed 1:1 match.

### 4. Terminology and cross-references

Smaller frictions worth flagging for a table: Inquisitor calls its extra
chargen points "bonus points," V20 calls the equivalent pool "freebie
points" (same function, different label — trivial, but worth a shared
vocabulary at session zero; *Hunters Hunted II* uses "freebie points"
throughout, for what it's worth, so that's the more broadly-used V20
term). Blessings and Curses occasionally reference specific vampire
Discipline behavior (e.g., Holy Ground forcing Rötschreck checks,
certain Curses keying off Dominate/Presence/Obfuscate resistance) — V20
kept these Discipline names and their broad strokes intact, so most of
this ports cleanly, but if a specific power's exact mechanical wording
matters to your table, it's worth spot-checking that power's V20
write-up rather than assuming zero drift.

## A conversion package

Here's a practical set of house rules to reconcile the two books for a
V20 Dark Ages chronicle. This is a fan conversion, not an official one —
treat it as a starting point to playtest and adjust, not gospel.

**Chargen budgets — use as printed, or borrow *Hunters Hunted II*'s
Ability spread if you want tougher hunters.**
Inquisitor's Attribute (6/4/3), Ability (11/7/4), freebie point (21 at
5/dot Attributes, 2/dot Abilities), Virtue (7), and Background (5)
numbers already match V20's own mortal/ghoul-tier chargen exactly. Run
them as written for a game that keeps Inquisitor's original "mortals are
fragile relative to Cainites" calibration. If your table would rather
lean on the newer, more V20-native precedent instead, swap in *Hunters
Hunted II*'s 13/9/5 Ability spread (keeping Attributes at 6/4/3, or its
own optional 7/5/3) — this produces noticeably more capable inquisitors
and is a legitimate, officially-sourced V20 alternative rather than a
from-scratch house rule. Either way, the only genuinely new addition on
top of whichever budget you pick is the inquisitor-specific track
(starting Superior Virtue dot beyond the free one, an Endowment or order
benefit, an Orison, and the Curse/Merit-Flaw layer), which the book
already prices out itself in the same chargen sequence, so nothing needs
to be imported from V20 or reconciled against it.

**Superior Virtues / Conviction / Piety / Curses — port wholesale, unchanged.**
Because V20's base Virtues are the same three traits on the same 1–5
scale, extending them to a 10-dot cap via Faith/Wisdom/Zeal works exactly
the same way mechanically in V20 as in the classic system. No conversion
math is actually needed here — just import Chapter Four and Five's
subsystem as printed, recalculating starting Willpower using the book's
own formula (Courage + Zeal) after Attributes/Abilities are set. There's
no V20 shortcut available for this one (see conflict #1 above) —
*Hunters Hunted II*'s Numina system solves a related but different
design problem and isn't a substitute.

**True Faith — three options, pick one explicitly.**
1. *As Inquisitor intends:* PC inquisitors use Superior Virtues/Piety in
   place of True Faith entirely, and V20's standard True Faith Trait is
   reserved for NPC mortals only (saints, other unaffiliated hunters,
   etc.) exactly as V20 already defaults.
2. ***Hunters Hunted II* hybrid:** if a PC in your troupe isn't a
   card-carrying inquisitor (a devout hanger-on, a mortal ally, a
   Storyteller character promoted to more screen time), give them
   *Hunters Hunted II*'s capped True Faith Numina Path instead of full
   Superior Virtues — a lighter-weight, V20-native way to let a
   non-inquisitor mortal have a taste of the same "faith repels the
   undead" fantasy without importing the inquisitor-specific corruption
   engine wholesale for a character who isn't actually part of the order.
3. *Sidebar conversion, if you need a single number:* Inquisitor's own
   conversion (Servant = True Faith 1, Acolyte = 2, Advocate = 3, Judge =
   4) is there if something outside the inquisitor's own mechanics needs
   to reference "their True Faith rating" as a flat number — a relic
   that reacts to True Faith, for instance.

Whichever you choose, avoid letting two of the three systems apply to
the same character at once — that's the actual risk, not any one system
in isolation.

**Merits & Flaws — verify, don't assume; start from two confirmed collisions.**
Before a session zero, walk Inquisitor's disallowed list and its new
Merits/Flaws chapter against V20's actual Merits & Flaws appendix
together with your group, and flag anything renamed, removed, or
recosted. Two known collisions to resolve explicitly rather than
discover mid-session: **Holy Aura** (2-pt Merit in both books, different
effects — pick one or merge them) and **Ecstatic** (same phenomenon, a
2-pt Flaw in Inquisitor and a 2-pt Merit in *Hunters Hunted II* — decide
whether your table treats ecstatic fits as a liability, an asset, or
lets the player choose which framing fits their character). Beyond
those two, this is still a five-minute table exercise, not a rewrite —
most of the classic entries either survived into V20 intact or have an
obvious V20 equivalent.

**Backgrounds and new Skills — no changes needed, with two edition-spanning
echoes worth knowing.**
Torture and Interrogation slot in as new Skills with no conflict (V20
explicitly supports custom Skills), and every Background Inquisitor uses
— the new ones (Chapter-House, Exposure, Flock, Holy Relics, Rank) and
the standard ones it reuses (Allies, Contacts, Influence, Mentor,
Resources, Retainers) — already exist under the same names in V20 Dark
Ages. Two are worth flagging for flavor even though no mechanical fix is
needed: Inquisitor's **Holy Relics** Background (a personal relic that
recharges Conviction) is the same underlying concept as the Society of
Leopold's **Reliquary** Background in *Hunters Hunted II* (p. 123-124:
Church-granted access to a relic from the Vatican vaults) — different
names for the same idea, seven centuries apart. Separately, Inquisitor's
**Rank** Background (standing within the Inquisition hierarchy)
corresponds to the Society of Leopold's **Status** Background in
*Hunters Hunted II* (p. 123-124: Tertiary → Councilor → Abbé → Censor →
Provincial) — *not* to *Hunters Hunted II*'s own, differently-scoped
"Rank" Background, which belongs to an unrelated chapter (US government
agents). Worth a one-line note at the table so nobody reaches for the
wrong "Rank."

**Optional lore hooks.**
- *Leopold von Murnau, across the centuries:* if your troupe includes,
  or interacts with, a member of the House of Murnau — Inquisitor's own
  Prelude protagonist is Brother Leopold von Murnau, whose ultimate fate
  the book leaves open — consider that he's almost certainly the same
  "Leopold of Murnau" venerated centuries later as the founding martyr
  of the modern Society of Leopold in *Hunters Hunted II* (killed by a
  vampire, author of "The Testament of Leopold," commemorated in a relic
  made from his bones). This gives a V20 Dark Ages chronicle centered on
  Leopold, or on House Murnau generally, a built-in, edition-spanning
  payoff: the PCs' actions can be played as the seed of an organization
  whose full V20 write-up already exists in this library's
  `v20-hunters-hunted-ii` bundle. See that bundle's `book_index.md`
  ("Cross-cutting themes") and this library's top-level `library_index.md`
  ("The modern view from the other side") for the fuller case.
- *The Cainite Heresy:* V20 Dark Ages independently describes its own
  "Cainite Heresy," attributed specifically to Lasombra priests and
  bishops who preach vampirism as a mark of divine favor. Inquisitor's
  Crimson Curia (a Cainite conspiracy inside the Church hierarchy) never
  names the Lasombra as its source, and V20's Heresy entry never
  mentions a Crimson Curia — but nothing stops you from treating them
  as the same phenomenon seen from two angles, which gives your V20
  conversion a built-in, edition-spanning central mystery for the
  inquisitors to chase.

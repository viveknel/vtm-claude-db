# Running *Dark Ages: Inquisitor* with V20

*Dark Ages: Inquisitor* (White Wolf, 2002) says outright that it "is not a
complete game" and requires the *original* *Dark Ages: Vampire* core
rulebook — classic Storyteller System, not V20's revised trait set. In
practice, though, the real gaps are narrower than that disclaimer
suggests. Below is what's actually incompatible, what already lines up
fine, and a conversion package to make the book playable at a V20 Dark
Ages table.

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

This matters practically: it means Inquisitor's core resolution
mechanics — combat, Virtue rolls, Willpower spends, and chargen itself —
don't need to be rebuilt. The real incompatibilities are narrower than
they first look, and concentrated in one entirely book-specific
subsystem V20 has no equivalent for, plus a couple of smaller frictions.

## Where they actually conflict

### 1. Superior Virtues, Conviction, Piety, and Curses have no V20 equivalent

Inquisitor's entire Chapter Four/Five mechanical spine — Superior Virtues
(Faith/Wisdom/Zeal extending Conscience/Self-Control/Courage from a 5-dot
cap to 10), Conviction (a 1–10 fuel resource for Blessings), Piety (a
Road-like moral-standing score), Callousness (triggered when Conviction
exceeds Piety), and the five Curse categories culminating in Cocytus —
is a bespoke system built for the classic line. V20 doesn't revise or
replace it, because V20 doesn't include a hunter subsystem at all; it's
simply absent. This isn't so much an *incompatibility* as a *gap*: there's
nothing in V20 to reconcile it against, so the whole subsystem has to be
imported wholesale rather than converted piecemeal.

### 2. True Faith is handled two different ways

V20 core gives **True Faith** as a Storyteller-controlled Trait (rated
1–5, mechanical effects escalating by dot, from warding off vampires at
Faith 1 up to forcing a vampire to flee at Faith 5) — it's explicitly rare
and not normally player-purchasable. Inquisitor deliberately *doesn't*
use this Trait for player characters; instead it builds Superior
Virtues/Piety as True Faith's in-fiction replacement and gives a sidebar
conversion for translating between the two systems. If you run Inquisitor
unmodified inside a V20 game, you now have two parallel "resist the
supernatural through faith" systems in play at the same table (V20's
True Faith for any NPC mortals, Superior Virtues for PC inquisitors) —
workable, but it needs an explicit ruling, or players and Storytellers
will default to whichever one they remember first.

### 3. The Merits & Flaws catalog has drifted

Inquisitor's "Disallowed" list and its own roughly twenty new
Merits/Flaws are keyed to the *classic* core Vampire Merits & Flaws
catalog (it explicitly disallows things like *13th Generation*, *Prey
Exclusion*, *Blood Madness* — all classic-line entries). V20 reorganized
and partly rewrote its Merits & Flaws chapter. Some names, costs, and
even the existence of specific entries differ between the two editions.
None of this breaks Inquisitor's *new* Merits/Flaws (those are
self-contained), but the disallowed list and any cross-references to
"standard Vampire Merits/Flaws" need a line-by-line check against V20's
actual catalog rather than an assumed 1:1 match.

### 4. Terminology and cross-references

Smaller frictions worth flagging for a table: Inquisitor calls its extra
chargen points "bonus points," V20 calls the equivalent pool "freebie
points" (same function, different label — trivial, but worth a shared
vocabulary at session zero). Blessings and Curses occasionally reference
specific vampire Discipline behavior (e.g., Holy Ground forcing
Rötschreck checks, certain Curses keying off Dominate/Presence/Obfuscate
resistance) — V20 kept these Discipline names and their broad strokes
intact, so most of this ports cleanly, but if a specific power's exact
mechanical wording matters to your table, it's worth spot-checking that
power's V20 write-up rather than assuming zero drift.

## A conversion package

Here's a practical set of house rules to reconcile the two books for a
V20 Dark Ages chronicle. This is a fan conversion, not an official one —
treat it as a starting point to playtest and adjust, not gospel.

**Chargen budgets — use as printed.**
Inquisitor's Attribute (6/4/3), Ability (11/7/4), freebie point (21 at
5/dot Attributes, 2/dot Abilities), Virtue (7), and Background (5)
numbers already match V20's own mortal/ghoul-tier chargen exactly. Run
them as written. The only genuinely new addition on top of that budget
is the inquisitor-specific track (starting Superior Virtue dot beyond
the free one, an Endowment or order benefit, an Orison, and the
Curse/Merit-Flaw layer) — which the book already prices out itself in
the same chargen sequence, so nothing needs to be imported from V20 or
reconciled against it.

**Superior Virtues / Conviction / Piety / Curses — port wholesale, unchanged.**
Because V20's base Virtues are the same three traits on the same 1–5
scale, extending them to a 10-dot cap via Faith/Wisdom/Zeal works exactly
the same way mechanically in V20 as in the classic system. No conversion
math is actually needed here — just import Chapter Four and Five's
subsystem as printed, recalculating starting Willpower using the book's
own formula (Courage + Zeal) after Attributes/Abilities are set.

**True Faith — retire it for inquisitor PCs, keep it for NPCs.**
Formally rule that player-character inquisitors use Superior
Virtues/Piety in place of True Faith entirely, per the book's original
intent, and reserve V20's standard True Faith Trait for NPC mortals only
(saints, other unaffiliated hunters, etc.) exactly as V20 already
defaults. This avoids two overlapping "resist the supernatural" systems
sitting on the same character.

**Merits & Flaws — verify, don't assume.**
Before a session zero, walk Inquisitor's disallowed list and its new
Merits/Flaws chapter against V20's actual Merits & Flaws appendix
together with your group, and flag anything renamed, removed, or
recosted. This is a five-minute table exercise, not a rewrite — most of
the classic entries either survived into V20 intact or have an obvious
V20 equivalent, but it's worth confirming rather than guessing mid-game.

**Backgrounds and new Skills — no changes needed.**
Torture and Interrogation slot in as new Skills with no conflict (V20
explicitly supports custom Skills), and every Background Inquisitor uses
— the new ones (Chapter-House, Exposure, Flock, Holy Relics, Rank) and
the standard ones it reuses (Allies, Contacts, Influence, Mentor,
Resources, Retainers) — already exist under the same names in V20 Dark
Ages.

**Optional lore hook.** If it's useful for your chronicle: V20 Dark Ages
independently describes its own "Cainite Heresy," attributed specifically
to Lasombra priests and bishops who preach vampirism as a mark of divine
favor. Inquisitor's Crimson Curia (a Cainite conspiracy inside the Church
hierarchy) never names the Lasombra as its source, and V20's Heresy entry
never mentions a Crimson Curia — but nothing stops you from treating them
as the same phenomenon seen from two angles, which gives your V20
conversion a built-in, edition-spanning central mystery for the
inquisitors to chase.

---
type: concept
title: "Elements, pantheons and seed campaign arc"
created: 2026-11-23
updated: 2026-11-23
status: seed
tags:
  - concept
  - gdd
  - world-building
complexity: basic
domain: game-design
related:
  - "[[wiki/concepts/boss-and-race-theme-overlays|Boss and race theme overlays]]"
  - "[[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]]"
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/run-structure-seeds-and-biome-tiers]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-six-elements
---

# Elements, pantheons and seed campaign arc

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *World Building* and *Narrative* chapters of
[[wiki/sources/source-gdd-06-world-generation|GDD 06]]. The *Game Setting*
chapter (gods' origin, mortal civilisations, the Dungeon, the evershifting
dungeon) is headings only.

## Elements and alignments

- **Six elements**: Earth, Water, Air, Fire, Wild, Power – each with three
  alignments: positive, negative, neutral.
- Pairs of elements make **quasi-elements** (examples: metal, ice, magma, wood,
  acid, poison).
- Three elements tie to the main stats (STR, DEX, INT); three (the same or the
  others, undecided) tie to the resources (health, mana, stamina).
- Six crystal gems carry each element's power; dragons have scales of those
  colours, and rare aligned dragons hold the positive or negative variant (e.g.
  the moon dragon: curses, negative earth/core magic).

## Runic language as a clue system

The doc leans against a real procedural language: no letters, probably not
procedural, contextual meaning without consistent grammar ("Fire Alive",
"Fire Danger", "Dead Alive"). Requirements that matter for puzzles:

- elemental symbols recognisable in every script; STR/DEX/INT and alignment
  concepts may have runes too;
- each theme and creature group gets a written description;
- each element has a **symbolic animal** (may differ per culture or biome),
  "useful for puzzles".

**For the generator (synthesis):** element, stat and animal runes are the
clue vocabulary used by the Decision puzzle, elemental runestones, seals and
elemental riddles (see
[[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]]).
A clue key can therefore be typed by element, letting the content stage pick a
matching rune and biome.

## Pantheons

- Gods come in **trios per religion**: three neighbouring elements, aligned
  blessed / cursed / neutral. Up to three gods per element, differing in
  alignment. Elements are domains, not the gods' whole character.
- **Gods of action** reward deeds (kill monsters that desecrated a temple, stop a
  demon-summoning ritual, spare critters in the biome); **gods of virtue** reward
  status (INT above a threshold, low health, full inventory).
- A character follows one god, whose **edicts** raise and **anathemas** lower
  reputation. Faithful players get boons at altars; other gods bless only major
  deeds; hostile gods ignore your deeds; with no god, all start lower. Only the
  followed god's reputation is shown.

Relevance: deeds such as "kill the temple desecrators" match the sheet's
*Sequence Lock* example (offering loot from enemies who desecrated a temple),
so altars could be lock sites with god-specific keys. The *Adventure Camp*
notes that most deities punish attacking other adventurers.

## Seed campaign arc

The *Narrative* chapter turns the generator into a campaign of **seeds**:

- regular seeds slightly altered **mid generation**; the first few maybe end
  after the first boss;
- **MacGuffins** – tailored seeds whose story is about artefacts the village needs;
- **Betrayal** – halfway, someone betrays the party; a series of seeds with an
  open ending, altered so the betrayer reached the end first; forced frenzy
  meter, slightly higher difficulty;
- **Finale** – last seed, custom boss (the betrayer), higher but still moderate
  difficulty.

**For the generator (synthesis):** this needs hooks to inject a fixed goal
(artefact key, custom boss) into an otherwise random story graph, and a
difficulty parameter per seed – both belong to the generation-control work
package in [[wiki/questions/scope-and-open-questions|Scope and open questions]].

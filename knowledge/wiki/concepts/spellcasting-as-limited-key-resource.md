---
type: concept
title: "Spellcasting as a limited key resource"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - magic
  - lock-and-key
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions as locks and keys]]"
  - "[[wiki/entities/noita-style-staff-enhancement-ideas|Noita-style staff enhancement ideas]]"
  - "[[wiki/concepts/items-as-keys]]"
sources:
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04 – Magic and Statuses Overview]]"
claim_ids:
  - clm-explorio-magic-limited-usage
  - clm-explorio-spell-schools-list
---

# Spellcasting as a limited key resource

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Design intent

From *The point of spellcasting*:

- **Game goals**: add gameplay depth; give enemies unique, recognisable
  abilities that the player can also obtain.
- **Player goals**: a limited-use "get out of jail" card, a special player
  fantasy, recognising and exploiting enemy weaknesses.
- **Means**: magic is a **limited-usage tool** for monsters and most classes.
  Non-magical players find **charged spellcasting foci** and use them as
  powerful consumables; magic-focused characters have a spell repertoire they
  charge onto **staves** with a **mana** resource.
- Open question left in the doc: how magic is viewed in the world and whether
  any kind is forbidden.

## Spells listed

All five reference Brogue wands or staffs.

| Spell | Effect in doc | Possible key role (synthesis) |
|---|---|---|
| Telepathy / Detect life | (Brogue Telepathy) | CLUE key – reveals monsters behind a lock |
| Summon / Beckon | (Brogue Wand of Beckoning) | pull a monster to a spot – Monster Assist |
| Domination | target treats caster as an ally | Monster Assist, Charm-like |
| Blinking | teleports to the obstacle the spell hit | traversal over a gap – Tool assist |
| Summoning / Conjuration | creates phantom weapons | combat only |

## Spell schools

- Base schools: **Pyromancy, Water, Power, Air, Earth, Wild** (with a link to
  the Superpower Wiki's magical powers list).
- Quasi elements: **Wood, Metal, Magma**.
- Every school section is empty except Water: a *water trap* spell that
  teleports the target into deep water when hit.

## Mapping to key dimensions

Synthesis, not in the doc. GDD 04's split maps onto the
[[wiki/concepts/key-dimensions|key usage count]]:

| GDD 04 | Key usage | Note |
|---|---|---|
| charged focus used by a non-mage | consumable | like the potions in Tool assist |
| staff recharged with mana | reusable, rate-limited | reusable only while mana lasts – neither pure value fits |
| enemy ability the player learns | reusable | an enemy guarding a lock can also be the source of its key |

The mana-limited staff suggests a third usage value (recharging / rate-limited
key) that neither the product sheet nor the code has. The schools (fire, water,
air, earth, metal, wood, magma) line up with the elemental reactions in
[[wiki/concepts/elemental-status-interactions-as-locks-and-keys|elemental status interactions]],
so a lock typed by element could be opened by any key of that school.

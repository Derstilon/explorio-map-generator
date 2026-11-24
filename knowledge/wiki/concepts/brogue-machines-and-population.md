---
type: concept
title: "Brogue machines and dungeon population"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - inspiration
  - brogue
complexity: advanced
domain: procedural-generation
aliases:
  - Brogue
  - Machines
  - Blueprints
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/dev-branch-codebase|Dev branch codebase]]"
  - "[[wiki/concepts/lock-logic-gates|Lock logic gates]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-inspiration-web-research|Inspiration web research]]"
  - "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
claim_ids:
  - clm-explorio-brogue-key-chains
---

# Brogue machines and dungeon population

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Inspiration for: populating the dungeon (the content stage after the story
graph). The empty `machine_wfc/machines.py` in dev is named after this idea.
All facts below come from the Brogue CE source
([Architect.c](https://raw.githubusercontent.com/tmewett/BrogueCE/master/src/brogue/Architect.c),
[Rogue.h](https://raw.githubusercontent.com/tmewett/BrogueCE/master/src/brogue/Rogue.h),
[Items.c](https://raw.githubusercontent.com/tmewett/BrogueCE/master/src/brogue/Items.c),
[GlobalsBrogue.c](https://raw.githubusercontent.com/tmewett/BrogueCE/master/src/variants/GlobalsBrogue.c));
the Brogue wiki was not reachable.

## Level build order (`digDungeon`)

Rooms → `addLoops` → lakes → non-machine autogenerators → reward machines →
machine autogenerators (flavour) → lake clean-up → bridges.

- **Loops** are added only where a wall has floor on both sides whose pathing
  distance exceeds 20 – a loop must be a real shortcut.
- **Lakes** (water, lava, chasm, brimstone) are placed only if a flood fill
  shows the level stays connected.

## Machines

A **blueprint** is a template with flags and a feature list; a **machine** is
its instance. Roles: reward room, **vestibule** (guards a door), **key holder**
(guards a key), flavour area.

- `MF_OUTSOURCE_ITEM_TO_MACHINE` + `BP_ADOPT_ITEM`: a feature hands its item
  (key) to another machine, which recursively builds key chains: reward room →
  locked-door vestibule → key-holder machine → possibly another key.
- `MF_ALTERNATIVE`: build only one of a set of features (an OR choice).
- `MF_KEY_DISPOSABLE` (consumed here), `MF_SKELETON_KEY` (opens every lock in the
  machine); a key holds up to 20 lock locations, each with its own disposability.
- `TM_PROMOTES_WITH_KEY` / `WITHOUT_KEY`: tiles react to a key being placed or
  removed – altar cages close when you take one item and reopen when you put it
  back (library: "one item at a time").
- `BP_TREAT_AS_BLOCKING` / `BP_REQUIRE_BLOCKING`: abort a machine that would (or
  would not) break connectivity.

## Catalogue examples

- Vestibules: locked door, secret door, lever (portcullis / exploding wall),
  flammable barricade, statue needing a shattering scroll, pressure plate hit by a
  thrown item, guardian on a glyph.
- Key holders: flood room, collapsing floor, levitation challenge (potion **or**
  a lever elsewhere), lava moat (levitation, fire immunity **or** lever), thief
  fleeing with the key, guardian lured into water, sacrifice altar (lure a chosen
  monster), electric crystals, boss holding the key.

## Mapping to Explorio

| Brogue | Explorio |
|---|---|
| vestibule + key holder + outsourcing | production 1 c-variants (lock in front of a key) as recursive chains |
| `MF_ALTERNATIVE`, "potion or lever" | OR gate, Tool assist, spare keys |
| library altar cages | NAND / XOR with temporary mode (Mouse Trap, row 60 "put items back") |
| disposable / skeleton key | consumable / reusable key, multi-lock keys (doc's `locks(n)`) |
| lured monsters, thief, boss carrier | enemy-as-key (Monster Assist) |
| blocking checks, lake flood fill | solvability validation |
| flavour machines | encounter biomes |

The Brogue machine catalogue is a good template for the missing **concrete
content** step: each Explorio archetype becomes a set of blueprints with
feature lists, picked per biome.

## From the game design docs

- [[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]] names Brogue as the level-generation quality to reach
  ([[wiki/entities/reference-games-and-borrowed-features|Reference games and borrowed features]]).
- Enemy-as-key content for Explorio: slime key carriers, the Centurion's energy
  cell, monkey/gremlin thieves ([[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]]).
- Brogue's levitation key holder (levitation crosses chasms) fits Explorio:
  the owner decided levitation crosses chasms but cannot rise a layer ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]),
  overriding [[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]].

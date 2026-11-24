---
type: entity
title: "Monster encounter and biome affinity"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - bestiary
  - biomes
entity_type: catalogue
role: "Which monsters the bestiary ties to environment biomes and encounter themes"
first_mentioned: "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/bestiary-monster-families|Bestiary monster families]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/entities/biome-catalogue-with-generation-hints]]"
sources:
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01 – Bestiary]]"
claim_ids:
  - clm-explorio-slime-encounter-requirement
  - clm-explorio-mimic-lab-only
---

# Monster encounter and biome affinity

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Why this matters

The dev code assigns two kinds of biome to story-graph areas (see
[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]): 15
**environment biomes** (caves, dungeon, dwarven ruins, forest, frozen wastes,
molten caverns, abandoned castle, mineshaft, laboratory, desert cenotaph,
overgrown garden, swamp, abandoned settlement, forgotten workshop, sunken
caverns) and 18 **encounter biomes** (orcs, trolls, goblins, werewolf, vampires,
elements, necromancy, arcane, riches, infested, alchemy, hunting, sacral, cursed,
traps, help, dragons, mechanical). The bestiary is the first source that says
which monsters belong where. It **extends** the biome page: the two layers are
not independent, since several monsters need a specific environment *and* some
need a specific encounter.

## Hard requirements stated in the doc

These use the doc's words "requires", "only" or "access to".

| Monster | Requirement in the doc | Maps to (synthesis) |
|---|---|---|
| Magma Slime | "Requires Specific Environment → Magma Level" | environment: molten caverns |
| Blood Slime | "Requires Specific Encounter → Necromancy or Vampires" | encounter: necromancy, vampires |
| Holy Water Slime | "Requires Specific Encounter → Sacral or Werewolves" | encounter: sacral, werewolf |
| Chest Mimic | the only mimic type that can appear outside the laboratory | other mimics → environment: laboratory |
| Red Orcs / Frost Orcs | access to magma / cold locations | molten caverns / frozen wastes |

## Soft affinities (spawn hints)

"Higher chance", "spawns in", "locations" or a culture tag in the doc. Matching
the doc's words to the code's biome names is synthesis; elementals are placed by
the doc's general rule that they prefer an environment matching their element.

| Encounter biome (code) | Monsters the doc links to it |
|---|---|
| orcs | orc tribes and classes; Booze Slime (protected by an orc tribe); Drummer for camp encounters |
| goblins | goblin classes, hobgoblins, spider and wolf pets |
| trolls | seven troll types and their elites |
| werewolf | werebeasts, moonlight sources (moonshine, moon pond, moonstone, moon dragon); Holy Water Slime |
| vampires | vampire spawn, bruxa, vampire lord; vampire bats; gargoyles (made by vampires); Blood Slime; Blood Elemental |
| elements | slimes, elemental spawns, manifestations, genies |
| necromancy | Blood Slime; Flesh Aberration (ritual / unholy / necromantic places); graveyard trolls; undead |
| riches | Golden Slime ("higher chance in Treasure Encounter"); Treasure Elemental (treasury); Looter orc tribe; golden scarab; Magpie gremlin |
| infested | insect and vermin critters (rats, ants, spiders, eggs); synthesis, the doc does not use the word |
| alchemy | Lab golem, Homunculus, Doppelganger, mimics (laboratory); crowfolk are "masters of alchemy" |
| sacral | Holy Water Slime; Mystic orc tribe (chapels, cemetery) |
| dragons | kobolds (dragon worshippers), Dragon Priest; dragons, wyverns, faery dragon |
| mechanical | dwarven automatons; Machine orc tribe; kobold tinkerer; rune golems |
| traps | kobold bear traps, feral orc camp traps, gilded arachnid tripwires, mirage arthropods |
| hunting | Feral orc tribe and Beastmaster; primal trolls; Mama Bear |

| Environment biome (code) | Monsters the doc links to it |
|---|---|
| dwarven ruins | automatons; rune golems hidden as statues; automaton fish and eels in their water; Machine orcs (forges); Looter orcs (treasuries) |
| forest | bear cub / Mama Bear, wolves, foxes, ants; Feral orcs; forest trolls; treants and sylvanids |
| swamp | leeches, troglodytes, frog people |
| frozen wastes | frost orcs, ice trolls, ice slime and golem, Wendigo |
| molten caverns | Magma Slime, Magma Golem, red orcs, magma revenant |
| abandoned castle | gargoyles ("gothic castles") |
| laboratory | all mimic types except chest mimic; Lab golem; Homunculus; Doppelganger |
| desert cenotaph | scorpions, scarabs, sandling, mirage arthropods, sand worms, sphinx, canisphinx, desert mummies |
| sunken caverns | crabs ("aquatic caves"), coral slime, naga, Kelpie |
| caves / dungeon | rats (dark rooms), beetles, spiders, cave trolls |

## Vocabulary mismatches with the code

The doc uses location names that are not in either code list (synthesis):

- Locations: jungle, cemetery, chapels, ruins (non-dwarven), treasury, magma
  level, marshlands, oriental biome, desert (vs `desert cenotaph`), aquatic caves.
- Encounter kinds the doc names that are not themes but **encounter shapes**:
  camp encounter (orc drummer), chase encounter (Holy Water Slime), gauntlet
  encounter (chess golems), gremlin encounter (abductor spider is a "variant of
  gremlin encounter").
- Families with no matching encounter biome: pirates, demons, void
  monstrosities, sylvanids, amphibious humanoids, mimics as a theme. `cursed`
  and `arcane` have no explicit monster in the doc.

## Open questions

- Should encounter biomes carry `required_environment` / `allowed_environment`
  lists (they currently have only an empty `overlay_restrictions`)?
- Should a monster's encounter requirement (Blood Slime) become a constraint
  on the encounter-biome overlay, or a filter at spawn time?
- Is "encounter shape" (camp, chase, gauntlet) a separate axis from encounter
  theme?

---
type: concept
title: "Biomes and zone layering"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - biomes
complexity: intermediate
domain: procedural-generation
related:
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
---

# Biomes and zone layering

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Intent

A story graph becomes one **biome / zone** of the dungeon: a few interconnected
**layers** (floors). Biomes give the zone its environment and its encounter
themes. Stated by the project owner on 2026-11-23; no layer concept exists in
the dev code yet.

## Environment biomes (`biome_injections/environment_biomes.py`)

- 15 biomes defined (caves, dungeon, dwarven ruins, forest, frozen wastes, molten
  caverns, abandoned castle, mineshaft, laboratory, desert cenotaph, overgrown
  garden, swamp, abandoned settlement, forgotten workshop, sunken caverns).
- Each has `valid_start`, `valid_end` and `adjacency_restrictions` (biomes that
  must not border it).
- The algorithm uses only `caves` and `dungeon`, seeds `L0`/`K0` into the two
  halves, makes a randomized partition and refines it with Kernighan–Lin
  bisection on the graph without `unlocks` edges.
- `valid_start`, `valid_end` and adjacency restrictions are **not used**.

## Encounter biomes (`biome_injections/encounter_biomes.py`)

- 18 themes (orcs, trolls, goblins, werewolf, vampires, elements, necromancy,
  arcane, riches, infested, alchemy, hunting, sacral, cursed, traps, help,
  dragons, mechanical), each with an empty `overlay_restrictions`.
- Uses a fixed sample `orcs, trolls, traps, riches`; picks 4 random nodes and
  tags each plus up to 3 access-neighbours. Themes can overlap on a node.

## Open design points

- How layers are cut from the story graph (by depth? by lock? by cycle?).
- Whether biome choice should constrain archetypes (e.g. Burning bridges needs
  fire; Monster Assist needs a fitting monster per environment) – the sheet's
  examples are already biome-flavoured.
- Using adjacency restrictions and start/end validity, which are defined but
  ignored.

## From the game design docs

- **Biome catalogue:** [[wiki/sources/source-gdd-06-world-generation|GDD 06]] lists 41 example biomes and a to-do of biome
  attributes – connections, weights, tags, normal/hard version, size (Large,
  Small, Unique Layer), end-point/boss eligibility, encounters per layer by
  neighbouring biomes. See [[wiki/entities/biome-catalogue-with-generation-hints|Biome catalogue with generation hints]].
  End-point eligibility and connections match the code's unused `valid_end` and
  adjacency rules.
- **Layers:** first design statements anywhere: "Unique Layer" biomes fill one
  layer; "if the layer is surrounded by green biomes from both sides" may imply a linear layer
  order; hard versions and vertical sequences (Gothic Castle → Gothic Dungeons →
  Lord's Cenotaph) suggest multi-layer zones of related biomes; the Mimic boss
  theme builds two identical-layout layers.
- **Name drift:** the code's 15 environment biomes are a renamed or merged subset
  of the GDD list ("desert cenotaph" blends two GDD biomes; "laboratory" and
  "forgotten workshop" are one; GDD 02 also names Cold, Defiled Church, Cemetery,
  Treasury, Minotaur Maze, Crypt). To be fixed later ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
- **Encounter themes:** GDD 06 calls them race, magic and boss themes
  ([[wiki/concepts/boss-and-race-theme-overlays|Boss and race theme overlays]]); *mimic* has
  no code theme, and code themes riches, help, traps have no GDD counterpart.
- **Biome–faction pairs:** [[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]] pairs each biome with a faction (14 pairs,
  e.g. Castle & Vampires, Sewers & Ratfolk) and gives difficulty tiers (easy /
  hard / lower, hardmode variants); the code keeps the two layers independent
  ([[wiki/concepts/run-structure-seeds-and-biome-tiers|Run structure, seeds and biome tiers]]).
- **Monster requirements cross both layers:** [[wiki/sources/source-gdd-01-bestiary|GDD 01]] ties Magma Slime to magma
  levels, Blood Slime to necromancy/vampires, Holy Water Slime to sacral/werewolves,
  non-chest mimics to laboratories
  ([[wiki/entities/monster-encounter-biome-affinity|Monster encounter and biome affinity]]).
  Encounter biomes may need allowed/required environment lists; encounter shapes
  (camp, chase, gauntlet) look like a separate axis from themes.
- **Difficulty:** [[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]] asks for a challenge-rating budget per layer rising
  with depth, and its enemy pipeline (environment → encounter → enemy pool)
  matches the code's split ([[wiki/concepts/difficulty-scaling-across-depth|Difficulty scaling across depth]]).
- **Elements:** frozen wastes, molten caverns, swamp and sunken caverns map onto
  the element reactions in [[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions]].

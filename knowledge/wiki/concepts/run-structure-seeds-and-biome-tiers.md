---
type: concept
title: "Run structure, seeds and biome tiers"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - generation
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/meta-progression-and-unlocks|Meta progression and unlocks]]"
  - "[[wiki/questions/scope-and-open-questions|Scope and open questions]]"
  - "[[wiki/concepts/seed-save-and-run-reproducibility]]"
  - "[[wiki/concepts/elements-pantheons-and-seed-campaign-arc]]"
sources:
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05 – Gameplay and Progression Systems]]"
claim_ids:
  - clm-explorio-three-bosses-per-run
  - clm-explorio-keyless-first-boss
  - clm-explorio-seeded-missions
---

# Run structure, seeds and biome tiers

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

GDD 05 has no section on dungeon structure, but its achievements, hub and
event sections state several facts about a run. They are collected here
because they constrain the generator.

## Facts stated in the doc

| Fact | Where in GDD 05 |
|---|---|
| The mission table offers **seeded dungeons** with a plot hook; a custom seed can be entered | Hub Town – Mission table |
| Hub-provided seeds should be managed so each holds something achievable; maybe a server crawls seeds from the current date, or a static seed list shared by all players | Achievements – Tailored system |
| A run has **up to 3 bosses** ("Defeat all 3 bosses in a single run"; first and second boss named) | Achievements – Dungeon Crawler |
| A run has several **layers** ("Visit every layer in a single run") | Achievements – Cartographer |
| Biomes come in tiers: **easy**, **hard and lower** biomes; biomes have a **hardmode** variant ("Discover hardmode Dwarven Ruins", "hardmode Jungle") | Achievements – Cartographer, Biome specific examples |
| Runs have a **depth** ("Getting to the Depth X without being seen") | Achievements – Loose Ideas |
| The first boss can be defeated **without using a single key** (achievement "Where Did I Put My Keys?", reward: Prisoner class) | Achievements – Dungeon Crawler |
| Gremlin Lairs, easter-egg minibosses and gauntlets exist as findable secrets | Achievements – Loose Ideas |
| Seasonal events use a special generator with handmade seeds for a questline, plus regular generation | Events |

## Biome and faction pairs

The doc wants one achievement category per biome type and lists them as
environment–faction pairs: Dwarfs & Automatons, Desert & Arthropods, Orcs &
Trolls & Goblins, Jungle & Dinosaurs, Swamp & Frogfolk, Forest & Werewolves,
Castle & Vampires, Graveyard & Undead, Sewers & Ratfolk, Elementals, Demons &
Archons, Fungi & Troglodyte, Pirates & Merfolk, Treasures & Dragons.

Comparison with [[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]
(code on `dev`):

| GDD 05 pair | Code environment biome | Code encounter theme |
|---|---|---|
| Dwarfs & Automatons | dwarven ruins, forgotten workshop | mechanical |
| Desert & Arthropods | desert cenotaph | infested? |
| Orcs & Trolls & Goblins | – | orcs, trolls, goblins |
| Jungle & Dinosaurs | – (overgrown garden?) | hunting? |
| Swamp & Frogfolk | swamp | – |
| Forest & Werewolves | forest | werewolf |
| Castle & Vampires | abandoned castle | vampires |
| Graveyard & Undead | – | necromancy |
| Sewers & Ratfolk | – | – |
| Elementals | molten caverns, frozen wastes? | elements |
| Demons & Archons | – | sacral / cursed? |
| Fungi & Troglodyte | caves? | – |
| Pirates & Merfolk | sunken caverns? | – |
| Treasures & Dragons | – | riches, dragons |

Question marks are guesses (synthesis). GDD 05 pairs an environment with a
faction, while the code keeps environment and encounter as two independent
layers; jungle, graveyard, sewers, demons and pirates have no environment biome
in code.

## Generator implications (synthesis)

1. **Keyless route to the first boss.** For "Where Did I Put My Keys?" to be
   achievable, the first boss must be reachable without any key in at least
   some seeds: via OR gates with non-key alternatives (picklocks, breaking,
   stealth, monster assist) or via secret edges. In the vault's model this is
   a reachability query: "goal reachable with the key set restricted to non-key
   means". Note that "key" here means an in-game key item, narrower than the
   vault's abstract key.
2. **Achievement-aware seeds.** "Something achievable in each hub seed" asks
   the generator (or a crawler over it) to report per seed which properties it
   has (layers, boss count, biomes, archetypes). That argues for a stable,
   queryable export (work package 10).
3. **Layers per run, bosses per run.** Up to 3 bosses and several layers per
   run suggests a run spans several zones or layers; how bosses map to zones is
   not stated. Adds a data point to the open question "does one story graph
   equal one zone, or one layer?".
4. **Difficulty tiers.** Easy / hard / lower biomes and hardmode variants give
   a difficulty axis per biome, which can drive lock budgets and failable share
   per zone (work package 6).
5. **Seasonal generator variants.** Events want themed generation (icy, water
   and fire, critters, booze, pirates, all-cursed loot for April Fools), i.e.
   recipe-level overrides of biome and content weights.

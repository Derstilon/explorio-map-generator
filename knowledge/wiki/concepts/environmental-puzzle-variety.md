---
type: concept
title: "Environmental puzzle variety (Genshin Impact)"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - inspiration
  - genshin-impact
complexity: intermediate
domain: puzzle-design
aliases:
  - Genshin Impact
  - Puzzle variety
related:
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/lock-logic-gates|Lock logic gates]]"
sources:
  - "[[wiki/sources/source-inspiration-web-research|Inspiration web research]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
---

# Environmental puzzle variety (Genshin Impact)

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Inspiration for: the breadth of concrete puzzles behind one abstract lock.
Facts from the Genshin Impact fandom wiki pages
[Exploration](https://genshin-impact.fandom.com/wiki/Exploration),
[Elemental Monument](https://genshin-impact.fandom.com/wiki/Elemental_Monument) and
[Ruins Torch](https://genshin-impact.fandom.com/wiki/Ruins_Torch) (read through the
wiki API).

## Mechanic families

| Family | Examples |
|---|---|
| Elemental activation | monuments lit by a matching element, some permanent, some timed; Pyro torches, often a group of 4, sometimes only a subset must be lit |
| Weight | pressure plates pressed by a character, object or summon |
| Seals | red ring blocks a chest until nearby enemies die or another puzzle is solved; chests that lock themselves when approached |
| Time trials | destroy barrels / defeat enemies / reach a chest in time; Energy Extraction Device – carry 2–3 keys back, straying fails and resets |
| Escort | Seelies lead to their court and wait to be touched again |
| Traversal | wind currents (Anemo amber, 3 Anemograna), Illusory Keystones that vanish after use |
| Circuits | Electro Discharge / Relay stones lined up; Electro cubes where hitting one changes neighbours; cascade pools that toggle |
| Sequence / pattern | light-up tiles in order; obelisks matching paired symbols |
| World state | Whitenight / Evernight switching; Key Sigils of 5 types opening matching seals; carried Dendrograna lasting 30 s |
| Combat condition | Red Meanies must be killed at the same time or they regenerate |

## Mapping to Explorio

- **AND**: all 4 torches, all enemies, all relays (Broken Cycle, Advanced Puzzle).
- **Subset puzzles** (only some torches): XOR / XNOR / NAND patterns.
- **Temporary open mode**: timed monuments, plates that need weight, Two state
  obstacle (Whitenight/Evernight).
- **Consumable timed keys**: grana, ambers (Tool assist, perishable keys).
- **Typed reusable keys**: Key Sigils.
- **Failable**: time trials and extraction devices that reset on failure –
  model as a lock with a fail edge back to its base state.
- **Open base state**: chests that lock on approach (trap family).
- Neighbour-toggling Electro cubes match the sheet's "lights-out" Advanced
  Puzzle example.

## Takeaway

Genshin's variety comes from a small set of reusable mechanics recombined per
region and element. For Explorio that argues for archetypes × biome mechanics
(fire, ice, electricity, magnetism, light) rather than hand-made one-offs.

## Explorio's own element rules

The fire, cold, electricity and magnetism rules Explorio defines for itself are in
[[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions as locks and keys]]
([[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]).

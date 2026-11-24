---
type: entity
title: "Reference games and borrowed features"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - inspiration
entity_type: catalogue
role: "Games named in the misc-ideas doc and what Explorio takes from each"
first_mentioned: "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]]"
related:
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]"
  - "[[wiki/entities/noita-style-staff-enhancement-ideas|Noita-style staff enhancement ideas]]"
sources:
  - "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x – Misc Ideas]]"
claim_ids:
  - clm-explorio-brogue-level-gen-target
  - clm-explorio-unexplored-game-to-beat
---

# Reference games and borrowed features

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Reference games

From *Other similar games* in GDD 0x. "Role" is the doc's own one-liner.

| Game | Role in the doc | Generator relevance |
|---|---|---|
| **Brogue** | level generation quality we want to achieve | high – target for the generator |
| **Unexplored** | the game we want to kill; 3 default save slots | high – the benchmark to beat |
| Unexplored 2 | "the game she told us not to worry about"; UI and combat features (below) | low |
| Genshin / Elden Ring | puzzles and a few combat features | medium – puzzle variety |
| Cogmind | linear storyline with specific endings; unique NPCs and random events tied to the story | medium – story events on the graph |
| Sipho | non-conventional weapons and spells (tornadoes, hunting nets); UI for buff timers, cooldowns, energy | low |
| Rogue | "father of roguelikes" | – |
| Warcraft / Warhammer / DnD / Witcher 3 | cosmology templates and plot hooks | low |
| Graveyard Keeper | skill trees for meta progression | – |
| Battle Brothers | weapons and bosses | low – boss catalogue |
| Caves of Qud | fungal infections | – |
| Noita | spellcasting modifications for staffs and wands | medium – see [[wiki/entities/noita-style-staff-enhancement-ideas|Noita ideas]] |
| Heroes of Might and Magic 3 | monsters and spell ideas | low |
| Outward | co-op mechanics, weapon alternative attacks | – |

## Unexplored 2 features noted

- **Investigate** points of interest (doors, tablets) that have no regular
  interaction – a possible carrier for CLUE keys (synthesis).
- **Target information**: orientation, name and a state; aura colour shows
  aggro, wandering or friendly.
- **Combat**: damage numbers; sword or shield blocks up to 3 times in a row
  (shared counter, short reset cooldown), then an orange screen outline and
  damage gets through; the hitbox must touch the equipment; heavy attacks
  (hold 2 s) disable the parrying item for longer.
- **Fortune tests**: images only; one caption says "you can only look around
  from this place".

## Agreement with the vault

- **Agrees**: the vault already treats Unexplored (structure, cycles) and Brogue
  (machines, population) as main inspirations – see
  [[wiki/concepts/cyclic-dungeon-generation|cyclic generation]] and
  [[wiki/concepts/brogue-machines-and-population|Brogue machines]]. GDD 0x
  sharpens the roles: Brogue is the **quality bar** for level generation,
  Unexplored the **competitor**.
- **Agrees**: Genshin is named for puzzles, matching
  [[wiki/concepts/environmental-puzzle-variety|environmental puzzle variety]];
  GDD 0x adds Elden Ring alongside it.
- **New**: Cogmind's story-driven events and endings have no page in the vault.

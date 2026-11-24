---
type: concept
title: "Difficulty scaling across depth"
created: 2026-11-23
updated: 2026-11-23
status: seed
tags:
  - concept
  - gdd
  - difficulty
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/concepts/five-room-dungeon-biome-template|Five Room Dungeon biome template]]"
  - "[[wiki/concepts/backtracking-mitigation|Backtracking mitigation]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
sources:
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02 – Difficulty Balance and Bosses]]"
claim_ids:
  - clm-explorio-enemy-generation-pipeline
  - clm-explorio-regional-power-collectibles
---

# Difficulty scaling across depth

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

The "Difficulty Management" part of GDD 02. Most of it is still a to-do list;
this page separates what is specified from what is only named.

## Enemy composition pipeline

Specified in the doc:

```
Environment → Encounter → [Possible Enemies Pool] → Enemy
Enemy = TYPE (Orc, base stats)
      + VARIANT (Feral Orc stats)
      + CLASS (Boss class stats)
      + GEAR (random gear available to them)
      → Feral Orc Boss
```

- *Agrees with the code*: the dev branch already splits **environment biomes**
  from **encounter biomes**
  ([[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]); this
  pipeline is the step after both are assigned.
- "Boss" is a **class** layered on any type/variant, so mini-bosses can be
  produced from ordinary enemy pools (synthesis).

## Challenge rating per layer

Only headings and notes exist:

- what challenge rating (CR) is, for enemies, traps and the gear enemies carry,
  and how it stacks; traps are "somewhat neutral", ranged enemies are stronger
  combined with melee;
- **how much CR per layer and how it increases with depth**;
- how CR scales in multiplayer;
- mutations and an unlockable frenzy meter.

References: a Monte Carlo combat simulator (r/roguelikedev) and Cogmind's
spreadsheet-driven balance post.

Synthesis: a per-layer CR budget is a natural generation-control parameter
(work package 6 in [[wiki/questions/scope-and-open-questions|scope]]), and
"traps are neutral" suggests failable trap locks do not count toward the
combat budget. Neither is decided.

## Regional difficulty

Each biome could have **collectibles that raise power only in that biome**:
higher stats there, a higher stat cap for that area (stats still raised by
potions but capped per area), resistance to the biome's enemy or damage type,
or more damage to the biome's boss (cf. Death's Gambit collectibles). Goal:
every biome stays somewhat hard even after heavy exploration earlier.

Synthesis: these collectibles are optional keys whose lock is a soft
difficulty gate (the biome boss). They fit an *optional* access key in the
lock model and give optional branches a reward to place.

## Difficulty setting and Ascension

- **Sweatless game balance**: action combat depends on player skill more than
  turn-based play. The easiest difficulty should let a player finish the first
  act with mostly starting equipment; the hardest should require much side
  content and careful use of consumables.
- **Ascension system** (like Hades' Pact of Punishment or Slay the Spire's
  Ascension): each run on a random seed raises a *frenzy meter*; each level
  raises difficulty; defeat drops the meter to the last checkpoint; each
  checkpoint has an achievement; past the last tier, checkpoints every other
  level.

Synthesis for the generator: difficulty level could set the share of optional
branches and the number of spare keys, since the hardest setting assumes
players need side content.

## Open questions

- What is the CR budget per layer and its growth curve?
- Do frenzy levels change the story graph (more failable locks, fewer spare
  keys) or only enemy stats?

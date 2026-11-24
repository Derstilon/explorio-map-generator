---
type: concept
title: "Meta progression and unlocks"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - progression
complexity: intermediate
domain: game-design
related:
  - "[[wiki/entities/character-classes-and-starting-kits|Character classes and starting kits]]"
  - "[[wiki/concepts/run-structure-seeds-and-biome-tiers|Run structure, seeds and biome tiers]]"
  - "[[wiki/concepts/player-verbs-and-abilities-as-keys|Player verbs and abilities as keys]]"
sources:
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05 – Gameplay and Progression Systems]]"
claim_ids:
  - clm-explorio-dex-xp-for-locks
  - clm-explorio-no-in-run-xp
---

# Meta progression and unlocks

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

How progress carries between runs, per GDD 05 sections "Meta Progression",
"Hub Town" and "Achievements".

## Two layers of progression

| Layer | Mechanism | Doc statement |
|---|---|---|
| In-run (character) | items, stat-boost potions (permanent and temporary), skill books, runes, sigils | "Don't do XP, to avoid grinding on monsters" (Polish note, "Stats / Character Sheet") |
| Meta (between runs) | XP into STR / DEX / INT talent trees; class, item and cosmetic unlocks | "Skill Trees", "Unlockables" |

So "experience" in the doc belongs to meta progression only. The doc does not
reconcile this explicitly; the reading above is synthesis.

## Vertical vs horizontal unlocks

The doc weighs both without choosing.

- **Vertical**: sense of growth, specialization, grinding difficulty down; but
  linear, discourages experimentation, and first runs become nearly impossible
  if difficulty scales to maxed progression. Examples: unlocking crafting,
  enhancing, god boons, **capes and cape skills**, a pre-run gear shop; raising
  floors (start funds, inventory size, shop stock); biasing loot (more potions of
  one stat, double consumable-tool stacks, sigils swapped for books of the same
  element).
- **Horizontal**: replayability, adaptability, focus on basics; but complexity,
  no immediate payoff, an inevitable "optimal" pick. Examples: empty in the doc.
  Achievements give horizontal rewards (new challenge class or shop item).

## Experience sources per tree

| Tree | Earned by |
|---|---|
| Neutral | defeating enemies (by difficulty rating), opening loot chests (by rarity) |
| Strength | killing enemies, kills by environmental hazards (by trap type), smashing furniture, forging and recycling, crowd control |
| Dexterity | critical damage, crafting potions, **opening locks and puzzles**, applying damage over time |
| Intelligence | reading books, crafting scrolls, casting spells, creating reactions between status effects |

Implication (synthesis): solving locks is rewarded in the DEX tree, and
environmental kills in the STR tree. The count and type of locks in a generated
dungeon therefore feed meta progression. That makes per-zone lock budgets
(work package 6 in
[[wiki/questions/scope-and-open-questions|Scope and open questions]]) a
progression-balance lever, not only a difficulty lever.

## Hub town as the progression front-end

- **Mission table**: first thing to interact with; offers a set of **seeded
  dungeons** with a short plot hook, or a custom seed. Online players can enter
  public town instances and form parties.
- **Training grounds**: shooting range, wooden training weapons, dummies,
  maybe PvP.
- **Marketplace** (five shops) and **Temple**: swap starting gear among
  unlocked items and give tips tailored to the last run (last death, last enemy's
  resistances, last spell school, cursed items met). The temple sets the deity
  for the run and explains karma tiers.
- **Town secrets**: each NPC is a secret hard PvE boss (Forgemaster, Supreme
  Artisan, Sovereign Marksman, Revered Oracle, Genius Apothecary, Divine
  Bishop), each with a counter-strategy.

## Effect on dungeon gating (synthesis)

- Unlocks that add verbs or tools (capes, explosives, picklocks, classes)
  change which locks a player can open. If the generator places locks whose
  only key is a meta unlock, early players are blocked. Either such locks stay
  optional (bonus rooms), or the dungeon always places an in-world key.
- Achievement rewards such as "scroll of Mapping in a shop" or herb/monster-part
  unlocks in shops change starting loadouts, not dungeon structure.
- The doc never says that meta progression changes the generator's difficulty
  or lock mix; that link is open.

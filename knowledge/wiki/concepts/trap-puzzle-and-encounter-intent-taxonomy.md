---
type: concept
title: "Trap, puzzle and encounter intent taxonomy"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - lock-and-key
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]]"
  - "[[wiki/entities/environmental-hazard-and-container-catalogue|Environmental hazard and container catalogue]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-trap-intent-three
---

# Trap, puzzle and encounter intent taxonomy

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *Dungeon contents* section of
[[wiki/sources/source-gdd-06-world-generation|GDD 06]]. The doc classifies
obstacles by **what the dungeon's builder wanted**, which is a different axis
from the product sheet's logic gates.

## Guiding rule

Overcoming a trap, puzzle or encounter should tell the player about the group it
belongs to: notes in a camp, what the puzzle rewarded, how deadly the trap was,
what the trial tests, why nearby groups did not get the treasure (or how they
did, if a camp or ambush lies further on).

## Traps by intent

| Intent | Goal | Doc notes |
|---|---|---|
| Lure | keep someone in a specific place | not obvious; traps, wastes time or kills; treasure security systems count here |
| Deter | keep someone out of a place | obvious danger; illusions of danger also count |
| Alarm | tell someone where the intruder is | sound, smell, field of view, or activating a defence system |

## Puzzles by intent

| Category | Meaning | Examples in the doc |
|---|---|---|
| Trial of the worthy | set up to admit only those who prove themselves | gauntlets, logic puzzles, timed trials |
| Environmental obstacle | the decaying dungeon created a problem | broken machines to fix; natural obstacles overcome with nearby items and monsters |

## Monster encounters

| Type | Behaviour | Graph reading (synthesis) |
|---|---|---|
| Ambush | group waits in place and strikes when approached, like a lure trap; the way back can close behind the player (temporary entrance via consumable, collapsing bridge) so they must fight to another exit or to an item that opens one | Point of no return / Ambush at the Gate |
| Camp | monsters keep a camp, do chores, rotate guards; trespassers are threats | guarded area; camp loot as key source (sheet LP 33 trinkets) |
| Wandering | wild animals or patrols, spawned continuously; no progression role | population only, not a graph node |
| Fight | two groups already fighting (rival tribes, predator and prey); the player is a third party ignored unless a serious threat | optional / stealth route |

The *Adventure Camp* (3–6 well-equipped NPC adventurers; trade or fight, very
hard, good loot; most deities penalise attacking them) is a special camp.

## Mapping to the lock model (synthesis)

| Doc pattern | Closest sheet archetype | Notes |
|---|---|---|
| Alarm trap, *Test at a gunpoint* (turrets fire on a plate, bad path or wrong solution) | Alarm (LP 52), Punishment (LP 20) | failable; the trigger is the key |
| Lure / security on treasure | Mouse Trap (LP 28), unnamed LP 60 | open base state, closes on looting |
| Deter, *Illusion trap* (fake boulder, fake burnt bridge, fake seal) | – | a **false lock**: looks closed but is open; no sheet cell models it |
| *Obvious trap* (visible trap hides the real one) | Death Trap (LP 38) | the visible part is a decoy clue |
| *Trapped lock* (snake/skull-shaped lock spawns a creature) | Alarm | opening is free but has a cost |
| *Timer trap* (hourglass, flooding, crushing wall, falling floor, bullet hell) | Parkour (LP 6), Tool assist (LP 55) | temporary + failable; a **fake-out timer** variant opens nothing special and can be restarted |
| *Decision puzzle* (two obstacles, permanent choice, runes hint the challenge type) | Production 3 Decision / Pick your poison (LP 49) | runes = clue key |
| *Key clue* (key's art or note holds the puzzle answer) | – | one item is both primary key and clue: AND of key + clue |
| Trial of the worthy | Advanced Puzzle (LP 0) | required, permanent |
| Environmental obstacle, *Monster handling*, *Rubble* | Broken Cycle (LP 2), Monster Assist (LP 78), unnamed LP 48 | see [[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]] |
| *Deadly hazard* (gas vents: steam, caustic, poison, explosive, confusion, paralytic; barrels of acid, flammables, scent) | Death Trap | scent fluids lure critters or orcs: a trap that makes an encounter |

## What this adds to the vault

- **Extends** [[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]:
  intent (lure / deter / alarm; trial / environmental) is a candidate extra
  attribute for choosing archetypes per theme, orthogonal to the five sheet
  dimensions.
- **New case:** illusion traps and fake-out timers are obstacles that are not
  locks at all. If the generator should place them, it needs a "decoy" node or
  attribute.
- Wandering encounters confirm that not every enemy is a graph element.

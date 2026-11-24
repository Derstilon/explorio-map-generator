---
type: concept
title: "Enemy lure and deterrence"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - enemy-ai
complexity: basic
domain: game-design
related:
  - "[[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]"
sources:
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01 – Bestiary]]"
claim_ids:
  - clm-explorio-lure-lever-example
---

# Enemy lure and deterrence

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Summary

The bestiary's "Enemy AI" chapter defines two stimulus lists: things that
**deter** enemies and things that **lure** them. The player controls these
stimuli with items (torches, food, booze, shiny items, spells), so enemy
movement becomes a puzzle tool. This is the AI mechanism behind the matrix's
Monster Assist archetype. The chapter's "Enemy tactics" section is empty.

## Stimuli

| Deterrents | Lures |
|---|---|
| smell of undead or poison | smell of things they like: booze, brew, honey, blood, cheese |
| light source: fire, magic, lava | light sound |
| loud sound (bell) | sight of prey (predators only) |
| sight of pointy weapons | sight of an item on the ground (precious, useful, unique) |
| sight of the killer of their friends (packs flee) | sight of water in a desert (splatters or a bottle) |
| large size (predator, imposing presence) | Charm spell (pacifies and strongly lures to the caster) |
| Fear spell (strongly deters from the caster) | |

Monster entries add family-specific hooks: critters, simple bats and rats fear
fire; vampire bats can't be scared; critter mimics aren't scared of fire or
pointy weapons; kobolds are drawn to thrown gold or a lit torch; frogs eat
fairies; monkeys drop stolen items when thrown food; the faery dragon attacks
only if it sees a captured fairy.

## Puzzle examples from the doc

1. Spears or torches scare small critters away so they pose no danger.
2. Throw a deterrent into a room through bars so the enemy pulls a lever to
   escape, **opening all doors** of the room.
3. Throw cheese next to a sleeping rat so it wakes and leaves the **pressure
   plate** it slept on.
4. Leave a shiny item on the floor to catch a gremlin.
5. Splash booze on the floor to lure one orc away from its guard post.
6. Splash brew on enemies so wolves attack them.

## Mapping to lock-and-key terms (synthesis)

| Example | Key | Lock | Likely matrix fit |
|---|---|---|---|
| 2. enemy pulls the lever | deterrent (consumable) + the enemy | lever behind bars | Monster Assist / Tool assist |
| 3. rat leaves the plate | cheese (consumable) | plate held down by a monster (base state: held) | Broken Cycle–like (remove the blocker) |
| 5. orc leaves its post | booze (consumable) | guard post | Stealth Mission / Infiltration |
| 6. wolves attack enemies | brew (consumable) | enemy group | combat bypass, no gate |

The pattern is a **two-part key**: a consumable stimulus item and a monster of a
fitting type nearby. For the generator this means a Monster Assist lock depends
on both the item population and the monster population of its area, which ties
it to the area's encounter biome (see
[[wiki/entities/monster-encounter-biome-affinity|Monster encounter and biome affinity]]).

## Open questions

- Is the stimulus item a separate key node in the graph, or part of the lock's
  content?
- How are lure items guaranteed to be available before the lock (spare keys,
  respawning food)?

---
type: concept
title: "Cyclic dungeon generation (Unexplored)"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - inspiration
  - unexplored
complexity: advanced
domain: procedural-generation
aliases:
  - Unexplored
  - Missions and spaces
  - Cycles
related:
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/graph-grammar-productions|Graph grammar productions]]"
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
sources:
  - "[[wiki/sources/source-inspiration-web-research|Inspiration web research]]"
  - "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
claim_ids:
  - clm-explorio-dormans-lock-properties
---

# Cyclic dungeon generation (Unexplored)

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Inspiration for: the overall structure (story graph first, space later) and
loops. Unexplored 1 & 2 by Ludomotion / Joris Dormans.

## Techniques

- **Mission vs space.** A mission graph (tasks) is generated first with a graph
  grammar; a space is then grown for it with a shape grammar; one mission maps to
  many spaces ([Dormans 2010](https://www.pcgworkshop.com/archive/dormans2010adventures.pdf)).
  This is exactly Explorio's [[wiki/concepts/story-graph-not-dungeon-layout|story graph]]
  split.
- **Mission alphabet**: key, lock, multi-piece key/lock, final key/lock, test,
  secret test, item test, bonus/quest item, mini-boss, boss, entrance, goal;
  non-terminals Chain, Fork, Gate, **Hook** (attachment point for optional
  content) (same paper).
- **Tight vs loose coupling** edges: a tightly coupled node must be placed
  *behind* its parent in space, so keys land behind their tests (same paper).
- **Cycles**: two arcs from start to goal; arcs are gameplay, not necessarily
  corridors; new cycles are inserted into arcs of existing cycles
  ([Game Developer: Unexplored's secret](https://www.gamedeveloper.com/design/unexplored-s-secret-cyclic-dungeon-generation-)).
- 24 major cycle types (e.g. ThreeLeverHub, Hub, Lake); generation on an
  annotated 5×5 node grid; keys keep a special edge to their lock; **hard lock**
  (key required) vs **soft lock** (key helps); "Obstacle" placeholder resolved
  late into enemy, puzzle or trap
  ([Boris the Brave](https://www.boristhebrave.com/2021/04/10/dungeon-generation-in-unexplored/)).
- Unexplored 2 "Theory of the Place": Place / Vault / Environment / Path /
  Antechamber / Secondary entrances; the environment must be fully traversable;
  a gating key should be obtainable from both sides or the area needs another
  exit; optionality decides where an encounter goes; levels can be chained or
  nested ([Game Developer: Theory of the Place](https://www.gamedeveloper.com/game-platforms/the-theory-of-the-place-a-level-design-philosophy-for-unexplored-2)).

## Lock and key properties – match with the sheet

The cyclic-generation article lists key and lock properties that line up with
the [[wiki/entities/puzzle-archetype-matrix|archetype matrix]] dimensions almost one-to-one:

| Dormans property | Explorio dimension |
|---|---|
| key reusable / consumable | usage count |
| key perishable (temporary potion) | – (Tool assist examples) |
| key physical / abstract (weapon as key to a monster lock) | Monster Assist, Tool assist |
| lock conditional / non-conditional (passable, easier with key) | OR gate, optional access |
| lock permanent / timed / relockable | open mode |
| lock unidirectional (valve, collapsing bridge) | Point of no return, Burning bridges |
| lock **unsafe** (no guaranteed solution; secrets only) | failable access |

## Takeaways for Explorio

- Allow failable (unsafe) locks only off the critical path, or pair them with
  production 9's secret edge.
- Add cycle productions; today's graph is lock-tree shaped.
- Keep "obstacle" abstract until the archetype/biome step.
- Use hooks for optional content; Explorio's Required/Optional merge loses this.
- Theory of the Place's layering (place, antechamber, environment) is a ready
  model for [[wiki/concepts/biome-and-zone-layering|zone layering]].

## From the game design docs

- [[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]] frames Unexplored as the competitor to beat
  ([[wiki/entities/reference-games-and-borrowed-features|Reference games and borrowed features]]).
- [[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]] names cyclic generation as the way to make backtracking unnecessary
  ([[wiki/concepts/backtracking-mitigation|Backtracking mitigation]]) – an owner design goal,
  not only research.
- Further forms of key perishability from [[wiki/sources/source-gdd-03-items-compendium|GDD 03]]: cloak cooldowns, breakable
  tools, wand charges.

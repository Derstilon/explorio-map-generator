---
type: concept
title: "Backtracking mitigation"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - structure
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
  - "[[wiki/concepts/five-room-dungeon-biome-template|Five Room Dungeon biome template]]"
  - "[[wiki/concepts/difficulty-scaling-across-depth|Difficulty scaling across depth]]"
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
sources:
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02 – Difficulty Balance and Bosses]]"
claim_ids:
  - clm-explorio-cyclic-reduces-backtracking
---

# Backtracking mitigation

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

GDD 02 weighs whether players should backtrack (with Cogmind's post "On
Backtracking in Roguelikes" as reference) and lists ways to limit its costs.
Lock-and-key graphs create backtracking by design (key in a branch, lock on
the main path), so this section directly constrains the generator.

## Pros and cons

| Pros | Cons |
|---|---|
| nonlinear game – easier to choose where to go, you can always go back | revisiting cleared areas removes tension and action |
| crafting any time once a workstation is found | after the first workstation of a type, others only shorten the walk |
| under-equipped players can explore earlier areas for upgrades | players stash bulky items in old chests or on the floor |
| players must choose which items to carry | the game stays fair only if players carry the items it expects them to use |

## Ways to reduce the costs

- **Teleportation** – consumables (a craftsman's scroll to a chosen
  workstation; a biome-bound item that teleports anywhere in that biome) or
  waypoint travel, possibly priced, e.g. *leylines* that restore mana and link
  to each other. The doc notes Unexplored places cross-level teleporters at the
  ends of dead-end paths.
- **Unique workstations** – recipes and ingredients found next to them; each
  workstation a historic legacy in a unique room or even a whole layer; each
  specialised (discounts, unique results such as a fire forge adding a fire
  sigil); neutral races may guard them. The doc warns this alone makes crafting
  rare or backtracking monotone.
- **Lost and Found** – the dungeon is "evershifting": do not preserve player
  changes, but **track which puzzles were solved and which containers were
  used**, and delete what was left behind; or let gremlins or NPC adventurers
  collect left items; or add a stash (as in DCSS) or infinite inventory.
- **Pay to win** – unlimited ingredient/money storage and recycling of useless
  items into base ingredients (list cut off in the doc).

## Making backtracking unnecessary

- **Cyclic dungeon generation**: "if dungeon generation leans more into cyclic
  design there will be less backtracking because each side objective returns
  you back on the main path" (link to Sersa Victory's cyclic generation page).
  *Agrees with* [[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon
  generation]] and supports work package 5 (cycles) in
  [[wiki/questions/scope-and-open-questions|scope]].
- **DIY crafting** without workstations: crafting scrolls, merging items in
  the inventory, portable anvil / cooking pot / inkwell.
- **Sweatless balance**: difficulty settings so that a direct route is viable
  for average players (see
  [[wiki/concepts/difficulty-scaling-across-depth|Difficulty scaling]]).

## Implications for the generator

Synthesis:

- Prefer productions that close side branches back onto the main path (cycles,
  shortcuts, one-way return edges) over dead-end key branches.
- Dead ends that must stay should end with a teleporter or shortcut (the
  Unexplored pattern the doc cites).
- "Track solved puzzles and used containers" means lock and key state must be
  persistent and addressable per node, even if the dungeon re-shuffles
  everything else.
- Workstations placed as unique rooms or layers are a node type the story
  graph does not model yet.

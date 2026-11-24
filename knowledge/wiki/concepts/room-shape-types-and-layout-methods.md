---
type: concept
title: "Room shape types and layout methods"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - layout
complexity: intermediate
domain: procedural-generation
related:
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/biome-catalogue-with-generation-hints|Biome catalogue with generation hints]]"
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-room-types-eight
  - clm-explorio-lock-grammar-as-room-purpose
---

# Room shape types and layout methods

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

The *Dungeon Generation* chapter of
[[wiki/sources/source-gdd-06-world-generation|GDD 06]] is the only place in the
design docs that talks about the **spatial** stage that comes after the story
graph. Most of its subsections are headings with no text yet; what is written
is summarised here.

## Two-step strategy in the doc

The doc splits *Generation strategies* into two groups:

| Group | Methods listed (headings only, no text) |
|---|---|
| Walkable area generation | Room accumulation, Cellular Automata, Random Walk, Subdivision, Wave Function Collapse |
| Room purpose classification | 5 Room Dungeon, Cycle Based Generation, Lock and Key Grammar |

Reference links next to the walkable-area group: DCSS layout types, Zorbus
(accumulation of prefab room shapes), Dyson's Dodecahedron hand-made maps (for
themes), Cogmind's generation overview. The chapter opens with three links on
Unexplored's cyclic generation (see
[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]).

**Relation to the vault (synthesis):**

- The grouping files the lock-and-key grammar under *room purpose
  classification*, i.e. assigning roles to spaces, alongside the 5-room dungeon
  and Unexplored's cycles. That is compatible with
  [[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]
  if the grammar output is later mapped onto geometry; it could also be read as
  "generate geometry first, then classify rooms", the opposite order. The doc
  does not say which. **Decided:** story graph first, forced into the room map;
  unused rooms get standalone content ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
- **Wave Function Collapse** appears here as a *geometry* method. The dev readme
  uses WFC for turning abstract elements into concrete types
  (`machine_wfc/`). Two different uses of the same name – **decided: both are
  wanted** ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).

## Generation system graphs

Two diagrams are referenced but only as images or encoded Mermaid links (not
ingested): a simplified *Brogue Architect* level-generation flow and a Godot node
tree for *Dungeon Architect*. The Brogue build order is already covered in
[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]].

## Room types

Eight room types, each with the shape primitive the doc proposes for it:

| Type | Meaning | Shape / algorithm |
|---|---|---|
| Room | space processed or dug by intelligent creatures | circles and rectangles of different sizes and offsets |
| Tunnel | narrow connector between two rooms | narrow line: straight, broken or curly |
| Clearance | large area loosely fenced with low or high walls | giant cellular-automata blob, or walker algorithm |
| Cavern | medium room with columns and wide entrances | CA blob |
| Shelter | room located inside a larger room | one rectangle or one circle |
| Relic | building or creature remains forced into the wall of a larger room | one or more rectangles with many holes, or a prefab shape (e.g. snail shell) with holes |
| Barrier | blob of non-walkable surface | giant CA blob or regular shape |
| Plaza | man-made giant open space with decorated walls and entrances | giant square or circle with rooms around it |

Biomes then pick from these types (e.g. Sanctuary → circular plaza, Swamp →
watery clearance, Ship Graveyard → shipwreck relics); see
[[wiki/entities/biome-catalogue-with-generation-hints|Biome catalogue with generation hints]].

## Why it matters for the generator

(Synthesis.) The room types give the layout stage a small vocabulary that an
area node of the story graph could be tagged with, much as Unexplored 2 tags
places. A **Shelter** (room inside a room) and a **Barrier** (non-walkable blob,
in some biomes destructible: ore veins, wax, hedges) are natural spatial forms
for a lock: the shelter's entrance or the barrier itself is the obstacle. A
**Tunnel** is the default edge between areas. None of this is in the dev code.

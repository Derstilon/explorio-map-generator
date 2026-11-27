---
type: concept
title: "Flavour spread and archetype weights"
created: 2026-11-25
updated: 2026-11-27
status: seed
tags:
  - concept
  - biomes
  - lock-and-key
complexity: intermediate
domain: procedural-generation
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/graph-grammar-productions|Graph grammar productions]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
sources:
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
---

# Flavour spread and archetype weights

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Design proposal for parts 4 (generation plan) and 6 (flavours) of the
story-graph epic. Nothing here is implemented or decided.

## Problem

Some archetypes only make sense in some flavours: Faulty Mechanism and Misfire
(proposed in `data/archetypes.yaml`) belong in a malfunction or mechanical zone.
How often each archetype appears should therefore depend on the flavour of the
area where its lock is created.

Today both biome passes run **after** all productions: environment biomes split
the finished graph in two (Kernighan–Lin bisection), and encounter biomes pick 4
seed nodes and spread each theme to up to 3 neighbours. They colour the result
but cannot change which locks get created.

## Proposal

1. **Taint early.** The seed graph, or the first few productions, give each
   area a flavour.
2. **Inherit with a small chance of change.** Every production creates its new
   area next to or behind an existing one. The new area takes that area's
   flavour; with a small seeded chance it starts a new flavour instead. Because
   the graph grows outward from the tainted areas, connected regions of one
   flavour form by themselves, and the result stays deterministic per seed.
3. **Flavour weights archetypes.** Each archetype gets a weight per flavour
   (zero outside the flavours it fits). A production picks among the
   archetypes it can create using the weights of its area's flavour. This makes
   archetype frequency vary per flavour and keeps flavour-only archetypes
   inside their zones.
4. **Archetypes weight each other.** Some archetypes pair well: a failable
   archetype can use another one as its failure state. When Clean Sweep is
   created, Point of Commitment gets a higher weight nearby, so the bridge the
   player can drop on the camp, or break under themselves, is what a mixed
   approach costs.
5. **Some archetypes stay rare.** One Offering (an altar that takes exactly one
   of several items) works only as an occasional surprise, so its base weight is
   low in every flavour.
6. **Borders are useful.** A lock between two flavour regions is a natural
   place for a transition archetype. The biome adjacency restrictions in
   `biome_injections/environment_biomes.py` can block bad neighbours when a new
   flavour starts.

## Open points

- Which layer the flavour is: the environment biome (Molten Caverns), the
  encounter theme (Mechanical, Traps), or a separate layer. If it is the
  encounter theme, this moves the existing spread before the productions.
- Weights need a choice to act on: today a production's archetype follows from
  its lock attributes and the access mode it inherits, and nothing picks among
  archetypes.
- Candidate flavours for puzzles, besides the environment biomes: **Mineshaft**
  with minecarts and rail switches (Shifting Fork's mine-cart junction, tracks
  as routes, carts as moving platforms or weights).
- Where the per-flavour weights live: likely a field of each entry in
  `data/archetypes.yaml`, added with part 6.

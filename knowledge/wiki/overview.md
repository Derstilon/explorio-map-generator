---
type: overview
title: Vault Overview
status: developing
created: 2026-11-23
updated: 2026-11-23
tags:
  - overview
---

# Vault Overview

Knowledge base for the **Explorio map generator**: a Python proof of concept
(branch `dev`) that generates a roguelike dungeon's abstract lock-and-key
**story graph** with graph-grammar productions. The graph is not a final map;
a later stage turns it into one biome/zone of a few interconnected layers.

- Model: areas, locks and keys; locks have a logic gate, open mode, access and
  base state; keys are reusable or consumable. 96 combinations, 25 named puzzle
  archetypes in the product sheet.
- Generator: productions P1–P9 specified; only P1 implemented; biome tagging is
  a sketch; the WFC/content step is empty.
- Inspirations: Unexplored (missions vs spaces, cycles), Brogue (machines, key
  chains, population), Genshin Impact (puzzle mechanic families).
- Game design docs 01–06 + misc: bestiary, bosses and difficulty, items,
  magic and statuses, progression, world generation. They supply the concrete
  keys and locks (items, player verbs, monsters, bosses, element reactions),
  the first statements about layers, a Five Room Dungeon template per biome
  and three boss acts per run.

Start at [[wiki/maps/explorio-knowledge-map|Explorio knowledge map]]. Use
[[index|Wiki index]] to find pages, [[hot|Recent context]] to resume work, and
[[log|Operation history]] for completed operations.

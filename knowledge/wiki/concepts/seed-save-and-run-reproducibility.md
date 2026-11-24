---
type: concept
title: "Seed save and run reproducibility"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - procedural-generation
complexity: basic
domain: game-design
related:
  - "[[wiki/entities/dev-branch-codebase|Dev branch codebase]]"
  - "[[wiki/questions/scope-and-open-questions|Scope and open questions]]"
  - "[[wiki/questions/implementation-status-and-gaps|Implementation status and gaps]]"
  - "[[wiki/concepts/run-structure-seeds-and-biome-tiers]]"
sources:
  - "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x – Misc Ideas]]"
claim_ids:
  - clm-explorio-seed-save-metadata
---

# Seed save and run reproducibility

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Proposed seed save

From *Game Menu Features > Seed Save* in GDD 0x:

- A text file keeps game information: a **list of map seeds**, the **game
  version** when each seed was created, and the **date of seed creation**.
- An in-game menu shows recent (or all) seeds used.
- Each player character is a folder, saved in Steam Cloud.
- Multiple save folders, **3 slots by default**, similar to Unexplored.

## What it requires from the generator

Synthesis, not in the doc:

- A seed is only useful if the whole pipeline (story graph → layers → content)
  is **deterministic** for a given seed and generator version. Storing the game
  version with the seed implies seeds are not expected to survive version
  changes.
- The dev code is not deterministic today: `main.py`'s choice between `L1` and
  `L2` is unseeded, and the productions reseed with a fixed `1` on every call
  (see [[wiki/entities/dev-branch-codebase|dev branch codebase]]). The
  "fix the seeding" item in
  [[wiki/questions/scope-and-open-questions|scope work package 1]] is therefore
  a prerequisite for this feature, not only a clean-up.
- A per-zone or per-layer sub-seed derived from the map seed would let one
  layer be regenerated or debugged without the rest.

## Open points

- Whether "map seed" means one seed per run or per zone is not stated.
- Naming convention (next section in the doc) is empty.

---
type: question
title: "Scope and open questions"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - question
  - scope
question: "What has to be decided and built to take the generator from PoC to a zone-level story-graph tool?"
assessment: provisional
risk: normal
related:
  - "[[wiki/questions/implementation-status-and-gaps|Implementation status and gaps]]"
  - "[[wiki/questions/inconsistencies-sheet-doc-code|Inconsistencies]]"
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
  - "[[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]]"
---

# Scope and open questions

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Everything below is a proposal for scoping, not a decision.

## Scope boundary

**In scope** (this tool): the abstract story graph of one zone – areas, locks,
keys, their attributes and archetypes, cycles, layer assignment, biome tags,
validation, export.

**Out of scope** (later stages): room geometry, tiles, art, enemy stats, the
game engine.

## Work packages

1. **Clean-up** – fix or drop the master tests/examples, align vocabulary
   ([[wiki/questions/inconsistencies-sheet-doc-code|inconsistencies]]), fix the
   seeding.
2. **Attribute-aware matching** – pattern conditions on lock/key attributes.
3. **Productions 1a, 2–9** – one rule per variant, each with a test.
4. **Gate semantics and solver** – evaluate AND…XNOR, temporary/permanent,
   failable paths; prove the goal is reachable and find soft-locks.
5. **Cycles** – productions that add loops, in the style of
   [[wiki/concepts/cyclic-dungeon-generation|cyclic generation]].
6. **Generation control** – recipes / weights / budgets per zone, target metrics
   (depth, number of locks per gate family, optional share, failable share).
7. **Archetype assignment** – map each lock to a sheet archetype; fill the empty
   matrix cells or mark them unusable.
8. **Concrete content** – the WFC / machines step
   ([[wiki/concepts/brogue-machines-and-population|Brogue machines]]); biome-aware
   choice of tools, monsters and hazards.
9. **Layers and biomes** – cut the zone into interconnected layers; use the
   adjacency and start/end rules.
10. **Export** – a stable format (JSON) for the layout stage.

## Open questions

- Does one story graph equal one zone, or one layer?
- How many layers per zone, and do layer transitions themselves become locks
  (Point of no return, Burning bridges drop you a floor)?
- Should every one of the 96 matrix cells get an archetype, or are some cells
  meaningless (e.g. consumable + NAND + permanent + required + open)?
- Do the two missing cells and the P4/P5 swap reflect intent or slips?
- How are failable locks kept fair: secret edges (production 9), spare keys,
  respawning keys?
- Are enemies-as-keys (Monster Assist) and tools-as-keys (Tool assist) typed in
  the graph, or resolved in the content stage?
- What does the WFC step collapse over: archetypes per lock, rooms per area, or
  biome tiles?
- Which Genshin-style mechanic families should be supported first (see
  [[wiki/concepts/environmental-puzzle-variety|puzzle variety]])?
- Target tech: stay in Python as a design tool, or port to the game engine?

## Questions raised by the game design docs

Structure and order
- ~~Is the lock-and-key grammar run before geometry or used to classify rooms of
  an existing layout? Which WFC is meant?~~ **Answered:** story graph first, forced
  into a room map, unused rooms get standalone content; WFC for both geometry and
  content ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
- Is the Five Room Dungeon (entrance, puzzle, setback, climax, reward) the spine
  of each zone graph, with productions expanding each stage ([[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]])?
- Keys and one-way entrances in *neighbouring* biomes ([[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]): does the zone
  graph need cross-zone edges, or a run-level graph above it?
- How do bosses enter the graph: lock kind, key holder, or layer switch? How do
  the 3 bosses of a run map to zones and layers ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]])?
- Partial answer to "one graph = one zone or one layer": GDD 06 has biomes sized
  as a whole layer and a boss theme that dictates two stacked layers, so several
  layers per zone are expected; the graph-to-layer mapping is still open.
- Layer transitions as locks: GDD 06's Ambush encounter and GDD 03's rope /
  Descend scroll are candidates.

Keys and locks
- Is the generator class/loadout-aware, or must every seed be solvable for every
  class ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]])? Must some seeds reach the first boss with no key item
  (achievement "Where Did I Put My Keys?")?
- Should keys/locks carry an element tag ([[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]])? ~~Is Levitation meant to cross
  chasms?~~ **Answered:** yes, but it cannot rise to the previous layer ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
- Are keys indestructible by monster effects globally, or only for the Magma
  Slime ([[wiki/sources/source-gdd-01-bestiary|GDD 01]])? Is a key stolen by a thief a failable lock?
- Is a lure item its own key node, given a lure puzzle needs the item *and* a
  fitting monster in the area ([[wiki/sources/source-gdd-01-bestiary|GDD 01]])?
- Should the graph model decoys and key burdens, or leave them to the content
  stage? Should a production add clue keys to compound puzzles ([[wiki/sources/source-gdd-06-world-generation|GDD 06]])?
- Does the graph carry an item class per key (crowbar, rope, web solvent…) or
  leave it to the content stage ([[wiki/sources/source-gdd-03-items-compendium|GDD 03]])? Can the Friendly mimic key appear?

Generation control and seeds
- Seed save needs a deterministic, version-stamped pipeline ([[wiki/sources/source-gdd-0x-misc-ideas|GDD 0x]];
  [[wiki/concepts/seed-save-and-run-reproducibility|Seed save and run reproducibility]]) –
  this makes "fix the seeding" (work package 1) a prerequisite.
- Is a seed per run or per zone? Should the export report per-seed properties so
  hub seeds can promise "something achievable" ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]])?
- Per-seed difficulty and injected fixed goals (artefact keys, custom final boss)
  for the seed campaign arc ([[wiki/sources/source-gdd-06-world-generation|GDD 06]]).
- Lock counts feed DEX meta XP ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]); does meta progression change the lock
  mix or difficulty?
- Can player state (curses on gear) be a generator input ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]])?

---
type: concept
title: "Lock and key abstraction"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - lock-and-key
complexity: intermediate
domain: procedural-generation
aliases:
  - Key and lock
  - High-level lock and key
related:
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
claim_ids:
  - clm-explorio-lock-generalised
---

# Lock and key abstraction

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Core idea

A **lock** is anything that stops progress until a condition is met; a **key**
is anything that satisfies that condition. Both are abstract roles, not items.
The product sheet's examples show the range:

| Role | Literal | Generalised examples from the sheet |
|---|---|---|
| Key | key, gem, battery | consumable potion (invisibility, levitation, iron skin), clue, a monster lured to break a wall, a laser automaton, killing an ice elemental |
| Lock | door, chest | burning bridge, quicksand, laser grid, alarm system, cipher seal, gap only crossable by riding enemy AI, gas room |

So an enemy can be a lock (guard), a key (Monster Assist: the spider bridges a
chasm) or a punishment (Alarm opens monster cages).

## Three node roles in the graph

- **Area** (code: `access` node) – a place the player can stand in; it makes
  locks and keys reachable ("opens to" edges).
- **Lock** – has a logic gate over its keys and opens to areas, keys or other
  locks.
- **Key** – reachable from an area, points ("unlocks") to exactly one lock in the
  current code.

Each lock and key carries attributes; see
[[wiki/concepts/lock-dimensions|Lock dimensions]] and
[[wiki/concepts/key-dimensions|Key dimensions]]. Five binary/hex dimensions give
96 lock/key combinations, catalogued in
[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]].

## Key types (productions doc)

- **Primary** – opens the lock directly.
- **Spare** – an alternative way in (Tool assist, Gambit puzzle).
- **Clue** – reusable knowledge that changes or reveals how to open the lock
  (Decision production, Death trap).

## Design consequences

- Logic gates let one lock express puzzles, traps and choices, not only "has key".
- Failable access and temporary open mode create states the player can lose;
  the grammar must keep the dungeon solvable (see
  [[wiki/entities/production-catalogue|Production 9 – Failure decrease]]).
- Keys that are enemies or environment effects need the later population stage
  to know which archetype was chosen.

## From the game design docs

- **Keys the player brings:** control verbs (grab, crouch/investigate, interact,
  cape skill), class kits (picklocks, pickaxe, explosives, stealth ring) and gear
  act as keys that are never placed in an area, so the available key set depends
  on class and meta unlocks ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]];
  [[wiki/concepts/player-verbs-and-abilities-as-keys|Player verbs and abilities as keys]]).
- **Item keys:** concrete key items (crowbar, lockpicks, rope, Descend scroll, web
  solvent, lures, clue items) in [[wiki/concepts/items-as-keys|Items as keys]]; physical
  key items have no design yet ([[wiki/sources/source-gdd-03-items-compendium|GDD 03]]).
- **Monster and boss keys/locks:** slimes swallow keys, the Centurion's energy cell
  opens doors, thieves steal keys ([[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]],
  [[wiki/concepts/enemy-lure-and-deterrence|Enemy lure and deterrence]]); bosses can be
  the lock, the key or a layer switch ([[wiki/concepts/bosses-as-locks-and-gates|Bosses as locks and gates]]).
- **Element and status keys:** wet/electric/fire/cold reactions, flying over
  chasms ([[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions]]).
- **More lock/key examples** from [[wiki/sources/source-gdd-06-world-generation|GDD 06]]: rolling boulder on a plate, burden
  orbs, lure gases, a strength check; sight sensors, ritual seals, powerless
  machines, containers by material
  ([[wiki/entities/environmental-hazard-and-container-catalogue|Environmental hazard and container catalogue]]).
  Door size scales the gate: small = 1 key, medium = mechanism, large = 3 keys.
- **Key clue:** GDD 06's key whose art holds the solution is both primary and
  clue; the one-type-per-key model cannot express it.
- **Key burden, compound puzzles, decoys:** a key can carry a cost from pickup to
  use; a lock whose keys all sit behind another lock can get an extra clue key;
  obstacles that are not locks (illusions, fake-out timers) have no node type
  ([[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]],
  [[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|Trap, puzzle and encounter intent taxonomy]]).

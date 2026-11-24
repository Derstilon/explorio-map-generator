---
type: concept
title: "Key burden and compound puzzles"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - lock-and-key
complexity: advanced
domain: procedural-generation
related:
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
  - "[[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|Trap, puzzle and encounter intent taxonomy]]"
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-key-burden-returns
  - clm-explorio-compound-puzzle-trigger
---

# Key burden and compound puzzles

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *Puzzles Overview* and *Environmental Hazards* in
[[wiki/sources/source-gdd-06-world-generation|GDD 06]]. These are the patterns
in the doc that speak most directly to the story-graph generator: they are
rules about **where keys sit relative to locks** and **what carrying a key
costs**.

## Key burden

Main features as written:

- The key to the puzzle is **far away**.
- The key is a **burden**: a debuff, or enemies that chase the carrier (an easier
  version of Unexplored's *Guardian of Yendor*).
- The burden **goes away when the player returns the key**.

Variants:

| Variant | Examples |
|---|---|
| Status needed to pass a trap | blood or water from a fountain disables security |
| Large item that enables traversal; burden is one occupied hand | shining orb enables light bridges; magnetic orb lets you pass a magnetic field; fire-bubble orb protects in lava |
| Item or status that draws attacks | honey gem lures bees; item makes you cold so wet areas freeze you; cursed mirror spawns ghosts; contraption triggers alarms and constructs |
| Fragile transport (Hollow Knight's delicate flower) | torch lit with holy flame carried to the next bonfire without water geysers, gas explosions or wind; or "take no damage while carrying" |
| Transformation | the item polymorphs you in a given room into a form that flies or swims, is immune to local hazards, or is ignored by local fauna |

**Against the vault:** [[wiki/concepts/key-dimensions|Key dimensions]] has only
usage count (reusable / consumable) and type (primary / spare / clue). A burden
is a new property: a **carry cost between pickup and use**. It makes the *path
length* from key to lock a difficulty knob, and it fits Unexplored's "far key"
cycles ([[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]).
Fragile transport is also failable access applied to the key rather than the
lock. (Synthesis.)

## Compound puzzles

> If a puzzle is locked with all its keys behind another lock, that's when we can
> generate compound puzzles. (paraphrase of the doc)

The on-site clues then lack part of the information:

- statues in a row show the order or count of interactions, but the coloured
  items (e.g. weapons in hand) that link each statue to its interactable are
  missing and must be found;
- the activation device no longer works and needs a tool (oil, cog).

**For the generator (synthesis):** this is a graph-level trigger the grammar can
check directly – a lock *L* whose every key is reachable only through another
lock *M*. Such an *L* can be upgraded by adding a clue or tool key outside *M*.
That is close to the productions doc's *spare* and *clue* key types, but no
production in the [[wiki/entities/production-catalogue|Production catalogue]]
currently fires on this pattern.

## Related key-placement patterns in the doc

| Pattern | What it says | Model |
|---|---|---|
| Key clue | a door needs a key **and** a puzzle; the key's art or note holds the solution | key is both primary and clue |
| Partially buried puzzle | clues or mechanisms are partly buried to make it harder | difficulty modifier on an existing lock |
| Time-gated clue | the clue shows only briefly (light circling a dark room, a toggled light, mist); player memorises it | temporary clue key |
| Elemental riddle | orbs with element runes; pillars or slots with riddles about each element | AND over typed keys |
| Tombstones | sort tombstones by material, image or date; or count/order of tombstones gives a combination; failures spawn ghosts and lock the puzzle | failable; biome skin of a statue puzzle |
| Rotation disc | turning a disc to match lines shows which pedestals need items from another room | clue in one area, keys in another |
| Floating chest | needs levitation or frozen water | Tool assist |
| Magnetic mechanism | magnetise items and throw them to rotate it | Tool assist with a crafted key |
| Chess | on a board, a piece tile forces that piece's moves; illegal move drops you into a pit; "king" variant dodges checks | failable traversal |
| Sudoku, odd-one-out, symbol on a cube | images only | – |

## Monster handling as keys

Using monster mechanics to get past a puzzle (the sheet's Monster Assist):

- spider web makes a bridge; elementals change lake fluids into a bridge;
- lure a creature by smell or sound off the throne that holds a gate shut;
- polymorphed wizard rewards you if you lift his curse (lure his critter form, or
  use an item from the floor);
- lure a giant, ogre, elemental or golem to smash rubble (a pickaxe also works);
  a dune worm breaks rubble from below; wind clears sand or leaves. Some rubble
  only leads to more enemies – a clue shows the real path.

The last point is a **decoy lock**: a breakable obstacle whose reward is a
dead end, signposted by a clue. Same open point as in
[[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|the intent taxonomy]].

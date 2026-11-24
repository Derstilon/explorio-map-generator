---
type: concept
title: "Lock dimensions"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - lock-and-key
complexity: intermediate
domain: procedural-generation
related:
  - "[[wiki/concepts/lock-logic-gates|Lock logic gates]]"
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
---

# Lock dimensions

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Four lock dimensions; with key usage count they span the
[[wiki/entities/puzzle-archetype-matrix|96-cell archetype matrix]].

## Logic gate (6 values)

`AND`, `NAND`, `NOR`, `OR`, `XOR`, `XNOR` – how the lock's keys combine.
Detailed reading per gate: [[wiki/concepts/lock-logic-gates|Lock logic gates]].

## Open mode

| Sheet | Doc | Code (`OpenMode`) | Meaning |
|---|---|---|---|
| Permanent | PERM | `PERMANENT` | once open, stays open (or once closed, stays closed) |
| Temporary | TEMP | `TEMPORARY` | state reverts: timers, pressure plates, toggles |
| – | – | `DUNGEON` | only on seed lock `L0` |

## Access mode

| Sheet | Doc | Code (`Importance`) | Meaning |
|---|---|---|---|
| Required/Optional | X (inherited) / OPTIONAL | `MANDATORY`, `MISSABLE` | normal progression or side content |
| Failable | FAILABLE | `FAILABLE` | the player can fail and lose access or get punished |

The sheet merges required and optional into one value; the code splits them
(`MANDATORY` vs `MISSABLE`). Productions use an inherited access `X` and add the
rule `X != FAILABLE` on the parent area for trap productions.

## Base state

| Sheet | Doc | Code (`LockState`) | Meaning |
|---|---|---|---|
| Closed | CLOSED | `LOCKED` | blocks until keys satisfy the gate |
| Open | OPEN | `UNLOCKED` | passable until keys (triggers) close it: traps, collapsing paths |

"Open" locks are the trap/threat family: Burning bridges, Tripwire trap, Mouse
Trap, Point of no return, Stealth Mission.

## Counters

Doc locks carry `keys(n)`; areas carry `locks(L)` and `keys(K)` counters that
productions increment. The code stores `keys` as a set on the lock and
`keys`/`locks` sets on access nodes.

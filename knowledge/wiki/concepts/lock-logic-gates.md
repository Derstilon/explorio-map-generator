---
type: concept
title: "Lock logic gates"
created: 2026-11-23
updated: 2026-11-25
status: developing
tags:
  - concept
  - lock-and-key
complexity: intermediate
domain: procedural-generation
related:
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
---

# Lock logic gates

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

The gate says how a lock's inputs (keys, triggers) combine. The readings below
are this vault's synthesis from the named sheet examples; the sheet itself only
lists the gate per row.

| Gate | Reading in play | Sheet archetypes |
|---|---|---|
| AND | all keys needed | Advanced Puzzle, Locked Chest, Broken Cycle, Legendary Quest, Sequence Lock, Parkour, Burning bridges |
| OR | any one key is enough; alternatives, spares | Gate Lock, Tool assist, Pick your poison, Alarm, Gambit puzzle, Point of no return |
| NAND | opens unless *all* inputs are active; remove any one | System Shutdown (pull any battery), Punishment, Mouse Trap (take everything → trap) |
| NOR | open only while *no* input is active; any trigger fails it | Tripwire trap, Death Trap, Stealth Mission, Rotating Passage |
| XOR | exactly one of the inputs; choices exclude each other | Cipher, Two state obstacle, Monster Assist, Ambush at the Gate |
| XNOR | all or nothing; consistent state | Infiltration (full stealth or kill everyone) |

## Reading by count of active inputs (proposal)

For more than two inputs the boolean names are ambiguous (XOR could mean parity
or "exactly one"). `data/archetypes.yaml` writes its play patterns against this
reading, pending an owner decision:

| Gate | Passable when the number of active inputs is |
|---|---|
| AND | all (n) |
| OR | 1 to n |
| NAND | 0 to n−1 |
| NOR | 0 |
| XOR | exactly 1 |
| XNOR | 0 or n |

The gate only says which inputs must be reachable. Order and timing between
inputs (sequences, time windows) are placement constraints for the room-map
and content steps, not part of the gate.

## Patterns

- **AND / OR** are classic puzzles and alternatives.
- **NAND / NOR** with base state *Open* are traps and stealth: the player keeps
  the path by *not* doing something.
- **XOR** expresses mutually exclusive choices and state toggles (two-state
  rooms, true/false statuettes).
- **XNOR** is the least explored: 16 cells, one named archetype.

See [[wiki/questions/scope-and-open-questions|Scope and open questions]] for the
under-filled gate families.

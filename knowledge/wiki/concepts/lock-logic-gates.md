---
type: concept
title: "Lock logic gates"
created: 2026-11-23
updated: 2026-11-23
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

## Patterns

- **AND / OR** are classic puzzles and alternatives.
- **NAND / NOR** with base state *Open* are traps and stealth: the player keeps
  the path by *not* doing something.
- **XOR** expresses mutually exclusive choices and state toggles (two-state
  rooms, true/false statuettes).
- **XNOR** is the least explored: 16 cells, one named archetype.

See [[wiki/questions/scope-and-open-questions|Scope and open questions]] for the
under-filled gate families.

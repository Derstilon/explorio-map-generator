---
type: entity
title: "Production catalogue"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - graph-grammar
entity_type: specification
role: "Lock-and-key graph grammar productions P1–P9 of the dev branch"
first_mentioned: "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
related:
  - "[[wiki/concepts/graph-grammar-productions|Graph grammar productions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/questions/inconsistencies-sheet-doc-code|Inconsistencies]]"
sources:
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
claim_ids:
  - clm-explorio-only-p1-implemented
---

# Production catalogue

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: `lock_and_key_productions/productions.md` on `dev` (mermaid class
diagrams, pattern → replacement). Nodes marked `*` are new.

Most productions come in three variants, by what the new lock is inserted in
front of:

- **a** – a new empty area,
- **b** – an existing closed lock,
- **c** – an existing key to a closed lock.

| # | Name | New lock | New keys | Effect | Sheet row | Code |
|---|---|---|---|---|---|---|
| 1 | Chest | AND · CLOSED · PERM · keys 1 | 1 consumable primary | put a node behind a chest-like lock | LP 1 Locked Chest | 1b ≈ `L2`, 1c ≈ `L1` |
| 2 | Gate | OR · CLOSED · TEMP · keys 2 | 2 reusable primary, one on each side | gate openable from both sides | LP 50 Gate Lock | – |
| 3 | Decision | OR · **OPEN** · PERM · keys 2 | consumable primary + reusable **clue** | a decider key changes which obstacle opens the lock | LP 49 Pick your poison (sheet says Closed) | – |
| 4 | Tripwire | NOR · OPEN · PERM · FAILABLE · keys 2 | consumable primary, optional | trap an area behind a tripwire; parent `X != FAILABLE` | LP 45 Tripwire trap (sheet P5) | – |
| 5 | Ambush | NAND · OPEN · TEMP · OPTIONAL · keys 1 | reusable primary inside the area | area with its key inside works as an ambush | LP 73 Ambush at the Gate (sheet P4, XOR/consumable) | – |
| 6 | Tool assist | OR · CLOSED · TEMP · FAILABLE · keys 2 | consumable primary + consumable spare | obstacle passable with a consumable tool | LP 55 Tool assist | – |
| 7a | Sequence lock | AND · CLOSED · PERM | consumable primary, failable | one lock, a trap area and a success area | LP 5 | – |
| 7b | Gambit puzzle | OR · CLOSED · PERM · FAILABLE · keys 2 | consumable primary + spare | two equal areas, only one opens for good | LP 53 | – |
| 7c | Death trap | NOR · CLOSED · TEMP · FAILABLE | reusable clue | failure drops the player into a killzone area they may escape | LP 38 | – |
| 8 | Complexity increase | (any lock with < 3 keys, not failable) | +1 key | adds a key to an existing puzzle lock | – | – |
| 9 | Failure decrease | – | – | adds a **secret** edge from the area before a failable lock to the area behind it | – | – |

Productions 8 and 9 are meta-rules: they tune difficulty and recoverability
instead of adding a new archetype.

## Implementation status

Only production 1 exists in code, as `L1` (lock in front of a key, ≈ 1c) and
`L2` (lock in front of a lock, ≈ 1b), both hard-coded to AND · LOCKED · PERMANENT
· MANDATORY with one consumable MAIN key. Variant 1a and productions 2–9 are not
implemented. See [[wiki/questions/implementation-status-and-gaps|Implementation status and gaps]].

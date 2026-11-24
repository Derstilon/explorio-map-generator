---
type: concept
title: "Key dimensions"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - lock-and-key
complexity: basic
domain: procedural-generation
related:
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
---

# Key dimensions

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Usage count (reusability)

| Sheet | Productions doc | Code (`Reusability`) | Meaning |
|---|---|---|---|
| Reuseable | REUSE | `REUSABLE` | key stays after use (lever, clue, button) |
| Consumable | CONSUME | `CONSUMABLE` | key is used up (potion, gem, sacrifice) |
| – | – | `DUNGEON` | only on the seed key `K0`; dungeon-wide entry key |

## Key type

| Productions doc | Code (`KeyType`) | Meaning |
|---|---|---|
| PRIMARY | `MAIN` | intended key |
| SPARE | `SPARE` | alternative key (often riskier or consumable) |
| CLUE | `CLUE` | information or decider that changes how the lock opens |

The sheet has no key-type column; key type only appears in the productions doc
and code.

## Access

Keys carry the same access value as locks (required / optional / failable).
In productions 4–7 keys are often `OPTIONAL` while their lock is `FAILABLE`.

## Counters

The productions doc tracks `locks(n)` on each key (how many locks it opens).
The code stores a single `lock` attribute, so one key opens one lock.

## From the game design docs

- **Usage is not binary:** [[wiki/sources/source-gdd-03-items-compendium|GDD 03]] items break by chance (crowbar, lockpicks),
  work on cooldowns (cloaks), have charges (wands) or cost HP per use (Friendly
  mimic key); [[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]] staves recharge from mana. Candidate attributes:
  durability / cost, and a rate-limited value between reusable and consumable
  ([[wiki/concepts/items-as-keys|Items as keys]],
  [[wiki/concepts/spellcasting-as-limited-key-resource|Spellcasting as a limited key resource]]).
- **Element tag:** GDD 04 reactions suggest keys (and locks) carry an element or
  status tag.
- **Enemy keys:** bosses and monsters act as keys or locks ([[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]], [[wiki/sources/source-gdd-01-bestiary|GDD 01]]);
  `KeyType` MAIN/SPARE/CLUE cannot mark that.
- **Key burden:** a cost between pickup and use ([[wiki/sources/source-gdd-06-world-generation|GDD 06]];
  [[wiki/concepts/key-burden-and-compound-puzzles|Key burden and compound puzzles]]).

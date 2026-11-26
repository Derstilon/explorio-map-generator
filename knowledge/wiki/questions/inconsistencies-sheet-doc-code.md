---
type: question
title: "Inconsistencies between sheet, productions doc and code"
created: 2026-11-23
updated: 2026-11-25
status: developing
tags:
  - question
  - consistency
question: "Where do the product sheet, the productions doc and the dev code disagree?"
assessment: provisional
risk: normal
related:
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
  - "[[wiki/entities/dev-branch-codebase|Dev branch codebase]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
claim_ids:
  - clm-explorio-p4-p5-swapped
  - clm-explorio-vocabulary-drift
---

# Inconsistencies between sheet, productions doc and code

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Each item needs a decision on which source is right. None is resolved here.

## Sheet vs productions doc

1. **P4 and P5 swapped.** Sheet: Ambush at the Gate = 4, Tripwire trap = 5. Doc:
   Production 4 = Tripwire, Production 5 = Ambush. **Resolved:** the sheet's
   numbering ([[wiki/questions/owner-decisions|owner decision 2026-11-26]]).
2. **Ambush attributes differ.** Sheet LP 73: consumable key, XOR, temporary,
   required/optional, open. Doc P5: NAND lock, reusable key, optional access,
   temporary, open. **Resolved:** the sheet's XOR and consumable key, with the
   doc's shape ([[wiki/questions/owner-decisions|owner decision 2026-11-26]]).
3. **Decision / Pick your poison base state.** Sheet LP 49 (P3) is *Closed*; doc
   P3 "Decision" lock is `state(OPEN)`. The names differ too, and the sheet's only
   example ("tripwire in the corridor triggers a trap") does not describe a
   decision. **Resolved:** CLOSED, as the sheet
   ([[wiki/questions/owner-decisions|owner decision 2026-11-26]]).
4. **Sequence lock access.** Sheet LP 5 (7a) marks the lock *Failable*; doc 7a
   gives the lock inherited access `X` and makes the key and the trap area
   failable. **Resolved:** the lock is FAILABLE, and the key and trap area stay
   failable ([[wiki/questions/owner-decisions|owner decision 2026-11-26]]).
5. **Meta productions** 8 (Complexity increase) and 9 (Failure decrease) have no
   sheet row – expected, but the sheet's "PRODUCTION" column then is not a full
   index of productions.

## Inside the sheet

6. 94 rows for 96 combinations; two cells missing in the XOR/XNOR block (see
   [[wiki/entities/puzzle-archetype-matrix#Matrix defects|matrix defects]]).
   **Resolved:** `data/archetypes.yaml` has all 96 combinations in one fixed
   order; the two missing cells have no sheet LP.
7. Typo-level names: "Point of no? return", "Reuseable". **Resolved:** fixed in
   `data/archetypes.yaml` (the importer maps them).

## Doc / sheet vs code vocabulary

| Concept | Sheet | Doc | Code |
|---|---|---|---|
| Base state | Closed / Open | CLOSED / OPEN | `LOCKED` / `UNLOCKED` |
| Access | Required/Optional, Failable | X, OPTIONAL, FAILABLE | `MANDATORY`, `MISSABLE`, `FAILABLE` |
| Key type | – | PRIMARY, SPARE, CLUE | `MAIN`, `SPARE`, `CLUE` |
| Extra values | – | – | `DUNGEON` for `Reusability` and `OpenMode` |
| Place node | – | Area | `access` node |
| Edge | – | "opens to" | `access`, `unlocks` |
| Counters | – | `locks(L)`, `keys(K)`, `keys(n)`, `locks(n)` | sets; one `lock` per key |

## Raised by the game design docs

8. **Levitation vs chasms.** Sheet Tool assist ("levitation over a chasm") and
   Brogue's levitation key holder assume levitation crosses chasms; [[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]] says
   only Flying does. **Resolved:** levitation crosses chasms but cannot float up
   to the previous layer ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
9. **Biome names** differ between the code's 15 environment biomes and
   [[wiki/sources/source-gdd-06-world-generation|GDD 06]] / [[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]] (see [[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]).
   **Deferred:** to be fixed later ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
10. **WFC** means geometry generation in [[wiki/sources/source-gdd-06-world-generation|GDD 06]] but abstract-to-concrete content
    in the dev readme. **Resolved:** both uses are wanted ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
11. **Bestiary vs matrix:** the matrix's "magnetic sandworm" and Monster Assist
    creatures (spider, water elemental, treant, laser automaton) are not in
    [[wiki/sources/source-gdd-01-bestiary|GDD 01]].
12. **Inside GDD 05:** WIS is a base stat but missing from the class table; "spells
    can have minimal strength requirement" is likely meant as INT.

## Gate labels

13. **Alarm gate.** Sheet LP 52 *Alarm* is R · OR · Perm · Fail · Closed, but it
    plays as a trap: any trigger (the turret spotting the player) springs it and
    opens the monster cages. That is NOR over the triggers, the same family as
    *Stealth Mission* (LP 42). Proposal: move Alarm to R · NOR · Perm · Fail ·
    Open, the empty LP 44. It then differs from Stealth Mission by open mode and
    access: Stealth's alarms reset after a while (Temporary, Required/Optional),
    Alarm's cages stay open (Permanent, Failable). LP 52's cell (R · OR · Perm ·
    Fail · Closed) is then empty and needs an archetype or an unusable reason.

## Recommendation (proposal)

Pick one vocabulary (the sheet's is the most readable), rename the code enums to
match, and make the sheet's production column the single index once P4/P5 and
P3 are settled.

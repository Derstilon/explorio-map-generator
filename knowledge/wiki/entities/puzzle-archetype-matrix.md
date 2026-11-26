---
type: entity
title: "Puzzle archetype matrix"
created: 2026-11-23
updated: 2026-11-25
status: developing
tags:
  - entity
  - lock-and-key
  - product-sheet
entity_type: dataset
role: "Catalogue of lock/key attribute combinations with named puzzle archetypes and examples"
first_mentioned: "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
related:
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/concepts/lock-logic-gates|Lock logic gates]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-product-sheet-key-lock-matrix|Product sheet]]"
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
claim_ids:
  - clm-explorio-matrix-coverage
  - clm-explorio-matrix-missing-cells
---

# Puzzle archetype matrix

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: [[wiki/sources/source-product-sheet-key-lock-matrix|Explorio Product Sheet]].
Examples are translated from Polish and shortened.

## Source of truth: `data/archetypes.yaml`

The matrix lives in the repo as [`data/archetypes.yaml`](../../../data/archetypes.yaml):
one entry per combination (all 96), with an id, name, status, abstract play
pattern or unusable reason, productions, sheet LP and the translated examples.
`archetypes.py` loads and validates it, and the generator tags every lock with
its archetype id (GUI tooltip, JSON export). The file was seeded once from the
sheet by `tools/import_archetype_sheet.py` and is edited by hand since. The
tables below are a summary of the sheet as captured; the data file wins where
they differ.

Status in the data file (part 3 of the epic, waiting for owner review):

| Gate | Named | Proposed | Unusable |
|---|---|---|---|
| AND | 7 | 9 | 0 |
| OR | 6 | 10 | 0 |
| NAND | 3 | 13 | 0 |
| NOR | 4 | 12 | 0 |
| XOR | 4 | 12 | 0 |
| XNOR | 1 | 15 | 0 |
| **Total** | **25** | **71** | **0** |

## Shape

- Dimensions: key usage (2) × logic gate (6) × open mode (2) × access (2) × base
  state (2) = **96 combinations**.
- Rows `LP 0–93`: **94 rows**, all distinct.
- **25 rows are named archetypes**; 4 more unnamed rows carry examples; 65 rows
  are empty placeholders.
- 9 rows carry a production number that links them to the
  [[wiki/entities/production-catalogue|Production catalogue]].

### Named archetypes per gate

| Gate | Named / 16 cells |
|---|---|
| AND | 7 |
| OR | 6 |
| NOR | 4 |
| XOR | 4 |
| NAND | 3 |
| XNOR | 1 |

### Matrix defects

- Two combinations are missing: *Consumable · XOR · Permanent · Required/Optional
  · Closed* and *Reusable · XNOR · Permanent · Required/Optional · Closed*.
- The XOR and XNOR rows (LP 64–93) are not in the sort order used for the other
  gates, so LP numbers there do not follow the pattern; this is why two cells went
  missing.

## Named archetypes

Key: R = reusable, C = consumable; Perm/Temp; Req = Required/Optional, Fail =
Failable; Cl = Closed, Op = Open. **P#** = production number in the sheet.

| LP | P# | Archetype | Key | Gate | Mode | Access | State | Examples |
|---|---|---|---|---|---|---|---|---|
| 0 | | Advanced Puzzle | R | AND | Perm | Req | Cl | activate elements in order; rotate until all match; toggling one toggles neighbours (lights-out); hourglasses within a time window, last one beyond the door |
| 1 | 1 | Locked Chest | C | AND | Perm | Req | Cl | key or shaped item in a socket; door needs 2 gems / 3 obelisks; multi-stage drawbridge |
| 2 | | Broken Cycle | R | AND | Temp | Req | Cl | broken circuit – throw metal or find wire; crates block a laser; crystal not in fire; water wheel without current |
| 4 | | Legendary Quest | R | AND | Perm | Fail | Cl | assemble a legendary warrior's outfit to open his chambers or enchant a weapon |
| 5 | 7a | Sequence Lock | C | AND | Perm | Fail | Cl | offering of loot from enemies who desecrated a temple; item to destroy in a gas room, gas potions or vent switches as spare key |
| 6 | | Parkour | R | AND | Temp | Fail | Cl | buttons start an obstacle course with a safe way back; turning bridge whose route you must remember; lava blocks; door open for a short moment |
| 13 | | Burning bridges | C | AND | Perm | Fail | Op | bridge burning from both ends – water/ice potions; closing trash compactor drops you a floor; dwarven drills destroy a ledge; corridor filling with water/sand |
| 18 | | System Shutdown | R | NAND | Temp | Req | Cl | pull any battery of a force field (batteries on both sides); lower any beacon to calm quicksand |
| 20 | | Punishment | R | NAND | Perm | Fail | Cl | cages open on a wrong three-lever combination |
| 28 | | Mouse Trap | R | NAND | Perm | Fail | Op | magnetic sandworm pulls you by the items you pick up; whole room is a mimic that grows with loot taken; trap fires if you loot the whole vault / temple feast |
| 34 | | Rotating Passage | R | NOR | Temp | Req | Cl | rotating bridge can't open all routes at once; switch which portals work; kill the ice elemental freezing the mill's river |
| 38 | 7c | Death Trap | R | NOR | Temp | Fail | Cl | spikes under a wrong panel; floor collapses on a wrong panel or reversed combination |
| 42 | | Stealth Mission | R | NOR | Temp | Req | Op | trigger no alarm; alarms reset after a while but you start over |
| 45 | 5 | Tripwire trap | C | NOR | Perm | Fail | Op | simple room guard with no second chance; tripwire closes the door |
| 49 | 3 | Pick your poison | C | OR | Perm | Req | Cl | tripwire in the corridor triggers a trap |
| 50 | 2 | Gate Lock | R | OR | Temp | Req | Cl | pressure plates on both sides of a door; two teleport pairs |
| 52 | | Alarm | R | OR | Perm | Fail | Cl | turret spots the player and opens monster cages |
| 53 | 7b | Gambit puzzle | C | OR | Perm | Fail | Cl | failed ritual: finish the blood circle to summon an enemy, or holy water to summon a chest |
| 55 | 6 | Tool assist | C | OR | Temp | Fail | Cl | invisibility potion across a battlefield; iron-skin potion in a magnetic room over lava; levitation over a chasm; holy-light scroll through cursed shadows; speed potion / teleport wand for a timed puzzle |
| 57 | | Point of no return | C | OR | Perm | Req | Op | passage collapses; player must find another way back |
| 67 | | Cipher | C | XOR | Perm | Fail | Cl | one solution opens, the other seals forever; magic seal to remove or strengthen; glowing symbols; cultist blood symbols on crates; dwarven generator codes overload; one true statuette among false ones |
| 73 | 4 | Ambush at the Gate | C | XOR | Temp | Req | Op | ambush beyond a portal; enemy disables portals with a lever after you teleport |
| 74 | | Two state obstacle | R | XOR | Temp | Req | Op | room toggles between states (bridges, magnetism, lasers/force fields, lighting that holds back ghosts); use both |
| 78 | | Monster Assist | R | XOR | Temp | Fail | Op | use enemy AI to cross a gap (spider/chasm, ice elemental/bog, water elemental/lava, treant/acid); charging enemy breaks the crystal holding a key; laser automaton fires a mechanism |
| 89 | | Infiltration | C | XNOR | Temp | Req | Op | enemy stronghold: full stealth or kill everyone |

## Unnamed rows with examples

| LP | Combination | Example |
|---|---|---|
| 33 | C · NOR · Perm · Req · Cl | monster trinket from one of several camps opens a monster door or chest |
| 48 | R · OR · Perm · Req · Cl | use any nearby effect source: coil to charge a battery, move a crate out of a laser, lure a sandworm to break rocks |
| 54 | R · OR · Temp · Fail · Cl | gas room full of dead enemies, vent switch, elemental boss |
| 60 | R · OR · Perm · Fail · Op | looting the whole vault springs a trap; put items back to cancel it |

## Cross-references from the game design docs

- **Monster Assist (LP 78):** [[wiki/sources/source-gdd-01-bestiary|GDD 01]] supports Ice Slime (freezes water),
  passive Sand Worm (digs through sand walls) and golem charges, but has no
  spider-over-chasm, water elemental, treant or laser automaton. See
  [[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]] and
  [[wiki/concepts/enemy-lure-and-deterrence|Enemy lure and deterrence]].
- **Mouse Trap (LP 28):** the "magnetic sandworm" has no bestiary match (sand worms
  are not magnetic; the Magnetic Slime is); the room mimic is the bestiary's Room
  Mimic miniboss.
- **Tool assist (LP 55):** "levitation over a chasm" stays valid: levitation
  crosses chasms but cannot rise to the previous layer ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]; overrides
  [[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]). Cape skills and class
  kits ([[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]) can also supply these keys, so the row needs an in-world
  alternative to stay solvable for every class.
- **LP 54 (unnamed, R · OR · Temp · Fail · Cl):** synthesis – a reusable twin of
  Tool assist: cloak skills, Flask of endless water ([[wiki/sources/source-gdd-03-items-compendium|GDD 03]];
  [[wiki/concepts/items-as-keys|Items as keys]]).
- **Legendary Quest (LP 4):** [[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]] has a matching idea – armour set pieces as
  keys, rewarded by a blessing or a fight with the previous owner's ghost.

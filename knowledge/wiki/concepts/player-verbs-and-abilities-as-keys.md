---
type: concept
title: "Player verbs and abilities as keys"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - lock-and-key
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/entities/character-classes-and-starting-kits|Character classes and starting kits]]"
  - "[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]"
  - "[[wiki/concepts/items-as-keys]]"
sources:
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05 – Gameplay and Progression Systems]]"
claim_ids:
  - clm-explorio-player-verb-set
  - clm-explorio-cape-movement-skill
  - clm-explorio-curses-lifted-by-condition
---

# Player verbs and abilities as keys

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

GDD 05 defines what the player can *do*. Every verb below is a candidate
**reusable key** in the story graph that the player always carries, so it never
needs to be placed in an area. This page lists them and maps them to the
lock-and-key model; the mapping is synthesis, not stated in the doc.

## Control verbs

From the keyboard and gamepad schemes (section "Controls"):

| Verb | Keyboard | Doc notes | Key role (synthesis) |
|---|---|---|---|
| Movement | WASD | movement speed modified by armor, skills, enchants, potions, scrolls | baseline; speed matters for timed (temporary) locks |
| Sprint | hold Spacebar | costs stamina; heavy armor reduces regeneration | timed locks, Parkour, chases |
| Cape skill | Spacebar | active/passive skill from the cape slot | traversal key (see below) |
| Crouch / Investigate | Ctrl | one button for sneaking and inspecting | stealth locks (Stealth Mission, Infiltration); finding hidden clues (CLUE keys) |
| Grab entity | Alt / hold A | grab entities | moving crates, bodies, throwables (Broken Cycle "move a crate out of a laser") |
| Interact | E / Y | levers, doors, NPCs | default operator for reusable switch keys |
| Use item (main / alternative) | LMB/RMB, Shift+LMB/RMB | each hand has a main and an alternative use | tools as keys; two hands allow two tools at once |
| Equip to hand | 1–8, Shift for second hand | toolbar of 3 slots, up to 8 with gear | limits how many tool-keys are ready at once |
| Quick slot | X | use an item on self instantly | consumable self-buff keys (potions in Tool assist) |
| Drop item | Q + mouse | drop from either hand | placing weight on plates, offering items |

## Traversal and cape abilities

- The **cape** slot holds one active or passive skill: a movement skill with a
  cooldown, a special attack with stamina cost, or a passive stealth or
  enemy-repellent skill with drawbacks (section "Inventory").
- The Polish notes name concrete cape skills: **dodge, dash, blink**, a one-off
  multishot, or a shot plus disengage. A cape could also scare off one kind of
  enemy (or small / medium / large creatures) at the cost of the movement skill.
- The Arcane Tailoring shop sells capes and explains cape abilities; "capes and
  cape skills" are listed as a possible **vertical meta unlock**.

Implication (synthesis): blink and dash are classic traversal keys (gap,
barrier). Because the cape is one slot and may be locked behind meta
progression, the generator cannot assume the player has one. A traversal lock
should either be optional, or be an OR gate with a world key (levitation
potion, bridge lever) – which matches the existing Tool assist row (LP 55:
"levitation over a chasm", "teleport wand").

## Ranged and environmental verbs

Tips from the Fletching shop list what the game expects the player to use:

- **activating things at a distance** with an arrow or a thrown weapon,
- **gases, fire and other natural effects spreading**,
- **stealth** and when a critical blow is possible,
- **salvaging** items (melt metals, burn grimoires) for materials.

Achievement ideas add more verbs used on the environment: extinguishing an
enemy's torch, electrifying water, rooting an enemy under water, pushing enemies
off a cliff with air, making steam clouds, moving gases with air. These match
the element families on
[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]
and the Monster Assist / Broken Cycle rows of the
[[wiki/entities/puzzle-archetype-matrix|archetype matrix]].

## Items with key-like behaviour

| Item / system | Doc source | Lock-and-key reading (synthesis) |
|---|---|---|
| Picklocks (Prisoner kit, "a lot") | Unlockables – Classes | consumable spare key for locked doors/chests |
| Pickaxe, lantern, explosives (Miner kit) | Unlockables – Classes | reusable dig key, light key, consumable breach key |
| Stealth ring (Prisoner) | Unlockables – Classes | reusable stealth key |
| Head gear with water breathing | Gear slots | reusable traversal key for flooded areas |
| Boots with elemental debuff immunity | Gear slots | pass fire/water hazards without catching fire or getting soaked |
| Scroll of "Mapping", "Detect magic" | Achievements – Cartographer, Scientist | CLUE keys (reveal layout / magic) |
| Unique items: Umbrella, Mimic Key, Serpent staff, Deck of cards | Achievements – Loose Ideas | named uniques, behaviour not described |
| Armor pieces used as keys | Achievements – Loose Ideas | a puzzle where keys are armor pieces of a set; reward is a blessing or a fight with the previous owner's ghost – matches Legendary Quest (LP 4) |

## Curses lifted by a condition

The Polish notes propose that curses on gear are removed not only by a scroll,
NPC or altar but by a **specific place or an action repeated some number of
times**. A run or class could start with all gear randomly cursed, with
cleansing as an optional bonus objective or the sole objective, "so the dungeon
can be generated more around your curses". Cursed gear would be stronger than
starting gear but have side effects (example: a sword that teleports hit
enemies a short distance, so they surround you).

Reading (synthesis): this is a lock on the *player*, whose key is placed in the
dungeon (a place or a repeatable action). It is the first explicit request for
the generator to take player state as input.

## Agreement with the vault

- Extends [[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]:
  the vault so far treats keys as things placed in areas. Verbs and starting
  kits are keys the player brings; the graph needs a notion of "keys available
  at start" per class/loadout.
- Supports the open question in
  [[wiki/questions/scope-and-open-questions|Scope and open questions]] on
  whether tools-as-keys are typed in the graph or resolved in the content
  stage: class kits make tool availability vary per run, so the solver needs it.

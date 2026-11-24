---
type: entity
title: "Environmental hazard and container catalogue"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - lock-and-key
entity_type: catalogue
role: "Hazards, interactables and containers the design doc offers as building blocks for locks, keys and traps"
first_mentioned: "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
related:
  - "[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|Trap, puzzle and encounter intent taxonomy]]"
  - "[[wiki/concepts/elemental-status-interactions-as-locks-and-keys]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
---

# Environmental hazard and container catalogue

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *Environmental Hazards*, *Chests and Containers Overview* and *Materials*
in [[wiki/sources/source-gdd-06-world-generation|GDD 06]]. The *Role* column is
my reading of each element in lock/key terms (L = can be a lock, K = can be a
key or key source, T = trap / hazard, C = clue carrier).

## Hazards and interactables

| Element | Doc description | Role |
|---|---|---|
| Spikes | – | T |
| Pendulum blade / buzzsaw belt | damaging collider moving back and forth or one way | T |
| Sight sensor | items usable only while you look away (walk a maze backwards); variant: a watcher that fires if its view of you is clear – puzzle: trigger all watchers without them blocking each other | L, T |
| Rolling boulder | comes from a wall hole, stops on collision, presses plates and buttons | K (presses plates) |
| Mirage items | lever turns into a snake, plate into spiked jaws; desert animals; tied to a legendary snake staff; special theme | T, decoy |
| Moving platforms | move while their activator keys stay active; for ranged fights and parkour | L (temporary) |
| Wall torches | fire source; puzzle may need lighting or putting out | K, L |
| Window | sight but no movement; can be locked; can show a clue | C |
| Turrets | magic (element symbols), jungle darts with status effects, gun (long recharge) | T |
| Vents | gas or flames when activated | T |
| Locked doors | **small: one key; medium: mechanism; large: 3 keys** | L |
| Boxing door | punches outward when opened | T |
| Interactive shadow / reflection | the shadow or puddle reflection of an item can be used like the item | C, K |
| Teleport platforms | one- or two-way | edge type |
| Wooden bridges | flammable | L (Burning bridges) |
| Retractable bridges, walls, windows | cover or vision independent of access; bridge as a fancy door; walls make mazes or hide clues | L |
| Light bridges | toggled by a mechanism | L |
| Pit | spike, lava, void | L, T |
| Lakes | water, lava, mud, quicksand, brimstone, ambrosia, acid, honey | L |
| Puzzle mechanism | few states, advances on activation, may activate neighbours | L (lights-out) |
| Lasers | redirected by mirrors, pass through crystals changing colour, stop on anything else | L, K |
| Pressure tiles | predetermined path across all tiles | L |
| Levers | – | K |
| Chairs | sit out of combat; throne-like ones trigger traps or puzzles | K, T |
| Pressure plates | active while something stands on them | K (temporary) |
| Fountain | infinite fluid source, acts as shallow water; statue may come alive | K, T |
| Button | active for a fixed time (hourglass?) | K (temporary) |
| Elemental runestone | activates on heat, cold, wet, wind, current, magnetism, moonlight or sunlight; element symbol is the clue | L, C |
| Elemental device | makes wind, heat, freezing, light, water jets, magnetism | K |
| Darkness | no ambient light on the layer; shadows deal damage | T (layer-wide) |
| Sunlight crack | hurts trolls (?); activates light runestones | K |
| Moonlight crack | turns and empowers werewolves | T |
| Ritual | blood circles or runes, completed with blood or by moving items | L |
| Seal | locked door or chest behind a ritual; one large symbol is the clue; symmetrical rune shapes | L, C |
| Machine without power | needs a magic battery, current, coal in a furnace or a water current (dwarven furnace: coal; laboratory: soul stone) | L (Broken Cycle) |

Two items are **layer-wide** (Darkness, Sunlight/Moonlight cracks), i.e. a
property of a layer or biome rather than of a room.

## Containers

| Container | Rule | Role |
|---|---|---|
| Chest | locked with a key or opened by interaction | L |
| Crate | cannot be opened normally; works as cover | L (needs force) |
| Sarcophagus | strength check to open | L (stat gate) |
| Barrel / silk cocoon | fluid, corpses, gas, small enemies or one stack of an item | K, T |
| Clam / statue head | opened by attacks; gas plus one item; closes after a few seconds, damaging anyone still looting | T |
| Tree hollow | critters or one item | K |
| Pillar / stump | one item on top; can lock and keep it | L |
| Armour stand / weapon rack | only the armour or weapons visible on it | K |
| Bookshelf | paper, books, scrolls | C |
| Cabinet | bookshelf items plus jewellery, keys, gems, food | K |

### Materials

- Ceramic: breaks in one hit.
- Wood: somewhat vulnerable to physical and fire damage.
- Stone: smashed by a charging large enemy (Monster Assist).
- Iron: reacts to electricity and magnetism (maybe opens under current).

Material therefore decides **which key types open a container**, a natural
input for archetype choice per biome (synthesis).

## Materials of the world

Liquids (splatters and puddles, Noita-style) and gases are headings only, apart
from two lure gases: **pheromones** attract arthropods, **greasy aroma**
attracts predator beasts – both usable as keys for Monster Assist.

## Relation to the vault

- **Agrees** with the sheet's examples (burning bridges, lasers, quicksand,
  batteries, rituals) and the Genshin mechanic families in
  [[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]].
- **Extends** with gate sizes for doors (1 key / mechanism / 3 keys = AND over 3)
  and stat-checked containers (sarcophagus), a key type the sheet lacks: a
  character **stat** as key.

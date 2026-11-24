---
type: entity
title: "Boss and elite catalogue"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - bosses
entity_type: catalogue
role: "List of bosses, mini-bosses, gauntlets, elites and mounted bosses from GDD 02, with biome and gating hooks"
first_mentioned: "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02]]"
related:
  - "[[wiki/concepts/bosses-as-locks-and-gates|Bosses as locks and gates]]"
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/concepts/five-room-dungeon-biome-template|Five Room Dungeon biome template]]"
  - "[[wiki/entities/bestiary-monster-families]]"
sources:
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02 – Difficulty Balance and Bosses]]"
---

# Boss and elite catalogue

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## What makes a boss

GDD 02 defines a boss by two traits – **real threat** and **unique mechanics**
– and two roles – a **memorable encounter** and a **storytelling climax**. The
four headings have no body text yet.

## Mini-bosses and named encounters

"Biome / place" is the doc's location; "Gating hook" is what can act as a
lock or key (see [[wiki/concepts/bosses-as-locks-and-gates|Bosses as locks and
gates]]). Empty cells: the doc says nothing.

| Name | Biome / place | Core mechanics | Gating hook |
|---|---|---|---|
| Amber colossus | – | spawns a medium insect at a health threshold; hits drop amber shards that spawn small insects | – |
| Shipwreck | – | only two inspiration links (wreck hulk / shipwreck golem) | – |
| Lorekeeper (Desert Lich) | own room; ruins/desert implied by name | respawns at phylacteries, ghosts, Raise Dead, barriers, flying skulls, column collapse, lightning that spares its honour guard, 3 teleport scrolls usable only in its room, lifesteal | entry gate after a puzzle; gate closes; exit by kill or timed buttons; collapse timer |
| Archpriest / Ascending Demon | Defiled Church | two phases; phase 1 behind an impenetrable barrier while corpses spawn enemies; phase 2 demon charges, eats and throws corpses | destroy ritual elements to start phase 2 |
| Lynx Barbarian (mini-boss / elite) | Cold Biome | aggressive, dual axes | – |
| Kraken (Swamp Monster) | Swamp Biome | head plus independent tentacles rising from the ground | – |
| Elemental Wolf Pack | – | pack led by an elemental spawn shaped like a wolf | – |
| Magma Basilisk Lair | magmatic area of a few rooms | basilisks pose as statues; petrifying gaze slows; blunt hits on statues stun the player, slashing dazes, piercing is safe; weak to bludgeoning, immune to fire, high piercing resistance | identify the real basilisk |
| Tomb of Great Knight | tomb of many small rooms | skeletons/undead and wandering ghosts enter a stasis phase when killed and come back | killing the knight removes ghosts and stops undead returning |
| Bonespawn in the Crypt | Crypt | fight starts when all skeletons are killed | open question: doors close? |

Rewards are described only for the Lorekeeper (runes, magic items, an ancient
tome, high-end crafting materials) and the Basilisk (armour or materials, loot
of past victims).

## Gauntlet arenas

Longer fights with multiple enemy waves.

| Name | Mechanic |
|---|---|
| Elemental Colosseum | elemental gems change the environment periodically |
| Chess Golem Gauntlet | big room in Ruins with a chessboard; stepping on the king's square starts it; pawns advance one move per second; killing a piece activates the one behind it; pieces move by chess rules |
| Haunted Colosseum Gauntlet | undead audience; haunted armory (spectral weapons); haunted armada (spectral ships in bottles) |

## Elites

| Elite | Traits | Locations | Gating hook |
|---|---|---|---|
| Elite pirates | "piratified" elite monsters | – | – |
| Phantom Frigate | medium-sized ghost ship | – | – |
| Werewolf | with a wolf pack; resists magic | – | easy to kill with silver |
| Vampire | lifesteal bite, disarming and offensive spells, bats on death, immune to arrows, magic resistance; ashes are an alchemical component | Ruins, Mausoleum, Cemetery | respawns from coffin unless *Last Rites* scroll/spell; drops nothing until then; coffin holds treasure |
| Minotaur | two-handed axe, high HP; Rage, Rush (breaks barrels/chests on its path); drops Minotaur Horns | Minotaur Maze | – |
| Djinn | resistant to magic; neutral, asks for a wish ("Gold" spawns a Golden Golem) | Desert, Treasury | wish choice |

## Mounted bosses

Two creatures combined into one enemy. Inspirations: Nuckelavee, Dullahan
(floating jack-o'-lantern sharing its health bar), the Four Horsemen, the Wild
Hunt, Nazgûl, Kelpie.

| Horseman | Powers | Mount | Weapon | Core ideas |
|---|---|---|---|---|
| War | Heat + Cold | T-Rex monster | Greatsword | mount switches elemental infusion; heat hardens weapon or disarms; cold slows or knocks prone |
| Pestilence | Void + Necrosis | Spider monster | Greatmaul | void webbing drains; summons poison rats or void spiders; polymorph idea |
| Famine | Purification + Resistance | Boar monster | Longbow | mount corrodes gear; arrows clear player effects; rider cleanses self and gains resistance |
| Death | Divination + Temporal | Crow monster | Scythe | reveals player, slows time in areas; death mark lowers resistance to last damage type; scythe ages the player |

## Relation to the vault

- Biome names used here (Cold, Swamp, Defiled Church, Ruins, Mausoleum,
  Cemetery, Desert, Treasury, Minotaur Maze, Crypt) only partly match the 15
  environment biomes in the dev code (e.g. *swamp* and *desert cenotaph* exist;
  *cold* is close to *frozen wastes*; Defiled Church, Cemetery, Treasury do not
  exist). See [[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]].
- Vampire, werewolf and undead themes match encounter biomes *vampires*,
  *werewolf* and *necromancy* in the code.

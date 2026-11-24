---
type: entity
title: "Bestiary monster families"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - bestiary
entity_type: catalogue
role: "Catalogue of Explorio monster families with tiers and non-combat roles"
first_mentioned: "[[wiki/sources/source-gdd-01-bestiary|GDD 01]]"
related:
  - "[[wiki/entities/monster-encounter-biome-affinity|Monster encounter and biome affinity]]"
  - "[[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]]"
  - "[[wiki/concepts/enemy-lure-and-deterrence|Enemy lure and deterrence]]"
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/boss-and-elite-catalogue]]"
sources:
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01 – Bestiary]]"
claim_ids:
  - clm-explorio-slime-size-split
  - clm-explorio-critters-nonaggressive
---

# Bestiary monster families

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Classification axes

The doc tags monsters along six independent axes (a monster takes one value per
axis). These are candidate tags for spawn filtering; the doc does not say how
they are used.

| Axis | Values |
|---|---|
| Physical body | Mechanical, Organic, Elemental, Incorporeal |
| Intelligence | Elders, Humanoids, Beasts, Critters |
| Biological division | Reptile, Arthropod, Amphibious, Avian |
| Relation to life | Immortal, Undead |
| Plane of existence | Demonic, Ethereal, Ancient |
| Culture | Dwarven, Pirate, Atlantic, Of Dunes, Elven, Artificial |

## Families

"Elite / mini / boss" lists the stronger variants the doc names. "Non-combat
role" is what matters for puzzles and gating (detailed in
[[wiki/concepts/monsters-as-keys-and-locks|Monsters as keys and locks]]).

| Family | Members (selection) | Elite / miniboss / boss | Non-combat role |
|---|---|---|---|
| Critters | animated books, leeches, birds (parrot), fellfowl, cinder swarm, pebblemental, sandling, fairies/wisps, monkeys, bats, lizards, frogs, fish, eels, bear cub, goat, rats, beetles/scarabs, spiders, crabs, wolves/foxes, ants, eggs, scorpions, wasps | Cockatrice; Mama Bear; worgs; Hermit Galleon | books give lore/clues; parrot alerts pirates; fairies are light, jar item and altar sacrifice; monkeys steal items; leeches enter the inventory |
| Slimes | base, electric, magnetic, shadow, acid, magma, tar/mud, jungle, poison, coral, ice, water, stone, explosive, wind, blood, holy water, golden | Mist Aberration, Booze Slime (mini); Titan Slime (boss) | swallow items and **keys**; splatters are crafting fluids (glue, superconductor, acid, freeze, levitation, water breathing, explosion) |
| Elemental spawns | Phoenix, Kelpie, Atlas, Wendigo, Quetzalcoatl, Raiju, Fell spawn, Nightmare | – | drop elemental runes |
| Elemental manifestations | treasure, blood, water, mud, poison, mirror/crystal elementals; sand, air, magma revenants; fire apparition | Treasure Elemental (mini); Mirror Elemental with special arena | drop elemental runes |
| Genies | Djinn, Efreet, Oni, Marid, Dao, Qorrashi, Khayal, Janni | (powerful by default) | command lesser elementals |
| Golems | stone, rune, ice, magma, candle-wax, acolyte, garden guardian, harvest, gargoyle, chess, chain | Adamantine (boss), Lab golem (mini), chain golem boss | hide as statues until a condition wakes them; chess golems as a gauntlet |
| Orcs | green, frost, red, black; tribes Machine, Looter, Feral, Mystic, Warmonger; classes Warboss…Drummer | Warboss | Warboss summons orcs; drummer buffs a camp |
| Goblins / hobgoblins | chief, rider, stalker, grunt, shaman, bombardier | Chief | poison, bombs |
| Rat men | pack leader, slave, warrior, mutant | Pack leader | – |
| Kobolds | archer, thief, mage, soldier, tinkerer | Dragon Priest (mini) | lured by gold or torches; lay bear traps and totems; thief steals a weapon |
| Trolls | cave, forest, ice, coast, night, graveyard, primal | hag, trapper, assassin, chieftain, raptor rider, pterodactyl pilot | – |
| Other land humanoids | troglodytes, cyclops, jotunkin, ogres, snakefolk, werewolves | Heartless Ogre | – |
| Flying humanoids | crowfolk, harpies, valkyries, winged demon | – | – |
| Amphibious humanoids | naga, salamander, gorgon/medusa, frog people | Gorgon | gorgon's gaze can end the run; her head drops as a wand |
| Hybrids | koibra, griffs, owlbear, hippocampus, flying monkey, manticore, fell beasts, sphinx, canisphinx, chimera | – | – |
| Cursed humanoids | werebeasts, vampire spawn, bruxa, vampire lord | Vampire lord | moonlight sources boost werebeasts; players can become werewolf or vampire |
| Mimics | chest, wall, critter, item, bottle, room | Room Mimic (mini); Homunculus, Doppelganger (bosses) | disguise as chests, walls, doors, bridges, items |
| Arthropods and worms | abductor spider, honeypot ant, whitenight moth, mirage arthropods (serpent staff, scorpion lever, golden scarab, sandstone termites, brass centipede, gilded arachnid), sand worms | – | disguise as levers, pressure plates, hourglass, coins; become tools when caught; sand worm digs a path |
| Magical reptiles | behir, basilisk, wyvern, dragons, faery dragon, dinosaurs, hydra, Loch Ness monster | Nightmare Dragon (mini) | faery dragon aggressive only if you capture fairies |
| Void monstrosities | shades, wraiths, nightmare spawn | – | shades share your location with all void creatures on the floor |
| Undead | zombie, drowned, flying brain, skeletons, ghouls, ghost, haunted object, mummies, flesh aberration, lich, death knight | Banshee (mini); Gray Philosopher (boss) | ghosts phase through solid objects |
| Sylvanids | treants, flower tendrils, dryad, gremlins, memory moss, magical flowers, myconids | Hangman treant (mini) | gremlins steal one item type and teleport to a lair; memory moss steals spells |
| Automatons | sphere defender, mechanical spider, centurion, drone fly, scarab | Centurion (mini) | centurion's energy cell opens doors; drone fly alarms constructs |
| Pirates | subtype of any humanoid | – | pirates of any race are mutually neutral; all races hostile to pirates |
| Demons | imps, imp mother, infernal, inquisitor, satyr, fellguard, overseer | Fellguard boss with its own arena | fell damage ignores armor resistances |

## Threat tiers and pacing hints

The doc has no formal difficulty scale, but it gives tier signals the generator
could use for pacing (synthesis):

- **Critters** are "of lesser significance": they don't attack unless attacked
  or approached, mostly don't chase, and many flee from light, pointy weapons or
  the death of a pack-mate.
- **Size tiers**: slimes have sizes (e.g. Size IV); a larger slime splits into at
  most two of the next size, or one of the next size plus two of the size below.
  Stone, golden and titan slimes do not split.
- **Equipment tiers**: orc warriors have Tier I–III; Warboss and goblin Chief can
  take a second class.
- **Level hints**: hobgoblins are "harder goblins for lower levels"; the rat-man
  Pack Leader is a medium-level enemy that can spawn in low-level locations.
- **Variant ladder**: most families have a normal → elite → miniboss → boss
  ladder (e.g. fellfowl → Cockatrice; slime → Titan Slime; ghost → Banshee →
  Gray Philosopher).

## Gaps in the doc

- Many entries are a heading only (troglodytes, cyclops, snakefolk, wasps,
  zombie, lich, death knight, basilisk, manticore…).
- "Blood Elemental" is listed under both manifestations and undead; "Flesh
  Aberration" appears twice under undead.
- "Enemy tactics" is an empty section.

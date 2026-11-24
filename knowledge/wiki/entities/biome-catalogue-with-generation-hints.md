---
type: entity
title: "Biome catalogue with generation hints"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - biomes
entity_type: catalogue
role: "The design doc's list of biomes, their layout hints and the biome attributes still to define"
first_mentioned: "[[wiki/sources/source-gdd-06-world-generation|GDD 06]]"
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/concepts/room-shape-types-and-layout-methods|Room shape types and layout methods]]"
  - "[[wiki/concepts/boss-and-race-theme-overlays|Boss and race theme overlays]]"
  - "[[wiki/entities/monster-encounter-biome-affinity]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-biome-todo-attributes
---

# Biome catalogue with generation hints

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *Biomes* section of
[[wiki/sources/source-gdd-06-world-generation|GDD 06]]. The doc lists 41 example
biomes (my count); about half have a one-line description and a dozen have a
layout hint. Families below are my grouping, not the doc's.

## Biome attributes still to define

The doc's own *To do* list for every biome:

| Attribute | Notes from the doc | Vault / code counterpart |
|---|---|---|
| Connections between biomes | – | `adjacency_restrictions` in `environment_biomes.py` (defined, unused) |
| Biome weights | "where should the connection start? before or after the transition" | none |
| Special enemies | – | encounter biomes (code) |
| Tags | e.g. *Cold* | none |
| Normal / Hard version | e.g. Stronghold of The First Kings is the hard Dwarven Ruins | none |
| Size | **Large, Small, Unique Layer** | none; no layer concept in code |
| Can be end-point / boss biome | – | `valid_end` (defined, unused) |
| Encounters per biome and per layer | "green biomes should have more plant encounters if the layer is surrounded by green biomes from both sides"; treasure in castles and ruins concentrated in one place | none |
| Generic variants | variants driven by strong themes of the neighbours | none |

**Implications (synthesis):** "Unique Layer" means some biomes fill exactly one
layer; "surrounded … from both sides" suggests layers sit in a sequence where a
layer has two neighbours. Both feed the open question of how a zone is cut into
layers in [[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]].

## Catalogue

Layout hints use the [[wiki/concepts/room-shape-types-and-layout-methods|room types]].
*Code* = matching name in the dev branch's 15 environment biomes (my matching;
"?" = uncertain).

| Family | Biome | Description / layout hint (from the doc) | Code |
|---|---|---|---|
| Rock | Caves | standard caves, stalactites, stalagmites, underground water | caves |
| Rock | Crystal Caverns | glowing crystals and gems with magical properties | – |
| Rock | Abandoned Mines | mineshafts, minecart tracks, old equipment, hostile creatures | mineshaft |
| Rock | Underground Tunnels | straightforward man-made tunnels or bunkers; barriers as ore veins | – |
| Rock | Abyssal Depths | darkest depths; abyssal / Lovecraftian themes | – |
| Fire | Magma Chamber | depths of the crust, molten lava | – |
| Fire | Molten Caverns | – | molten caverns |
| Fire | Volcanic Wastes | lava flows, geysers, unique resources | – |
| Ice | Ice Caverns | ice formations, glaciers, frozen creatures | – |
| Ice | Frozen Wastes | – | frozen wastes |
| Green | Fungal Forest | bioluminescent mushrooms, unique flora and fauna | – |
| Green | Forest | – | forest |
| Green | Jungle | lush underground ecosystem | – |
| Green | Primal (Jurassic) Jungle | – | – |
| Green | Overgrown Garden | abandoned castle grounds taken by nature; clearance of hedge walls that can be destroyed but spawn angry treants | overgrown garden |
| Green | Hive Cluster | part of a green biome grown into a hive; clearance of small honeycomb rooms with breakable walls, or a wax-blob barrier on a regular level | – |
| Green | Oriental Biome | cherry blossom, meditation garden, bamboo forest | – |
| Water | Subterranean River / Lake | underground body of water, aquatic life | – |
| Water | Swamp | stagnant water, dangerous flora, amphibians; clearance with lots of water and long walls | swamp |
| Water | Marshland | – | – |
| Water | Sunken Waterways | beaches, water passages, submerged chambers; islands in water, or long water-filled tunnels linking sections | sunken caverns ? |
| Water | Ship Graveyard | **unique aquatic layer**; shipwrecks, vengeful undead, scavengers; relics from prefab shipwrecks | – |
| Desert | Buried Desert | dunes and mirages underground | – |
| Desert | Eternal Oasis | swamp/waterway layout, desert style and enemies | – |
| Desert | Dunes | – | – |
| Desert | Desert Tomb | – | desert cenotaph ? |
| Undead | Ancient Catacombs | burial chambers, haunted, undead | – |
| Undead | Cemetery | clearance filled with tombstones | – |
| Undead | Crypts | – | – |
| Undead | Mausoleum | – | – |
| Built | Dwarven Ruins | special rooms: treasury, library, menagerie | dwarven ruins |
| Built | Stronghold of The First Kings | **hard version of Dwarven Ruins**; top layer may be a stronghold plaza | – |
| Built | Ruined Underground City | buried city, crumbling structures, artefacts | – |
| Built | Underground Bastion | hostile maze of traps, puzzles, strong enemies | – |
| Built | Labyrinth | maze corridors between rooms, or a plaza that is a grid labyrinth | – |
| Built | Sanctuary (Temple / Shrine) | sacred site, unique architecture and guardians; circular plaza | – |
| Built | Forgotten Workshop | falling-apart laboratory, magical entities, failed experiments, mechanical puzzles | forgotten workshop, laboratory ? |
| Built | Abandoned Settlement | gravel and dirt caverns with eroded structures; clearance with riverbed and waterwheel shelter | abandoned settlement |
| Castle | Gothic Castle | paintings, dining rooms, corridors; huge, possibly spiral stairs | abandoned castle ? |
| Castle | Gothic Dungeons | under the castle: traps, prison cells, torture chambers | dungeon ? |
| Castle | Lord's Cenotaph | honours the (presumably) long-gone lord; statues, treasure, followers | desert cenotaph ? |

## Agreement and gaps versus the code

- 10 of the 15 code biomes have a clear match; *dungeon*, *abandoned castle*,
  *laboratory*, *desert cenotaph* and *sunken caverns* only match loosely. The
  code's "desert cenotaph" blends the doc's Desert Tomb and (castle) Lord's
  Cenotaph.
- The castle trio (Gothic Castle → Gothic Dungeons → Lord's Cenotaph) and the
  dwarven pair (Ruins → Stronghold) read as vertical biome sequences: candidates
  for multi-layer zones (synthesis).
- Several layout hints create lock material directly: destructible hedge walls
  guarded by treants, breakable honeycomb walls, ore-vein barriers, islands that
  need water crossing. See
  [[wiki/entities/environmental-hazard-and-container-catalogue|Environmental hazard and container catalogue]].

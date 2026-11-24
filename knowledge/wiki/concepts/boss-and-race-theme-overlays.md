---
type: concept
title: "Boss and race theme overlays"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - biomes
  - themes
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/biome-catalogue-with-generation-hints|Biome catalogue with generation hints]]"
  - "[[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|Trap, puzzle and encounter intent taxonomy]]"
sources:
  - "[[wiki/sources/source-gdd-06-world-generation|GDD 06 – World Generation]]"
claim_ids:
  - clm-explorio-mimic-boss-two-layers
---

# Boss and race theme overlays

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source: *Themes* section of
[[wiki/sources/source-gdd-06-world-generation|GDD 06]].

## Theme layers

A **theme** changes biomes and encounters so they fit a faction. The doc names
three kinds:

- **Race themes** – every humanoid race has its own theme; other enemy types
  share a general theme (e.g. *Elemental* for elemental creatures); dragons have
  both a separate and a general theme.
- **Magic themes** – every elemental power has a theme; races tied to an element
  use it (all elementals take their element). The undead entry is unfinished.
- **Boss themes** – a zone's boss dresses its surroundings (below).

This is the design-side version of the dev code's **encounter biomes**
(`encounter_biomes.py`: orcs, trolls, werewolf, vampires, dragons, necromancy,
…), which paint themes over clusters of the story graph – see
[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]].

## Boss themes

| Boss | Effect on the zone | Code encounter theme |
|---|---|---|
| Draconic | lakes boiling or unnaturally warm; dragon-worshipping kobolds nearby; claw marks; burnt spots and blood; no bones (eaten whole); broken trees | dragons |
| Orcish | many outposts and camps (banners, spiked wooden barricades); cut-down trees; dirt paths instead of grass | orcs |
| Trollish | toll camps (skulls on poles, tents with masks); cooking pots, puddles of negative potions | trolls |
| Lich | corrupted land and plants; many undead; dug-out graves; maybe burning corpse piles | necromancy (my match) |
| Mimic | two mirrored layers (below); mimics and tricksters | – |
| Vampiric | more vampires and bats; corpses but no blood; paintings of the vampire lord; red accents; empty coffins | vampires |
| Werewolf | blood and skeletons; medium claw marks on walls and trees; clean poor-quality sleeping bags in corners | werewolf |

Most entries are set dressing for a later population stage. Two add structure:
the Orcish **camps** and Trollish **toll camps** are encounter sites (see
*Camp encounter* in
[[wiki/concepts/trap-puzzle-and-encounter-intent-taxonomy|Trap, puzzle and encounter intent taxonomy]]),
and the Mimic boss changes layer generation.

## Mimic boss: a layer-generation rule

- Generation creates **two layers, one below the other, with identical layout but
  different machines**.
- A secret entrance on one layer can be a trap on the other.
- Both layers are packed with mimics and trickster enemies: mimic chests where the
  treasure would be on the second layer, mimic doors, animated carpets, a mimic
  room encounter instead of a safe room, cinder wisps on torches, symmetrical
  rooms with illusory mirrors, enemies that make illusions, turn invisible or
  teleport.

**For the generator (synthesis):** this is the first concrete statement in any
source that a zone has stacked layers and that a boss can dictate how they
relate. It implies the layout and the lock/key content ("machines") are generated
separately, so one layout can carry two contents. It also means a theme can
change the **graph** (secret edge on one layer = trap node on the other), not
only decoration.

## Gaps

- No theme lists its allowed biomes; the code's `overlay_restrictions` are
  empty too.
- How a boss theme's radius ("in the vicinity") maps to graph distance or layers
  is not defined.
- The doc also wants encounters, traps and puzzles to tell the player what the
  owning group is like (notes in a camp, what a trap tests); theme should
  therefore drive archetype choice, not only art.

---
type: concept
title: "Elemental status interactions as locks and keys"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - lock-and-key
  - statuses
complexity: intermediate
domain: game-design
related:
  - "[[wiki/entities/status-effect-catalogue|Status effect catalogue]]"
  - "[[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/entities/environmental-hazard-and-container-catalogue]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04 – Magic and Statuses Overview]]"
claim_ids:
  - clm-explorio-wet-element-reactions
  - clm-explorio-burning-wet-plant-rules
  - clm-explorio-levitation-vs-flying-terrain
---

# Elemental status interactions as locks and keys

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

GDD 04 defines several statuses by how they react with elements, terrain and
equipment. These rules are what a puzzle can be built from: an element or a
status becomes a **key**, a terrain or a hazard becomes a **lock**. Facts are
from the doc's *Statuses* section; the mapping tables are synthesis.

## Element reaction chains

| Status | Trigger | Result (from the doc) |
|---|---|---|
| Wet | Electric spell | double damage, loses Wet, gains Electrified (temporary slow) |
| Wet | Fire spell | half damage, loses Wet, creates a **steam cloud** |
| Wet | Cold spell | stunned, loses Wet, gains Frozen |
| Wet | time | fades; fades faster near heat sources (torches, campsite, lava) |
| Heat | – | minimal resistance to Cold and Wet |
| Burning | Wet applied | removed |
| Burning | nearby objects/characters | chance to spread fire |
| Burning | scrolls in the backpack | 1–2 scrolls may burn and fire at a random target; a scroll in hand fires more reliably ("quick cast") |
| Burning (DoT) | plant-type effect | only way to refresh its duration ("fuel") |
| Metallic | Electricity | conducts it; metal armour takes more electric damage |
| Magnetic | metal | attracts metal items and metallic creatures |
| Blessed | attack | deals Radiant damage that destroys Undead |
| Cursed | attack | deals Cursed damage that heals Undead and curses others |

A Water-school spell idea, the *water trap*, teleports the target into deep
water when it hits.

## Traversal statuses versus terrain

| Status | Pressure plates | Chasms | Deep water | Net |
|---|---|---|---|---|
| Levitation | not triggered | can cross (owner decision; GDD 04 says cannot); cannot rise to a higher layer | can cross | still levitates; cannot be interrupted by snare or stun |
| Flying | not triggered | can cross | can cross | drops to the ground, stops flying |
| Amphibious / Water breathing | – | – | swims underwater without drowning | – |
| Slippery | – | chance to fall down a chasm | – | – |

Other statuses that touch exploration rather than combat:

- **Lost** – minimap stops updating, player marker hidden; cleared on finding
  the stairs or another player without Lost.
- **Blinded**, **Fear** – map disabled (Blinded also cuts line of sight).
- **Hidden** – standing still in shadow or a bush hides a character.
- **Camouflage / Invisible** – stealth; Camouflage breaks on attack or damage,
  Invisible does not.
- **Sleeping** – line of sight zero; wakes on nearby sound.
- **Smoldering / Fire immunity** – listed as a heading only.

## Mapping to lock archetypes

Synthesis, not in the doc: how these rules could fill archetypes in the
[[wiki/entities/puzzle-archetype-matrix|puzzle archetype matrix]].

| Mechanic from GDD 04 | Lock | Key(s) | Archetype fit |
|---|---|---|---|
| Wet + Cold → Frozen | water/bog gap | cold spell on a wet target or water surface | Monster Assist (ice elemental over bog), Tool assist |
| Wet + Electric → conduction | broken circuit, electric crystal | wet floor, metallic object | Broken Cycle ("throw metal or find wire") |
| Burning spreads, Wet removes | flammable barricade / burning bridge | fire source; water to stop it | Burning bridges, Brogue flammable barricade |
| Heat dries Wet | wet-only puzzle state (temporary) | torch, lava nearby | temporary open mode |
| Levitation skips plates | pressure-plate trap | levitation potion | Death Trap / Tripwire trap bypass (spare key) |
| Levitation or flying crosses chasms | chasm | levitation, flying | Tool assist |
| Magnetic attracts metal | magnetic room | iron skin vs metal gear | Mouse Trap (magnetic sandworm) |
| Hidden / Invisible / Sleeping | guarded area | shadows, bushes, invisibility | Stealth Mission, Infiltration |
| Blessed vs Cursed | undead / cursed area | radiant source | Tool assist ("holy-light scroll through cursed shadows") |
| Lost cleared at stairs | navigation | finding stairs | layer transitions as soft goals |

The typed reactions suggest that the graph's keys need an **element/status
tag**, not only usage and type – see
[[wiki/concepts/key-dimensions|key dimensions]], which has no such field.

## Agreement and contradictions with the vault

- **Agrees**: [[wiki/concepts/environmental-puzzle-variety|Environmental puzzle variety]]
  recommends archetypes × biome mechanics (fire, ice, electricity, magnetism,
  light); GDD 04 supplies fire, cold, electric, metallic/magnetic and
  blessed/cursed rules.
- **Resolved**: GDD 04 says Levitation cannot cross chasms, unlike the matrix's
  Tool assist example and Brogue's levitation key-holder (see
  [[wiki/concepts/brogue-machines-and-population|Brogue machines]]). The owner
  decided levitation **can** cross a chasm but cannot float up to the previous
  layer ([[wiki/questions/owner-decisions|owner decision 2026-11-23]]).
- **Extends**: Brogue's lava moat (levitation, fire immunity or lever) – GDD 04
  lists Fire immunity but does not say whether levitation crosses lava.
- **Open**: environment biomes (frozen wastes, molten caverns, swamp, sunken
  caverns) in [[wiki/concepts/biome-and-zone-layering|biome layering]] are
  natural homes for these reactions, but no biome–element link exists yet.

---
type: entity
title: "Character classes and starting kits"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
entity_type: catalogue
role: "The 15 playable classes, their stats, talent-tree proficiency, starting kit and unlock condition"
first_mentioned: "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05]]"
related:
  - "[[wiki/concepts/player-verbs-and-abilities-as-keys|Player verbs and abilities as keys]]"
  - "[[wiki/concepts/meta-progression-and-unlocks|Meta progression and unlocks]]"
sources:
  - "[[wiki/sources/source-gdd-05-gameplay-and-progression-systems|GDD 05 – Gameplay and Progression Systems]]"
claim_ids:
  - clm-explorio-fifteen-classes
---

# Character classes and starting kits

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Source section: "Unlockables – Classes". Proficiency is the class's multiplier
on the STR / DEX / INT talent trees (see
[[wiki/concepts/meta-progression-and-unlocks|Meta progression and unlocks]]).

## Class table

| Tier | Class | Proficiency | STR | DEX | INT | Starting kit / notes | Unlock |
|---|---|---|---|---|---|---|---|
| Base | Adventurer | default in all | 3 | 3 | 3 | versatile equipment | – |
| Base | Warrior | triple STR | 5 | 2 | 2 | melee equipment | – |
| Base | Mage | triple INT | 2 | 2 | 5 | spellcasting equipment | – |
| Base | Rogue | triple DEX | 2 | 5 | 2 | stealth equipment | – |
| Advanced | Berserker | 2 STR, 1 DEX | 5 | 3 | 0 | no armor, melee weapon | unlocked (how: not stated) |
| Advanced | Musketeer | 2 DEX, 1 STR | 3 | 5 | 0 | handgun | unlocked |
| Advanced | Cleric | 2 INT, 1 STR | 3 | 0 | 5 | bludgeoning weapon, spellcasting equipment | unlocked |
| Advanced | Archer | 2 STR, 1 INT | 5 | 0 | 3 | bow | unlocked |
| Advanced | Alchemist | 2 DEX, 1 INT | 0 | 5 | 3 | random identified potion, stealth equipment | unlocked |
| Advanced | Archeologist | 2 INT, 1 DEX | 0 | 3 | 5 | random identified scroll; equipment line unfinished | unlocked |
| Challenging | Werewolf | default in all | 2 | 2 | 2 | cursed cape: turn into a werewolf (STR 6, DEX 4, INT 0) | achievement "The Beast Within" |
| Challenging | Chosen One | default in all | 4 | 4 | 4 | lots of food and gold, walking-stick weapon | achievement "Heroic Feat" |
| Challenging | Miner | triple STR | 8 | 0 | 0 | no armor or weapons; pickaxe, lantern, a few explosives | achievement "Dwarven Soul" |
| Challenging | Warlock | triple INT | 0 | 0 | 8 | no armor or food; cursed grimoire and spellcasting focus | not stated |
| Challenging | Prisoner | triple DEX | – | – | – | no armor or weapons; stealth ring, many picklocks | achievement "Where Did I Put My Keys?" |

Stat totals: base classes 9, advanced 8, challenging 6–12 (Prisoner has no
stats listed). WIS appears as a fourth base stat in "Base stats" but not in the
class table – an internal inconsistency of the doc.

## Base stats

| Stat | Effects listed in the doc |
|---|---|
| Strength | bonus health, physical resistance, bonus critical strike; items may need minimum STR |
| Dexterity | bonus health, bonus stamina, critical chance, faster weapon swings |
| Intelligence | bonus health, bonus mana, elemental resistance; spells may need a minimum ("strength" in the doc, likely a slip for INT) |
| Wisdom | bonus health, deity favor, chance to refund a spell charge |

## Generator relevance (synthesis)

- **Starting kits are keys.** Miner (pickaxe, lantern, explosives), Prisoner
  (picklocks, stealth ring), Archer and Musketeer (ranged – "activate at a
  distance"), Alchemist and Archeologist (an identified potion or scroll) each
  bring different keys. A dungeon that is solvable for one class may not be for
  another unless every required lock has a key placed in the dungeon or an OR
  alternative.
- **Minimum stat requirements** on items are a soft lock on equipment, not on
  map areas; out of generator scope.
- **Class choice happens before the seed is played** (mission table, temple),
  so the generator could receive the class/loadout as an input if the design
  wants class-aware dungeons. The doc does not say whether seeds are
  class-independent.

## Other progression facts

- No experience in a run, to avoid grinding: the character improves through
  items and potions, permanent and temporary (section "Stats / Character
  Sheet").
- A journal per character and a global one: monsters and their stats become
  viewable once defeated, in any run.
- Inventory: backpack slots (upgradable at a crafting station, tabs for
  specific item kinds), quick slot, toolbar slots (base 3, up to 8 via gear),
  layered gear slots (chainmail / padding under plate, Kingdom Come style).

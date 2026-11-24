---
type: concept
title: "Items as keys"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - lock-and-key
  - items
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/entities/item-catalogue|Item catalogue]]"
  - "[[wiki/entities/cursed-and-unique-items|Cursed and unique items]]"
  - "[[wiki/concepts/bosses-as-locks-and-gates|Bosses as locks and gates]]"
  - "[[wiki/concepts/player-verbs-and-abilities-as-keys]]"
  - "[[wiki/concepts/spellcasting-as-limited-key-resource]]"
sources:
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03 – Items Compedium]]"
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02 – Difficulty Balance and Bosses]]"
claim_ids:
  - clm-explorio-crowbar-lockpick-break-chance
  - clm-explorio-cloaks-cooldown-not-charges
  - clm-explorio-rations-as-lures
  - clm-explorio-layer-descent-items
  - clm-explorio-keys-section-empty
---

# Items as keys

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

The product sheet's examples already use items as keys (potions in *Tool
assist*, gems in *Locked Chest*). GDD 03 is the first catalogue of what those
items could be. This page lists every item the compendium gives a
lock-opening, traversal, lure or clue use, and sorts them by how they are used
up.

## Key-capable items

"Use" is the doc's text, shortened. "Lock it fits" is synthesis.

| Item | Group | Use (doc) | Lock it fits (synthesis) |
|---|---|---|---|
| Crowbar | tool | opens locked doors and chests; chance to break | spare key for physical locks |
| Lockpicks | tool | opens locked doors and chests; chance to break | spare key for physical locks |
| Tools (kit) | tool | disarm traps; craft items without a workstation | trap locks (Tripwire, Death Trap) |
| Hook | tool | whip that attaches to a target; second action pulls target or player there; fishing rod is a kind of hook | gaps, out-of-reach keys |
| Rope | tool | jump to the lower depth without damage | layer transition |
| Torch | tool | light source; can be thrown | darkness, burnable obstacles |
| Flint & Steel | tool | lights fire, torches, candles | fire-triggered mechanisms |
| Candle | tool | light; useful in rituals | ritual locks |
| Net | tool / throwable | slows enemies, grounds flying ones | combat lock helper |
| Caltrops, bear traps | tool | deployable spikes; bear traps are one-use and snare | – |
| Pickaxe, Axe | tool | listed with no description | (assumed: rock / wood obstacles) |
| Bottle | tool | making and carrying potions | carries liquid keys |
| Bread / Fortune cookie | ration | cookie gives clues when eaten | CLUE key |
| Fruit | ration | can be traded with a monkey | NPC/creature trade lock |
| Cheese / Meat | ration | lure rats / lure carnivores | Monster Assist lure |
| Garlic | ration | scent that fends off vampires and bats | passage through a vampire/bat area |
| Levitation, Invisibility, Speed, Resist Fire potions | potion | names only | Tool assist (sheet examples use exactly these) |
| Web Solvent potion | potion | dissolves web traps | explicit key → web lock |
| Freezing, Explosion, Corrosion, Gas, Smoke potions | potion | names only | elemental / destructible obstacles (assumed) |
| Teleportation scroll | scroll | random or to cursor | spare key for gaps and sealed rooms |
| Room Mapping scroll | scroll | maps the whole room | CLUE key |
| Descend scroll | scroll | name only | layer transition |
| Light / Darkness scrolls | scroll | names only | light and stealth locks |
| Last Rites scroll | scroll | name only; GDD 02: puts a vampire down permanently and stuns it | boss lock (permanent kill) |
| Remove Curse scroll | scroll | name only | curse locks |
| Friendly mimic key | unique | opens any door missing exactly one key, costs 1–5 HP | universal spare key for AND locks |
| Flask of endless water | unique | splash or pour into a cauldron any number of times | reusable form of a water key |
| Umbrella shield/token | unique | one option: prevents fall damage when travelling between layers | layer transition |
| Incense Torch | unique | dim light; smoke sleeps enemies for one second | Stealth Mission / Infiltration |
| Pipes of sewers | unique | casts charm; refunds cost on rats or ratfolk | Monster Assist |
| Scrying Orb | unique | found in treasure rooms; identifies one item for free | CLUE key |
| Tarot deck | unique | minor buffs, debuffs and clues | CLUE key |
| Boots enchant | gear | silent walking | Stealth Mission |
| Armour visibility / noise stats | gear | "greatly affect" stealth | Stealth Mission, Infiltration |

Weapons act as soft keys to enemy locks, using GDD 02's resistances: silver
kills werewolves, piercing is the safe way to test basilisk statues, vampires
are immune to arrows, and blessings add radiant damage to undead.

## Reusable vs consumable

The vault's key model has two usage values, reusable and consumable
([[wiki/concepts/key-dimensions|Key dimensions]]). GDD 03 shows at least
five ways an item can be used up:

| Usage pattern | Items in GDD 03 | Fits the binary model? |
|---|---|---|
| Single use | potions, scrolls, rations, bear traps, bombs | yes – consumable |
| Charges | wands (Plague of Locust: "limited use wand"; Plague of the First Born: X uses, may recharge with EXP) | partly – consumable with a count |
| Chance to break | crowbar, lockpicks | **no** – reusable until a random failure |
| Cooldown | cloaks ("cooldown on usage instead of limited charges"): blink, dash, long dash in water, burrow, invisibility, cleanse | reusable, but only temporarily available |
| Worn / permanent | rings (work while worn), runes ("doesn't use up"), boots enchant, gear stats | yes – reusable |
| Cost per use | Friendly mimic key (1–5 HP) | reusable with a price |

The same split repeats in weapon upgrades: an **enchantment** (e.g. fire
damage) is used up in combat, a **rune** is not.

Synthesis: break chance, cooldowns and HP cost could be modelled as a
"durability" or "cost" attribute on reusable keys, or folded into lock
*failable* access. The cloak/potion pairs (invisibility cape vs invisibility
potion; long water dash vs levitation) mean the same lock can take a
reusable or a consumable key.

## Mapping to the archetype matrix

Synthesis. Codes as on
[[wiki/entities/puzzle-archetype-matrix|the matrix page]].

| Archetype (LP) | Key usage in sheet | Items from GDD 03 |
|---|---|---|
| Tool assist (55) | consumable | levitation, invisibility, speed, resist fire potions; teleport scroll; Light scroll vs cursed shadows |
| unnamed R · OR · Temp · Fail · Cl (54) | reusable | the reusable twins of Tool assist: invisibility cloak, dash, burrow; Flask of endless water |
| Locked Chest (1) | consumable | physical keys, orbs with runes, figures of specific material (stubs; reading them as socket keys is an assumption) |
| Burning bridges (13) | consumable | freezing potion, Flask of endless water (sheet: water/ice potions) |
| Monster Assist (78) | reusable | Pipes of sewers (charm); cheese/meat lures are consumable, so they fall in a C · XOR cell instead |
| Stealth Mission (42), Infiltration (89) | R / C | invisibility potion, incense torch, silent boots, low-noise armour |
| Point of no return (57) | consumable | rope, Descend scroll, umbrella – tools for taking or surviving one-way drops |
| any AND lock | – | Friendly mimic key replaces one missing input |

## Gaps and contradictions

- **Keys section is empty**: it holds only a link to a Reddit thread on
  procedurally generated keys. Orbs ("orbs with specific runes") and Figures
  ("made from specific material") are one line each. The physical keys the
  generator places have no item design yet.
- **Extends** [[wiki/concepts/key-dimensions|Key dimensions]]: the binary
  reusable/consumable value cannot express break chance, cooldown or HP cost.
- **Identification**: scrolls must be identified (high Magic Knowledge, using
  them, or books). A key the player cannot recognise makes a lock harder to
  read; failable locks may need a clue or spare key for fairness.
- The Friendly mimic key deliberately breaks AND locks with one missing key;
  the solver would need to know whether it can appear in a run.
- Layer-crossing items (rope, Descend scroll, umbrella) make "drop to the next
  layer" a player choice, which bears on whether layer transitions are locks
  ([[wiki/questions/scope-and-open-questions|scope]]).

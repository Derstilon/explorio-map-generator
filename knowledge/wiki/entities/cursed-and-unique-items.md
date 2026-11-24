---
type: entity
title: "Cursed and unique items"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - items
entity_type: catalogue
role: "Curse sets and unique (rare, conditional) items from GDD 03, incl. the Friendly mimic key"
first_mentioned: "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
related:
  - "[[wiki/concepts/items-as-keys|Items as keys]]"
  - "[[wiki/entities/item-catalogue|Item catalogue]]"
  - "[[wiki/entities/boss-and-elite-catalogue|Boss and elite catalogue]]"
sources:
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03 – Items Compedium]]"
claim_ids:
  - clm-explorio-friendly-mimic-key
---

# Cursed and unique items

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Unique items

"Extremely rare and powerful in conditional scenarios" (reference: Tales of
Maj'Eyal item sets).

| Item | Effect (doc) | Key role (synthesis) |
|---|---|---|
| Friendly mimic key | at a cost of 1–5 HP opens any door you are missing **one** key for; doors with several keyholes open only if exactly one key is missing; the sentence on doors opened by other means (gem slots, puzzle solving) is cut off | universal spare key for AND locks |
| Flask of endless water | splash or pour into a cauldron any number of times | reusable water key |
| Serpent staff | casts wild spells; thrown as a charge attack it becomes a snake that snares; turns back into the item when its target dies; can be killed, losing the item | – |
| Umbrella shield/token | possible effects: shields from statuses but not damage; opening it splashes your negative effects in a cone; levitation when hit or knocked away; prevents fall damage between layers (must be in a hand slot) | layer-transition helper |
| Incense Torch | dimmer torch whose smoke puts enemies to sleep for 1 s; immune until they leave the smoke for a while | stealth helper |
| Staff that casts random spell | name only | – |
| Pipes of sewers | casts charm; refunds the cost on rats or ratfolk | monster helper |
| PokeBall flask | name only | – |
| Booze Elixir | from the Laboratory biome; makes the player drunk but may save staff charges or cut spell mana cost | – |
| Tarot deck | minor buffs, debuffs and clues | clue key |
| Automaton device | automaton weapon such as a mechanical claw or buzzsaw | – |
| Scrying Orb | tool in treasure rooms; identifies one item for free | clue key |

Two unique items name places the generator knows: *Laboratory* is one of the
15 environment biomes in the dev code; *treasure rooms* match the Reward room
of the [[wiki/concepts/five-room-dungeon-biome-template|Five Room template]].

## Curses

Cursed items are marked purple and have both upsides and downsides (references:
Master the Dungeon cursed-item guides).

### Seven deadly sins

| Curse | Upside | Downside |
|---|---|---|
| Lust | fast weapon with lifesteal | first damage from a humanoid charms you for 1 s |
| Pride | resistance to the last damage type received | taking damage slows you |
| Sloth | immune to slow and snare | no movement ability |
| Wrath | kills give slight speed | stamina bar hidden |
| Gluttony | +2 to every stat | must eat a ration every 5 min or it becomes −2 |
| Envy | damage bonus for the last damage type you received | – |
| Greed | shop discount | cannot discard valuable items |

### Four horsemen

| Curse | Upside | Downside |
|---|---|---|
| War | mana bar acts as a shield bar that takes damage first | every enemy always knows where you are |
| Famine | greatly increased stealth | rations heal 1 HP |
| Pestilence | every attack adds a damage-over-time effect | – |
| Death | damaged enemies get a percentage death-mark DoT | an Avatar of Death chases you and respawns |

### Plagues of Egypt

| Curse | Effect |
|---|---|
| Tainted blood | vulnerable to blood stains (heavy acid damage); attacks cause heavy bleeding |
| Croaking mind | constant hallucinations; critters passive to you, hostile to others |
| Vermin presence | killed enemies spawn fast larvae; damaged enemies slowed |
| Pressuring Boils | cursed weapon (steam wand) with infinite charges, bound to you |
| Hellborn Storm | you cause wildfires and lightning; weaker to fire and power damage |
| Locust Appetite | limited-use wand spawning hostile locusts; its kills drop no loot |
| Everlasting Nightfall | permanently blind, but permanent lifesight through fog of war |
| The First Born | reusable crafting rune with X uses, may recharge with EXP; wielder takes more damage; may add curses to the crafted item |

## Relation to the vault

- Curses that change stealth or enemy awareness (Famine, War) change how
  stealth locks (Stealth Mission, Infiltration) play; a generator that places
  such locks cannot assume a fixed player profile (synthesis).
- *Remove Curse* scroll and blessing rituals exist in the item catalogue, so a
  curse can itself be a lock with a consumable key (synthesis).

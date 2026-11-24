---
type: entity
title: "Item catalogue"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - items
entity_type: catalogue
role: "Gear, consumables, tools, containers and scrolls listed in GDD 03, with their stated rules"
first_mentioned: "[[wiki/sources/source-gdd-03-items-compendium|GDD 03]]"
related:
  - "[[wiki/concepts/items-as-keys|Items as keys]]"
  - "[[wiki/entities/cursed-and-unique-items|Cursed and unique items]]"
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
sources:
  - "[[wiki/sources/source-gdd-03-items-compendium|GDD 03 – Items Compedium]]"
claim_ids:
  - clm-explorio-scrolls-need-identification
  - clm-explorio-rune-vs-enchantment-reuse
---

# Item catalogue

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

What GDD 03 lists, grouped as in the doc. Lock-and-key uses are on
[[wiki/concepts/items-as-keys|Items as keys]].

## Gear

### Gear logic

Open design questions, most without answers: why wizards avoid armour
(answered: materials have magic capacity, conductivity or isolation, so melee
weapons cannot carry spells and metal armour lowers spell power or mana
regeneration), whether to carry every weapon type, plate armour and stealth,
parrying hitboxes, crit builds (answered with a list: stabs crit more between
armour plates, heavy slashes scale if not absorbed, stunned/sleeping targets
and backstabs take bonus damage, unarmoured targets take near-certain crits),
armour penetration (goblins vs full plate, dagger vs dragon), ammo shortage.
Inspiration links: NetHack and SLASH'EM item tables, Unexplored 2 sigil
effects (Polish note: no descriptions, so use loosely).

### Worn items

| Slot | Rules |
|---|---|
| Rings | work while worn; max two |
| Cloaks | held or worn, **cooldown instead of charges**; capes give a movement or protection skill with a short cooldown (like a MOBA skill). Examples: cape, alchemy smock, mummy wrapping. Effects: speed boost, short blink, dash and rage, blinding disengage, cursed werewolf-form cape for challenge runs, short invisibility, short reflection, long dash in water, burrow for 1 s, cleanse, absorb next hit, auto-drink health potion on mortal damage |
| Armour | stats: min. strength, piercing / slashing / blunt defence, **toolbar slots** (utility over protection), **visibility** and **noise** (both greatly affect stealth). Head: wizard hat, hood, explorer's fedora, miner's hard hat, iron helm. Torso: dragonscale, scale, chestplate, chain, plate, skin coat, robe. Gloves: gauntlets, gloves. Boots/legs: one enchant grants silent walking |
| Belts / bags | add an inventory tab for specific items with custom stacking; refill toolbar consumables; special toolbar slot for the bag's first item. Examples: quiver, herbalist kit, leatherworking kit, alchemist kit |

### Weapons

- **Range**: short (daggers, shortswords), medium (longswords), long (spears,
  halberds, whips), far (pikes, longer whips – keeps enemies away, useful in
  co-op; risk of attacking through walls).
- **Upgrades**: enchantment (e.g. fire damage, used up in combat), coating
  (poison), blessing (radiant damage vs undead), rune (an enchantment that is
  not used up).
- **Quality**: +1 to +3, +4 = Masterwork.
- **Types**: melee (dagger, sword, cleaver – bleeding, mace – vs armour and
  stun, spear, axe, flail, whip); ranged (bows, crossbows, firearms, slings;
  also blowpipe, musket); throwable (javelins, throwing axes, nets, bombs:
  explosive, fire pot, acid flask, smoke pot, flash pot).
- **Damage types**: base (bludgeoning, slashing, piercing), elemental,
  blessed/positive and cursed/negative. Armour types protect by different
  percentages per base type; some also protect from elements and statuses.
- **Grimoires**: one per elemental school; cover shows mastery; can be blessed
  or cursed by ritual; once mastered, a cross-school spell can be added with a
  sigil of the neighbouring element on the cosmology graph (up to 3 main
  symbols, 1 blessing/curse, up to 5 quasi-elemental symbols).
- **Magic focus**: wands, staves. Shields and "white weapons": headings only.

## Consumables

### Rations

| Item | Use |
|---|---|
| Bread | eat only; regeneration |
| Fortune cookie | gives clues when eaten |
| Fruit | trade with a monkey |
| Cheese | lure rats |
| Meat | lure carnivores |
| Garlic | scent fends off vampires and bats |
| Egg | – |

### Potions

- Schema: name, effect, colour/image, duration, cost (gold), recipe, where
  made (inventory or alchemy station).
- Mixing with alcohol makes a magical drink that works on an enemy who drinks
  it (poison, teleport, acid, paralysis); harmful potions can be poured into a
  healing-potion bottle to trick enemies.
- Types: antidote, healing, invisibility, levitation, life, resist fire (etc.),
  speed, strength, corrosion, drain magic, deafness, explosion, gas, freezing,
  incineration, myst, poison gas, smoke, vampirism, lycanthropy, web solvent.

### Scrolls

- Same schema as potions. Must be **identified**: high Magic Knowledge, by
  using them, or from books. Casting time of a few seconds. Can be activated by
  burning, on the ground or (low chance) in the inventory.
- Offensive: fireball, lightning bolt, ice spike.
- Utility: teleportation (random / to cursor), identify, enchant, last rites
  (Polish note: could also be a cleric class ability), resurrection (co-op
  only), room mapping, protection, recharging, remove curse, descend,
  darkness, light, pain, alarm.
- Summoner (marked "?"): summon a monster, friendly or not.

## Tools and containers

- **Tools**: hook, crowbar and lockpicks (open locked doors and chests, chance
  to break), pickaxe, axe, rope (jump to the lower depth without damage),
  torch (light, throwable), candle (light, rituals), caltrops and bear traps,
  net, paper (copying scrolls), bottle, flint & steel, tool kit (disarm traps,
  craft without a workstation). Reference: NetHack tools.
- **Containers**: quiver, bag, bandolier, toolbelt, bottles/test tubes (a tube
  holds half the effect but stacks four times denser).
- **Keys**: link only. **Orbs**: "orbs with specific runes". **Figures**:
  "made from specific material".

## Runic enchantments

Applied to weapons or armour at a blacksmith; one rune per element; at most
**3 runes** per item; whip- and flail-like weapons can gain multi-attack from
sigils. Runes/sigils are a reforge that gives spell effects, separate from
enchanting.

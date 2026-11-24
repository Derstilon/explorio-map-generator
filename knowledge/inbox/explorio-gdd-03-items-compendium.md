<!-- Google Doc: Explorio | 03 | Items Compedium (1xMIgJoZpMxb4u-tCU1YN2IKjq1pYOF9ItjxH6obSB50) -->

# Curiosities Compendium

*A Journey Through Treasuries of Explorio*

# Table of Contents

[https://www.reddit.com/r/roguelikedev/comments/18sgiiv/how_do_you_get_started_with_designing_stats/?share_id=x2OY6uEqmqVZxJuiagui5&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1](https://www.reddit.com/r/roguelikedev/comments/18sgiiv/how_do_you_get_started_with_designing_stats/?share_id=x2OY6uEqmqVZxJuiagui5&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1) 

# Items

![](explorio-gdd-03-items-compendium-images/image001.png)

## Gear

### Gear logic

| **Wizard armor flavor - Why would wizard not use armor?** | Materials can have magic capacity potencial, magic conductivity, or magic isolation. That can explain why spears can't work as a staves, and fighters focused on a magic primarily don't use metal armor. Mechanically it would reflect in melee weapons not being able to have magical spells attached to them (no magus class), and metal armor has negative effect on spell power or mana regeneration |
|---|---|
| **Toolset accessibility - Should adventurer keep each weapon type on them, or just most useful for current specific theme.** |  |
| **Spellcasting - Why weapons with wooden handle can’t be spell foci but wooden wands and staves can?** |  |
| **What playstyle needs as many toolbar slots as possible regardless of armor loss?** |  |
| **Fully plated thief - How gear influences stealth?** |  |
| **Parring logic - Are there hitboxes for polearm handles? Can you parry only with weapon actions or passively?** |  |
| **Crit build - Should game allow to build around critical strikes or maybe those attacks should serve as a reward for efficient usage of stealth, weapon class, and crowd control?** | - Critical strike could simulate direct strike on the enemy with full potential of the weapon.<br>- Stabs are easier to connect between armored elements directly into a vulnerable body. There could be higher chance for critical strike.<br>- Heavy slashing weapon strikes should deal massive damage if they aren’t absorbed by an armor. Critical strikes in this situations should scale even better.<br>- When enemy is stunned or sleeping it is already easier to hit them, because they are sitting still, but maybe there should be guaranteed bonus damage because player character can strike precisely in the deadlies way possible.<br>- Many lightier armor types have less protected backside. Additionally backstab comes usually by surprise and attacked can’t protect themself with hands. There is incentive to give higher damage to those strikes.<br>- Butt naked enemy against any weapon should take highest possible damage almost every time they get hit. No armor at all should result in huge bonus critical strike chance for attacker. |
| **Armor penetration - Are goblins supposed to pose any threat to adventurer in full plate armor?** | - Armor rating<br>- Armor penetration stat |
| **Poking with a toothpick - Can dagger realistically do any significant damage to an enemy with size of the dragon?** | - Armor rating<br>- Armor penetration stat |
| **Ranged weapons - How armor interacts with ranged weapons? Should ammo shortage be a problem that needs to be overcomed?** | - Armor penetration stat |

https://hot.fandom.com/wiki/Footwear

[Efekty z unexplored 2](https://unexplored-2-the-wayfarers-legacy.fandom.com/wiki/Category:Sigil_Effects) (bez opisu więc można się luźno inspirować)

[https://github.com/SLASHEM-Extended/SLASHEM-Extended/blob/5480e3df776fc71e0bfcc54a59b80d9d73206a74/src/objects.c](https://github.com/SLASHEM-Extended/SLASHEM-Extended/blob/5480e3df776fc71e0bfcc54a59b80d9d73206a74/src/objects.c) (thousands of items to check out)

[https://github.com/Vanilla-NetHack/NetHack-3.4.3/blob/ad815fc0428aa652d64f33e0f407242be7930fb1/src/objects.c](https://github.com/Vanilla-NetHack/NetHack-3.4.3/blob/ad815fc0428aa652d64f33e0f407242be7930fb1/src/objects.c) (Also a lot of items to check out)

### Rings

![](explorio-gdd-03-items-compendium-images/image002.png)

- Rings work as long as they are worn
- Max two equipped

### Cloaks

Items that have to be equipped or held in hand to be used with cooldown on usage instead of limited charges

- Capes give movement or protection skill with relatively short cooldown (smth like regular skill in moba)

#### Charm examples for inspiration

![](explorio-gdd-03-items-compendium-images/image003.png)

![](explorio-gdd-03-items-compendium-images/image004.png)

#### Cloak examples  
![](explorio-gdd-03-items-compendium-images/image005.png)

- Cape
- Alchemy Smock
- Mummy wrapping

Cloak effects

- Temporary speed boost
- Short blink
- Dash and rage
- Disengage with blind harmless attack in front
- Cursed binded beastial form cape for challenge run as Werewolf
- Turn invisible for short duration
- Gain reflective for short duration
- Long dash in water
- Burrow in place for 1s
- Cleanse status effects
- Absorb next damage instance
- Auto drink health potion on mortal damage

### Armor Equipment

![](explorio-gdd-03-items-compendium-images/image006.png)![](explorio-gdd-03-items-compendium-images/image007.png)

- Armour Stats
  - Min. Strength
    - The minimum level of strength required to wear item without penalties
  - [ Piercing Defense ]
    - The level of protection the armor provides against stabs from pointed weapons and other items
  - [ Slashing Defense ]
    - The level of protection the armor provides against slash type attacks, such as a swinging sword
  - [ Blunt Defense ]
    - The level of protection the armor provides against blunt type attacks, such as an attack with a mace
  - [ Toolbar Slots ]
    - Utility over protection
  - [ Visibility ]
    - How visible you are, greatly affects your stealth potential
  - [ Noise ]
    - The amount and level of sound the armor causes with movement, greatly affects your stealth potential

![](explorio-gdd-03-items-compendium-images/image008.png)

![](explorio-gdd-03-items-compendium-images/image009.png)

![](explorio-gdd-03-items-compendium-images/image010.png)

![](explorio-gdd-03-items-compendium-images/image011.png)

![](explorio-gdd-03-items-compendium-images/image012.png)

![](explorio-gdd-03-items-compendium-images/image013.png)

#### Head

Wizard hat / Cornuthaum

Hood

Explorer’s Fedora

Miner’s Hard Hat

Iron Helm

#### Torso

Dragonscale mail

Scale mail

Chestplate

Chain mail

Plate mail

Skin coat

Robe

#### Gloves

Gauntlets

Gloves

#### Boots/Legs

One enchant grants silent walking

### Belts/Bags

Give an additional tab in inventory.

Can store only specific items.

Have custom stacking values.

Refills consumables from toolbar with those from the bag

Creates a special toolbar slot that is a shortcut to the first item from the bag.

![](explorio-gdd-03-items-compendium-images/image014.png)

#### Examples

Quiver

Herbalist Kit

Leatherworking Kit

Alchemist Kit

### Weapons

![](explorio-gdd-03-items-compendium-images/image015.png)

![](explorio-gdd-03-items-compendium-images/image016.png)![](explorio-gdd-03-items-compendium-images/image017.png)

![](explorio-gdd-03-items-compendium-images/image018.png)![](explorio-gdd-03-items-compendium-images/image019.png)

[Weapons | Legendmod Wiki | Fandom](https://legendmod.fandom.com/wiki/Weapons) 

[Melee Weapons | Battle Brothers Wiki](https://battlebrothers.fandom.com/wiki/Melee_Weapons#Two-Handed_Spears)

[Ranged Weapons | Battle Brothers Wiki](https://battlebrothers.fandom.com/wiki/Ranged_Weapons) 

[Category:Runic | Brogue Wiki](https://brogue.fandom.com/wiki/Category:Runic)

- Effects
  - Some weapons can cause [ Bleeding ] or [ Stunned ] Effects
- [ Weapon Range ]
  - [ Short ]
    - Like shortswords and dagger
  - [ Medium ]
    - Longswords and similar
  - [ Long ]
    - Spears, halberds, whips
  - [ Far ]
    - Longer whips?
    - Pikes
    - Not very helpful in combat, can keep range from enemy ( AI shouldn’t try to get into the spike )
    - For Coop can have sense
  - Problems
    - Possible Attacking Through Walls with Far Range weapons

![](explorio-gdd-03-items-compendium-images/image020.png)

- [ Weapon Upgrades ]
  - [ Enchantment ] ( + Fire Damage, etc that is being used up in combat)
  - [ Coating ] ( Poison )
  - [ Blessing ] ( Radiant Damage to Undead )
  - [ Rune ] ( Another Enchantment that doesn't use up )
- [ Weapon Quality ] ( & Rarity )
  - +1
  - +2
  - +3
  - **+4** - [ Masterwork ]
- [ Weapon Type ]
  - Melee
    - Dagger
      - Short and quick
    - Sword ( One / Two - Handed )
    - Cleaver
      - Specialised in [ Bleeding ]
    - Mace ( One / Two - Handed )
      - Specialised in dealing more Damage to armoured opponents and [ Stunning ]
    - Spear
    - Axe ( One / Two - Handed )
    - Flail ( One / Two - Handed )
    - Whip
  - Ranged
    - Bows
    - Crossbows
    - Firearms
    - Slings
  - Throwable
    - Throwing Weapons
      - Javelins, Throwing Axes, etc
    - Nets
    - Bombs
      - Explosive
      - Fire Pot
      - Acid Flask
      - Smoke Pot
      - Flash Pot
  - 
- [ Damage Type ]
  - [ Base ] ( Bludgeoning, Slashing, Piercing )
  - [ Elemental ] ( Fire, etc )
  - [ Blessed/Positive ] / [ Cursed/Negative ]

![](explorio-gdd-03-items-compendium-images/image021.png)

![](explorio-gdd-03-items-compendium-images/image022.png)

![](explorio-gdd-03-items-compendium-images/image023.png)

![](explorio-gdd-03-items-compendium-images/image024.png)

#### White weapons

![](explorio-gdd-03-items-compendium-images/image025.png)

#### Projectile weapons

- Bow
- Blowpipe
- Crossbow
- Sling
- Musket

#### Shields

#### Grimoires

[Scarlet Sand Slate and Increasing the Clearance Level | Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Scarlet_Sand_Slate)

- There is one for each elemental magic school.
- Has a symbol of its magic alignment on its cover.
  - It shows current mastery level

![](explorio-gdd-03-items-compendium-images/image026.png)

- Can be blessed or cursed with a ritual
  - (gains blessing or curse symbol on the cover as well)
- If the school is mastered by a player they can add a cross-school spell by combining the book with sigil of neighboring element on the cosmology graph.
  - (gains symbol of this quasi-element on the cover)
- There could be in the end:
  - 3 symbols or 3 stages of a single symbol for the main element
  - 1 symbol for blessing or curse
  - Up to 5 (maybe less) symbols for 5 different quasi-elemental spells

![](explorio-gdd-03-items-compendium-images/image027.png)

#### Magic Focus

- Wands  
![](explorio-gdd-03-items-compendium-images/image028.png)
- Staves   
[Staves | Unexplored Wiki](https://unexplored.fandom.com/wiki/Staves)  
![](explorio-gdd-03-items-compendium-images/image029.png)

### Weapons vs Armor dynamics

Armor types have different protection percentages from slashing, piercing, bludgeoning damage types

Some armor items can additionally protect from elemental and status effects.

[2d6 Weapon vs Amor Combat Chart | Patreon](https://www.patreon.com/posts/2d6-weapon-vs-81233220)

![](explorio-gdd-03-items-compendium-images/image030.png)![](explorio-gdd-03-items-compendium-images/image031.png)

## Consumables

### Rations

Bread

- Can only be eaten
- Gives regeneration

Fortune cookie

- Gives clues when eaten

Fruit

- Can be traded with monkey

Cheese

- Can be used to lure rats

Meat

- Can be used to lure carnivores

Garlic

- Gives scent that fends off Vampires and bats

Egg

### Potions

### ![](explorio-gdd-03-items-compendium-images/image032.png)  
![](explorio-gdd-03-items-compendium-images/image033.png)![](explorio-gdd-03-items-compendium-images/image034.png)![](explorio-gdd-03-items-compendium-images/image035.png)![](explorio-gdd-03-items-compendium-images/image036.png)

- [ Schematic ]
  - [ Name ]
  - [ Effect ]
  - [ Color ] / [ Image ]
  - [ Duration ]
  - [ Cost ] ( in Gold )
  - [ Recipe ]
  - Where to make ( Inventory or Alchemy Station, etc. )
- Potion can be mixed with alcohol
  - Creates a bottle of alcohol with magical effect
  - When enemy drinks it it activates its effect as normal potion
  - Poison, teleportation, acid, paralysis, etc.
- Other potions can be placed in empty bottle potion of healing to fool enemy into drinking it during combat and activating its harmful effect
- Potion Types
  - Antidote
  - Healing
  - Invisibility
  - Levitation
  - Life
  - Resist Fire / etc.
  - Speed
  - Strength
  - Corrosion
  - Drain Magic
  - Deafness
  - Explosion
  - Gas
  - Freezing
  - Incineration
  - Myst
  - Poison Gas
  - Smoke
  - Vampyrism Potion
  - Lycanthropy Potion
  - Web Solvent (to dissolve web traps)

## Other

### Tools

[Tool - NetHack Wiki](https://nethackwiki.com/wiki/Tool)

- Hook
  - Whip that attaches to the target location
  - Second attack pulls either target or player to this location
  - Fishing rod is a unique type of hook
- Crowbar
  - Opens Locked Doors and Chests
  - Chance to brake
- Lockpicks
  - Opens Locked Doors and Chests
  - Chance to break
- Pickaxe
- Axe
- Rope
  - Allows to jump to the lower depth without taking damage
- Torch
  - Light source
  - Can be thrown
- Candle
  - Light source
  - Useful in rituals
- Caltrops and Bear traps
  - Deployable spikes
  - Bear traps are one use and snare the enemy
- Net
  - Can be thrown to slow down enemies and ground flying ones
- Paper
  - Material for copying the scrolls
- Bottle
  - Useful for making and transporting potions
- Flint & Steel
  - Light up fire/torches/candles
- Tools
  - Disarm traps
  - Craft items on fly (without workstation)

### Containers

- Quiver
- Bag
- Bandolier
- Toolbelt
- Bottles/Test tubes
  - Tubes have half the effect of fluid but can stack 4 times more compact
  - 

### Keys

- [r/proceduralgeneration - Procedurally generated keys](https://www.reddit.com/r/proceduralgeneration/comments/1726sbl/procedurally_generated_keys/)

![](explorio-gdd-03-items-compendium-images/image037.png) klucz do niebieskich drzwi na 3 piętrze

### Orbs

- Orbs with specific runes

### Figures

- Made from specific material (see containers for more info)

### Scrolls

### ![](explorio-gdd-03-items-compendium-images/image038.png)

- [ Schematic ]
  - [ Name ]
  - [ Effect ]
  - [ Color ] / [ Image ]
  - [ Duration ]
  - [ Cost ] ( in Gold )
  - [ Recipe ]
  - Where to make ( Inventory or Alchemy Station, etc. )
- Scrolls need to be identified
  - High [ Magic Knowledge ]
  - By using them
  - Finding book / information about them
- They have [ Casting Time ] of few seconds
- Scrolls can be activated by burning them
  - Either on the ground or in [ Player Inventory ] ( Low chance )
- Scrolls are divided into two groups
  - Offensive / Damage
    - Fireball
    - Lightning Bolt
    - Ice spike
    - 
  - Utility
    - Teleportation ( Random / to cursor )
    - Identify
    - Enchant
    - Last Rites → ( Może też jako class ability dla kleryka )
    - Resurrection ( Resurrect friendly player, does not spawn in single player runs )
    - Room Mapping ( Maps whole room )
    - Protection
    - Recharging
    - Remove Curse
    - Descend
    - Darkness
    - Light
    - Pain
    - Alarm
  - Summoner ?
    - Summon monster ( friendly or not )
    - 

## Runic Enchantments

[Elemental Weapon - TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/ElementalWeapon)

[100 Minor Magical Properties - A d100 Table of Magical Properties Designed To Spruce Up And Diversify Your Magic Items : r/UnearthedArcana](https://www.reddit.com/r/UnearthedArcana/comments/k3c7b8/100_minor_magical_properties_a_d100_table_of/)

![](explorio-gdd-03-items-compendium-images/image039.png)

[Daedric Artifacts (Skyrim) | Elder Scrolls | Fandom](https://elderscrolls.fandom.com/wiki/Daedric_Artifacts_(Skyrim))

Effects applied to the weapon or armor in a blacksmith

There is a rune for each element

Items can take at most 3 runes

Whip-like/flail-like weapons can get multattack from sigils aquireing multiple heads

![](explorio-gdd-03-items-compendium-images/image040.png)

#### Runes / Sigils

- Apart from [ Enchanting ] weapons and armor can be reforged with [ Runes ] to give them spell effects

## Curses

[How to Make Quick Cursed Items for DnD - Master The Dungeon](https://www.masterthedungeon.com/quick-cursed-items/)

[DnD 5e Cursed Items - Master The Dungeon](https://www.masterthedungeon.com/dnd-5e-cursed-items/)

### Description

Cursed Items are marked with purple color

Those items have downsides and upsides of some sort

### Examples (Work in progress)

#### Seven deadly sins curses

[Cursed items based on the seven deadly sins. : r/DMAcademy](https://www.reddit.com/r/DMAcademy/comments/rk4afv/cursed_items_based_on_the_seven_deadly_sins/)

![](explorio-gdd-03-items-compendium-images/image041.png)

- Lust
  - Fast weapon with lifesteal
  - The first time you take damage from humanoid enemy it charms you for 1s
- Pride
  - Bonust to resistance for last damage type you received
  - Taking damage gives slowness
- Sloth
  - Immune to slow and snare
  - Can’t use movement ability
- Wrath
  - Kills give slight movement speed
  - Can’t see stamina bar
- Gluttony
  - +2 to each statistic
  - Has to eat rations once every 5 min or buff turns into -2 to each statistic
- Envy
  - Bonus to damage for last damage type you received yourself
  - 
- Greed
  - Shop discount
  - Cannot discard valuable items

#### Four horsemen of the apocalypse curses

![](explorio-gdd-03-items-compendium-images/image042.png)

- War
  - Mana bar works like a bonus shield health bar that takes damage first
  - Every enemy is constantly aware of your location
- Famine
  - Greatly increased stealth
  - Rations heal for 1 HP
- Pestilence
  - All your attacks apply one additional damage over time effect (poison/acid/frostbite/burning/bleed)
  - 
- Death
  - All enemies you damage with cursed weapon are inflicted with mark of death (percentage dot)
  - You are chased by Avatar of death that will respawn even if you kill it (it is immune to mark of death)

#### Plagues of egypt

- Plague of Tainted blood
  - You are vulnerable to blood steins (they deal massive acid damage)
  - Your attacks inflict massive bleeding damage
- Plague of Croaking mind
  - You are constantly under hallucinations
  - Critters are passive to you and aggressive to everything else
- Plague of Vermin presence
  - Enemies you kill spawn fast aggressive larvas
  - Enemies damaged by you are slowed significantly
- Plague of Pressuring Boils
  - Cursed weapons (steam wand) has infinite charges
  - Cursed weapon is bound to you (can’t be unequipped)
- Plague of Hellborn Storm
  - You are constantly causing wildfires and thunder strikes
  - You are more vulnerable to flame and power damage
- Plague of Locust Appetite
  - Limited use wand that spawns aggressive locust
  - Enemies killed by it drop no loot
- Plague of Everlasting Nightfall
  - You are forever blinded
  - You forever have lifesight (can see presence of lifeforms through fog of war)
- Plague of The First Born
  - Reusable rune/sigil from crafting
  - X amount of uses and possibly can recharge with EXP
  - When enchanted weapon is equipped players takes more damage
  - Has a chance to add additional curses to the item it is crafted with

## Unique Items

[Item set - Tales of Maj'Eyal](https://te4.org/wiki/Item_set)

Unique items that are extremely rare and powerful in conditional scenarios

### Examples

#### Friendly mimic key

At the cost of 1-5 hp will open any door that you are missing one key for. (Doors with multiple keyholes will be opened only if one key is missing)

Doors that open with other means (gem slots, puzzle solving,

#### Flask of endless water

Water that the player can splash or pour into the cauldron any number of times they want.

![](explorio-gdd-03-items-compendium-images/image043.png)

#### Serpent staff

Is used to cast wild spell

Can be thrown as a charge attack to transform into a snake that snares enemies. When its target dies it will transform back into an item. It can be killed, losing the item in a process.

#### Umbrella shield/token

Possible effects

- Shields from status effects but not the damage
- Shield and spear, shielding yourself opens the umbrella and splashes your negative effects in cone in front.
- Gives levitating when player takes damage/is knocked away
- Prevents fall damage from dangerous travel between layers (needs to be equipped in one of the hand slots)

#### Incense Torch

Torch with dimmer light that also creates smoke effect

Smoke puts enemies into sleep for one second. They can’t be affected by it again until they leave the incense smoke for some time

#### Staff that casts random spell

#### Pipes of sewers

Cast charm. Refunds cost if casted on rats or ratfolk

#### PokeBall flask

#### Booze Elixir

Item from Laboratory Biome that makes player drunk but gives a chance to not use charges on staff / reduces mana cost of spells

#### Tarot deck

Minor buffs debuffs and clues

#### Automaton device

Some sort of weapon form automatons, like a mechanical claw or buzzsaw

#### Scrying Orb

Tool inside treasure rooms. Let’s player identify one item for free.

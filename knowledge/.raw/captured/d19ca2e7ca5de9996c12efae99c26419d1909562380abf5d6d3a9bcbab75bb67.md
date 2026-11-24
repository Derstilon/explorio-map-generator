<!-- Google Doc: Explorio | 05 | Gameplay and Progression Systems (1TJ1BpCXJoYnM9CTHYtSXkE7QEH6v__0YlYicvdMIAl4) -->

# Adventurer's Handbook

*A Beginner's Guide to Explorio’s Dungeon Delving and Player Progression*

# Table of Contents

# Game Basics

## Controls

[Padcrafter layouts](https://www.padcrafter.com/?templates=Scheme+A%7CScheme+B&startButton=MAIN+MENU%7CMAIN+MENU&backButton=INVENTORY%7CINVENTORY&leftStickClick=CROUCH+TOGGLE%7CCROUCH+TOGGLE&leftStick=MOVEMENT%7CMOVEMENT&dpadUp=EQUIP+FOCUSED+TO+SECONDARY+HAND%7CFOCUS+TOGGLE&dpadDown=EQUIP+FOCUSED+TO+MAIN+HAND%7CCROUCH+TOGGLE&dpadRight=SWITCH+TOOLBAR+FOCUS%2C+%5BHOLD%2BY%5D+DROP+ITEM+FROM+PRIMARY+HAND%7CDROP+FROM+MAIN+HAND&col=%23242424%2C%23606A6E%2C%23FFFFFF&dpadLeft=SWITCH+TOOLBAR+FOCUS%2C+%5BHOLD%2BY%5D+DROP+ITEM+FROM+SECONDARY+HAND%7CDROP+FROM+SECONDARY+HAND&leftTrigger=MAIN+USE+SECONDARY+HAND%7CACTION+WHEEL+FOR+SECONDARY+HAND&leftBumper=ALTERNATIVE+USE+SECONDARY+HAND%7CMAIN+USE+SECONDARY+HAND%2C+%5BHOLD+X%5D+ALTERNATIVE+USE+SECONDARY+HAND+&rightStick=MOVE+CAMERA%2C+CHANGE+FOCUS+TARGET%7CMOVE+CAMERA%2C+CHOOSE+ACTION+WHEEL%2C+CHANGE+FOCUS+TARGET&rightStickClick=FOCUS+TOGGLE%7CFOCUS+TOGGLE&rightTrigger=MAIN+USE+PRIMARY+HAND%7CACTION+WHEEL+FOR+PRIMARY+HAND&rightBumper=ALTERNATIVE+USE+PRIMARY+HAND%7CMAIN+USE+PRIMARY+HAND%2C+%5BHOLD+X%5D+ALTERNATIVE+USE+PRIMARY+HAND&bButton=CAPE+SKILL+%5BHOLD%5D+SPRINT%7CCAPE+SKILL+%5BHOLD%5D+SPRINT&xButton=QUICK+SLOT%7CQUICK+SLOT&yButton=INTERACT%7CINTERACT&aButton=%5BHOLD%5D+GRAB%7C%5BHOLD%5D+GRAB&plat=%7C%7C0)

| ### Scheme A<br>![](explorio-gdd-05-gameplay-and-progression-systems-images/image001.png) | ### Scheme B<br>![](explorio-gdd-05-gameplay-and-progression-systems-images/image002.png) |
|---|---|

### Keyboard Scheme

| ![](explorio-gdd-05-gameplay-and-progression-systems-images/image003.png) |  |  |  |
|---|---|---|---|
| **WASD** | **Movement** | **X** | **Use Item on self from quickslot** |
| **Tab** | **Inventory** | **LMB/RMB** | **Use Item** |
| **Esc** | **Main Menu** | **SHIFT + LMB/RMB** | **Alternative Use Item** |
| **Ctrl** | **Crouch/Investigate** | **ALT** | **Grab Entity** |
| **Q + LMB/RMB** | **Drop Item** | **Numbers 1 to 8** | **Equip to main hand, + SHIFT to secondary hand** |
| **E** | **Interact** | **Spacebar** | **Cape skill, Hold for sprint** |

# Player Character

## Attributes

### Core Concepts

#### Mind–body dualism

Attributes commonly can be split into two categories: 

1. **Physical** and **Mental**;
1. **Hard** and **Soft**;
1. **Body** and **Mind**;

Those attributes are then used in specific formulas to increase character proficiency in specific tasks.

Some stats like **Perception** or **Luck** could be classified as middle-ground stats.

For balanced gameplay there should be symillar amount of physical and mental stats to make build variety evenly spread.

#### Base and derived stats

| **Pros** | **Cons** |
|---|---|
| **Streamlined character progression -** one stat can function as a main power progression path for many classes without need to create various minor stats progressions that will be useless for most characters | **Less class differentiation -** with less main stats that can be tweaked some classes can end up with symillar capabilities due to identical stats. |
| **Easier to balance -** gear can be designed to buff only specific skills while level up potions increase major attributes giving meaningful boost to power | **Lack of specialization -** without ability to focus on one specific skill during progression prevents consistent builds with specialized ideas in mind. |

#### Attribute requirements

Items that require **minimal stat value** to be equipped or used efficiently. This can also come in the form of **spell slots** and **equip load**

#### Examples of attribute systems

![](explorio-gdd-05-gameplay-and-progression-systems-images/image004.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image005.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image006.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image007.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image008.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image009.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image010.png)

#### Systems that need to be acknowledged

https://youtu.be/azfbnHc8e0Y?si=fmrTKQ1J4KmYVYEL

| **Class identity**  <br>How class is represented in the stat block? | **This can be achieved throgh:**<br>- Wide primary stat list with classed affiliated with pairs of stats<br>- Minimal attribute value for class flavored gear<br>- Starting gear with small bonuses to class specific skills<br>- Challenge classes with low stats but more favoured starting gear |
|---|---|
| **Revelance in numbers**<br>Is mage with high strength more powerful than one with low strength? | **Response concepts:**<br>- All stats buff specific universal mechanic (attack speed, crit value, debuf duration, gods favor, perception)<br>- All stats buff universally needed elements (health, resistance)<br>- Every few stat levels can give choice of bonus with multiple options (talents, passive skills) |
| **Item identification**  <br>How alchemist and wizards use spells? | **Main solutions:**<br>- Item identification attribute (Perception)<br>- Item identification skills associated with attributes  <br>(Wisdom/Inteligence/Faith for scrolls and Dexterity/Agility/Finesse for potions)<br>- Single item identification skill for both classes and different secondary stat affiliation to differentiate wizards from alchemists<br>- (Dex + Wis -> Alchemist and Int + Wis -> Wizard) |
| **Praying to gods**  <br>Should cleric or paladin have more favours from the gods? | **Implementation idea:**<br>- Make 4 stats, one for each resource, and last one for faith system, among others. Adequately add fourth progression tree with faith related unlocks.<br>- Create specific faith related skill that increases bonuses from favorable deeds and decreases penalty from sinful deeds.<br>- Add god alignment as a system that allows to choose before a run a worshiped deity to gain a faithfulness bar displayed during a run.<br>- Cleric should work as a class that relies on boons from the gods to gain more power as they serve their god. |
| **Fear of missing out**  <br>What is a balance between highly customizable build, and expectance that player has efficient build? | **Loose thoughts about issue:**<br>- Don’t overdo Level Up potions, keep stat distribution up to the loot generation and acquired stat boost potions.<br>- Increase health with every stat, as this is universal resource and every build will be glad to have more of it is should increase regardles of what stats are upgraded. |
| **Damage calculation**  <br>How stats effect my dagger, geatclub, wand spells, and scroll spells? | **Different approaches:**<br>- Specific weapons and spells scale with specific stats Eldering-style<br>- Base weapon stats scale with stats, but better weapons and spells  exists and they have stats requirements.<br>- Weapons don’t change, but there are player buffs for specific types of damage, increased crit value, speed of animations, cooldowns and spell charge refund chance<br>- Weapons and spells scale with skills associated with them (swordmanship, melee, archery, elemental mastery, finesse) |
| **How resources scale**<br>Will spellcaster have enough stamina baseline to ignore its stat for the whole run? | **Design ideology:**<br>- No stat increase should feel unimpactful. Even if one attribute is not the primary source of player progression, player still should feel incentive to try to increase if the opportunity arises.<br>- No base stat gameplay should feel tedious, but every first upgrade in each stat should be impactful in one way or another<br>- Examples of benefits for pure Int caster character:<br>  - Higher str opens up more armor options to choose from<br>  - Higher dex gives significant amount of max stamina and increases animation speed slighly making combat gameplay more dynamic and fun<br>  - Higher wis allows for easier identification of potions and scrolls making them more reliable tool to use, as well as gives |
| **Build specialization**<br>When will my sneaky thief get better at stealing? | **Skill scaling systems:**<br>- Skills represent modifier but stats dictate scaling. That way players won’t be able to brute force their way to swordsmanship through strength attribute boosting. +0 Swordmanships will still results in no bonus no matter the str. But +1 skill will be as powerful as related to it primary attribute.<br>- Skills increase every X stat boost. Makes skill progression a rare occurrence but every highly stated character becomes jack-of-all-trades<br>- Dungeon bookshelves contain skill books. Reading them consumes them and grants +1 that skill. Higher than +1 levels have related attribute requirements.<br>- Boosting attribute stat grants point to spend on any related skill.<br>- **Usage based system**: skills like lockpicking, swordsmanship or specific spell schools mastery increase over usage. Base starts change the rate how fast skills are leveled up. |

### Base stats

| #### Strength | #### Dexterity | #### Inteligence | #### Wisdom |
|---|---|---|---|
| - Bonus Health<br>- Increased resistance to Physical Damage<br>- Bonus critical strike<br>- Items can have minimal strength requirement | - Bonus Health<br>- Bonus Stamina<br>- Bonus critical chance<br>- Faster weapon swing animations | - Bonus Health<br>- Bonus Mana<br>- Increased resistance to Elemental Damage<br>- Spells can have minimal strength requirement | - Bonus Health<br>- Bonus deity favor<br>- Increased chance to refund spell charge |

### Main stats

- [ Race ]
  - Racial Bonuses
- [ Class ]
  - Class Abilities
  - Class Bound Equipment
  - Starting Knowledge
  - Extra Items for Start
- [ Health ]  
![](explorio-gdd-05-gameplay-and-progression-systems-images/image011.png)
  - Regeneration
  - Health
  - Dead Player - Can be resurrected with
- [ Armor ]
  - Bonuses from equipped items
- [ Stealth bonuses ]
  - Mix of visibility and noisiness
  - Competes with armor for balance
- [ Toolbar bonus slots ]
  - Gives versatility in action
  - Competes with armor stats
- [ Stats ]
  - Character Attributes
  - Equipped items bonuses
- [ Stamina ]
  - [ Movement Speed ]
    - Modified by Armor, Skills, Enchants, Potions, Scrolls, etc.
  - Sprint
  - Regenerates quickly after it hasn’t been used for a few seconds
  - Melee Attack
  - Shield block
  - Certain active skills
  - Armor weight reduces regeneration
- [ Mana ]
  - Replenished with [ Soul Stone ] ( Skyrim )
    - Enemies soul can be captured to use as magic
- [ Critical Hit ]
  - 1% Base
  - Increased by worn [ Items ], [ Abilities ], [ Effects ] ( Attack from behind, sneaking, reaction, crit enchant / proficiency + x% chance for crit )

## Inventory

- [ Backpack slots ]
- [ Quick slot ]
  - Immediate use of the item on self.
- [ Toolbar slots ]
  - Base 3
  - Different gear items give different amounts of bonus slots (up to 8)
- [ Gear slots ]
  - Slots:
    - Head:  
armor / magic weapon or intelligence buffs / water breathing / int requirements
    - Chest:  
multilayered? / armor classes with stealth or speed drawbacks / strength requirements / specific element or magic type protection
    - Boots:  
armor / stealth or dexterity buffs / elemental debuff immunity (can take fire damage or water damage but won’t catch fire or get soaked)
    - Trinket / Jewelry:  
any base stat buff / possibly advanced stat buff?
    - Cape:  
active or passive skill / movement skill with cooldown / special attack skill with stamina cost / passive skill for stealth or enemy-repellent with additional drawbacks
  - Hand slots:
    - Multiple offhand that can be switched mid combat without windup ?
    - Two-hand grip to reduce strength requirement
    - Switch hands button
    - Change offhand button (empty offhand auto enables two-handed mode)
    - [ Weapon ]
      - Type
      - Damage
        - Slashing
        - Bludgeoning
        - Piercing
        - Elemental
      - Knockback
        - Force
- [ Currency ] / [ Trading ]
  - Gold for most shops and services
  - Some crafting items could be bartered with neutral races?

ability slot

Uskok, dash, blink

peleryna ma to w sobie, multishot jednorazowy

Albo shot plus disengage

Nie musi konkurować z pancerzem o slota

Ale może być jakaś taka wzmocniona peleryna

Co daje też pancerz.i tylko tyle

Może być jakaś co odstrasza jeden konkretny rodzaj przeciwnika

I wtedy masz to kosztem movement ability

przedmioty żeby były generowane losowo

mają ilość punktów do rozdysponowania

i 'losują' z dostępnych ulepszeń

przedmiot ma 13 punktów do wydania,

bycie +1 kosztuje go 10 pkt, poison damage 3 pkt, i tak powstaje

Czyli na skillach aktywnych można by cool down zmniejszyć per punkt przedmiotu

Albo ja odstrasza to małe/ średnie/ duże stwory

Albo jak zwiększa regenerację staminy czy coś

skill point jak z unexplored, jak go dasz na broń to możesz wybrać co upgradujesz, dostajesz +10 per skill point i wybierasz upgrady, albo łączysz z runami / scrollami

Runy pewnie by dawały bardziej complex Buffy albo takie co byłyby op w dużej ilości

Np reach broni bym widział na runie

Air runa czy coś

Klątwy w sumie miałem taką myśl

Że zamiast scrollem ściągać

To mają condition

Znaczy scroll wciąż może być

Albo jakaś inna metoda u npc albo przy ołtarzu

Ale poza tym

To jest konkretne miejsce albo czynność wykonana ileś razy i ona ściąga klątwę

Można By nawet wtedy run zrobić

Albo klasę

Że zaczynasz z całym ekwipunkiem losowo przeklętym

I musisz go oczyścić

Albo jako opcjonalny bonus objective

Albo jako jedyny

Żeby bardziej się mógł dungeon wygenerować pod twoje klątwy

Tylko wtedy te klątwy muszą być takie obusieczne

Że jest to ekwipunek trochę powyżej mocy startowego gearu

Ale ma side efekty bardziej  lub mniej niekorzystne 

Miecz co teleportuje losowo trafionych przeciwników

Ale nie za daleko

Tak żeby efektywnie to po prostu cię otaczali xd

Colorblind xd

Mikstury nie zapamiętujesz xd

### Equipped Items

![](explorio-gdd-05-gameplay-and-progression-systems-images/image012.png)

- ‘Layered’ Slots
  - Player can wear [ Chainmail ] / [ Padder Armor ] under [ Plate Mail ]
  - Similar to Kingdom Come Deliverance
  - [ Head Slot ]
    - Necklace
    - Chainmail
    - Padding
    - Helmet
  - [ Body Slot ]
    - Chainmail
    - Padding
    - Cloth
    - Plate
    - Cape
  - [ Hands Slot ]
    - Rings ( *x2* **?**)
    - Gloves
  - [ Legs ]
    - Leggings
    - Boots
- Possible to make a [ Heavy Armored Knight ] build but at expense of reduced [ Stamina ]
- Slow movement
- Armor items can be enchanted with [ Lightweight / whatever ] to reduce weight
- [ Armor Stats ]
  - [ Armor ] Bonus / Protection it provides
    - Flat Bonus
    - x% ( 30% ) to reduce x ( 6 ) [ Damage Type ]
  - [ Stamina ] & [ Stamina Regeneration ] Reduction
  - Cost in [ Gold ]
  - [ Durability ] ( ***?*** )

![](explorio-gdd-05-gameplay-and-progression-systems-images/image013.png)![](explorio-gdd-05-gameplay-and-progression-systems-images/image014.png)

### Inventory / Backpack

- Inventory → fixed number of slots or upgradable backpack
  - backpack can be found or upgraded at [ Crafting Station ] with materials like [ Leather ], etc

![](explorio-gdd-05-gameplay-and-progression-systems-images/image015.png)

- Backpack upgrades → more slots / więcej zakładek
  - w danych zakładkach mogę być tylko konkretne przedmioty, np. upgrade mikstur

![](explorio-gdd-05-gameplay-and-progression-systems-images/image016.png)

### Stats / Character Sheet

- Upgrade poprzez statystyki
- Nie robić expa żeby unikać grindowania / expienia na potworach
  - ulepszenie przez przedmioty / mikstury
    - permanentne i chwilowe
- 

### Journal/ Discovered Items

Dziennik per postać i ogólny → odkryte potwory i ich statystyki można sprawdzać jak się ich raz pokona ( nie ważne, w którym runie )

![](explorio-gdd-05-gameplay-and-progression-systems-images/image017.png)

## Classes

[Fantasy Character Classes - TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/FantasyCharacterClasses)

### Core Concepts

#### Gameplay focus

Classes provide core gameplay focus that allows their gameplay to feel different from each other with added bonus of allowing players to focus on just one aspect of the game mechanics and still being competitive.

#### Rock–Paper–Scissors

The concept that balance is cycled. There is no class that can’t be countered and every strategy has at least one valid scenario. This takes form of weapon triangles, spell counters, and damage type vulnerabilities. Each class should include in their identity specific mechanic to ensure their viability.

### Resources

| #### Depletable | #### Regenerating |
|---|---|
|  |  |

| #### Karma | #### Pool |
|---|---|
|  |  |

# Hub Town

## Main points of interest

### Mission table

Gives you set of seeded dungeons with barebone description of plot hook

Allows to choose next mission from a list or with custom seed

Mission table is a first thing that needs to be interacted with before player can go into town area. Town ( Social Area )

- If [ Player ] decides to [ Play Online ] he can choose to enter one of [ Public Towns ] ( Or look the same, just different instances )
- This location contains all places where [ Player ] can prepare before going to [ Dungeon ]
  - Buy Items
  - Invite [ Players ] to [ Party ]

![](explorio-gdd-05-gameplay-and-progression-systems-images/image018.png)

### Training grounds

Has some shooting range, 

place where you can equip any weapon type in training variant (wooden)

Training dummy for fight, shield training

PvP area? 

### Marketplace

Contains various merchant NPCs

As the player progresses the game they can unlock different starting classes and items. NPCs also give useful tips based on recent runs the player ended.

Every NPC suggests visiting other merchants (if they have relevant tips)

#### Steel and armor smithy

Allows to swap starting weapons, shields and armor for unlocked ones.

Gives access only to heavy armor

Gives tips:

- What enemies are resistant to specific physical damages (for example skeletons and piercing)
- How counters between white weapons work
  - (ax vs shield, mace vs heavy armor, fast weapons vs spears)
- Informs how armor layering works
- Suggests specific runes for armor enchantment (based on last death or random)
- Suggest specific runes for weapon enchantment (based on resistances from last enemy fought)
- Explains advantages of cursed armor (if encountered one in a last run)

#### Leather and wood crafts

Allows to swap starting armor, trinkets, wands, staves and bags

Gives access only to medium armor

Gives access to throwing sticks as well.

Bags and belts are what modifies stack sizes in the inventory

Gives tip:

- How to manage toolbar effectively
- Explains how quickslot works:
  - Instant use of an item in there.
  - If there is a way the item is used on self
- Suggests what to have in quickslot
  - (healing potion or trinket that gives the player higher chance of survival)
- Explains differences between spell foci
  - Trinkets, wands and staves
  - Differentiated by amount of charges, spell cast time
- Suggests specific runes for armor enchantment (based on last death or random)
- Suggest specific runes for spell foci enchantment (based on the last spell school used)
- Suggests how to manage your health.

#### Fletching and Arms goods

Allows to swap starting bow, crossbow, pistol, and musket

Gives access to explosives

Gives tip:

- What can you activate at a distance with an arrow or throwing weapon
- How gasses, fire, and other natural occurrences spread.
- How stealth works and when you can strike a critical blow.
- Suggests how to manage your stamina.
- Gives tips on how to salvage items (melt metals, burn grimoires, etc) for useful materials
- Explains the advantages of cursed weapons (if encountered one in a last run)

#### Arcane Tailoring and Bookstore

Allows to swap starting Grimoires, sigils, robes, and capes.

Gives tip:

- Explains what are the benefits of cape ability and how to use it
- Suggest how to manage your mana.
- Explains intricacies of spellcasting
  - What you need to cast a spell (Grimoires and focus)
  - How to advance in a spell school
  - How quasi-element spells work
  - How aligned magic works
  - How to craft Grimoires
  - What sort of reactions the last spell school you used can accomplish
- Suggest specific robe enchantment  (based on the last death or random)
- Suggests specific available spell school to try (based on resistances from the last enemy fought)
- Explains the advantages of cursed spell foci (if encountered one in a last run)

#### Alchemist

Allows to swap starting potions and drinks

Gives tip:

- How to identify potions (throw/drink and when it identifies)
- Suggests exchange of health to mana potions (based on mana and health level last run)
- Explains how to craft potions
  - Where to find specific ingredients
- Explains what are the benefits of STR, DEX, and INT potions   
(based on the last class chosen in the run)
- Explains the advantages of negative effect potions (if encountered one in a last run)

#### Temple

Allows you to choose your deity for a run.

Gives tip:

- How karma works
  - Tiers of deeds
  - What following changes in terms of deeds
    - Slight bad deeds are ignored if you aren’t following the deity that dislikes those
    - All good deeds are valued more extensively
    - When you don’t follow any deity you get lower overall karma due to your ignorance towards the divine.
- Explains the alignment of deities, magic, and environment.
- Suggests to do certain things or avoid when following certain gods. (based on how your karma levels changed during your last run)
- Suggests following certain god (based on the number of applicable good deeds from previous run)

## Town Secrets

### Bosses

Every NPC could also be a secret hard PvE boss for some sort of event or achievement, build your loadout with shop items and fight hard boss NPC on the level beyond regular progression.

#### The Forgemaster

They could have many powerful weapons with an absurd amount of sigils on them.

The strategy would be to let them waste stamina and then attack.

#### Supreme Artisan

They could use quirky spells from a distance and agility to keep the player at a distance.

The strategy would be to use ranged weapons.

#### Sovereign Marksman

They could make the fight a bullet hell. Hiding behind the cover and creating many projectiles that multiply due to sigils on the weapons. 

The strategy would be to… learn to dodge.

#### Revered Oracle

They would bombard the player with a huge amount of high-damage spells.

The strategy is to play defensively and wait for the boss to burn their mana.

#### Genius Apothecary

They would be swapping their immunity during a fight and use the same damage type on the player. 

The strategy would be to use current environmental effects to inflict damage that isn’t currently resisted.

#### Divine Bishop

They would constantly receive help from the gods. 

The strategy would be to force him to do bad deeds.

# Meta Progression

## Skill Trees

### Vertical unlocks

| #### Pros | #### Cons |
|---|---|
| - **Sense of growth -** players clearly see the progress they have made<br>- **Pursuit of specialization -** players can choose specific aspects of the game to specialize their build<br>- **Grind difficulty down -** players can overcome hard challenges through boost acquired from vertical progression.<br>- **Learning curve -** keeping complexity of the game to minimum allows player to naturally grasp core gameplay and more complex systems can be explained as their are unlocked. | - **Linear progression -** having predictable paths of progression and optimal paths that can be taken, makes gameplay less interesting<br>- **Discourages experimentation -** there is no incentive to experiment with different playstyles if player already has strong investment in their current build<br>- **First run imbalance -** to keep the challenge fresh difficulty should be scaling up to maxed out progression, making first runs virtually impossible to win. |

#### Examples

- Unlocking universal systems
  - crafting items,
  - enhancing items,
  - boons from the gods,
  - capes and cape skills,
  - gear shop before run,
- Increasing floor level for specific systems
  - more funds for starting gear,
  - bigger inventory size,
  - more items in the shops during a run,
- Influence loot quality or type
  - more stat boost potions of specific type at the cost of the others,
  - double the yield stack of consumable tools in loot,
  - change sigil loot to books of the same element,

### Horizontal unlocks

| #### Pros | #### Cons |
|---|---|
| - **Replayability -** unlocks bring the fresh tools for the player just in time when they might be getting bored of their current<br>- **Adaptability -** horizontal unlocks allow players express their skill through clever usage of newly acquired tools to get the advantage without disrupting the balance too much.<br>- **Focus on the basics -** without many choices and customization players can focus on the core gameplay on the start and have no problem jump over to the more complex options | - **Complexity -** too many unlocks available at the same time can overwhelm the player when they need to choose one of them.<br>- **No immediate payoff -** spending the points for something that isn’t immediately better than current stuff player has will feel bad<br>- **Optimal choice -** it’s inevitable that there will be unlocks that from the minmax type of player are top priority. It’s important to make the path to them as straightforward as possible without any “filler unlocks” on the way. |

#### Examples

- 

### Experience sources

#### Neutral Experience

| **Requirement** | **Scaling** |
|---|---|
| Defeating enemy | Based on enemy difficulty rating |
| Opening chests with loot | Based on rarity of loot |

#### Strength Experience

| Defeating enemy with environmental hazards | Based on enemy difficulty rating and trap type |
|---|---|
| Smashing furniture and other environmental entities | Based on entity type and dropped loot |
| Forging and recycling items | Based on item rarity |

| #### Strength   <br>Experience |  | #### Dexterity   <br>Experience |  | #### Intelligence Experience |  |
|---|---|---|---|---|---|
| Defeating enemy |  |  |  |  |  |

### Bonus experience

### Perks overview:

#### Strength tree:

Exp for killing enemies, smashing stuff and crafting items, crowd control

#### Dexterity tree:

Exp for crit damage, crafting potions, opening locks and puzzles, applying DoT

#### Intelligence tree:

Exp for reading books, crafting scrolls, casting spells and creating reactions between status effects.

## Unlockables

[Unlockables - Tales of Maj'Eyal](https://te4.org/wiki/Unlockables)

### Classes

#### Base:

Adventurer 

- (default proficiency in all trees)
- STR+3, DEX+3, INT+3
- Versatile equipment

Warrior 

- (triple proficiency in strength tree)
- STR+5, DEX+2, INT+2
- Equipment specialized for melee combat

Mage 

- (triple proficiency in intelligence tree)
- STR+2, DEX+2, INT+5
- Equipment specialized for spellcasting

Rogue 

- (triple proficiency in dexterity tree)
- STR+2, DEX+5, INT+2
- Equipment specialized for stealth

#### Advanced (Have to be unlocked):

Berserker 

- (proficiency 2 str 1 dex)
- STR+5, DEX+3, INT+0
- No armor
- Melee combat weapon

Musketeer 

- (proficiency 2 dex 1 str)
- STR+3, DEX+5, INT+0
- Has handgun

Cleric 

- (proficiency 2 int 1 str)
- STR+3, DEX+0, INT+5
- Has bludgeoning weapon
- Equipment specialized for spellcasting

Archer 

- (proficiency 2 str 1 int)
- STR+5, DEX+0, INT+3
- Has bow

Alchemist  

- (proficiency 2 dex 1 int)
- STR+0, DEX+5, INT+3
- Has random identified potion
- Equipment specialized for stealth

Archeologist 

- (proficiency 2 int 1 dex)
- STR+0, DEX+3, INT+5
- Has random identified scroll
- Equipment specialized for

#### Challenging (Have to be unlocked with achievements):

Werewolf 

- (default proficiency in all trees)
- STR+2, DEX+2, INT+2
- Has cursed cape that allows to turn into a werewolf with STR+6, DEX+4, INT+0

Chosen One

- (default proficiency in all trees)
- STR+4, DEX+4, INT+4
- Starts with a lot of food and gold
- Has walking stick weapon

Miner 

- (triple proficiency in strength tree)
- STR+8, DEX+0, INT+0
- Starts without armor or weapons
- Has Pickaxe, lantern and few explosives

Warlock 

- (triple proficiency in intelligence tree)
- STR+0, DEX+0, INT+8
- Starts without armor or food
- Has cursed grimoire and spellcasting focus

Prisoner

- (triple proficiency in dexterity tree)
- Starts without armor or weapons
- Has stealth ring and a lot of picklocks

### Starting Items

### Hubtown cosmetics

### Character cosmetics

#### Character titles

# Achievements

## Overview

### Purpose

The purpose of achievements is to give players a long term goal in a game, encourage them to test different playstyles, and reward them for snooping around for secrets.

### Tailored system

To help players with 100% completion of the game hub provided seeds should be managed in a way that there is guarantee for something achievable in them. 

Maybe a server that crawls seeds generated from current date or static list of seeds shared by all players.

### Neat things

Add a screenshot for whenever the player finishes an achievement and attach it to set achievement in the menu.

### Types

| Objective type |  |  |  |
|---|---|---|---|
| One specific objective | One repeatable objective | Multiple specific objectives | High score objective |
| Reward type |  |  |  |
| No reward:  <br>Usually for joke achievements like dying to smth stupid or really luck dependent achievement. | Horizontal progression reward:  <br>New challenge class or shop item to exchange. | Cosmetic reward:  <br>For a town market, for player character, magic effects | Exp reward:  <br>Bonus EXP for talent trees |

## Examples

Here are examples of achievements group by categories

### Cartographer

Category centered around exploration.

| #### Not Breaking a Sweat | Use the scroll of “Mapping”. |
|---|---|
| #### Thorough Explorer | Visit every layer in a single run. |
| #### Experienced Cartographer | Discover every easy biome.<br>**Reward:** scroll of “Mapping” in a shop. |
| #### Veteran Cartographer | Discover every hard and lower biome. |
| #### Ultimate Cartographer | Discover all biomes. |

### Fighter

Category centered around combat.

| #### Sword Practitioner | Defeat 5 enemies with the same sword. |
|---|---|
| #### Sword Expert | Defeat 20 enemies with the same sword. |
| #### Sword Master | Defeat 100 enemies with the same sword. |
| #### Bullseye | Hit a target with an arrow from at least X tiles away. |
| #### Come prepared | Gather over X amount of any ammo. |

### Scientist

Category centered around identification of items.

| #### Bad luck | Identify a curse. |
|---|---|
| #### Best Lab Assistant | Use the scroll of “Detect magic”. |
| #### Daredevil | Drink an unidentified potion. |
| #### Brute-force deciphering | Use an unidentified scroll. |
| #### Glyphic Hypothesis | Use glyphs on the unidentified item. |
| #### Alchemical Expertise | Identify all types of potions in a single run. |
| #### Literary Expertise | Identify all types of scrolls in a single run. |
| #### Experimental method | Identify Weapon or gear through usage. |
| #### Critical error | Get defeated by polymorphed enemy. |

### Mystic Arts

Category centered around magic and faith

| #### Way of the [X] | Defeat spellcaster using X grimoure.  <br>**Reward:** X grimoure unlocked in arcane shop. |
|---|---|
| #### Pilgrimage of the Faithful | Obtain divine favor from every god |
| #### Divine Punishment | Get punished by every god |
| #### Sorcery Practitioner | Obtain first tier spell |
| #### Sorcery Expert | Obtain second tier spell |
| #### Sorcerer Supreme | Obtain third tier spell |
| #### Ice Age | Keep an enemy frozen for over Xs |
| #### Hands Up! | Disarm 3 enemies with a single magnetic spell |
| #### Lights Out! | Ambush and kill enemy by extinguishing their torch. |
| #### Shock Therapy | Electrocut an Enemy by targeting a body of water with electric attack. |
| #### Tangle Kelp | Drown enemy by rooting it with wild attack under the water. |
| #### Spartan Tactic | Throw enemy of the clif using an air attack. |
| #### Steamy Retreat | Loose enemies by creating steam cloud with a magic attack. |
| #### Wind of Change | Affect an enemy by moving gases with air attack. |
| #### Tank Mode | Have 3 different defensive buffs at the same time. |
| #### Gods favor | Use any blessed spell |
| #### Dark arts | Use any cursed spell |

### Craftsman

Category centered around item crafting, enhancement forging and alchemical brewing

| #### Masterwork | Enhance item with sigils three times (max amount of sigils) |
|---|---|
| #### Cast It Into a Fire! | Destroy cursed item |
| #### Schoolar’s Work | Craft any elemental grimoire |
| #### Master’s Thesis | Upgrade grimoire with a special spell. |
| #### Aligned Assistance | Get your grimoire/sigil cursed or blessed. |
| #### On the house | Mix spiced booze |
| #### Practical use | Burn grimoire and acquire sigil from it. |
| #### Herbalist | Collect 10 different herbs or fugi in a single run<br>**Reward:** common herbs unlocked in alchemy shop |
| #### Monster Hunter | Collect 10 different monster igridients in a single run<br>**Reward:** common monster parts unlocked in a leatherworking shop |
| #### Alchemist | Collect 10 different fluids using bottles in a single run<br>**Reward:** common fluids (oil/slime/spores) unlocked in a alchemy shop |
| #### Granadier | Defeat an enemy by throwing a potion at them. |

### Dungeon Crawler

Category centered around finishing the runs.

| #### Rising Star | Defeat a boss enemy. |
|---|---|
| #### Heroic Feat | Defeat 2 bosses in a single run.<br>**Reward:** Challenge class, the Chosen One. |
| #### The Beast Within | Defeat the second boss of a run while being affected by Lycanthropy.<br>**Reward:** Challenge class, the Werewolf. |
| #### Where Did I Put My Keys? | Defeat the first boss of a run without using a single key.<br>**Reward:** Challenge class, the Prisoner. |
| #### Stuff of Legends | Defeat all 3 bosses in a single run. |
| #### Legendary Warrior | Max out Strength talent tree. |
| #### Legendary Rogue | Max out Dexterity talent tree. |
| #### Legendary Mage | Max out Intelligence talent tree. |

## Biome specific examples

One such category per type of biome 

Dwarfs & Automatons, Desert & Arthropods, Orcs & Trolls & Goblins, Jungle & Dinosaurs, Swamp & Frogfolk, Forest & Werewolves, Castle & Vampires, Graveyard & Undead, Sewers & Ratfolk, Elementals, Demons & Archons, Fungi & Troglodyte, Pirates & Merfolk, Treasures & Dragons

### Dwarven Remains

| #### Ancient Capital | Discover hardmode Dwarven Ruins |
|---|---|
| #### Long Lost Craftsmanship | Craft Mythril Item |
| #### Dwarven Soul | Fully enhance pickaxe, with sigils.<br>**Reward:** Challenge class, the Miner. |
| #### Emergency Shutdown | Disable automaton with energy shock |
| #### Scrap Expert | Defeat every type of Dwarven Automaton |

### Welcome to the Jungle

| #### Primal Heart | Discover hardmode Jungle |
|---|---|
| #### Higher Diplomacy | Trade your stolen item for food with monkey |
| #### Questionable Barter | Exchange golden fruit for useless junk |
| #### Clever Girl | Witness Raptor opening a door |
| #### Extinction Cause | Defeat every type of Dinosaur |

## Loose Ideas

- Achievement for feeding wisp to a frog
- Achievement for killing gunslinger with a gun
- Achievement for finding Gremlin Lair (maybe for each type?)
- Burning Crusade achievement for burning plant creature? All plant creatures?
- Achievements for causing each possible status reaction.
- Achievement for being poisoned for a specific amount of time or percentage of health.
- Achievements for beating each specific easter egg miniboss or gauntlet.
- Achievement for reaching stat threshold (X Str/Dex/Int)
- Achievement for having every piece of gear enhanced.
- Achievement for having both items in hands cursed.
- Achievements for finding every unique curse from curse series (Deadly sins, Horseman of Apocalypse, Plagues)
- Achievement for completing every unique armor set collection (From this puzzle idea with keys as an armor pieces and reward is either blessing from the previous user or fight with his ghost)
- Achievement for finding every unique item (Umbrella, Mimic Key, Serpent staff, Deck of cards)
- Solving X amount of puzzles (in a biome or in general)
- Dying to a trap element
- Getting to the Depth X without being seen
- Give the orc some spiced booze
- Cook forest boar with fire or electrycity. (In forest biome section)
- Deck on fire (something with pirates and fire)
- Burn thorn barricade created by plant enemies

[https://te4.org/wiki/Achievement](https://te4.org/wiki/Achievement)

# Events

[[Random Thursday] Party Time! | Dyson's Dodecahedron](https://dysonlogos.blog/2011/02/17/random-thursday-party-time/)

[Online Event - Tales of Maj'Eyal](https://te4.org/wiki/Online_Event)

Seasonal special dungeon generator with handmade seeds for main questline but also working regular generation.

A few special enemies or buffed out old ones.

Somewhat similar to free DLC’s for Unexplored.

Special seasonal challenge classes.

Seasonal questlines.

Rewards with cosmetics for starting items, magic effects, hub town decorations.

#### Examples

1. Winter Solstice + Xmas
  1. Snow decorations in the hub
  1. Icy dungeon generation with elite snow and ice related buffs
  1. Icy cosmetics
1. Summer Solstice + Tropical vibes
  1. Beach decorations in the hub
  1. Water and fire generation with enemies using beach related buffs
1. Spring Equinox + Easter + Hide and seek
  1. Critter filled hub town
  1. Critter focused generation with boss enemy appearing once in a while.
  1. Easter eggs hidden all over the levels working like a vases with good loot inside
1. Fall Equinox + Halloween + Death
  1. Pumpkin and undead focused event
  1. Spooky decorated hub
1. April Fools' Day
  1. Special dungeon in a questlong where illusion and misdirectionlike themes are more prominent and every item in chests and on monsters is cursed.
1. Boozefest + Carnaval
  1. Booze centered generation
  1. Special whacky challenges do complete in the run
1. Talk Like a Pirate Day
  1. Prate invasion in a run and city hub
  1. Special pirate items and enhancement sygils in a exchange shop before event run
  1. Lots of funds in a exchange shop to allow more tailored builds
1. Steam sale + Arena Tournament
  1. 3 funds breakpoints for totally customizable build
  1. Arena mode with kig of the hill similar to Elden Ring
1. Anniversary
  1. New content with special seed centered around it

<!-- Google Doc: Explorio | 04 | Magic and Statuses Overview (1hm1Kb-XulAxdIdN5GpzwKFfXd9mFeZdzuZFXzwPM0fQ) -->

# Arcane Remedies

*A Healer's Look Into Explorio's Deadly Magic and Conditions*

# Table of Contents

# The point of spellcasting

What game tries to accomplish with this system?

- Add gameplay depth
- Make unique enemies with abilities that are recognizable and achievable to get for player 's arsenal.

What player wants to achieve using spells?

- Limited usage get out of the jail card
- Live out special player fantasy.
- Recognize and exploit enemy weakness.

How to achieve this effect?

- Make magic for monsters and most classes a limited usage tool.
  - Non-magical playstyle player can find and use charged spellcasting foci as a powerful consumables.
  - Characters focused on magic have spell repertoire that can be charged on the staves using mana resource.

How is magic viewed in this world? Are there any forbidden types of magic, and why?  

# Spells

- **Telepathy/Detect life**  
[Telepathy | Brogue Wiki](https://brogue.fandom.com/wiki/Telepathy)
- **Summon/Beckon**  
[Wand of Beckoning | Brogue Wiki](https://brogue.fandom.com/wiki/Wand_of_Beckoning)
- **Domination**  
[Wand of Domination | Brogue Wiki](https://brogue.fandom.com/wiki/Wand_of_Domination)
  - Target treats caster as an ally
- **Blinking**  
[Staff of Blinking | Brogue Wiki](https://brogue.fandom.com/wiki/Staff_of_Blinking)
  - Teleports to the obstacle spell collided with
- **Summoning/Conjuration**  
[Staff of Conjuration | Brogue Wiki](https://brogue.fandom.com/wiki/Staff_of_Conjuration)
  - Creates phantom weapons

## Base Spellschools

[Category:Magical Powers | Superpower Wiki](https://powerlisting.fandom.com/wiki/Category:Magical_Powers)

### Pyromancy

### Water

- water trap spell (teleport you to deep water if you get hit)

### Power

### Air

### Earth

### Wild

## Quasi Elements

### Wood

### Metal

### Magma

# Status Effects

![](explorio-gdd-04-magic-and-statuses-overview-images/image001.png)

![](explorio-gdd-04-magic-and-statuses-overview-images/image002.png)

## Visual indicators

### Constitution indicators

- 3 or 4 colors indicating going below a certain threshold.
- First threshold should be not far of the 100%  
Elite enemy should reach first threshold with around two attacks from the player?  
Players can estimate how tanky the boss or miniboss is by comparing amounts of hits between their encounters.
- Last threshold could be a constant amount of health. Ignoring armor and resistances, all enemies below this threshold should be within the same amount of hit  before they die.

![](explorio-gdd-04-magic-and-statuses-overview-images/image003.png)

- Bloodied: 50% of health  
Mortal: constant small amount of health dropping on the ground

### Status indicators

- Drunk - bubbles around the head  
![](explorio-gdd-04-magic-and-statuses-overview-images/image004.png)

## Damage over time:

### Visualization

Characters have slight tint on them when inflicted with damage over time.

Healing effects can use same types and damage effects

### Types

Types of mechanics for damage over time effects and selected effects that will inherit these mechanics.

#### Percentage

Character takes percentage of their health as damage with minimum of 1 HP per trigger

- Acid (It deals both percentage and constant based damage)
- Death mark

#### Decreasing

Character takes damage based on the amount of triggers the effect has left (15 HP when 15 triggers left, then 14, 13 e.t.c.)

- Poison (Amount of stacks of poison increases also the poison resistance. That way huge amount of poison won’t be overpowered)

#### Increasing

Each time the effect is triggered the next amount is increased by a constant

- Frostbite (The longer you take frostbite damage the bigger it gets)

#### Constant

Effect has constant amount of damage that is inflicted each time it triggers

- Burning (Duration can be refreshed only by adding plant type effect on character to fuel the status)
- Acid (It deals both percentage and constant based damage)

#### Evenly from pool

Effect deals damage based on the amount of triggers left and total amount of damage it should inflict. Increasing the total damage increases amount if deals per trigger

Increasing the amount of triggers decreases the damage per trigger and does not change the amount it will deal in total.

- Bleed (Each refresh adds both damage to the pool and one additional trigger of effect)

#### Ticking bomb

Some sort of effect triggers after some amount of triggers activate

- Madness (Stuns, deals percentage damage and drains mana after all triggers (damage and drain is based on amount of stacks inflicted on character))
- Paralysis (Stun and huge slow after some amount of triggers that is larger than one application)
- Acid (corrodes armor and weapons after some amount of triggers that is larger than one application)

## Statuses

![](explorio-gdd-04-magic-and-statuses-overview-images/image005.png)

Discord, stun and other status effects based on element of damage and type of enemy (organic, mechanic, undead, demon, etc)

[How to Make an RPG: Stats](http://howtomakeanrpg.com/a/how-to-make-an-rpg-stats.html)

[Properties - NetHack Wiki](https://nethackwiki.com/wiki/Property)

[Category:Status | Brogue Wiki](https://brogue.fandom.com/wiki/Category:Status)

[Status Effects | Elden Ring Wiki](https://eldenring.wiki.fextralife.com/Status+Effects)

- **Lost**
  - Minimap won’t update
  - Player marker is disabled
  - Effect get’s cleared when player finds the stairs or another player without this effect
- **Wet**
  - Wet Character:
    - takes double damage from [ Electric ] spells and loses [ Wet ]
      - applies [ Electrified ]
    - takes half damage from [ Fire ] spells and loses [ Wet ]
      - creates Steam cloud
    - gets stunned by [ Cold ] spells and loses [ Wet ]
      - applies  [ Frozen ]
  - Wet status disappears over time.
    - Disappears faster near fire / heat sources ( Torches, campsite, lava, … )
- **Electrified**
  - Temporary slow
- **Madness**
  - Damage
- **Paralysis**
  - Paralyzed Character can’t access items from it’s inventory
  - Gets [ Stunned ] by another application of [ Paralysis ]
  - Gives immunity to paralysis when ends.

![](explorio-gdd-04-magic-and-statuses-overview-images/image006.png)

- **Petrified**
  - Symilar to paralysis
  - Adds armor but stays longer
- Warmed
  - ![](explorio-gdd-04-magic-and-statuses-overview-images/image007.png)
- **Stunned**
  - Stunned Characters cannot attack
- **Confused**  
[Confused | Brogue Wiki](https://brogue.fandom.com/wiki/Confused)
  - Player has inverted controls
    - Another Confusion effects makes Character [ Stunned ]
- **Discorded**  
[Discorded | Brogue Wiki](https://brogue.fandom.com/wiki/Discorded)
  - Treats every creature as enemy
- **Bleed**
  - Bleeding Character:
    - loses X Health over time
    - gets refreshed duration when applied again, damage stays the same unless higher was applied
  - Bleed effect can be removed via [ Bandage ], [ Potion of Healing ], [ Potion of Life ], …
- **Rot**
  - Burns max HP
- **Poison**
  - Poisoned Character:
    - loses X Health over time
    - damage grows when applied again but, duration get’s increased but at most half what was applied before (10s -> +5s -> +2.5s)
  - Can be removed by drinking [ Antidotum / Holy Water ]
  - [ Stamina ] does not regenerate
    - OR Gets drained
  - Natural [ Health ] regeneration is halted
  - Applying regeneration reduces poison stacks instead
- **Heat**
  - Gives minimal resistance to [ Cold ] and [ Wet ] effects
  - 
- **Burning**
  - Characters will take X Damage over time
  - Can be removed by water ( Applying [ Wet ] Status )
  - Burning character has a chance to spread fire to nearby objects / characters
  - If Character does have [ Scrolls ] in their backpack they can be burned and activated with random target ( Max 1 - 2 Scrolls )
    - [ Scrolls ] in [ Hands ] have bigger chance to instantly activate and it can be used to [ Player ] advantage to [ Quick Cast ] [ Spells ] from scrolls
- Freezing
  - Character receives [ Cold Damage ] over time
- **Blinded**
  - [ Line of Sight ] greatly reduced
  - Map temporarily disabled
- **Swallowed**
  - Grappled+Root
  - Hitbox temporarily disabled
- **Frozen**
- **Corroded**
  - Percentage damage
  - Downgrades equipment after another aplication
- **Levitation**
  - Doesn’t trigger [ Pressure Plates ]
  - Cannot levitate over [ Chasms ]
  - Can levitate above [ Deep Water ]
  - Cannot be interrupted with snare or stun
  - If Character gets caught in [ Net ] it can still levitate
- **Flying**
  - Doesn’t trigger [ Pressure Plates ]
  - Can fly over [ Chasms ] and [ Deep Water ]
  - If Character gets caught in [ Net ] it drops to the ground and stops flying
- **Fear**
  - Player has disabled map
  - AI runs away from the source of their fear.
- **Protected/Shielded**  
[Shielded | Brogue Wiki | Fandom](https://brogue.fandom.com/wiki/Shielded)
  - Damage received directly from creature collider interaction is redirected to magical shield
  - Damage from status effects and their interactions is not prevented.
- **Resistant to X**
  - Prevents [ Negative Effects ] related to [ X ]
  - Reduces incoming damage from [ X ]
- **Immune to [ X ]**  
[Immune to Fire | Brogue Wiki](https://brogue.fandom.com/wiki/Immune_to_Fire)
  - Prevents [ Negative Effects ] related to [ X ]
  - Prevents incoming damage from [ X ]
- **Charm**  
[Entrancement | Brogue Wiki](https://brogue.fandom.com/wiki/Staff_of_Entrancement)
  - Character forgets creatures it saw
  - Characters has movement guided by caster commands (look around controls)
- **Sleeping**  
[Sleeping | Brogue Wiki | Fandom](https://brogue.fandom.com/wiki/Sleeping)
  - Sleeping Characters have its [ Line of Sight ] reduced to zero
  - Can wake up if hears sound near them
    - Magical sleep has timer for when the sound can wake up the character
  - Attacks on Sleeping Characters deal more damage ( Critical or flat 2x bonus )
- **Mana infused**  
[http://crawl.chaosforge.org/Magic_contamination](http://crawl.chaosforge.org/Magic_contamination)
  - Bleeds magic fluid
  - Glows
  - Lethal dose is mortal
- **Invisible**  
[Invisible | Brogue Wiki](https://brogue.fandom.com/wiki/Invisible)
  - Character is temporary invisible
  - Attacks don’t break invisibility
  - Taking damage doesn’t brake invisibility
- **Camouflage**
  - Character is temporary invisible if it stays still or moves slowly
  - Attacks break invisibility
  - Taking damage breaks invisibility
- **Reflect**
  - Recasts spells towards the attacker
  - Still will take damage from the spells unless is resistant or immune
- **Hidden**
  - Character staying still in [ Shadow ] or [ Bush ] can become hidden
  - Deals more damage to unsuspecting Characters
- **Drunk**
  - Players have blurry shader on a camera
  - Movement is not straight
  - Ranged attacks have increased spread
  - AI is dumb
- Hallucinating  
[Hallucinating | Brogue Wiki](https://brogue.fandom.com/wiki/Hallucinating)
  - All enemies take weird appearance
  - 
  - Distorted sound, vision
- **Blessed**
  - Protection from [ Negative Effects ]
  - Slowly Heals Character
  - Attack deals [ Radiant ] Damage that destroy [ Undead ]
- **Cursed**
  - ‘Protection’ from [ Positive Effects ]
  - Reduces Character Vision
  - Attack deals [ Cursed ] Damage that heal [ Undead ] and curse other Creatures
- **Slowed**
  - Movement is halved
  - Attack Speed Reduced / Slower Stamina Regeneration ?
  - Effect wears down with time
  - Hasted overwrites Slowed and the other way around
- **Hasted**
  - Faster Movement
  - Faster Attack speed / Faster stamina regeneration
- **Weakened (Str)**
- **Drained (Dex)**
- **Fogged (Int)**
  - Temporarily decrease this stat
- **Empowered (Str)**
- **Swifted (Dex)**
- **Enlightened (Int)**
  - Temporarily increase this stat
- **Enraged**
  - Deals more Damage but also takes more
  - [ Player ] doesn’t see its [ Health ] when raging
- **Slippery**
  - Chance to drop items in hands or fall down the chasm
- **Magnetic**
  - Attracts metal items
  - Attracts metallic creatures
- **Metallic**
  - Conducts [ Electricity ]
  - Characters in Metal Armor takes more damage from [ Electricity ]
- 
- **Snared**
  - Can’t move
- **Illusion**
  - Secret status
  - All effects and stats of this creature are copied from the caster target
  - Magic damage reduces duration of Illusion
- **Saturated (albo coś innego z regeneracją)**
- **Amphibious/Water Breathing**
  - Can swim underwater without drowning
- **Smoldering/Fire immunity**
- **Boost do konkretnej statystyki:**
- **Enlightenment (Int)**
- **Vigorous (Dex?/Str?)**

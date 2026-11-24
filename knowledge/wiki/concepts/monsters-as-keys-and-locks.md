---
type: concept
title: "Monsters as keys and locks"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - bestiary
  - lock-and-key
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/lock-and-key-abstraction|Lock and key abstraction]]"
  - "[[wiki/concepts/key-dimensions|Key dimensions]]"
  - "[[wiki/concepts/lock-dimensions|Lock dimensions]]"
  - "[[wiki/entities/puzzle-archetype-matrix|Puzzle archetype matrix]]"
  - "[[wiki/concepts/brogue-machines-and-population|Brogue machines and population]]"
  - "[[wiki/concepts/enemy-lure-and-deterrence|Enemy lure and deterrence]]"
  - "[[wiki/entities/bestiary-monster-families|Bestiary monster families]]"
  - "[[wiki/concepts/bosses-as-locks-and-gates]]"
sources:
  - "[[wiki/sources/source-gdd-01-bestiary|GDD 01 – Bestiary]]"
claim_ids:
  - clm-explorio-slime-key-carrier
  - clm-explorio-keys-indestructible
  - clm-explorio-centurion-energy-cell
---

# Monsters as keys and locks

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Summary

The bestiary gives many monsters a role in progression, not only in combat.
Grouping them (synthesis) gives five roles a generator could assign to a
story-graph key or lock: **key carrier**, **key-as-monster** (the monster
itself, steered by AI, opens the way), **lock-as-monster** (the monster blocks
or is the obstacle), **disguised mechanism** (a monster pretending to be a
lever, plate, wall or chest), and **alarm / trap trigger**.

## Key carriers

The key exists as an item, but a monster holds it.

| Monster | Mechanic in the doc | Graph reading (synthesis) |
|---|---|---|
| Slimes | can have a `[ Key ]` inside; swallowed items are visible from outside; on split the key may drop, and another slime can swallow it again; if it does not drop it passes to a smaller slime | key placed "in" a guard; the player must finish the whole split tree or grab the key in a window |
| Magma Slime | melts swallowed metal items (steel dagger → steel orb) but "can only destroy basic items (not keys, etc.)" | invariant: **keys are indestructible** by monster effects |
| Corrosive Slime | whatever it swallows "can be corroded" | same invariant applies (the doc only states it for magma) |
| Magnetic Slime | stores metallic items as armor | metallic key carrier |
| Centurion | "powered by steam or energy cell that can be used to open doors"; guards important rooms | guardian whose loot is the key (Brogue's "boss holding the key") |
| Lab golem | always drops the enchanted item that powered it (skillstone, lab battery, lich's phylactery) | miniboss drops a story key |
| Gorgon | drops her head, a special item that works like a wand | boss drop as a reusable tool-key |
| Monkeys, kobold thief, gremlins, golden scarab | steal items (any unattended item, a weapon, one item type, coins); gremlins teleport to a lair; monkeys drop loot if fed | the key can be *taken from* the player: a reverse key carrier |

## Monsters as keys (enemy AI opens the way)

This is the bestiary side of the matrix's **Monster Assist** archetype (R · XOR ·
Temp · Fail · Op) and of the unnamed row 48 ("lure a sandworm to break rocks").

| Monster | What it can do for the player |
|---|---|
| Sand Worm (passive) | digs a **temporary path in a sand wall** |
| Ice Slime | freezes water it touches (makes a crossing over water) |
| Golems | charge at a distant enemy (can break a crystal or wall in its path, per the matrix example; the doc only says "charge") |
| Lured enemy | pulls a lever to escape a deterrent, opening all doors (see [[wiki/concepts/enemy-lure-and-deterrence|lure and deterrence]]) |
| Sleeping rat | moves off a pressure plate when lured with cheese |
| Fairies / wisps | caught in a jar, give light; can be sacrificed on an altar |
| Whitenight Moth | in a bottle, a lantern-like trinket that casts magical darkness |
| Honeypot Ant | juvenile used as a potion sprayer |
| Brass Centipede | turned like an hourglass, slows time in a radius ("can be exploited") |
| Moonstone / moonlight | a creature holding a moonstone emits moonlight that boosts werebeasts |

Captured-critter tools (fairy, moth, ant) are consumable or reusable **tool keys**
that come from monsters, which bridges Monster Assist and Tool assist.

## Monsters as locks and obstacles

| Monster | Lock behaviour in the doc |
|---|---|
| Wall Mimic | mimics a wall in a corridor, a door, or **a bridge over a 1-wide chasm** |
| Room Mimic | miniboss that grows stronger the more you loot the room (matches matrix row 28 Mouse Trap) |
| Chess Golems | gauntlet in a big chessboard area; clues about the chess challenge are placed elsewhere in the dungeon |
| Gorgon | special room with many columns to hide behind; first gaze slows, second turns the player to stone and **ends the run** (failable lock) |
| Rune Golem / Gargoyle | hide as statues until "certain conditions" awaken them |
| Mirror Elemental | special arena with reflective lasers |
| Fellguard (boss) | its own battleground arena |
| Abductor Spider | grabs a player, teleports to its lair, applies [Lost] (hides minimap); the lair has a **secret passage back** to the map |

The Abductor Spider describes a one-way edge into a pocket area plus a secret
return edge, close to production 9's secret edge in the
[[wiki/entities/production-catalogue|production catalogue]] (synthesis).

## Disguised mechanisms

The "mirage arthropods" are desert critters "that take the form of objects":

- **Scorpion lever** – mimics a lever and stings whoever pulls it.
- **Sandstone termites** – look like a fancy pressure plate; eat items and turn
  them into upgrade materials; flee an enchanted item to an adjacent tile.
- **Golden scarab** – looks like coins; infects your coins; when thrown runs to
  the nearest gold vein.
- **Gilded Arachnid** – sets silk tripwires across the layer, sleeps in cocoons
  until one fires, then turns invisible; webs hidden traps it meets.
- **Serpent staff** – a magic focus that can be thrown as a friendly snake.

With chest, item and critter mimics, these make fake levers, plates and chests a
generator could place next to real ones (synthesis: decoys for Cipher-style
"one true statuette among false ones" locks).

## Alarms and trap triggers

- Parrot alerts pirates; Dwarven Drone Fly alarms other constructs; Shades
  share your location with all void creatures on the floor. These fit the
  matrix **Alarm** (52) and **Stealth Mission** (42) archetypes.
- Kobolds lay bear traps and totems; feral orc camps have more traps; gremlins
  can be caught with a shiny item.

## Agreement and conflicts with the vault

- **Agrees**: Monster Assist examples "ice elemental / bog" and "charging enemy
  breaks the crystal" fit Ice Slime and golem charge; row 48 "lure a sandworm to
  break rocks" fits the passive Sand Worm; Mouse Trap's "whole room is a mimic
  that grows with loot taken" is the Room Mimic.
- **Extends**: slimes as key carriers, keys immune to destruction, the
  Centurion's energy cell, Wall Mimic bridges, Abductor Spider pocket areas,
  mirage arthropods as fake mechanisms.
- **Not in the bestiary**: Monster Assist's spider over a chasm, water elemental
  over lava, treant over acid, and the laser automaton; the matrix's "magnetic
  sandworm" (the doc's sand worms are not magnetic; the Magnetic Slime is).

## Open questions

- Are monster key roles typed in the story graph (a key node "carried by
  monster X") or chosen in the content stage? (Already open in
  [[wiki/questions/scope-and-open-questions|scope and open questions]].)
- Is "keys cannot be destroyed" a global rule, or only for the Magma Slime?
- Is a stolen key (monkey, gremlin) a failable lock, or must the thief always be
  recoverable?

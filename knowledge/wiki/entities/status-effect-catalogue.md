---
type: entity
title: "Status effect catalogue"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - gdd
  - statuses
entity_type: catalogue
role: "All status effects listed in GDD 04, grouped, with their gating relevance"
first_mentioned: "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04]]"
related:
  - "[[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions as locks and keys]]"
  - "[[wiki/concepts/damage-over-time-and-health-indicators|Damage over time and health indicators]]"
  - "[[wiki/questions/owner-decisions|Owner decisions]]"
sources:
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04 – Magic and Statuses Overview]]"
claim_ids:
  - clm-explorio-paralysis-immunity
---

# Status effect catalogue

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Every status in GDD 04's *Statuses* list, shortened. The "Gating" column is
synthesis: **T** = traversal/terrain, **S** = stealth/perception, **E** =
element reaction, **–** = combat only. Several statuses link to Brogue wiki
pages as reference; the doc also links NetHack, Elden Ring and
"How to Make an RPG: Stats". It notes that discord, stun and other statuses
should depend on the damage element and enemy type (organic, mechanic, undead,
demon...).

## Elemental and damage statuses

| Status | Effect | Gating |
|---|---|---|
| Wet | reacts with Electric, Fire, Cold; fades, faster near heat | E |
| Electrified | temporary slow | E |
| Heat | minimal resistance to Cold and Wet | E |
| Warmed | heading only (image) | – |
| Burning | DoT; removed by Wet; may spread fire; can set off carried scrolls | E |
| Freezing | cold damage over time | E |
| Frozen | heading only (result of Wet + Cold) | E |
| Bleed | DoT; reapplying refreshes duration, keeps the higher damage; removed by bandage or healing/life potion | – |
| Poison | DoT; damage grows on reapply, added duration halves each time (10 s → +5 s → +2.5 s); antidote / holy water cures; stamina and health regeneration stop; regeneration lowers stacks | – |
| Rot | burns max HP | – |
| Corroded | percentage damage; second application downgrades equipment | – |
| Madness | damage (ticking bomb, see DoT page) | – |
| Mana infused | bleeds magic fluid, glows; a lethal dose kills | S (glow) |

## Control statuses

| Status | Effect | Gating |
|---|---|---|
| Paralysis | no inventory access; reapplying stuns; **immunity to paralysis when it ends** | – |
| Petrified | like paralysis, adds armour, lasts longer | – |
| Stunned | cannot attack | – |
| Confused | inverted controls; a second confusion stuns | – |
| Discorded | treats every creature as an enemy | – |
| Charm | forgets seen creatures; movement guided by the caster | monster-as-key |
| Fear | map disabled; AI flees the source | S |
| Sleeping | sight zero; wakes on nearby sound (magical sleep: after a timer); sleepers take 2× or critical damage | S |
| Swallowed | grappled + rooted, hitbox disabled | – |
| Snared | cannot move | T |
| Slowed / Hasted | halve / raise movement and attack speed; overwrite each other | T (timed locks) |
| Drunk | blurry camera, crooked movement, wider ranged spread, dumb AI | – |
| Hallucinating | enemies look strange, distorted sound and vision | – |
| Enraged | more damage dealt and taken; player cannot see own health | – |
| Illusion | secret; copies the target's effects and stats; magic damage shortens it | – |

## Perception and movement statuses

| Status | Effect | Gating |
|---|---|---|
| Lost | minimap frozen, marker hidden; cleared at stairs or by meeting a non-Lost player | T |
| Blinded | sight greatly reduced, map disabled | S |
| Hidden | still in shadow or bush; bonus damage on unsuspecting targets | S |
| Invisible | not broken by attacking or taking damage | S |
| Camouflage | invisible when still or slow; broken by attacking or damage | S |
| Levitation | skips pressure plates; crosses deep water and chasms (owner decision; GDD 04 says not chasms), cannot rise to a higher layer; immune to snare/stun; keeps levitating in a net | T |
| Flying | skips pressure plates; crosses chasms and deep water; a net grounds it | T |
| Slippery | may drop held items or fall into a chasm | T |
| Amphibious / Water breathing | swims underwater without drowning | T |
| Magnetic | attracts metal items and metallic creatures | E, T |
| Metallic | conducts electricity; metal armour takes more electric damage | E |

## Protective and stat statuses

| Status | Effect |
|---|---|
| Protected / Shielded | damage from creature contact goes to a shield; status damage is not stopped |
| Resistant to X | prevents X's negative effects, reduces X damage |
| Immune to X | prevents X's negative effects and X damage |
| Reflect | recasts spells at the attacker; still takes the damage |
| Blessed | protection from negative effects, slow heal, Radiant damage destroys Undead |
| Cursed | blocks positive effects, less vision, Cursed damage heals Undead |
| Weakened / Drained / Fogged | lower Str / Dex / Int temporarily |
| Empowered / Swifted / Enlightened | raise Str / Dex / Int temporarily |
| Saturated | placeholder ("or something else with regeneration") |
| Smoldering / Fire immunity | heading only |
| Enlightenment (Int), Vigorous (Dex?/Str?) | placeholders under "boost to a specific stat" |

## Status indicators

Only one is specified: Drunk shows bubbles around the head.

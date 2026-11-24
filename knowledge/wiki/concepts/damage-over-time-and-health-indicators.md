---
type: concept
title: "Damage over time and health indicators"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - combat
complexity: intermediate
domain: game-design
related:
  - "[[wiki/entities/status-effect-catalogue|Status effect catalogue]]"
  - "[[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions as locks and keys]]"
sources:
  - "[[wiki/sources/source-gdd-04-magic-and-statuses-overview|GDD 04 – Magic and Statuses Overview]]"
claim_ids:
  - clm-explorio-six-dot-types
---

# Damage over time and health indicators

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Combat-side rules from GDD 04. Low relevance to the story-graph generator,
except as input for difficulty pacing (see the last section).

## DoT mechanic types

GDD 04 defines six reusable mechanics; each status effect inherits one or more.

| Type | Rule | Statuses |
|---|---|---|
| Percentage | % of health per trigger, minimum 1 HP | Acid, Death mark |
| Decreasing | damage = triggers left (15, 14, 13...) | Poison – more stacks also raise poison resistance, so huge stacks don't dominate |
| Increasing | each trigger adds a constant to the next | Frostbite |
| Constant | same damage each trigger | Burning (refreshed only by a plant-type effect), Acid |
| Evenly from pool | total pool split over remaining triggers; more triggers = less per trigger, same total | Bleed – each refresh adds damage to the pool and one trigger |
| Ticking bomb | effect fires after a number of triggers | Madness (stun, % damage, mana drain by stacks), Paralysis (stun + heavy slow), Acid (corrodes armour and weapons) |

Acid combines three types (percentage, constant, ticking bomb). The same types
are meant to serve healing-over-time effects too. Afflicted characters get a
slight colour tint.

## Health threshold indicators

- 3–4 colours mark health thresholds.
- The first threshold sits close to 100 %: an elite enemy should cross it after
  about two player attacks, so players can compare how tanky a boss or miniboss
  is by counting hits.
- The last threshold is a constant amount of health, so every enemy below it
  dies in about the same number of hits (ignoring armour and resistances).
- Named states: **Bloodied** at 50 %, **Mortal** at a small constant amount.

## Relevance to generation

Synthesis: the doc gives no pacing rules, but the thresholds make enemy
toughness readable per encounter. If the generator later scores difficulty per
area (encounter biomes in
[[wiki/concepts/biome-and-zone-layering|biome layering]]), "hits to first
threshold" is a candidate unit. Not discussed anywhere in the vault yet.

---
type: concept
title: "Five Room Dungeon biome template"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - concept
  - gdd
  - structure
  - biomes
complexity: intermediate
domain: game-design
related:
  - "[[wiki/concepts/biome-and-zone-layering|Biomes and zone layering]]"
  - "[[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]]"
  - "[[wiki/concepts/bosses-as-locks-and-gates|Bosses as locks and gates]]"
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
sources:
  - "[[wiki/sources/source-gdd-02-difficulty-balance-and-bosses|GDD 02 – Difficulty Balance and Bosses]]"
claim_ids:
  - clm-explorio-five-room-biome-template
  - clm-explorio-three-act-bosses
---

# Five Room Dungeon biome template

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

GDD 02 proposes two nested story structures: a **three-act run** with one main
boss per act, and the **Five Room Dungeon** as the structure of each biome
("a system that will work well within our biome system"). Both are top-down
templates that the bottom-up lock-and-key grammar does not have yet.

## Three acts and bosses A, B, C

| Act | Boss | Role in the doc |
|---|---|---|
| 1 | Boss A | sets up the run's themes; mildly builds up Boss A; works standalone – the player can end the run here or go deeper for lore |
| 2 | Boss B | bigger place in the plot; moderate build-up; links B and C without revealing much about C |
| 3 | Boss C | a plot twist can shift power to the last boss; the climax builds on mechanics from previous **lairs** and adds a few new ones |
| end | rewards | achievement per final boss type, cosmetics (customisation, town statue), a summary text of the player's deeds, a hub NPC talking about the run |

- The plot should be generated "like a random encounter table with 2–4
  variables". About 20 plot hooks follow (seals to break, manipulated bosses,
  stolen artefacts, rival bosses, cults finishing a summoning).
- Plot hook 4 ("break the seals", two for bosses A and B or three mini-bosses
  holding seals, then Boss C) is the guard-dog lock at run scale.

## The five rooms

In the doc each "room" is a stage of a biome, not a single chamber; the Puzzle
room is "a prime candidate to be multiplied for wider biomes".

| # | Room | Doc content | Gating notes from the doc |
|---|---|---|---|
| 1 | Entrance and Guardian | introduces the biome's themes; mostly easy enemies found across the dungeon, plus one medium enemy to set expectations | – |
| 2 | Puzzle or Challenge | introduces new mechanics tied to the lair's main boss or the biome's flavour; puzzles, parkour, combat with several approaches; camps and bookshelves carry lore | its mechanics "should not prevent travelling further down" |
| 3 | Setback or Red Herring | wildcard in the middle (boss army camp, giant hive) to break monotony; needs urgency (enemy steals something and flees to the neighbouring biome) | great place for a **one-way entrance to a neighbouring biome**; it should "in a meaningful way prevent the player from accessing the next room as long as it is a dead end" |
| 4 | Climactic Battle or Challenge | main camp of the biome's forces: a mini-boss, a gauntlet, or many medium enemies with environmental danger | – |
| 5 | Reward, Revelation and Plot Twist | richer than average but trapped, guarded or puzzled (vein, treasury, hoard, workshop store, junk pit, burial ground); story clues about the act | if it holds an entrance to another biome, mix in Entrance-room elements, e.g. a guardian themed on both biomes |

"5 Room Variations": if the biome's entrance is not at the top, the layout
can be something other than a railroad (no further detail).

## Fit with the story-graph model

Synthesis, not in the doc:

- The five rooms map naturally onto a coarse zone graph: start → challenge
  hub(s) → setback lock → climax lock → reward/exit. Productions could expand
  each stage, and stage 2 can be replicated for wider biomes.
- Stage 2 says new mechanics must not block progress, which reads as locks
  with *optional* access or with a guaranteed spare key.
- Stage 3 introduces **inter-biome edges** (one-way entrances, an enemy
  fleeing into the next biome). The vault scopes one story graph to one zone, so
  these edges need a level above the zone graph
  ([[wiki/questions/scope-and-open-questions|scope]]).
- The "lair" of each act's boss suggests a biome (or group of biomes) per act;
  how acts, biomes, zones and layers nest is not settled in any source.
- The template is linear by default; the doc itself names
  [[wiki/concepts/cyclic-dungeon-generation|cyclic generation]] as the cure for
  backtracking, so the generator may need to add cycles between stages.

## Open questions

- Is one biome = one zone = one story graph, with five stages as its spine?
- Which room hosts the act boss: Climactic Battle (4), or a separate lair after
  Reward (5)?
- What does "prevent access as long as it is a dead end" mean for the Setback
  room's lock type?

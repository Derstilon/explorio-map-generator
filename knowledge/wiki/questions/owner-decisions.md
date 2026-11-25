---
type: question
title: "Owner decisions"
created: 2026-11-23
updated: 2026-11-24
status: developing
tags:
  - question
  - decision
question: "What has the project owner decided about open design points?"
assessment: accepted
risk: normal
related:
  - "[[wiki/questions/inconsistencies-sheet-doc-code|Inconsistencies]]"
  - "[[wiki/questions/scope-and-open-questions|Scope and open questions]]"
claim_ids:
  - clm-explorio-decision-way-back-after-one-way-link
  - clm-explorio-decision-no-short-way-back
  - clm-explorio-decision-graph-first-into-room-map
  - clm-explorio-decision-wfc-both-uses
  - clm-explorio-decision-levitation-crosses-chasms
  - clm-explorio-decision-biome-names-deferred
---

# Owner decisions

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Decisions the project owner gave in conversation. Newest first. Each one
resolves an item in [[wiki/questions/inconsistencies-sheet-doc-code|Inconsistencies]]
or [[wiki/questions/scope-and-open-questions|Scope and open questions]].

## 2026-11-24

### Every one-way link needs a way back

After a one-way link, the player must have a way back. In the later room map
this means every drop needs an accessible path to stairs back up.

- **Accessible:** the way back may cross locks, as long as their keys can be
  reached from where the player lands.
- **Strict mode (config option):** the locks on the way back must not be
  failable. That rules out locks with access FAILABLE and locks opened by a
  consumable key that could be wasted before reaching them.
- Consequence (synthesis): the solver needs reachability from any node with a
  given set of keys, not only from the start, and treats a wastable consumable
  key as a failable path.

### Point of no return and Burning bridges: no short way back

[[wiki/entities/puzzle-archetype-matrix|Point of no return]] (LP 57) and
Burning bridges (LP 13) mean **no short way back**: the collapse removes the
quick route, and the long way back must still exist. Both archetypes stay
usable under the rule above.

## 2026-11-23

### Generation order: story graph first, forced into a room map

The story layout (lock-and-key graph) is generated first and then **forced into
a room map**. Rooms of the map that the story graph does not use get
**standalone content** (content not driven by the story graph).

- Confirms [[wiki/concepts/story-graph-not-dungeon-layout|Story graph, not dungeon layout]].
- Reading of GDD 06: "lock-and-key grammar" under *room purpose classification*
  describes this mapping step, not geometry-first generation
  ([[wiki/concepts/room-shape-types-and-layout-methods|Room shape types and layout methods]]).
- Implies a pipeline step "embed story graph in room map" and a filler step for
  unused rooms (synthesis).

### Wave Function Collapse is used for both

"Wave function collapse is wave function collapse. We can do both." WFC can
generate geometry (as in GDD 06) and turn abstract elements into concrete
content (as in the dev readme). The two uses are not a conflict.

### Levitation crosses chasms, but cannot rise a layer

Levitation **can cross a chasm**, but the player **cannot float upwards** to go
back to the previous layer. A chasm crossed by levitation is passable; a drop
into it is one-way.

- Overrides GDD 04's "Cannot levitate over [ Chasms ]"
  ([[wiki/concepts/elemental-status-interactions-as-locks-and-keys|Elemental status interactions]]).
- Keeps the sheet's Tool assist example "levitation over a chasm" and Brogue's
  levitation challenge valid.
- Consequence (synthesis): layer descents are one-way even with levitation, so a
  chasm can act as a Point-of-no-return lock between layers.

### Biome names: fix later

The mismatch between the code's biome names and the GDD biome lists is known and
will be fixed later. No action now.

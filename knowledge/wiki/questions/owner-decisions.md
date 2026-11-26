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

## 2026-11-26

### Productions follow the sheet where it disagrees with the productions doc

Settled while implementing productions 1–9. The sheet wins on numbering and
attributes; the doc's diagrams still give each production's shape.

- **Numbering:** 4 = Ambush at the Gate, 5 = Tripwire trap (the doc has them the
  other way round).
- **P3 Decision:** the lock is CLOSED, so it is Pick your poison (LP 49). The doc
  draws it OPEN, which would make it Point of no return.
- **Ambush:** XOR with a consumable key, as the sheet's LP 73, in the doc's shape
  (key inside the ambush area, optional access). The doc's NAND with a reusable
  key would be Overloaded Circuit (LP 26).
- **P7a Sequence lock:** the lock is FAILABLE, so it is Sequence Lock (LP 5); the
  doc's failable key and trap area stay.

### Objective productions hide the goal

A production with the `objective` role puts the zone's goal behind its lock. P7a
(Sequence lock) matches the area that holds the goal and moves the goal into its
success area. Its lock is failable, so the same step adds a secret passage from
the area to the success area: failing costs the short way, never the goal. P7b
(Gambit) is a filler: only one of its two areas opens for good, so it cannot hold
the goal; its areas hold an equal reward.

### Fillers can move a secret passage's entrance deeper

Fillers get a variant d (P2d, P3d, P4d, P7cd): it moves the entrance of a secret
passage from the matched area behind the filler's new lock, so a passage such as
P7a's no longer starts in the first area. A passage that has to stay
non-failable (a fallback, like P7a's and P9's) can't move into a failable area;
fillers whose new area is always failable (Tripwire, Tool assist, Gambit) have
no variant d.

### Failable means content the player can lose access to

Access mode FAILABLE marks content the player can lose access to, not only a
lock the player can fail. A new lock therefore inherits FAILABLE from the area,
lock or key it is built on: a chest (P1) inside a failable area is a Sequence
Lock, a gate (P2) there is Endless Tool.

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

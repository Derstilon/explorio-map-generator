---
type: concept
title: "Graph grammar productions"
created: 2026-11-23
updated: 2026-11-26
status: developing
tags:
  - concept
  - graph-grammar
complexity: intermediate
domain: procedural-generation
aliases:
  - Graph rewriting
  - Productions
related:
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
  - "[[wiki/entities/dev-branch-codebase|Dev branch codebase]]"
  - "[[wiki/concepts/cyclic-dungeon-generation|Cyclic dungeon generation]]"
sources:
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
---

# Graph grammar productions

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

## Mechanism in this repo

A production is a **left-hand pattern graph** and a **replacement**. The engine
finds the pattern in the dungeon graph with networkx `GraphMatcher`
subgraph-isomorphism, picks one match with the seeded RNG and rewrites around it.
Pattern nodes and edges match on their attributes (`type`, `mode`, enum values)
and on predicates such as `X != FAILABLE` or `keys < 3`.

- `lock_and_key_productions/utils.py` – `find_isomorphisms`, deduplicating
  matches that cover the same node set and sorting them, so a seed gives the same
  pick.
- `lock_and_key_productions/rules.py` – all productions of the
  [[wiki/entities/production-catalogue|Production catalogue]] (P1a–P9, with
  variants a–d) as `Production` objects: pattern, rewrite, an optional extra
  check on a match, sheet number and role.

## Heritage from master

`master` is a university graph-grammar project: productions P1–P15 that subdivide
a layered, positioned graph (labels `El`, `I`, `E`, `pos`, `layer`) with tests
per production. `dev` keeps the matching approach and the test layout idea but
replaces the domain with lock-and-key nodes. The old tests and examples were not
ported (see [[wiki/questions/implementation-status-and-gaps|gaps]]).

## Control loop

`main.generate` picks a production by weight (default 1 each) for each step and
applies it; a production with no match is dropped for that step, and generation
stops early when none matches. There is no plan by role (objective → key spread →
filler), budget or stopping condition based on graph properties (depth, number of
locks, cycles).

## What a fuller grammar needs

Derived from the productions doc and the inspirations:

- a recipe or plan of productions per zone beyond weights (see
  [[wiki/concepts/cyclic-dungeon-generation|cyclic generation]] for a recipe
  approach);
- validation after each step (solvable, no soft-lock); the tests only check that
  the goal stays reachable when every failable lock stays shut.

---
type: concept
title: "Graph grammar productions"
created: 2026-11-23
updated: 2026-11-23
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
subgraph-isomorphism (nodes matched by `type`, edges by `mode`), picks one match
and rewrites around it.

- `lock_and_key_productions/utils.py` – `find_isomorphisms`, deduplicating
  matches that cover the same node set.
- `decorators.py` – `basic_isomorphism(left, all)` injects the first or all
  matches into `apply`; when nothing matches, `apply` gets `None` and returns
  `False`.
- `l1.py`, `l2.py` – the two implemented rules.

## Heritage from master

`master` is a university graph-grammar project: productions P1–P15 that subdivide
a layered, positioned graph (labels `El`, `I`, `E`, `pos`, `layer`) with tests
per production. `dev` keeps the matching approach and the test layout idea but
replaces the domain with lock-and-key nodes. The old tests and examples were not
ported (see [[wiki/questions/implementation-status-and-gaps|gaps]]).

## Control loop

`main.py` applies `L1` or `L2` at random until 9 applications succeed. There is
no scheduler, weighting, budget or stopping condition based on graph properties
(depth, number of locks, cycles).

## What a fuller grammar needs

Derived from the productions doc and the inspirations:

- attribute conditions on the pattern (`X != FAILABLE`, `keys < 3`) – doc uses
  them, code matches only on node type;
- variants a/b/c per production;
- a recipe or weighted selection of productions per zone (see
  [[wiki/concepts/cyclic-dungeon-generation|cyclic generation]] for a recipe
  approach);
- validation after each step (solvable, no soft-lock).

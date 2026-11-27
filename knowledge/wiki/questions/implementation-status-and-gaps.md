---
type: question
title: "Implementation status and gaps"
created: 2026-11-23
updated: 2026-11-26
status: developing
tags:
  - question
  - status
question: "What of the designed generator exists on dev, and what is missing or broken?"
assessment: provisional
risk: normal
related:
  - "[[wiki/entities/dev-branch-codebase|Dev branch codebase]]"
  - "[[wiki/entities/production-catalogue|Production catalogue]]"
  - "[[wiki/questions/scope-and-open-questions|Scope and open questions]]"
sources:
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
  - "[[wiki/sources/source-dev-productions-doc|Productions doc]]"
claim_ids:
  - clm-explorio-only-p1-implemented
  - clm-explorio-tests-broken
  - clm-explorio-wfc-empty
---

# Implementation status and gaps

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Status of `dev` with the productions change (2026-11-26). Earlier versions of
this page described the proof of concept before epic part 1.

## Exists

- Node model for areas, locks and keys; areas and keys carry an access mode
  like locks.
- Pattern matching by subgraph isomorphism, with attribute predicates
  (`X != FAILABLE`, `keys < 3`).
- All productions of the [[wiki/entities/production-catalogue|Production catalogue]]:
  P1a–P1c, P2a–P2c, P3a–P3c, P4–P6, P7a–P7c, P8, P9, each with a proposed role.
  Extra edge modes `returns` (Tripwire) and `secret` (P7a, P9).
- One seeded RNG for the whole run; same seed and parameters give the same graph.
- Archetype data for all 96 matrix cells (`data/archetypes.yaml`); every lock is
  tagged with its archetype.
- Depth tracking on areas; environment (2-way) and encounter (4 themes) biome
  tagging after generation.
- Interactive web GUI (`gui.py`): seed, weights, stepping, hover, JSON/PNG/SVG
  export (`explorio.story-graph.v1`).
- `pytest` suite and a headless browser check of the GUI.

## Missing

| Gap | Notes |
|---|---|
| Logic-gate semantics and solver | gates are stored and tagged but nothing evaluates them (epic part 5) |
| Generation plan | productions are picked by weight only, not objective → key spread → filler (part 4) |
| Cycles | only the secret passages of P7a and P9; no general cycle production |
| Flavours | no concrete content per archetype; see [[wiki/concepts/flavour-spread-and-archetype-weights|Flavour spread and archetype weights]] (part 6) |
| WFC / machines | `machine_wfc/machines.py` is `{}` |
| Zone layers | no layer concept |
| Biome rules | adjacency, start/end validity unused; biome picks hard-coded |
| GraphML export | optional, not done |

## Broken

- The GitHub workflow runs only for `master` and calls `derivation_a.py` and
  `derivation_b.py`, which no longer exist; `pytest` passes locally.
- `readme.md` still describes WFC, which the code does not have yet.

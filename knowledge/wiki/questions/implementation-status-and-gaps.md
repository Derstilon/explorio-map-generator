---
type: question
title: "Implementation status and gaps"
created: 2026-11-23
updated: 2026-11-23
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

Status from static reading of `dev` at `5b2372f`; the code was not run in this
session (no Python environment with networkx on this machine yet).

## Exists

- Node model for areas, locks and keys with all attribute enums.
- Subgraph-isomorphism matching and two rules (`L1`, `L2`) = production 1 b/c.
- Depth tracking on areas.
- Environment (2-way) and encounter (4 themes) biome tagging.
- Icon-based graph plotting.
- Specification of productions 1–9 in `productions.md`.

## Missing

| Gap | Notes |
|---|---|
| Productions 1a, 2–9 | spec only |
| Attribute conditions in patterns | doc uses `X != FAILABLE`, `keys < 3`; matcher compares only `type` / `mode` |
| Logic-gate semantics | gates are stored but nothing evaluates them |
| Solvability / soft-lock check | none; needed once failable and temporary locks exist |
| Generation control | fixed 9 steps, no recipe, weights or target metrics |
| Archetype assignment | sheet archetypes are not in code |
| WFC / machines | `machine_wfc/machines.py` is `{}` |
| Zone layers | no layer concept |
| Biome rules | adjacency, start/end validity unused; biome picks hard-coded |
| Cycles | graph grows as a tree of locks; no loop or cycle production |
| Export | no serialisation of the story graph for a later layout stage |

## Broken

- `tests/` and `examples/` still import `productions` (P1–P15 from master),
  which dev deleted, so `pytest` fails at import on dev.
- `readme.md` describes WFC and a test run that dev cannot do.
- `L1`/`L2` match selection is fixed by `Random(x=1)`; `Random(x=4)` in
  `main.py` does nothing.

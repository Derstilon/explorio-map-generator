---
type: entity
title: "Dev branch codebase"
created: 2026-11-23
updated: 2026-11-23
status: developing
tags:
  - entity
  - code
entity_type: software
role: "Python PoC of the Explorio story-graph generator (branch dev, commit 5b2372f)"
first_mentioned: "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
related:
  - "[[wiki/concepts/graph-grammar-productions|Graph grammar productions]]"
  - "[[wiki/questions/implementation-status-and-gaps|Implementation status and gaps]]"
sources:
  - "[[wiki/sources/source-dev-code-snapshot|Dev code snapshot]]"
---

# Dev branch codebase

Navigation: [[wiki/maps/explorio-knowledge-map|Knowledge map]]

Python, `networkx` + `matplotlib` (+ Pillow for node icons). Uses `str | None`
syntax, so Python 3.10+. Last dev commit `5b2372f` (2023-10-27); dev work ran
2023-10-21 → 2023-10-27 on top of the studies project.

## Branches

- `master` – studies project: layered-mesh graph grammar P1–P15, tests, CI.
- `dev` – repurposed for Explorio (9 commits: "Rewrite for new usage" … "Add
  more productions").

## Modules

| Path | Role |
|---|---|
| `main.py` | seed graph, 9 random `L1`/`L2` applications, env + encounter biomes, 4 plots |
| `nodes/node.py` | label counters, label printing |
| `nodes/lock.py` | `Lock`, enums `LogicGate`, `LockState`, `OpenMode`, `Importance` |
| `nodes/key.py` | `Key`, enums `Reusability`, `KeyType` |
| `nodes/access.py` | `Access` (area) nodes, depth propagation; commented-out complexity propagation |
| `lock_and_key_productions/` | `L1`, `L2`, isomorphism decorators, `productions.md` spec |
| `biome_injections/` | environment and encounter biome tagging |
| `machine_wfc/machines.py` | empty `machines = {}` – placeholder for WFC / Brogue-style machines |
| `visualization.py` | `draw_dungeon` (icons, kamada-kawai layout); legacy `draw_graph` |
| `custom_icons.py` | standalone matplotlib demo of image nodes |
| `img/` | key, lock, treasure icons, `Explorio.drawio.png` example graph |
| `tests/`, `examples/` | unchanged from master; import the removed `productions` package |

## Graph model

- Node types `access`, `lock`, `key`; labels `A#`, `L#`, `K#` from graph-level
  counters.
- Edge modes `access` (area makes something reachable, weight .5) and `unlocks`
  (key → lock, weight .85).
- Access nodes store `depth` (distance in locks from start) and `keys`/`locks`
  sets.

## Notable behaviour

- `Random(x=4)` in `main.py` creates and discards an instance; it seeds nothing.
- `L1`/`L2` pick a match with `Random(x=1).randint(...)`, a new generator seeded
  with 1 on every call, so the choice depends only on the number of matches.
- `main.py`'s choice between `L1` and `L2` is unseeded, so runs differ.
- The `Explorio.drawio.png` example shows a target shape with an OR lock (L5 with
  keys K5a/K5b) and a treasure goal, richer than what the code produces.

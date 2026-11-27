"""Graph-grammar productions P1–P9 from productions.md.

Each production matches a small pattern (an area, an area with a lock, an area
with a key, ...) with find_isomorphisms, picks one match with the seeded RNG
and rewrites the graph around it. Variants a/b/c insert the new lock in front
of a new empty area (a), an existing closed lock (b) or an existing key (c).
Fillers also have a variant d: it moves the entrance of a secret passage from
the matched area behind the new lock. A fallback passage (one that keeps the
goal or failable content reachable) never moves into a failable area or behind
a failable lock, so P7cd moves only passages that are not fallbacks.

Numbering follows the product sheet (owner decision 2026-11-26): 4 = Ambush,
5 = Tripwire. Where the sheet and productions.md disagree on a lock's
attributes, the sheet wins: P3's lock is CLOSED, Ambush is XOR with a
consumable key, and P7a's lock is FAILABLE.

Roles (proposal for part 4 of the epic): `spread` moves keys and locks deeper,
`filler` adds an obstacle, `objective` puts the zone's goal behind a main-objective
lock, `meta` tunes an existing lock.

Access: a production's new lock, areas and keys take the access mode (`X` in
productions.md) of the matched area, lock or key unless the production sets
one. Edge modes besides `access` and `unlocks`: `returns` (a one-way way back
from a trap area to the area before it) and `secret` (a secret passage, added
in both directions).
"""
from dataclasses import dataclass
from random import Random
from typing import Callable

import networkx as nx

from nodes import Access, AccessMode, Key, KeyType, Lock, LockState, LogicGate, OpenMode, Reusability
from .utils import find_isomorphisms

R, C = Reusability.REUSABLE, Reusability.CONSUMABLE
PRIMARY, SPARE, CLUE = KeyType.PRIMARY, KeyType.SPARE, KeyType.CLUE
REQUIRED, OPTIONAL, FAILABLE = AccessMode.REQUIRED, AccessMode.OPTIONAL, AccessMode.FAILABLE


def not_failable(access_mode) -> bool:
    return access_mode != FAILABLE


def area_pattern(**conditions) -> nx.DiGraph:
    pattern = nx.DiGraph()
    pattern.add_node('area', type='access', **conditions)
    return pattern


def area_with(kind: str, **conditions) -> nx.DiGraph:
    """An area and a lock or key standing in it."""
    pattern = area_pattern()
    pattern.add_node(kind, type=kind, **conditions)
    pattern.add_edge('area', kind, mode='access')
    return pattern


ANY_AREA = area_pattern()
SAFE_AREA = area_pattern(access_mode=not_failable)
AREA_CLOSED_LOCK = area_with('lock', lock_state=LockState.CLOSED)
AREA_KEY = area_with('key')


def goal_area_pattern() -> nx.DiGraph:
    """An area that is not failable and holds the zone's goal key."""
    pattern = area_pattern(access_mode=not_failable)
    pattern.add_node('goal', type='key', role='goal')
    pattern.add_edge('area', 'goal', mode='access')
    return pattern


SAFE_AREA_WITH_GOAL = goal_area_pattern()


def add_lock(G, area, gate, state, mode, access) -> str:
    lock = Lock.add_new_lock(G, gate, state, mode, access)
    Access.add_access_edge(G, area, lock)
    return lock


def move(G, node, from_area, to_area):
    """Move a lock or key from one area to another."""
    G.remove_edge(from_area, node)
    G.nodes[from_area]['locks' if G.nodes[node]['type'] == 'lock' else 'keys'].discard(node)
    Access.add_access_edge(G, to_area, node)


def lock_in_front(G, match, gate, state, mode):
    """Shared start of the a/b/c/d variants: a new lock in the matched area, opening to a new area.

    Variant b moves the matched lock, c the matched key and d the matched secret-passage entrance behind the
    new lock. Returns (area, new lock, new area, access mode X).
    """
    area = match['area']
    moved = match.get('lock') or match.get('key')
    access = G.nodes[moved or area]['access_mode']
    lock = add_lock(G, area, gate, state, mode, access)
    behind = Access.add_new_access(G, lock, access)
    if moved:
        move(G, moved, area, behind)
    move_passage_entrance(G, match, behind)
    return area, lock, behind, access


def chest(G, rng, match):
    area, lock, _, _ = lock_in_front(G, match, LogicGate.AND, LockState.CLOSED, OpenMode.PERMANENT)
    Key.add_new_key(G, C, PRIMARY, lock, area)


def gate(G, rng, match):
    area, lock, behind, _ = lock_in_front(G, match, LogicGate.OR, LockState.CLOSED, OpenMode.TEMPORARY)
    Key.add_new_key(G, R, PRIMARY, lock, area)
    Key.add_new_key(G, R, PRIMARY, lock, behind)


def decision(G, rng, match):
    area, lock, _, _ = lock_in_front(G, match, LogicGate.OR, LockState.CLOSED, OpenMode.PERMANENT)
    Key.add_new_key(G, R, CLUE, lock, area)
    Key.add_new_key(G, C, PRIMARY, lock, area)


def ambush(G, rng, match):
    area = match['area']
    lock = add_lock(G, area, LogicGate.XOR, LockState.OPEN, OpenMode.TEMPORARY, OPTIONAL)
    behind = Access.add_new_access(G, lock, OPTIONAL)
    Key.add_new_key(G, C, PRIMARY, lock, behind, OPTIONAL)
    move_passage_entrance(G, match, behind)


def tripwire(G, rng, match):
    area = match['area']
    lock = add_lock(G, area, LogicGate.NOR, LockState.OPEN, OpenMode.PERMANENT, FAILABLE)
    behind = Access.add_new_access(G, lock, FAILABLE)
    Key.add_new_key(G, C, PRIMARY, lock, area, OPTIONAL)
    G.add_edge(behind, area, mode='returns')


def tool_assist(G, rng, match):
    area = match['area']
    lock = add_lock(G, area, LogicGate.OR, LockState.CLOSED, OpenMode.TEMPORARY, FAILABLE)
    Access.add_new_access(G, lock, FAILABLE)
    Key.add_new_key(G, C, PRIMARY, lock, area, OPTIONAL)
    Key.add_new_key(G, C, SPARE, lock, area, OPTIONAL)


def two_outcomes(G, area, lock, first: tuple, second: tuple) -> list:
    """Open two areas behind one lock: each tuple is (outcome, access mode). Returns the new areas in that order."""
    areas = []
    for outcome, access in (first, second):
        behind = Access.add_new_access(G, lock, access)
        G.nodes[behind]['outcome'] = outcome
        areas.append(behind)
    return areas


def add_secret_passage(G, area, behind, fallback=True):
    """A secret passage both ways; the edge from `area` is its entrance.

    A fallback passage keeps the goal or failable content reachable, so it never moves into a failable area or
    behind a failable lock.
    """
    G.add_edge(area, behind, mode='secret', entrance=True, fallback=fallback)
    G.add_edge(behind, area, mode='secret', entrance=False, fallback=fallback)


def move_passage_entrance(G, match, new_area):
    """Variant d: rebind the matched passage's entrance from the matched area to new_area."""
    if 'exit' not in match:
        return
    area, exit_area = match['area'], match['exit']
    forward, backward = dict(G.edges[area, exit_area]), dict(G.edges[exit_area, area])
    G.remove_edges_from([(area, exit_area), (exit_area, area)])
    G.add_edge(new_area, exit_area, **forward)
    G.add_edge(exit_area, new_area, **backward)


def passage_pattern(**area_conditions) -> nx.DiGraph:
    """An area holding the entrance of a secret passage, and the area the passage leads to."""
    pattern = area_pattern(**area_conditions)
    pattern.add_node('exit', type='access')
    pattern.add_edge('area', 'exit', mode='secret', entrance=True)
    pattern.add_edge('exit', 'area', mode='secret')
    return pattern


def passage_may_enter(target_access):
    """`requires` for variant d: a fallback passage may not move behind a failable lock.

    target_access(G, match) gives the access mode of the lock the production adds; the area behind a failable lock
    is content the player can lose, whatever its own access mode.
    """
    def check(G, match):
        return not (G.edges[match['area'], match['exit']]['fallback'] and target_access(G, match) == FAILABLE)
    return check


AREA_PASSAGE = passage_pattern()
SAFE_AREA_PASSAGE = passage_pattern(access_mode=not_failable)


def sequence_lock(G, rng, match):
    """Objective: the goal moves into the success area. The lock is failable, so a secret passage leads from the
    area to the success area at once: failing costs the short way, never the goal."""
    area = match['area']
    access = G.nodes[area]['access_mode']
    lock = add_lock(G, area, LogicGate.AND, LockState.CLOSED, OpenMode.PERMANENT, FAILABLE)
    Key.add_new_key(G, C, PRIMARY, lock, area, FAILABLE)
    _, success = two_outcomes(G, area, lock, ('trap', FAILABLE), ('success', access))
    move(G, match['goal'], area, success)
    add_secret_passage(G, area, success)


def gambit(G, rng, match):
    area = match['area']
    access = G.nodes[area]['access_mode']
    lock = add_lock(G, area, LogicGate.OR, LockState.CLOSED, OpenMode.PERMANENT, FAILABLE)
    Key.add_new_key(G, C, PRIMARY, lock, area, access)
    Key.add_new_key(G, C, SPARE, lock, area, access)
    two_outcomes(G, area, lock, ('choice', FAILABLE), ('choice', FAILABLE))


def death_trap(G, rng, match):
    area = match['area']
    lock = add_lock(G, area, LogicGate.NOR, LockState.CLOSED, OpenMode.TEMPORARY, FAILABLE)
    Key.add_new_key(G, R, CLUE, lock, area, OPTIONAL)
    success, _ = two_outcomes(G, area, lock, ('success', OPTIONAL), ('killzone', FAILABLE))
    move_passage_entrance(G, match, success)


def primary_key(G, lock):
    return next((key for key in sorted(G.nodes[lock]['keys']) if G.nodes[key]['key_type'] == PRIMARY), None)


def complexity_increase(G, rng, match):
    lock = match['lock']
    data = G.nodes[lock]
    key_type = PRIMARY if data['logic_gate'] == LogicGate.AND and data['lock_state'] == LockState.CLOSED else CLUE
    usage = G.nodes[primary_key(G, lock)]['reusability']
    Key.add_new_key(G, usage, key_type, lock, match['area'], data['access_mode'])


def failure_decrease(G, rng, match):
    add_secret_passage(G, match['area'], match['behind'])


def complexity_pattern() -> nx.DiGraph:
    """A lock in an area that can take one more key: fewer than 3 keys, not failable, not OR, not the entrance.

    The production also needs the lock to have a primary key (has_primary_key).
    """
    def fits(data):
        return (len(data['keys']) < 3 and data['access_mode'] != FAILABLE and data['logic_gate'] != LogicGate.OR
                and data['open_mode'] != OpenMode.DUNGEON)
    return area_with('lock', where=fits)


def failable_passage_pattern() -> nx.DiGraph:
    """An area, a failable closed lock in it, and a failable area behind the lock, with no secret passage yet.

    The production also needs the area behind to have no passage at all (no_passage_behind), so a passage whose
    entrance was moved deeper is not added again.
    """
    pattern = area_with('lock', access_mode=FAILABLE, lock_state=LockState.CLOSED)
    pattern.add_node('behind', type='access', access_mode=FAILABLE)
    pattern.add_edge('lock', 'behind', mode='access')
    return pattern


@dataclass(frozen=True)
class Production:
    name: str
    number: str
    role: str
    description: str
    pattern: nx.DiGraph
    build: Callable
    requires: Callable = None  # extra check on a match, beyond the pattern

    def apply(self, G: nx.DiGraph, rng: Random) -> bool:
        """Apply to one match picked with rng; False when nothing matches."""
        matches = [{pattern_node: node for node, pattern_node in match.items()}
                   for match in find_isomorphisms(G, self.pattern)]
        if self.requires:
            matches = [match for match in matches if self.requires(G, match)]
        if not matches:
            return False
        self.build(G, rng, rng.choice(matches))
        return True


def no_passage_behind(G, match):
    return not any(G.edges[match['behind'], other]['mode'] == 'secret' for other in G.successors(match['behind']))


def area_access(G, match):
    return G.nodes[match['area']]['access_mode']


def has_primary_key(G, match):
    return primary_key(G, match['lock']) is not None


PRODUCTION_LIST = [
    Production('P1a', '1', 'spread', 'Chest: a new AND lock with one consumable key, in front of a new empty area',
               ANY_AREA, chest),
    Production('P1b', '1', 'spread', 'Chest: put an existing closed lock behind a new AND lock',
               AREA_CLOSED_LOCK, chest),
    Production('P1c', '1', 'spread', 'Chest: put an existing key behind a new AND lock', AREA_KEY, chest),
    Production('P2a', '2', 'filler', 'Gate: a temporary OR lock with a reusable key on each side, new area',
               ANY_AREA, gate),
    Production('P2b', '2', 'filler', 'Gate: put an existing closed lock behind a gate', AREA_CLOSED_LOCK, gate),
    Production('P2c', '2', 'filler', 'Gate: put an existing key behind a gate', AREA_KEY, gate),
    Production('P2d', '2', 'filler', 'Gate: move a secret passage entrance behind a gate', AREA_PASSAGE, gate,
               passage_may_enter(area_access)),
    Production('P3a', '3', 'filler', 'Decision: an OR lock with a consumable key and a reusable clue, new area',
               ANY_AREA, decision),
    Production('P3b', '3', 'filler', 'Decision: put an existing closed lock behind a decision',
               AREA_CLOSED_LOCK, decision),
    Production('P3c', '3', 'filler', 'Decision: put an existing key behind a decision', AREA_KEY, decision),
    Production('P3d', '3', 'filler', 'Decision: move a secret passage entrance behind a decision', AREA_PASSAGE,
               decision, passage_may_enter(area_access)),
    Production('P4', '4', 'filler', 'Ambush: an open XOR lock whose consumable key lies in the ambush area',
               SAFE_AREA, ambush),
    Production('P4d', '4', 'filler', 'Ambush: move a secret passage entrance into a new ambush area',
               SAFE_AREA_PASSAGE, ambush, passage_may_enter(lambda G, match: OPTIONAL)),
    Production('P5', '5', 'filler', 'Tripwire: an open failable NOR lock with an optional trigger; the trapped area '
               'returns to the area before it', SAFE_AREA, tripwire),
    Production('P6', '6', 'filler', 'Tool assist: a failable temporary OR lock with a consumable key and a spare',
               SAFE_AREA, tool_assist),
    Production('P7a', '7a', 'objective', 'Sequence lock: the goal moves behind a failable lock, into its success '
               'area, with a secret passage there; a trap area opens on failure', SAFE_AREA_WITH_GOAL, sequence_lock),
    Production('P7b', '7b', 'filler', 'Gambit: one failable lock in front of two equal areas, one opens for good',
               SAFE_AREA, gambit),
    Production('P7c', '7c', 'filler', 'Death trap: a failable NOR lock with a clue, in front of a success area and '
               'a killzone', SAFE_AREA, death_trap),
    Production('P7cd', '7c', 'filler', 'Death trap: move a secret passage entrance (not a fallback) into a new '
               'success area', SAFE_AREA_PASSAGE, death_trap, passage_may_enter(lambda G, match: FAILABLE)),
    Production('P8', '8', 'meta', 'Complexity increase: one more key on a non-failable, non-OR lock with fewer than '
               '3 keys', complexity_pattern(), complexity_increase, has_primary_key),
    Production('P9', '9', 'meta', 'Failure decrease: a secret passage around a failable lock',
               failable_passage_pattern(), failure_decrease, no_passage_behind),
]
PRODUCTIONS = {production.name: production for production in PRODUCTION_LIST}

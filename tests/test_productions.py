from random import Random

import pytest

from main import base_graph
from lock_and_key_productions import L1, L2
from nodes import AccessMode, KeyType, LockState, LogicGate, OpenMode, Reusability


def counts(G):
    types = [data['type'] for _, data in G.nodes(data=True)]
    return {kind: types.count(kind) for kind in ('access', 'lock', 'key')}


def access_parent(G, node):
    return [p for p in G.predecessors(node) if G.edges[p, node]['mode'] == 'access']


def assert_new_lock_shape(G, before):
    after = counts(G)
    assert after == {kind: before[kind] + 1 for kind in before}
    new_lock = f"L{G.graph['lock_count'] - 1}"
    new_key = f"K{G.graph['key_count'] - 1}"
    new_access = f"A{G.graph['access_count'] - 1}"
    lock = G.nodes[new_lock]
    assert (lock['logic_gate'], lock['lock_state'], lock['open_mode'], lock['access_mode']) == (
        LogicGate.AND, LockState.CLOSED, OpenMode.PERMANENT, AccessMode.REQUIRED)
    assert lock['keys'] == {new_key}
    key = G.nodes[new_key]
    assert (key['reusability'], key['key_type'], key['lock']) == (Reusability.CONSUMABLE, KeyType.PRIMARY, new_lock)
    assert G.edges[new_key, new_lock]['mode'] == 'unlocks'
    assert G.edges[new_lock, new_access]['mode'] == 'access'
    return new_lock, new_key, new_access


def test_l1_puts_a_key_behind_a_new_lock():
    G = base_graph()
    before = counts(G)
    assert L1.apply(G, Random(0))
    new_lock, new_key, new_access = assert_new_lock_shape(G, before)
    # K0 (the only key before) now sits behind the new lock, in the new access node
    assert access_parent(G, 'K0') == [new_access]
    assert 'K0' not in G.nodes['A0']['keys'] and 'K0' in G.nodes[new_access]['keys']
    # the new lock and its key are reachable from A0
    assert access_parent(G, new_lock) == ['A0'] and access_parent(G, new_key) == ['A0']
    assert G.nodes[new_access]['depth'] == G.nodes['A0']['depth'] + 1


def test_l2_puts_a_lock_behind_a_new_lock():
    G = base_graph()
    assert L1.apply(G, Random(0))  # gives A0 a lock to match
    before = counts(G)
    moved_lock = 'L1'
    assert L2.apply(G, Random(0))
    new_lock, new_key, new_access = assert_new_lock_shape(G, before)
    assert access_parent(G, moved_lock) == [new_access]
    assert moved_lock not in G.nodes['A0']['locks'] and moved_lock in G.nodes[new_access]['locks']
    # everything behind the moved lock is one level deeper now
    behind = [n for n in G.successors(moved_lock) if G.nodes[n]['type'] == 'access']
    assert all(G.nodes[n]['depth'] == G.nodes[new_access]['depth'] + 1 for n in behind)


def test_l2_does_not_apply_without_a_lock_in_an_access_node():
    G = base_graph()  # only L0, which no access node opens to
    assert L2.apply(G, Random(0)) is False
    assert counts(G) == {'access': 1, 'lock': 1, 'key': 1}


@pytest.mark.parametrize('seed', range(5))
def test_every_key_unlocks_exactly_one_lock_and_is_reachable(seed):
    G = base_graph()
    rng = Random(seed)
    for _ in range(12):
        (L1 if rng.randint(0, 1) else L2).apply(G, rng)
    for node, data in G.nodes(data=True):
        if data['type'] == 'key':
            assert [s for s in G.successors(node) if G.edges[node, s]['mode'] == 'unlocks'] == [data['lock']]
            assert len(access_parent(G, node)) == 1
        if data['type'] == 'access':
            assert isinstance(data['depth'], int)

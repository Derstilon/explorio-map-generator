from random import Random

import pytest

import archetypes
from lock_and_key_productions import PRODUCTION_LIST, PRODUCTIONS
from main import base_graph
from nodes import AccessMode, KeyType, LockState, Reusability

CATALOGUE = archetypes.load()


def counts(G):
    types = [data['type'] for _, data in G.nodes(data=True)]
    return {kind: types.count(kind) for kind in ('access', 'lock', 'key')}


def access_parent(G, node):
    return [p for p in G.predecessors(node) if G.edges[p, node]['mode'] == 'access']


def access_children(G, node):
    return [s for s in G.successors(node) if G.edges[node, s]['mode'] == 'access']


def new_nodes(G, before):
    added = sorted(set(G.nodes) - before)
    return ([n for n in added if G.nodes[n]['type'] == 'lock'], [n for n in added if G.nodes[n]['type'] == 'key'],
            [n for n in added if G.nodes[n]['type'] == 'access'])


def graph_with_closed_lock():
    """Seed graph plus one chest, so A0 holds a closed lock (L1) and its key."""
    G = base_graph()
    assert PRODUCTIONS['P1a'].apply(G, Random(0))
    return G


# production -> (archetype id of the new lock, number of new areas, number of new keys)
EXPECTED = {
    'P1a': ('locked-chest', 1, 1), 'P1b': ('locked-chest', 1, 1), 'P1c': ('locked-chest', 1, 1),
    'P2a': ('gate-lock', 1, 2), 'P2b': ('gate-lock', 1, 2), 'P2c': ('gate-lock', 1, 2),
    'P3a': ('pick-your-poison', 1, 2), 'P3b': ('pick-your-poison', 1, 2), 'P3c': ('pick-your-poison', 1, 2),
    'P4': ('ambush-at-the-gate', 1, 1), 'P5': ('tripwire-trap', 1, 1), 'P6': ('tool-assist', 1, 2),
    'P7a': ('sequence-lock', 2, 1), 'P7b': ('gambit-puzzle', 2, 2), 'P7c': ('death-trap', 2, 1),
}


@pytest.mark.parametrize('name', sorted(EXPECTED))
def test_each_lock_production_adds_its_archetype(name):
    archetype_id, areas, keys = EXPECTED[name]
    G = graph_with_closed_lock()
    before = set(G.nodes)
    assert PRODUCTIONS[name].apply(G, Random(1))
    locks, new_keys, new_areas = new_nodes(G, before)
    assert (len(locks), len(new_areas), len(new_keys)) == (1, areas, keys)
    lock = locks[0]
    archetypes.tag_locks(CATALOGUE, G)
    assert G.nodes[lock]['archetype'] == archetype_id
    assert PRODUCTIONS[name].number in CATALOGUE.by_id[archetype_id].productions
    assert G.nodes[lock]['keys'] == set(new_keys)
    assert sorted(access_children(G, lock)) == new_areas


def test_variant_b_moves_the_matched_lock_behind_the_new_lock():
    G = graph_with_closed_lock()
    before = set(G.nodes)
    assert PRODUCTIONS['P2b'].apply(G, Random(0))
    _, _, [behind] = new_nodes(G, before)
    assert access_parent(G, 'L1') == [behind]
    assert 'L1' not in G.nodes['A0']['locks'] and 'L1' in G.nodes[behind]['locks']
    assert all(G.nodes[n]['depth'] == G.nodes[behind]['depth'] + 1 for n in access_children(G, 'L1'))


def test_variant_c_moves_the_matched_key_behind_the_new_lock():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P3c'].apply(G, Random(0))
    _, keys, [behind] = new_nodes(G, before)
    assert access_parent(G, 'K0') == [behind]
    assert all(access_parent(G, key) == ['A0'] for key in keys), 'the decision keys stay in front of the lock'


def test_variant_b_needs_a_closed_lock_in_an_area():
    G = base_graph()  # only L0, which no area opens to
    assert PRODUCTIONS['P1b'].apply(G, Random(0)) is False
    assert counts(G) == {'access': 1, 'lock': 1, 'key': 1}


def test_gate_has_a_reusable_key_on_each_side():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P2a'].apply(G, Random(0))
    _, keys, [behind] = new_nodes(G, before)
    assert sorted(access_parent(G, key)[0] for key in keys) == ['A0', behind]
    assert all(G.nodes[key]['reusability'] == Reusability.REUSABLE for key in keys)


def test_ambush_key_lies_in_the_ambush_area():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P4'].apply(G, Random(0))
    [lock], [key], [behind] = new_nodes(G, before)
    assert access_parent(G, key) == [behind]
    assert G.nodes[behind]['access_mode'] == AccessMode.OPTIONAL and G.nodes[lock]['lock_state'] == LockState.OPEN


def test_tripwire_area_returns_to_the_area_before_it():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P5'].apply(G, Random(0))
    _, [key], [behind] = new_nodes(G, before)
    assert G.edges[behind, 'A0']['mode'] == 'returns'
    assert G.nodes[key]['access_mode'] == AccessMode.OPTIONAL and G.nodes[behind]['access_mode'] == AccessMode.FAILABLE


@pytest.mark.parametrize('name, outcomes', [('P7a', ['success', 'trap']), ('P7b', ['choice', 'choice']),
                                            ('P7c', ['killzone', 'success'])])
def test_multiple_area_locks_mark_each_outcome(name, outcomes):
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS[name].apply(G, Random(0))
    _, _, areas = new_nodes(G, before)
    assert sorted(G.nodes[area]['outcome'] for area in areas) == outcomes


@pytest.mark.parametrize('name', ['P4', 'P5', 'P6', 'P7a', 'P7b', 'P7c'])
def test_trap_productions_need_an_area_that_is_not_failable(name):
    G = base_graph()
    G.nodes['A0']['access_mode'] = AccessMode.FAILABLE
    assert PRODUCTIONS[name].apply(G, Random(0)) is False


def test_complexity_increase_adds_a_primary_key_to_a_closed_and_lock():
    G = graph_with_closed_lock()
    assert PRODUCTIONS['P8'].apply(G, Random(0))
    assert len(G.nodes['L1']['keys']) == 2
    assert {G.nodes[key]['key_type'] for key in G.nodes['L1']['keys']} == {KeyType.PRIMARY}


def test_complexity_increase_adds_a_clue_to_other_locks_and_stops_at_3_keys():
    G = base_graph()
    assert PRODUCTIONS['P4'].apply(G, Random(0))  # an open XOR lock
    for _ in range(2):
        assert PRODUCTIONS['P8'].apply(G, Random(0))
    assert {G.nodes[key]['key_type'] for key in G.nodes['L1']['keys']} == {KeyType.PRIMARY, KeyType.CLUE}
    assert len(G.nodes['L1']['keys']) == 3
    assert PRODUCTIONS['P8'].apply(G, Random(0)) is False


def test_complexity_increase_skips_or_failable_and_the_entrance():
    G = base_graph()
    assert PRODUCTIONS['P8'].apply(G, Random(0)) is False  # L0 is the entrance
    assert PRODUCTIONS['P2a'].apply(G, Random(0))  # OR
    assert PRODUCTIONS['P8'].apply(G, Random(0)) is False
    assert PRODUCTIONS['P5'].apply(G, Random(0))  # failable
    assert PRODUCTIONS['P8'].apply(G, Random(0)) is False


def test_failure_decrease_adds_one_secret_passage_around_a_failable_lock():
    G = base_graph()
    assert PRODUCTIONS['P9'].apply(G, Random(0)) is False
    before = set(G.nodes)
    assert PRODUCTIONS['P6'].apply(G, Random(0))
    _, _, [behind] = new_nodes(G, before)
    assert PRODUCTIONS['P9'].apply(G, Random(0))
    assert G.edges['A0', behind]['mode'] == 'secret' and G.edges[behind, 'A0']['mode'] == 'secret'
    assert PRODUCTIONS['P9'].apply(G, Random(0)) is False, 'one passage per failable lock'


def test_every_production_has_a_role_and_a_description():
    assert [production.name for production in PRODUCTION_LIST] == list(PRODUCTIONS)
    assert {production.role for production in PRODUCTION_LIST} == {'spread', 'filler', 'objective', 'meta'}
    assert all(production.description for production in PRODUCTION_LIST)


@pytest.mark.parametrize('seed', range(5))
def test_every_key_unlocks_exactly_one_lock_and_is_reachable(seed):
    G = base_graph()
    rng = Random(seed)
    for _ in range(25):
        rng.choice(PRODUCTION_LIST).apply(G, rng)
    for node, data in G.nodes(data=True):
        if data['type'] == 'key':
            assert [s for s in G.successors(node) if G.edges[node, s]['mode'] == 'unlocks'] == [data['lock']]
            assert len(access_parent(G, node)) == 1
        if data['type'] == 'access':
            assert isinstance(data['depth'], int)
            assert isinstance(data['access_mode'], AccessMode)


def test_objective_moves_the_goal_into_its_success_area_with_a_secret_passage():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P7a'].apply(G, Random(0))
    _, _, areas = new_nodes(G, before)
    [success] = [area for area in areas if G.nodes[area]['outcome'] == 'success']
    assert access_parent(G, 'K0') == [success]
    assert G.edges['A0', success]['mode'] == 'secret' and G.edges[success, 'A0']['mode'] == 'secret'
    assert G.nodes[success]['access_mode'] != AccessMode.FAILABLE, 'failing the lock never loses the goal'


def test_objective_needs_the_goal_and_an_area_that_is_not_failable():
    G = base_graph()
    G.nodes['A0']['access_mode'] = AccessMode.FAILABLE
    assert PRODUCTIONS['P7a'].apply(G, Random(0)) is False
    G = base_graph()
    assert PRODUCTIONS['P7a'].apply(G, Random(0))
    assert PRODUCTIONS['P7a'].apply(G, Random(0)), 'it applies again in the area the goal moved to'
    assert PRODUCTIONS['P1a'].apply(G, Random(0))
    G.remove_node('K0')
    assert PRODUCTIONS['P7a'].apply(G, Random(0)) is False, 'no goal, nothing to hide'


def test_only_objective_productions_have_the_objective_role():
    assert [production.name for production in PRODUCTION_LIST if production.role == 'objective'] == ['P7a']


def test_goal_leaves_the_first_area_when_an_objective_step_runs():
    from main import generate
    G = generate(42, 2)
    assert any(data['created_by'] == 'P7a' for _, data in G.nodes(data=True))
    assert access_parent(G, 'K0') != ['A0']


def secret_edges(G):
    return sorted((u, v) for u, v, data in G.edges(data=True) if data['mode'] == 'secret')


def graph_with_hidden_goal():
    """P7a on the seed graph: the goal sits in the success area, with a passage from A0 to it."""
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P7a'].apply(G, Random(0))
    _, _, areas = new_nodes(G, before)
    [success] = [area for area in areas if G.nodes[area]['outcome'] == 'success']
    return G, success


@pytest.mark.parametrize('name', ['P2d', 'P3d', 'P4d', 'P7cd'])
def test_variant_d_moves_the_passage_entrance_behind_the_new_lock(name):
    G, success = graph_with_hidden_goal()
    before = set(G.nodes)
    assert PRODUCTIONS[name].apply(G, Random(0))
    [lock], _, areas = new_nodes(G, before)
    [entrance] = [u for u, v in secret_edges(G) if v == success]
    assert entrance in areas and access_parent(G, entrance) == [lock]
    assert secret_edges(G) == sorted([(entrance, success), (success, entrance)])
    assert G.edges[entrance, success]['entrance'] and not G.edges[success, entrance]['entrance']
    assert G.nodes[entrance]['access_mode'] != AccessMode.FAILABLE


def test_variant_d_needs_a_passage_entrance_in_the_area():
    G = base_graph()
    assert PRODUCTIONS['P2d'].apply(G, Random(0)) is False
    G, success = graph_with_hidden_goal()
    G.remove_edges_from([('A0', success)])
    assert PRODUCTIONS['P2d'].apply(G, Random(0)) is False, 'the exit end is not an entrance'


def test_a_fallback_passage_never_moves_into_a_failable_area():
    G, success = graph_with_hidden_goal()
    G.nodes['A0']['access_mode'] = AccessMode.FAILABLE  # P2d's new area would inherit FAILABLE
    assert PRODUCTIONS['P2d'].apply(G, Random(0)) is False
    for edge in (('A0', success), (success, 'A0')):
        G.edges[edge]['fallback'] = False
    assert PRODUCTIONS['P2d'].apply(G, Random(0)), 'a passage that is not a fallback may move'


def test_failure_decrease_does_not_add_a_passage_again_after_its_entrance_moved():
    G = base_graph()
    before = set(G.nodes)
    assert PRODUCTIONS['P6'].apply(G, Random(0))
    _, _, [behind] = new_nodes(G, before)
    assert PRODUCTIONS['P9'].apply(G, Random(0))
    assert PRODUCTIONS['P2d'].apply(G, Random(0))
    assert ('A0', behind) not in G.edges
    assert PRODUCTIONS['P9'].apply(G, Random(0)) is False

import networkx as nx

from lock_and_key_productions.utils import attributes_match, find_isomorphisms
from nodes import AccessMode


def test_attribute_values_must_be_equal():
    assert attributes_match({'type': 'lock', 'keys': {'K1'}}, {'type': 'lock'})
    assert not attributes_match({'type': 'key'}, {'type': 'lock'})
    assert not attributes_match({}, {'type': 'lock'})


def test_callable_attributes_are_predicates_on_the_value():
    pattern = {'type': 'lock', 'keys': lambda keys: keys is not None and len(keys) < 3}
    assert attributes_match({'type': 'lock', 'keys': {'K1', 'K2'}}, pattern)
    assert not attributes_match({'type': 'lock', 'keys': {'K1', 'K2', 'K3'}}, pattern)
    assert not attributes_match({'type': 'lock'}, pattern)  # missing attribute -> predicate gets None


def test_where_is_a_predicate_on_the_whole_node():
    pattern = {'where': lambda data: data.get('access_mode') != AccessMode.FAILABLE}
    assert attributes_match({'access_mode': AccessMode.REQUIRED}, pattern)
    assert attributes_match({}, pattern)
    assert not attributes_match({'access_mode': AccessMode.FAILABLE}, pattern)


def test_find_isomorphisms_respects_conditions_and_direction():
    G = nx.DiGraph()
    G.add_node('A0', type='access')
    G.add_node('L1', type='lock', keys={'K1'}, access_mode=AccessMode.REQUIRED)
    G.add_node('L2', type='lock', keys={'K1', 'K2', 'K3'}, access_mode=AccessMode.FAILABLE)
    G.add_edges_from([('A0', 'L1'), ('A0', 'L2')], mode='access')

    pattern = nx.DiGraph()
    pattern.add_node(0, type='access')
    pattern.add_node(1, type='lock', keys=lambda keys: len(keys) < 3)
    pattern.add_edge(0, 1, mode='access')

    assert find_isomorphisms(G, pattern) == [{'A0': 0, 'L1': 1}]

    reversed_pattern = nx.DiGraph()
    reversed_pattern.add_node(0, type='access')
    reversed_pattern.add_node(1, type='lock')
    reversed_pattern.add_edge(1, 0, mode='access')
    assert find_isomorphisms(G, reversed_pattern) == []

import signal

import networkx as nx

from nodes import Access


def graph(edges):
    G = nx.DiGraph()
    for node in {n for edge in edges for n in edge}:
        G.add_node(node, type={'A': 'access', 'L': 'lock', 'K': 'key'}[node[0]], depth=None)
    G.add_edges_from(edges, mode='access')
    return G


def test_depth_counts_locks_from_the_root():
    G = graph([('L0', 'A0'), ('A0', 'L1'), ('L1', 'A1'), ('A1', 'L2'), ('L2', 'A2'), ('A1', 'K1')])
    Access.recompute_depths(G)
    assert [G.nodes[a]['depth'] for a in ('A0', 'A1', 'A2')] == [0, 1, 2]


def test_depth_terminates_on_a_cycle_and_takes_the_shortest_path():
    # A0 -> L1 -> A1 -> L2 -> A2, plus a shortcut A0 -> L3 -> A2 and a loop back A2 -> L4 -> A0
    G = graph([('L0', 'A0'), ('A0', 'L1'), ('L1', 'A1'), ('A1', 'L2'), ('L2', 'A2'),
               ('A0', 'L3'), ('L3', 'A2'), ('A2', 'L4'), ('L4', 'A0')])
    def hang(signum, frame):
        raise TimeoutError('recompute_depths did not terminate on a cycle')
    previous = signal.signal(signal.SIGALRM, hang)
    signal.alarm(5)
    try:
        Access.recompute_depths(G)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)
    assert [G.nodes[a]['depth'] for a in ('A0', 'A1', 'A2')] == [0, 1, 1]

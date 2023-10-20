from typing import Dict, List

from networkx import Graph
from networkx.algorithms.isomorphism import GraphMatcher


def get_adj_in_isomorphism(G_main: Graph, isomorphism_nodes: list, node: int) -> List[int]:
    adjacency = list(G_main.adj[node])
    for neighbour in adjacency:
        if neighbour not in isomorphism_nodes:
            adjacency.remove(neighbour)
    return adjacency


def find_isomorphisms(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    GM = GraphMatcher(G_main, G_to_find, node_match=lambda n1, n2: n1['type'] == n2['type'] if 'type' in n1 and 'type' in n2 else True, edge_match=lambda e1, e2: e1['mode'] == e2['mode'] if 'mode' in e1 and 'mode' in e2 else True)

    filtered_isomorphisms = []
    for isomorphism in GM.subgraph_isomorphisms_iter():
        if all([isomorphism.keys() != filtered_isomorphism.keys() for filtered_isomorphism in filtered_isomorphisms]):
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms
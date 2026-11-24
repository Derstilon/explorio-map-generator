from typing import Any, Dict, List

from networkx import DiGraph
from networkx.algorithms.isomorphism import DiGraphMatcher


def attributes_match(graph_data: Dict[str, Any], pattern_data: Dict[str, Any]) -> bool:
    """Check a graph node or edge against a pattern node or edge.

    Each pattern attribute is either a value, which must equal the graph
    attribute, or a callable predicate that receives the graph attribute
    (None when the graph element lacks it). The special key `where` holds a
    predicate over the whole attribute dict of the graph element.
    """
    for key, expected in pattern_data.items():
        if key == 'where':
            if not expected(graph_data):
                return False
        elif callable(expected):
            if not expected(graph_data.get(key)):
                return False
        elif graph_data.get(key) != expected:
            return False
    return True


def find_isomorphisms(G_main: DiGraph, G_to_find: DiGraph) -> List[Dict]:
    """Return matches of the pattern G_to_find in G_main as {graph node: pattern node} dicts.

    Matches are induced subgraph isomorphisms; matches covering the same set of
    graph nodes are reported once. The list is sorted by its node mapping,
    because networkx yields matches in an order that depends on Python's
    per-process hash seed; callers pick from it with a seeded RNG.
    """
    GM = DiGraphMatcher(G_main, G_to_find, node_match=attributes_match, edge_match=attributes_match)

    filtered_isomorphisms = []
    for isomorphism in GM.subgraph_isomorphisms_iter():
        if all(isomorphism.keys() != filtered.keys() for filtered in filtered_isomorphisms):
            filtered_isomorphisms.append(isomorphism)

    return sorted(filtered_isomorphisms, key=lambda isomorphism: sorted(isomorphism.items(), key=repr))

from random import Random
import networkx as nx
from .decorators import basic_isomorphism
from typing import Dict, List
from nodes import Lock, LockState, OpenMode, Importance, LogicGate, Key, KeyType, Reusability,Access


class L1():
    left = nx.DiGraph()
    left.add_node(0, type='access')
    left.add_node(1, type='key')
    left.add_edges_from([(0,1)], mode='access')

    @staticmethod
    @basic_isomorphism(left, True)
    def apply(G: nx.Graph, isomorphisms: List[Dict] = None):
        if isomorphisms is None:
            return False
        #random isomoprhism from list
        isomorphism_index = Random(x=1).randint(0,len(isomorphisms)-1)
        isomorphism = isomorphisms[isomorphism_index]
        # replace the key node with a lock node
        key = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'key')[0]
        access = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'access')[0]
        new_lock = Lock().add_new_lock(G, LogicGate.AND, LockState.LOCKED, OpenMode.PERMANENT, Importance.MANDATORY)
        new_access = Access().add_new_access(G, new_lock)
        Access.add_access_edge(G, access, new_lock)
        new_key = Key().add_new_key(G, Reusability.CONSUMABLE, KeyType.MAIN, new_lock)
        # get old edge between access and key
        G.remove_edges_from([(access, key)])
        Access.add_access_edge(G, new_access, key)
        return True

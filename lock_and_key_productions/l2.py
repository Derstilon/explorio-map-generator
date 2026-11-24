from random import Random
import networkx as nx
from .decorators import basic_isomorphism
from typing import Dict, List
from nodes import Lock, LockState, OpenMode, AccessMode, LogicGate, Key, KeyType, Reusability,Access


class L2():
    left = nx.DiGraph()
    left.add_node(0, type='access')
    left.add_node(1, type='lock')
    left.add_edges_from([(0,1)], mode='access')

    @staticmethod
    @basic_isomorphism(left, True)
    def apply(G: nx.DiGraph, rng: Random, isomorphisms: List[Dict] = None):
        if isomorphisms is None:
            return False
        isomorphism = rng.choice(isomorphisms)
        # replace the key node with a lock node
        lock = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'lock')[0]
        access = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'access')[0]
        new_lock = Lock().add_new_lock(G, LogicGate.AND, LockState.CLOSED, OpenMode.PERMANENT, AccessMode.REQUIRED)
        new_access = Access().add_new_access(G, new_lock)
        Access.add_access_edge(G, access, new_lock)
        new_key = Key().add_new_key(G, Reusability.CONSUMABLE, KeyType.PRIMARY, new_lock)
        # move the matched lock from the old access node behind the new lock
        G.remove_edges_from([(access, lock)])
        G.nodes[access]['locks'].discard(lock)
        Access.add_access_edge(G, new_access, lock)
        return True

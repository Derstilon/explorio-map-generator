import networkx as nx
from .node import Node
import math

class Access(Node):
       
    @staticmethod 
    def propagate_depth(G: nx.DiGraph, target: str, start_depth: int = 0):
        next_access_nodes = []
        depth = start_depth
        while True:
            successors = [node for node in G.successors(target) if G.edges[target,node]['mode'] == 'access']
            [next_access_nodes.append((successor, G.nodes[target]['depth'] if 'depth' in G.nodes[target] else depth)) for successor in successors]
            if len(next_access_nodes) == 0:
                break
            (target, depth) = next_access_nodes.pop()
            if(G.nodes[target]['type'] == 'access'):
                G.nodes[target]['depth'] = depth+ 1
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str = 'access_count'):
        return Node().increment_label_counter(G, counter)
    
    @staticmethod
    def add_new_access(G: nx.DiGraph, lock_node: str):
        new_node = f'A{Access.increment_label_counter(G)}'
        # read depth from access node with edge to lock node
        depth = min([G.nodes[access_node]['depth'] for access_node in G.predecessors(lock_node) if G.edges[access_node,lock_node]['mode'] == 'access']+[math.inf])+1
        if math.isinf(depth):
            depth = 0
        G.add_node(new_node, type='access', depth=depth, keys=set(), locks=set())
        G.add_edges_from([(lock_node,new_node)], mode='access')
        
        return new_node
    
    @staticmethod
    def add_access_edge(G: nx.DiGraph, access_node: str, accessible_node: str):
        G.add_edges_from([(access_node,accessible_node)], mode='access')
        G.nodes[access_node]['locks' if G.nodes[accessible_node]['type'] == 'lock' else 'keys'].add(accessible_node)
        Access.propagate_depth(G, accessible_node, G.nodes[access_node]['depth'])
    
    # @staticmethod
    # def propagate_complexity(G: nx.DiGraph, access_node: str, complexity_increase: int, over_horizon_nodes: Set[str] = set()):
    #     if access_node in over_horizon_nodes:
    #         return
    #     # propagate complexity to looks that don't have all keys
    #     # lock keys are not subset of access node keys
    #     not_complete_locks = [lock for lock in G.nodes[access_node]['locks'] if 'keys' in G.nodes[lock] and G.nodes[lock]['keys'].issubset(G.nodes[access_node]['keys']) and lock not in over_horizon_nodes]
    #     orphan_keys = [key for key in G.nodes[access_node]['keys'] if 'lock' in G.nodes[key] and G.nodes[key]['lock'] not in G.nodes[access_node]['locks'] and key not in over_horizon_nodes]
    #     # local keys for not_complete_lock 
    #     local_keys = [key for lock in not_complete_locks for key in G.nodes[lock]['keys'] if key in G.nodes[access_node]['keys'] and key not in over_horizon_nodes]
    #     foreign_locks = [G.nodes[key]['lock'] for key in orphan_keys if 'lock' in G.nodes[key] and G.nodes[key]['lock'] not in over_horizon_nodes]
        
    #     # propagate to orphan_keys and local keys for not_complete_locks
    #     for key in orphan_keys + local_keys:
    #         G.nodes[key]['complexity'] += complexity_increase
        
    #     # propagate to not_complete_locks and foreign locks of orphan_keys
    #     for lock in not_complete_locks + foreign_locks:
    #         G.nodes[lock]['complexity'] += complexity_increase
    #         # recurse on successors of locks
    #         [Access.propagate_complexity(G, successor, complexity_increase, over_horizon_nodes+ set(
    #             not_complete_locks + foreign_locks + orphan_keys + local_keys + [access_node]
    #         )) for successor in G.successors(lock) if G.nodes[successor]['type'] == 'access']

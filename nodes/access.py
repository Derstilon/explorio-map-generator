import networkx as nx
from .node import Node
import math

class Access(Node):

    @staticmethod
    def access_successors(G: nx.DiGraph, node: str):
        return [successor for successor in G.successors(node) if G.edges[node, successor]['mode'] == 'access']

    @staticmethod
    def recompute_depths(G: nx.DiGraph):
        """Set each access node's depth to the fewest locks crossed from a root lock.

        Root locks have no incoming access edge; the access nodes they open have
        depth 0. Breadth-first, so cycles terminate and each node gets its
        shortest depth. Access nodes not reachable from a root keep their depth.
        """
        root_locks = [node for node, data in G.nodes(data=True)
                      if data['type'] == 'lock'
                      and not any(G.edges[p, node]['mode'] == 'access' for p in G.predecessors(node))]
        frontier = [access for lock in root_locks for access in Access.access_successors(G, lock)
                    if G.nodes[access]['type'] == 'access']
        visited = set(frontier)
        depth = 0
        while frontier:
            next_frontier = []
            for access in frontier:
                G.nodes[access]['depth'] = depth
                for lock in Access.access_successors(G, access):
                    if G.nodes[lock]['type'] != 'lock':
                        continue
                    for successor in Access.access_successors(G, lock):
                        if G.nodes[successor]['type'] == 'access' and successor not in visited:
                            visited.add(successor)
                            next_frontier.append(successor)
            frontier = next_frontier
            depth += 1

    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str = 'access_count'):
        return Node().increment_label_counter(G, counter)
    
    @staticmethod
    def add_new_access(G: nx.DiGraph, lock_node: str, access_mode=None):
        """Add an area behind lock_node. Its access_mode defaults to the lock's."""
        new_node = f'A{Access.increment_label_counter(G)}'
        # read depth from access node with edge to lock node
        depth = min([G.nodes[access_node]['depth'] for access_node in G.predecessors(lock_node) if G.edges[access_node,lock_node]['mode'] == 'access']+[math.inf])+1
        if math.isinf(depth):
            depth = 0
        if access_mode is None:
            access_mode = G.nodes[lock_node]['access_mode']
        G.add_node(new_node, type='access', depth=depth, keys=set(), locks=set(), access_mode=access_mode)
        G.add_edges_from([(lock_node,new_node)], mode='access', weight=.5)
        
        return new_node
    
    @staticmethod
    def add_access_edge(G: nx.DiGraph, access_node: str, accessible_node: str):
        G.add_edges_from([(access_node,accessible_node)], mode='access', weight=.5)
        G.nodes[access_node]['locks' if G.nodes[accessible_node]['type'] == 'lock' else 'keys'].add(accessible_node)
        Access.recompute_depths(G)
    
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

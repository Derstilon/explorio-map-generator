from enum import Enum
import PIL
import networkx as nx

from nodes.access import Access

from .node import Node
from .lock import Lock

class Reusability(Enum):
    REUSABLE = 1
    CONSUMABLE = 2
    DUNGEON = 3
    def __str__(self):
        return self.name

class KeyType(Enum):
    MAIN = 1
    SPARE = 2
    CLUE = 3
    def __str__(self):
        return self.name

key_image = PIL.Image.open('img/key.drawio.png')

class Key(Node):
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str = 'key_count'):
        return Node().increment_label_counter(G, counter)
    
    @staticmethod
    def add_new_key(G: nx.DiGraph, reusability: Reusability, key_type: KeyType, lock_node:str, access_node: str | None = None):
        if access_node is None:
            [access_node,*_] = [access_node for access_node in G.predecessors(lock_node) if G.edges[access_node,lock_node]['mode'] == 'access']
        new_node = f'K{Key.increment_label_counter(G)}'
        
        G.add_node(new_node, label=new_node, type='key', complexity=0, lock=lock_node, reusability=reusability, key_type=key_type, image=key_image)
        
        Lock.add_unlocks_edge(G, new_node, lock_node)
        Access.add_access_edge(G, access_node, new_node)
        return new_node
        

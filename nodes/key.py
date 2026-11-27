from enum import Enum
from pathlib import Path
from PIL import Image
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
    PRIMARY = 1
    SPARE = 2
    CLUE = 3
    def __str__(self):
        return self.name

key_image = Image.open(Path(__file__).parent.parent / 'img' / 'key.drawio.png')

class Key(Node):
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str = 'key_count'):
        return Node().increment_label_counter(G, counter)
    
    @staticmethod
    def add_new_key(G: nx.DiGraph, reusability: Reusability, key_type: KeyType, lock_node:str, access_node: str | None = None,
                    access_mode=None):
        """Add a key to lock_node, placed in access_node (default: the area the lock stands in).

        Its access_mode defaults to the area's.
        """
        if access_node is None:
            [access_node,*_] = [access_node for access_node in G.predecessors(lock_node) if G.edges[access_node,lock_node]['mode'] == 'access']
        new_node = f'K{Key.increment_label_counter(G)}'
        
        if access_mode is None:
            access_mode = G.nodes[access_node]['access_mode']
        G.add_node(new_node, label=new_node, type='key', complexity=0, lock=lock_node, reusability=reusability, key_type=key_type,
                   access_mode=access_mode, image=key_image)
        
        Lock.add_unlocks_edge(G, new_node, lock_node)
        Access.add_access_edge(G, access_node, new_node)
        return new_node
        

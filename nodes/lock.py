import networkx as nx
from enum import Enum
import PIL
from .node import Node

class LogicGate(Enum):
    AND = 1
    OR = 2
    NAND = 3
    NOR = 4
    XOR = 5
    XNOR = 6
    def __str__(self):
        return self.name

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2
    def __str__(self):
        return self.name

class OpenMode(Enum):
    TEMPORARY = 1
    PERMANENT = 2
    DUNGEON = 3
    def __str__(self):
        return self.name

class Importance(Enum):
    FAILABLE = 1
    MISSABLE = 2
    MANDATORY = 3
    def __str__(self):
        return self.name

lock_image = PIL.Image.open('img/lock.drawio.png')

class Lock(Node):
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str = 'lock_count'):
        return Node().increment_label_counter(G, counter)
    
    @staticmethod
    def add_new_lock(G: nx.DiGraph, logic_gate: LogicGate, lock_state: LockState, open_mode: OpenMode, importance: Importance, access_node: str | None = None):
        new_node = f'L{Lock.increment_label_counter(G)}'
        
        G.add_node(new_node, label=new_node, type='lock', complexity=0, keys=set(), logic_gate=logic_gate, lock_state=lock_state, open_mode=open_mode, importance=importance, image=lock_image)
        if(access_node is not None):
            G.add_edges_from([(access_node,new_node)], mode='access', weight=.5)
        return new_node
    
    @staticmethod
    def add_unlocks_edge(G: nx.DiGraph, key_node: str, lock_node: str):
        G.add_edges_from([(key_node,lock_node)], mode='unlocks', weight=.85)
        G.nodes[lock_node]['keys'].add(key_node)

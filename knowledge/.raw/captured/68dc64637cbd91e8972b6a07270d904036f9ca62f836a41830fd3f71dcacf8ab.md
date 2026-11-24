# Dev branch code snapshot (commit 5b2372f)

## readme.md
````
# Generation and visualization of the Explorio Dungeon logical layout

This is a PoC for the dungeon generation system for the Explorio game.
Main methodology used is Lock and Key system implemented with Graph grammars as well as Wave Function Collapse to specify concrete types of abstract elements.

<img src="img/Explorio.drawio.png" alt="example" width="500"/>

## Working with the repo

### Create virtual environment

-   `python -m pip install venv`
-   `python -m venv env`

#### Windows

-   `env/Scripts/activate.ps1` for powershell
-   `env/Scripts/activate.bat` for cmd

#### Linux

-   `source env/bin/activate` in bash

### Install required packages

-   `python -m pip install -r requirements.txt`

### Run the example script to validate the environment

-   `python main.py`

### Run the tests

-   `python -m pytest`

````

## main.py
````
import argparse
from random import Random
import sys

import networkx as nx

from nodes import Lock, LockState, OpenMode, Importance, LogicGate, Key, KeyType, Reusability,Access
from biome_injections import EnvironmentBiomes, EncounterBiomes

from lock_and_key_productions import L1, L2
from visualization import draw_dungeon
Random(x=4)

def base_graph():
    G = nx.DiGraph(lock_count=0, key_count=0, access_count=0)
    l0 = Lock().add_new_lock(G, LogicGate.AND, LockState.UNLOCKED, OpenMode.DUNGEON, Importance.MANDATORY)
    a0 = Access().add_new_access(G, l0)
    Key().add_new_key(G, Reusability.DUNGEON, KeyType.MAIN, l0, a0)
    return G

def main(args):
    G = base_graph()
    draw_dungeon(G, ['label', 'depth'])
    x = 0
    while x < 9:
        x += 1 if (L1.apply(G) if Random().randint(0,1) else L2.apply(G)) else 0
    draw_dungeon(G,['label', 'depth'])
    EnvironmentBiomes.apply_environment_biomes(G)
    draw_dungeon(G,['depth', 'label', 'env_biome'])
    EncounterBiomes.apply_encounter_biomes(G)
    draw_dungeon(G,['depth', 'label', 'env_biome', 'enc_biome'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

````

## nodes/node.py
````
from typing import List
import networkx as nx

class Node():
    @staticmethod
    def print_arguments(G: nx.DiGraph, node: str, keys: List[str]):
        return '\n'.join([f'{G.nodes[node][key]}' for key in keys if key in G.nodes[node]])
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str):
        value = G.graph[counter]
        G.graph[counter] += 1
        return value
````

## nodes/lock.py
````
import networkx as nx
from enum import Enum
from PIL import Image
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

lock_image = Image.open('img/lock.drawio.png')

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

````

## nodes/key.py
````
from enum import Enum
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
    MAIN = 1
    SPARE = 2
    CLUE = 3
    def __str__(self):
        return self.name

key_image = Image.open('img/key.drawio.png')

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
        

````

## nodes/access.py
````
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
        G.add_edges_from([(lock_node,new_node)], mode='access', weight=.5)
        
        return new_node
    
    @staticmethod
    def add_access_edge(G: nx.DiGraph, access_node: str, accessible_node: str):
        G.add_edges_from([(access_node,accessible_node)], mode='access', weight=.5)
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

````

## lock_and_key_productions/l1.py
````
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

````

## lock_and_key_productions/l2.py
````
from random import Random
import networkx as nx
from .decorators import basic_isomorphism
from typing import Dict, List
from nodes import Lock, LockState, OpenMode, Importance, LogicGate, Key, KeyType, Reusability,Access


class L2():
    left = nx.DiGraph()
    left.add_node(0, type='access')
    left.add_node(1, type='lock')
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
        lock = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'lock')[0]
        access = list(n for n,_ in isomorphism.items() if G.nodes[n]['type'] == 'access')[0]
        new_lock = Lock().add_new_lock(G, LogicGate.AND, LockState.LOCKED, OpenMode.PERMANENT, Importance.MANDATORY)
        new_access = Access().add_new_access(G, new_lock)
        Access.add_access_edge(G, access, new_lock)
        new_key = Key().add_new_key(G, Reusability.CONSUMABLE, KeyType.MAIN, new_lock)
        # get old edge between access and key
        G.remove_edges_from([(access, lock)])
        Access.add_access_edge(G, new_access, lock)
        return True

````

## lock_and_key_productions/decorators.py
````
from .utils import find_isomorphisms

def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer

def all_isomorphisms(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)

        return inner

    return outer

def basic_isomorphism(left_side, all_isomorphisms=False, iso_finder=find_isomorphisms):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = iso_finder(G, left_side)
            if not isomorphisms: 
                return apply_fun(G, *args, **kwargs)
            if not all_isomorphisms:
                return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)
            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)
        return inner
    return outer
````

## lock_and_key_productions/utils.py
````
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
````

## biome_injections/environment_biomes.py
````
from typing import Dict, List
import networkx as nx
from networkx.algorithms.approximation import randomized_partitioning

biome_data = {
    "caves": {
        "label": "Caves",
        "description": "A dark, underground area with a high density of enemies.",
        "valid_start": True,
        "valid_end": True,
        "adjacency_restrictions": ["desert_cenotaph"],
    },
    "dungeon": {
        "label": "Dungeon",
        "description": "A dungeon with many rooms and corridors.",
        "valid_start": True,
        "valid_end": True,
        "adjacency_restrictions": ["overgrown_garden"],
    },
    "dwarven_ruins": {
        "label": "Dwarven Ruins",
        "description": "An ancient dwarven ruin, full of traps and puzzles.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["abandoned_castle", "overgrown_garden", "desert_cenotaph"],
    },
    "forest": {
        "label": "Forest",
        "description": "A dense forest with many trees and plants.",
        "valid_start": True,
        "valid_end": False,
        "adjacency_restrictions": ["frozen_wastes", "molten_caverns"],
    },
    "frozen_wastes": {
        "label": "Frozen Wastes",
        "description": "A frozen wasteland with little vegetation.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["forest", "molten_caverns", "desert_cenotaph"],
    },
    "molten_caverns": {
        "label": "Molten Caverns",
        "description": "A cavern with lava and fire everywhere.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["frozen_wastes", "forest"],
    },
    "abandoned_castle": {
        "label": "Abandoned Castle",
        "description": "An abandoned castle with many corridors and rooms.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["dwarven_ruins", "desert_cenotaph", "sunken_caverns"],
    },
    "mineshaft": {
        "label": "Mineshaft",
        "description": "An abandoned mineshaft rich in minerals.",
        "valid_start": True,
        "valid_end": False,
        "adjacency_restrictions": ["overgrown_garden"],
    },
    "laboratory": {
        "label": "Laboratory",
        "description": "A laboratory with many experiments and test subjects.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["forgotten_workshop"],
    },
    "desert_cenotaph": {
        "label": "Desert Cenotaph",
        "description": "A cenotaph buried in the desert sand.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["dwarven_ruins", "abandoned_castle", "sunken_caverns", "frozen_wastes", "caves"],
    },
    "overgrown_garden": {
        "label": "Overgrown Garden",
        "description": "A garden overgrown with plants and trees.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["frozen_wastes", "molten_caverns", "dwarven_ruins", "dungeon", "mineshaft"],
    },
    "swamp": {
        "label": "Swamp",
        "description": "A swamp with many trees and plants.",
        "valid_start": True,
        "valid_end": False,
        "adjacency_restrictions": [],
    },
    "abandoned_settlement": {
        "label": "Abandoned Village",
        "description": "An abandoned village with many houses.",
        "valid_start": True,
        "valid_end": False,
        "adjacency_restrictions": [],
    },
    "forgotten_workshop": {
        "label": "Forgotten Workshop",
        "description": "A workshop with many tools and machines.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["laboratory"],
    },
    "sunken_caverns": {
        "label": "Sunken Caverns",
        "description": "A cavern with water and plants everywhere.",
        "valid_start": False,
        "valid_end": True,
        "adjacency_restrictions": ["desert_cenotaph", "abandoned_castle"],
    },
}

class EnvironmentBiomes():
    def apply_environment_biomes(G: nx.DiGraph):
        selected_biomes:tuple[str,str,str] = ("caves","dungeon")
        tmp = nx.Graph(G)
        selected_nodes = ['L0', 'K0']
        tmp.remove_nodes_from(selected_nodes)
        print('tmp nodes',tmp.nodes)
        #Pair of iterables containing an initial partition.
        _, partition = randomized_partitioning(tmp, seed=42)
        print('randomized_partitioning',partition)
        #add selected nodes to partitions
        start_partition = (list(partition[0])  + [selected_nodes[0]], list(partition[1]) + [selected_nodes[1]])
        print('start_partition',start_partition)
        tmp = nx.Graph(G)
        # remove all edges with mode unlocks
        tmp.remove_edges_from([(u,v) for u,v,e in tmp.edges(data=True) if e['mode'] == 'unlocks'])
        partition1, partition2 = nx.community.kernighan_lin_bisection(tmp, start_partition)
        print('kernighan_lin_bisection','\n',partition1,'\n', partition2)
        # assign biomes to partitions
        for node in partition1:
            G.nodes[node]['env_biome'] = selected_biomes[0]
        for node in partition2:
            G.nodes[node]['env_biome'] = selected_biomes[1]
    
````

## biome_injections/encounter_biomes.py
````
import random
from typing import Dict, List
import networkx as nx
from networkx.algorithms.approximation import randomized_partitioning

biome_data = {
    'orcs': {
        'label': 'Orcs',
        'description': 'A dark, underground area with a high amount of orcish activity.',
        'overlay_restrictions': [],
    },
    'trolls': {
        'label': 'Trolls',
        'description': 'A place inhabited by trolls.',
        'overlay_restrictions': [],
    },
    'goblins': {
        'label': 'Goblins',
        'description': 'A narrow place inhabited by goblins.',
        'overlay_restrictions': [],
    },
    'werewolf': {
        'label': 'Werewolf',
        'description': 'A place inhabited by werewolves.',
        'overlay_restrictions': [],
    },
    'vampires': {
        'label': 'Vampires',
        'description': 'Lair ground of the vampires.',
        'overlay_restrictions': [],
    },
    'elements': {
        'label': 'Elements',
        'description': 'An area full of elemental powers and puzzles.',
        'overlay_restrictions': [],
    },
    'necromancy': {
        'label': 'Necromancy',
        'description': 'A grim place full of undead creatures.',
        'overlay_restrictions': [],
    },
    'arcane': {
        'label': 'Arcane',
        'description': 'A place full of magic and arcane monsters.',
        'overlay_restrictions': [],
    },
    'riches': {
        'label': 'Riches',
        'description': 'A place full of riches.',
        'overlay_restrictions': [],
    },
    'infested': {
        'label': 'Infested',
        'description': 'A place infested with spiders or other insects.',
        'overlay_restrictions': [],
    },
    'alchemy': {
        'label': 'Alchemy',
        'description': 'A place full of alchemical ingredients, poisonous gases and other alchemical hazards.',
        'overlay_restrictions': [],
    },
    'hunting': {
        'label': 'Hunting',
        'description': 'A hunting grounds with a lot of prey as well as dangerous predators.',
        'overlay_restrictions': [],
    },
    'sacral': {
        'label': 'Sacral',
        'description': 'A place of worship.',
        'overlay_restrictions': [],
    },
    'cursed': {
        'label': 'Cursed',
        'description': 'A cursed place.',
        'overlay_restrictions': [],
    },
    'traps': {
        'label': 'Traps',
        'description': 'A place full of trapped mechanisms.',
        'overlay_restrictions': [],
    },
    'help': {
        'label': 'Help',
        'description': 'A place where you can find help.',
        'overlay_restrictions': [],
    },
    'dragons': {
        'label': 'Dragons',
        'description': 'A place inhabited by dragons and their kin.',
        'overlay_restrictions': [],
    },
    'mechanical': {
        'label': 'Mechanical',
        'description': 'A place full of mechanical contraptions and robots.',
        'overlay_restrictions': [],
    },
}

class EncounterBiomes():
    def apply_encounter_biomes(G: nx.DiGraph):
        # sample = random.sample(biome_data.keys(), 4)
        sample = ['orcs', 'trolls', 'traps', 'riches']
        #sample 3 nodes from the graph
        selected_nodes = random.sample(list(G.nodes()), 4)
        #grow from the selected nodes few steps
        for i in range(len(sample)):
            tmp = nx.Graph(G)
            node = selected_nodes[i]
            neighbors = [n for n in tmp.neighbors(node) if tmp.edges[node, n]['mode'] == 'access']
            #get at most 3 neighbors
            neighbors = random.sample(neighbors, min(len(neighbors), 3))
            #add sample enc_biome to the neighbors and node
            for n in neighbors + [node]:
                G.nodes[n]['enc_biome'] = [sample[i]] if 'enc_biome' not in G.nodes[n] else G.nodes[n]['enc_biome'] + [sample[i]]
                
        
        
        
        
````

## machine_wfc/machines.py
````
machines = {
    
}
````

## visualization.py
````
import networkx as nx
import matplotlib.pyplot as plt

from nodes import Node


def map_label_to_color(label):
    color_map = {'el': '#ff0000', 'i': '#ffa500', 'e': '#5e90d7'}
    # get whats under label or default value
    return color_map.get(label.lower(), '#c1c1c1')


def map_pos_to_visual_pos(pos, layer):
    x_size = 10
    y_size = 10
    y_offset = 6

    # version with increasing x size
    # if layer >= 3:
    #     x_size *= 2**(layer-2)

    return (x_size * pos[0], -(y_size * pos[1] + layer * (y_size+y_offset)))


def get_layer_subgraph(graph: nx.Graph, layer: int):
    layer_nodes = []
    for node in graph.nodes(data=True):
        if node[1]['layer'] == layer:
            layer_nodes.append(node[0])
    return graph.subgraph(layer_nodes)


def relabel_labels_with_duplicated_pos(labels, positions):
    labels2 = labels.copy()
    pos_label_dict = {}
    for id, pos in positions.items():
        if pos in pos_label_dict:
            pos_label_dict[pos] += labels2[id]
        else:
            pos_label_dict[pos] = labels2[id]

    for id, pos in positions.items():
        labels2[id] = pos_label_dict[pos]

    return labels2

def draw_graph(graph: nx.Graph, layer=None, plot=True):
    if layer is not None:
        graph = get_layer_subgraph(graph, layer)

    labels = nx.get_node_attributes(graph, 'label')
    node_colors = list(map(map_label_to_color, labels.values()))

    visual_pos = nx.get_node_attributes(graph, 'pos')
    if layer is None:
        visual_pos = {node: map_pos_to_visual_pos(
            data['pos'], data['layer']) for node, data in graph.nodes(data=True)}

    labels = relabel_labels_with_duplicated_pos(labels, visual_pos)

    # add node id to label
    # for k, v in labels.items():
    #     labels[k] = f'{v}-{k}'

    nx.draw(graph, pos=visual_pos,
            labels=labels, font_size=12,
            node_size=300, node_color=node_colors)

    if plot:
        plt.show()

def draw_dungeon(G: nx.Graph, label_tags=['label'] ,plot=True):
    
    
    
    # Get a reproducible layout and create figure
    pos = nx.kamada_kawai_layout(G)
    # if 'env_biome' in label_tags:
    #     pos = nx.bipartite_layout(G, [node for node,data in G.nodes.data() if 'env_biome' in data and data['env_biome'] == 'caves'])
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Note: the min_source/target_margin kwargs only work with FancyArrowPatch objects.
    # Force the use of FancyArrowPatch for edge drawing by setting `arrows=True`,
    # but suppress arrowheads with `arrowstyle="-"`
    
    # Transform from data coordinates (scaled between xlim and ylim) to display coordinates
    tr_figure = ax.transData.transform
    # Transform from display to figure coordinates
    tr_axes = fig.transFigure.inverted().transform
    # Select the size of the image (relative to the X axis)
    icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
    icon_center = icon_size / 2.0

    nx.draw_networkx_edges(
        G,
        pos=pos,
        edge_color="gray",
        ax=ax,
        arrows=True,
        arrowstyle="-|>",
        # connectionstyle='angle',
        min_source_margin=5,
        min_target_margin=5,
    )

    # Define a function to offset the position of the labels
    def offset_pos(pos, offset=0.04*len(label_tags)):
        new_pos = {}
        for k, v in pos.items():
            new_pos[k] = (v[0], v[1] - offset)
        return new_pos

    # Draw the labels with an offset position
    nx.draw_networkx_labels(G,
                            labels={node: Node().print_arguments(G, node, label_tags) for node in G.nodes},
                            pos=offset_pos(pos),
                            ax=ax, font_size=12)
    nx.draw_networkx_nodes(G.subgraph(list(node for node,data in G.nodes.data() if 'image' not in data)), pos=pos, ax=ax, node_size=150, node_color='#c1c1c1')
                           

    # add padding to the axes
    ax.set_ylim(ax.get_ylim()[0] - 0.1, ax.get_ylim()[1] + 0.1)
    ax.set_xlim(ax.get_xlim()[0] - 0.1, ax.get_xlim()[1] + 0.1)
    
    # Add the respective image to each node
    for n in G.nodes:
        xf, yf = tr_figure(pos[n])
        xa, ya = tr_axes((xf, yf))
        # get overlapped axes and plot icon
        a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
        if "image" in G.nodes[n]:
            a.imshow(G.nodes[n]["image"])
        a.axis("off")
        
    if plot:
        plt.show()
````

## requirements.txt
````
matplotlib
networkx[default]
````

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
    
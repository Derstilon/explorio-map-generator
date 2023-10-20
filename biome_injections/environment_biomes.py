from typing import Dict, List
import networkx as nx

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
        
        # find nodes with middle depth
        # middle_nodes:Dict[List[str]] = {}
        # idx = 0
        # max_depth = 0
        # while True:
        #     if G.has_node(f'A{idx}'):
        #         max_depth = max(max_depth, G.nodes[f'A{idx}']['depth'])
        #         if G.nodes[f'A{idx}']['depth'] in middle_nodes:
        #             middle_nodes[G.nodes[f'A{idx}']['depth']].append(f'A{idx}')
        #         else:
        #             middle_nodes[G.nodes[f'A{idx}']['depth']] = [f'A{idx}']
        #         idx += 1
        #         continue
        #     break
        
        selected_nodes = [['L0'], ['K0']]
        
        while any(len(x) > 0 for x in selected_nodes):
            for i in range(len(selected_nodes)):
                if len(selected_nodes[i]) == 0:
                    continue
                node = None
                while len(selected_nodes[i]) != 0:
                    node = selected_nodes[i].pop()
                    if 'env_biome' not in G.nodes[node]:
                        break
                    node = None
                if node is None:
                    continue
                G.nodes[node]['env_biome'] = selected_biomes[i]
                for neighbor in [x for x in G.predecessors(node)] + [x for x in G.successors(node)]:
                    edge = G.edges[node,neighbor] if G.has_edge(node,neighbor) else G.edges[neighbor,node]
                    if edge['mode'] == 'access'  and 'env_biome' not in G.nodes[neighbor]:
                        selected_nodes[i].append(neighbor)
            print(selected_nodes)
    
from random import Random
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
    def apply_encounter_biomes(G: nx.DiGraph, rng: Random):
        # sample = random.sample(biome_data.keys(), 4)
        sample = ['orcs', 'trolls', 'traps', 'riches']
        # one seed node per theme; a graph smaller than the sample gets fewer themes
        selected_nodes = rng.sample(list(G.nodes()), min(len(sample), G.number_of_nodes()))
        #grow from the selected nodes few steps
        for i in range(len(selected_nodes)):
            tmp = nx.Graph(G)
            node = selected_nodes[i]
            neighbors = [n for n in tmp.neighbors(node) if tmp.edges[node, n]['mode'] == 'access']
            #get at most 3 neighbors
            neighbors = rng.sample(neighbors, min(len(neighbors), 3))
            #add sample enc_biome to the neighbors and node
            for n in neighbors + [node]:
                G.nodes[n]['enc_biome'] = [sample[i]] if 'enc_biome' not in G.nodes[n] else G.nodes[n]['enc_biome'] + [sample[i]]
                
        
        
        
        
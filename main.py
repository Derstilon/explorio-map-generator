import argparse
from random import Random
import sys
import matplotlib.pyplot as plt

import networkx as nx

from nodes import Lock, LockState, OpenMode, Importance, LogicGate, Key, KeyType, Reusability,Access
from biome_injections import EnvironmentBiomes

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))

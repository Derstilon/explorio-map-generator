import argparse
from random import Random
import sys

import networkx as nx

from nodes import Lock, LockState, OpenMode, AccessMode, LogicGate, Key, KeyType, Reusability, Access
from biome_injections import EnvironmentBiomes, EncounterBiomes

from lock_and_key_productions import L1, L2


def base_graph():
    G = nx.DiGraph(lock_count=0, key_count=0, access_count=0)
    l0 = Lock().add_new_lock(G, LogicGate.AND, LockState.OPEN, OpenMode.DUNGEON, AccessMode.REQUIRED)
    a0 = Access().add_new_access(G, l0)
    Key().add_new_key(G, Reusability.DUNGEON, KeyType.PRIMARY, l0, a0)
    return G


def generate(seed: int, steps: int = 9, on_stage=None):
    """Generate a dungeon story graph. The same seed and steps give the same graph.

    All randomness comes from one Random(seed) instance. on_stage(G, label_tags),
    when given, is called after each stage (seed graph, productions, environment
    biomes, encounter biomes) with the node attributes worth showing.
    """
    rng = Random(seed)
    G = base_graph()
    G.graph['seed'] = seed
    if on_stage:
        on_stage(G, ['label', 'depth'])
    applied = 0
    while applied < steps:
        production = L1 if rng.randint(0, 1) else L2
        if production.apply(G, rng):
            applied += 1
    if on_stage:
        on_stage(G, ['label', 'depth'])
    EnvironmentBiomes.apply_environment_biomes(G, rng)
    if on_stage:
        on_stage(G, ['depth', 'label', 'env_biome'])
    EncounterBiomes.apply_encounter_biomes(G, rng)
    if on_stage:
        on_stage(G, ['depth', 'label', 'env_biome', 'enc_biome'])
    return G


def main(args):
    seed = args.seed if args.seed is not None else Random().randrange(2**32)
    print(f'seed: {seed}')
    on_stage = None
    if not args.no_plot:
        from visualization import draw_dungeon
        on_stage = draw_dungeon
    generate(seed, args.steps, on_stage)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate an Explorio dungeon story graph.')
    parser.add_argument('--seed', type=int, help='RNG seed; a random one is picked and printed when omitted')
    parser.add_argument('--steps', type=int, default=9, help='number of productions to apply (default 9)')
    parser.add_argument('--no-plot', action='store_true', help='generate without opening plot windows')
    main(parser.parse_args(sys.argv[1:]))

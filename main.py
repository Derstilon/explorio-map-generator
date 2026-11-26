import argparse
from random import Random
import sys

import networkx as nx

import archetypes
from nodes import Lock, LockState, OpenMode, AccessMode, LogicGate, Key, KeyType, Reusability, Access
from biome_injections import EnvironmentBiomes, EncounterBiomes

from lock_and_key_productions import L1, L2


def base_graph():
    """Seed graph: the open entrance lock (role 'start'), the first area, and the dungeon key (role 'goal').

    Productions push the goal key deeper behind new locks; the entrance stays the root.
    """
    G = nx.DiGraph(lock_count=0, key_count=0, access_count=0)
    l0 = Lock().add_new_lock(G, LogicGate.AND, LockState.OPEN, OpenMode.DUNGEON, AccessMode.REQUIRED)
    a0 = Access().add_new_access(G, l0)
    k0 = Key().add_new_key(G, Reusability.DUNGEON, KeyType.PRIMARY, l0, a0)
    G.nodes[l0]['role'] = 'start'
    G.nodes[k0]['role'] = 'goal'
    return G


PRODUCTIONS = {'L1': L1, 'L2': L2}
ARCHETYPES = archetypes.load()


def pick_production(rng: Random, weights: dict):
    """Choose a production name by weight; weights must contain at least one positive value."""
    names = [name for name, weight in weights.items() if weight > 0]
    return rng.choices(names, weights=[weights[name] for name in names])[0]


def generate(seed: int, steps: int = 9, on_stage=None, *, weights: dict | None = None,
             environment_biomes: bool = True, encounter_biomes: bool = True, on_step=None):
    """Generate a dungeon story graph. The same seed and parameters give the same graph.

    All randomness comes from one Random(seed) instance.
    - steps: number of productions to apply. Generation stops earlier when no
      enabled production matches anywhere in the graph.
    - weights: relative weight per production name (see PRODUCTIONS); weight 0
      disables it. Default: all equal.
    - on_stage(G, label_tags): called after each stage (seed graph, productions,
      environment biomes, encounter biomes) with the node attributes worth showing.
    - on_step(G, production_name): called after each applied production.
    Every node gets `created_by`: 'seed', the production name that added it, or
    nothing for later stages (biome passes add no nodes). Every lock in the
    archetype matrix gets `archetype`, the id of its entry in ARCHETYPES.
    """
    weights = dict(weights) if weights is not None else {name: 1 for name in PRODUCTIONS}
    rng = Random(seed)
    G = base_graph()
    G.graph['seed'] = seed
    for node in G.nodes:
        G.nodes[node]['created_by'] = 'seed'
    archetypes.tag_locks(ARCHETYPES, G)
    if on_stage:
        on_stage(G, ['label', 'depth'])
    applied = 0
    while applied < steps:
        remaining = {name: weight for name, weight in weights.items() if weight > 0}
        while remaining:
            name = pick_production(rng, remaining)
            before = set(G.nodes)
            if PRODUCTIONS[name].apply(G, rng):
                for node in set(G.nodes) - before:
                    G.nodes[node]['created_by'] = name
                archetypes.tag_locks(ARCHETYPES, G)
                break
            del remaining[name]
        if not remaining:
            break
        applied += 1
        if on_step:
            on_step(G, name)
    G.graph['productions_applied'] = applied
    if on_stage:
        on_stage(G, ['label', 'depth'])
    if environment_biomes:
        EnvironmentBiomes.apply_environment_biomes(G, rng)
        if on_stage:
            on_stage(G, ['depth', 'label', 'env_biome'])
    if encounter_biomes:
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

"""JSON form of a story graph and of its derivation, for the GUI and for export.

Export schema `explorio.story-graph.v1`:
{
  "schema": "explorio.story-graph.v1",
  "seed": int,
  "params": {"steps": int, "weights": {name: number}, "environment_biomes": bool, "encounter_biomes": bool},
  "nodes": [{"id": str, "type": "access"|"lock"|"key", <attributes>}],
  "edges": [{"source": str, "target": str, "mode": "access"|"unlocks"}]
}
Edge mode `access`: the source makes the target reachable (a physical
connection). Edge mode `unlocks`: the key opens the lock (logic only).
Enum attributes are their names, sets are sorted lists.
Lock nodes carry `archetype`: the id of their entry in data/archetypes.yaml.
The zone entrance (role `start`, open mode DUNGEON) lies outside the matrix
and has none.
"""
from enum import Enum

import networkx as nx

from main import ARCHETYPES, PRODUCTIONS, generate

SCHEMA = 'explorio.story-graph.v1'
HIDDEN_ATTRIBUTES = {'image', 'label'}


def plain(value):
    if isinstance(value, Enum):
        return value.name
    if isinstance(value, (set, frozenset)):
        return sorted(plain(item) for item in value)
    if isinstance(value, (list, tuple)):
        return [plain(item) for item in value]
    return value


def graph_to_json(G: nx.DiGraph) -> dict:
    nodes = [{'id': node, **{key: plain(value) for key, value in sorted(data.items()) if key not in HIDDEN_ATTRIBUTES}}
             for node, data in G.nodes(data=True)]
    edges = [{'source': u, 'target': v, 'mode': data['mode']} for u, v, data in G.edges(data=True)]
    return {'nodes': nodes, 'edges': edges}


def edge_set(graph_json: dict) -> set:
    return {(edge['source'], edge['target'], edge['mode']) for edge in graph_json['edges']}


def derive(seed: int, steps: int = 9, weights: dict | None = None,
           environment_biomes: bool = True, encounter_biomes: bool = True) -> dict:
    """Generate a graph and record every stage and production as a frame.

    Each frame has `title`, `kind` ('seed', 'production', 'biomes'), `production`
    (name or null), `graph`, and the changes against the previous frame:
    `added_nodes`, `added_edges`, `removed_edges` ([source, target, mode]) and
    `changed_nodes` (ids whose attributes changed).
    `archetypes` maps each archetype id used in the frames to its `name`,
    `status` and `play_pattern`, for the GUI tooltip.
    """
    weights = dict(weights) if weights is not None else {name: 1 for name in PRODUCTIONS}
    frames = []

    def record(G, title, kind, production=None):
        graph = graph_to_json(G)
        previous = frames[-1]['graph'] if frames else {'nodes': [], 'edges': []}
        previous_nodes = {node['id']: node for node in previous['nodes']}
        frames.append({
            'title': title,
            'kind': kind,
            'production': production,
            'graph': graph,
            'added_nodes': [node['id'] for node in graph['nodes'] if node['id'] not in previous_nodes],
            'changed_nodes': [node['id'] for node in graph['nodes']
                              if node['id'] in previous_nodes and previous_nodes[node['id']] != node],
            'added_edges': sorted(map(list, edge_set(graph) - edge_set(previous))),
            'removed_edges': sorted(map(list, edge_set(previous) - edge_set(graph))),
        })

    stage_titles = iter(['Seed graph', None]
                        + (['Environment biomes'] if environment_biomes else [])
                        + (['Encounter biomes'] if encounter_biomes else []))

    def on_stage(G, _label_tags):
        title = next(stage_titles)
        if title is not None:  # the stage after productions repeats the last production frame
            record(G, title, 'seed' if title == 'Seed graph' else 'biomes')

    def on_step(G, production):
        record(G, f'Step {sum(frame["kind"] == "production" for frame in frames) + 1}: {production}',
               'production', production)

    G = generate(seed, steps, on_stage, weights=weights, environment_biomes=environment_biomes,
                 encounter_biomes=encounter_biomes, on_step=on_step)
    params = {'steps': steps, 'weights': weights, 'environment_biomes': environment_biomes,
              'encounter_biomes': encounter_biomes}
    used = {node['archetype'] for frame in frames for node in frame['graph']['nodes'] if 'archetype' in node}
    return {
        'schema': SCHEMA,
        'seed': seed,
        'params': params,
        'productions_applied': G.graph['productions_applied'],
        'frames': frames,
        'archetypes': {archetype_id: {'name': ARCHETYPES.by_id[archetype_id].label,
                                      'status': ARCHETYPES.by_id[archetype_id].status,
                                      'play_pattern': ARCHETYPES.by_id[archetype_id].play_pattern}
                       for archetype_id in sorted(used)},
        'export': {'schema': SCHEMA, 'seed': seed, 'params': params, **graph_to_json(G)},
    }

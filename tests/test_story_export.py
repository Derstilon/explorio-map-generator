import json

import pytest

from story_export import SCHEMA, derive


def test_frames_cover_seed_each_production_and_biome_passes():
    derivation = derive(42, 9)
    titles = [frame['title'] for frame in derivation['frames']]
    assert titles == ['Seed graph'] + [f'Step {i}: {frame["production"]}' for i, frame in
                                       enumerate(derivation['frames'][1:10], 1)] + ['Environment biomes', 'Encounter biomes']
    assert derivation['productions_applied'] == 9
    assert json.loads(json.dumps(derivation)) == derivation  # plain JSON, no sets or enums left


def test_each_production_frame_adds_one_area_lock_and_key():
    for frame in derive(7, 6)['frames'][1:7]:
        assert sorted(node[0] for node in frame['added_nodes']) == ['A', 'K', 'L']
        assert frame['removed_edges'], 'the matched key or lock moves behind the new lock'


def test_biome_frames_change_attributes_only():
    frames = derive(3, 5)['frames']
    for frame in frames[-2:]:
        assert frame['added_nodes'] == [] and frame['added_edges'] == [] and frame['removed_edges'] == []
        assert frame['changed_nodes']


def test_export_is_the_final_graph_with_seed_and_params():
    derivation = derive(5, 4, weights={'L1': 2, 'L2': 1}, encounter_biomes=False)
    export = derivation['export']
    assert export['schema'] == SCHEMA and export['seed'] == 5
    assert export['params'] == {'steps': 4, 'weights': {'L1': 2, 'L2': 1},
                                'environment_biomes': True, 'encounter_biomes': False}
    assert export['nodes'] == derivation['frames'][-1]['graph']['nodes']
    lock = next(node for node in export['nodes'] if node['id'] == 'L1')
    assert lock['type'] == 'lock' and lock['logic_gate'] == 'AND' and lock['lock_state'] == 'CLOSED'
    assert all('image' not in node for node in export['nodes'])
    assert {edge['mode'] for edge in export['edges']} == {'access', 'unlocks'}


@pytest.mark.parametrize('kwargs', [{'weights': {'L1': 0, 'L2': 1}}, {'steps': 0}])
def test_stops_early_when_nothing_can_apply_and_still_runs_biome_passes(kwargs):
    derivation = derive(1, **{'steps': 9, **kwargs})
    assert derivation['productions_applied'] == 0
    assert [frame['title'] for frame in derivation['frames']] == ['Seed graph', 'Environment biomes', 'Encounter biomes']


def test_frame_titles_follow_the_enabled_biome_passes():
    titles = [frame['title'] for frame in derive(1, 2, environment_biomes=False)['frames']]
    assert titles[-1] == 'Encounter biomes' and 'Environment biomes' not in titles


def test_export_marks_the_entrance_as_start_and_the_dungeon_key_as_goal():
    nodes = derive(11, 6)['export']['nodes']
    roles = {node['id']: node['role'] for node in nodes if 'role' in node}
    assert roles == {'L0': 'start', 'K0': 'goal'}
    goal = next(node for node in nodes if node['id'] == 'K0')
    assert goal['reusability'] == 'DUNGEON' and goal['lock'] == 'L0'

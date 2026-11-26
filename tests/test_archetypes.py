import copy
import logging

import pytest
import yaml

import archetypes
from archetypes import ArchetypeError, Catalogue
from main import base_graph, generate
from nodes import AccessMode, Key, KeyType, Lock, LockState, LogicGate, OpenMode, Reusability
from story_export import derive


@pytest.fixture(scope='module')
def entries():
    with archetypes.DEFAULT_PATH.open(encoding='utf-8') as file:
        return yaml.safe_load(file)


@pytest.fixture(scope='module')
def catalogue():
    return archetypes.load()


def test_real_file_covers_every_combination_once_in_the_fixed_order(entries, catalogue):
    combinations = [tuple(entry['combination'][dimension] for dimension in archetypes.DIMENSIONS)
                    for entry in entries]
    assert combinations == list(archetypes.all_combinations())
    assert len(combinations) == 96
    assert [archetype.id for archetype in catalogue] == [entry['id'] for entry in entries]


def test_real_file_keeps_the_sheet_rows(catalogue):
    lps = sorted(archetype.sheet_lp for archetype in catalogue if archetype.sheet_lp is not None)
    assert lps == list(range(94))
    assert sum(archetype.status == 'named' for archetype in catalogue) == 25
    assert all(archetype.examples or archetype.sheet_lp not in (33, 48, 54, 60) for archetype in catalogue)


def test_value_names_match_the_code_enums():
    assert set(archetypes.KEY_USAGES) == {Reusability.REUSABLE.name, Reusability.CONSUMABLE.name}
    assert set(archetypes.GATES) == {gate.name for gate in LogicGate}
    assert set(archetypes.OPEN_MODES) == {OpenMode.PERMANENT.name, OpenMode.TEMPORARY.name}
    assert set(archetypes.BASE_STATES) == {state.name for state in LockState}


def broken(entries, change):
    copied = copy.deepcopy(entries)
    change(copied)
    return copied


@pytest.mark.parametrize('change, message', [
    (lambda entries: entries.append(copy.deepcopy(entries[0]) | {'id': 'copy', 'name': 'Copy'}),
     'share the combination REUSABLE · AND'),
    (lambda entries: entries.pop(5), '1 combinations have no entry'),
    (lambda entries: entries[0]['combination'].update(gate='NOT'), "gate 'NOT' is not one of"),
    (lambda entries: entries[0]['combination'].update(access='REQUIRED'), "access 'REQUIRED' is not one of"),
    (lambda entries: entries[3].update(status='unusable', unusable_reason=''), 'needs an unusable_reason'),
    (lambda entries: entries[1].update(play_pattern=''), 'needs a name and a play pattern'),
    (lambda entries: entries[1].update(id=entries[0]['id']), 'two archetypes have the id'),
    (lambda entries: entries[1].update(name=entries[0]['name']), 'share the name'),
    (lambda entries: entries[0].update(productions=['8']), "unknown productions ['8']"),
    (lambda entries: entries[0].update(theme='fire'), "unknown fields ['theme']"),
])
def test_validation_rejects_broken_files_and_names_the_entry(entries, change, message):
    with pytest.raises(ArchetypeError, match=message.replace('[', r'\[').replace(']', r'\]')):
        Catalogue(broken(entries, change))


def test_validation_message_names_the_entry(entries):
    with pytest.raises(ArchetypeError, match=rf'entry 1 \({entries[0]["id"]}\)'):
        Catalogue(broken(entries, lambda copied: copied[0].update(status='done')))


@pytest.mark.parametrize('combination, archetype_id', [
    (('CONSUMABLE', 'AND', 'PERMANENT', 'REQUIRED', 'CLOSED'), 'locked-chest'),  # LP 1
    (('REUSABLE', 'OR', 'TEMPORARY', 'OPTIONAL', 'CLOSED'), 'gate-lock'),  # LP 50
    (('CONSUMABLE', 'XOR', 'TEMPORARY', 'REQUIRED', 'OPEN'), 'ambush-at-the-gate'),  # LP 73
    (('REUSABLE', 'NOR', 'TEMPORARY', 'FAILABLE', 'CLOSED'), 'death-trap'),  # LP 38
])
def test_lookup_by_combination(catalogue, combination, archetype_id):
    assert catalogue.lookup(*combination).id == archetype_id


def test_lookup_treats_required_and_optional_the_same(catalogue):
    required = catalogue.lookup('CONSUMABLE', 'AND', 'PERMANENT', AccessMode.REQUIRED.name, 'CLOSED')
    optional = catalogue.lookup('CONSUMABLE', 'AND', 'PERMANENT', AccessMode.OPTIONAL.name, 'CLOSED')
    assert required is optional
    assert required.combination[3] == 'REQUIRED_OR_OPTIONAL'


def lock_with_keys(*reusabilities_and_types, gate=LogicGate.AND, open_mode=OpenMode.PERMANENT):
    G = base_graph()
    lock = Lock.add_new_lock(G, gate, LockState.CLOSED, open_mode, AccessMode.REQUIRED, 'A0')
    for reusability, key_type in reusabilities_and_types:
        Key.add_new_key(G, reusability, key_type, lock, 'A0')
    return G, lock


def test_key_usage_comes_from_primary_keys():
    G, lock = lock_with_keys((Reusability.REUSABLE, KeyType.PRIMARY), (Reusability.CONSUMABLE, KeyType.SPARE))
    assert archetypes.lock_key_usage(G, lock) == 'REUSABLE'
    G, lock = lock_with_keys((Reusability.REUSABLE, KeyType.PRIMARY), (Reusability.CONSUMABLE, KeyType.PRIMARY))
    assert archetypes.lock_key_usage(G, lock) == 'CONSUMABLE'
    G, lock = lock_with_keys((Reusability.REUSABLE, KeyType.CLUE))
    assert archetypes.lock_key_usage(G, lock) is None


def test_entrance_lock_has_no_archetype(catalogue):
    G = base_graph()
    assert archetypes.lock_archetype(catalogue, G, 'L0') is None


def test_tagging_warns_once_for_an_unusable_combination(entries, caplog):
    def mark_locked_chest_unusable(copied):
        chest = next(entry for entry in copied if entry['id'] == 'locked-chest')
        chest.update(status='unusable', unusable_reason='test reason')
    catalogue = Catalogue(broken(entries, mark_locked_chest_unusable))
    G, lock = lock_with_keys((Reusability.CONSUMABLE, KeyType.PRIMARY))
    with caplog.at_level(logging.WARNING, logger='archetypes'):
        archetypes.tag_locks(catalogue, G)
        archetypes.tag_locks(catalogue, G)
    assert G.nodes[lock]['archetype'] == 'locked-chest'
    assert [record.getMessage() for record in caplog.records] == [
        f'lock {lock} has the unusable combination CONSUMABLE · AND · PERMANENT · REQUIRED_OR_OPTIONAL · CLOSED: '
        'test reason']


@pytest.mark.parametrize('seed', range(8))
def test_every_generated_lock_has_an_archetype(seed):
    G = generate(seed, 12)
    for node, data in G.nodes(data=True):
        if data['type'] == 'lock' and data.get('role') != 'start':
            assert data['archetype'] == 'locked-chest', node


def test_export_and_frames_carry_the_archetype():
    derivation = derive(3, 5)
    locks = [node for node in derivation['export']['nodes'] if node['type'] == 'lock']
    assert {node['id']: node.get('archetype') for node in locks if node['id'] != 'L0'} == {
        f'L{i}': 'locked-chest' for i in range(1, 6)}
    assert 'archetype' not in next(node for node in locks if node['id'] == 'L0')
    step_one = derivation['frames'][1]['graph']['nodes']
    assert next(node for node in step_one if node['id'] == 'L1')['archetype'] == 'locked-chest'
    assert derivation['archetypes'] == {'locked-chest': {
        'name': 'Locked Chest', 'status': 'named',
        'play_pattern': 'Bring every required key and spend it on the lock; it opens for good.'}}


def test_importer_seeds_the_same_combinations_and_sheet_rows_as_the_data_file(catalogue):
    from tools.import_archetype_sheet import DEFAULT_SHEET, build_entries, read_sheet
    seeded = build_entries(read_sheet(DEFAULT_SHEET))
    assert [(entry['sheet_lp'], entry['productions']) for entry in seeded] == [
        (archetype.sheet_lp, list(archetype.productions)) for archetype in catalogue]
    assert {entry['name'] for entry in seeded if entry['status'] == 'named'} == {
        archetype.name for archetype in catalogue if archetype.status == 'named'}


def tagged_chest(catalogue):
    G, lock = lock_with_keys((Reusability.CONSUMABLE, KeyType.PRIMARY))
    archetypes.tag_locks(catalogue, G)
    assert G.nodes[lock]['archetype'] == 'locked-chest'
    return G, lock, next(iter(G.nodes[lock]['keys']))


def test_retagging_follows_a_changed_lock(catalogue):
    G, lock, _ = tagged_chest(catalogue)
    G.nodes[lock]['logic_gate'] = LogicGate.OR
    archetypes.tag_locks(catalogue, G)
    assert G.nodes[lock]['archetype'] == 'pick-your-poison'


def test_retagging_follows_changed_keys(catalogue):
    G, lock, key = tagged_chest(catalogue)
    G.nodes[key]['reusability'] = Reusability.REUSABLE
    archetypes.tag_locks(catalogue, G)
    assert G.nodes[lock]['archetype'] == 'advanced-puzzle'


def test_retagging_drops_the_tag_when_the_lock_leaves_the_matrix(catalogue):
    G, lock, key = tagged_chest(catalogue)
    G.nodes[key]['reusability'] = Reusability.DUNGEON
    archetypes.tag_locks(catalogue, G)
    assert 'archetype' not in G.nodes[lock]

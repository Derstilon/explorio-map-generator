"""Abstract puzzle archetypes: one per cell of the lock/key matrix, loaded from data/archetypes.yaml.

A cell is a combination of key usage × gate × open mode × access × base state
(2 × 6 × 2 × 2 × 2 = 96). Values are the code's enum names, except access,
which the matrix splits only into REQUIRED_OR_OPTIONAL and FAILABLE: whether a
non-failable lock is required or optional depends on where it sits in the
graph, not on its archetype.
"""
import itertools
import logging
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import yaml

from nodes import AccessMode, KeyType, LockState, LogicGate, OpenMode, Reusability

DEFAULT_PATH = Path(__file__).parent / 'data' / 'archetypes.yaml'

# Order of the values; entries in the data file are sorted by gate, then key usage, open mode, access, base state.
KEY_USAGES = ('REUSABLE', 'CONSUMABLE')
GATES = ('AND', 'OR', 'NAND', 'NOR', 'XOR', 'XNOR')
OPEN_MODES = ('PERMANENT', 'TEMPORARY')
ACCESSES = ('REQUIRED_OR_OPTIONAL', 'FAILABLE')
BASE_STATES = ('CLOSED', 'OPEN')
DIMENSIONS = {'key_usage': KEY_USAGES, 'gate': GATES, 'open_mode': OPEN_MODES, 'access': ACCESSES,
              'base_state': BASE_STATES}
STATUSES = ('named', 'proposed', 'unusable')
# Productions that create an archetype; meta productions 8 and 9 only change existing locks.
KNOWN_PRODUCTIONS = ('1', '2', '3', '4', '5', '6', '7a', '7b', '7c')
FIELDS = ('id', 'combination', 'name', 'status', 'play_pattern', 'unusable_reason', 'productions', 'sheet_lp',
          'examples')

FILE_HEADER = """\
# Abstract puzzle archetypes: one entry per cell of the 96-cell lock/key matrix.
# Loaded and validated by archetypes.py; seeded once by tools/import_archetype_sheet.py, then edited by hand.
#
# id               stable slug, used in the code and the JSON export
# combination      key_usage (REUSABLE, CONSUMABLE), gate (AND, OR, NAND, NOR, XOR, XNOR),
#                  open_mode (PERMANENT, TEMPORARY), access (REQUIRED_OR_OPTIONAL, FAILABLE),
#                  base_state (CLOSED, OPEN)
# name             archetype name; empty only for unusable cells
# status           named (confirmed by the owner), proposed (waiting for the owner) or unusable
# play_pattern     one abstract line: what the player does, no theme (named and proposed)
# unusable_reason  why the cell can't be used (unusable only)
# productions      production numbers that create this archetype, e.g. ['1'], ['7a']
# sheet_lp         LP number of the product sheet row; empty for cells the sheet lacks
# examples         the sheet's examples, translated and shortened; for cells the sheet left empty,
#                  proposed ones drawn from the GDDs; reference for flavours, not read by the generator
#
# Gates count the active inputs: AND all, OR at least one, NAND not all, NOR none, XOR exactly one,
# XNOR none or all. Order and timing between inputs are left to the room-map and content steps.

"""

log = logging.getLogger(__name__)


class ArchetypeError(ValueError):
    pass


@dataclass(frozen=True)
class Archetype:
    id: str
    combination: tuple
    name: str
    status: str
    play_pattern: str
    unusable_reason: str
    productions: tuple
    sheet_lp: int | None
    examples: tuple

    @property
    def label(self) -> str:
        return self.name or self.id


def all_combinations():
    """Every matrix cell as (key_usage, gate, open_mode, access, base_state), in the data file's order."""
    for gate, key_usage, open_mode, access, base_state in itertools.product(
            GATES, KEY_USAGES, OPEN_MODES, ACCESSES, BASE_STATES):
        yield key_usage, gate, open_mode, access, base_state


def combination_slug(combination: tuple) -> str:
    return '-'.join(value.lower().replace('_', '-') for value in combination)


def describe(combination: tuple) -> str:
    return ' · '.join(combination)


def _entry_error(index: int, entry, message: str) -> ArchetypeError:
    name = entry.get('id') if isinstance(entry, dict) else None
    return ArchetypeError(f'archetype entry {index + 1}{f" ({name})" if name else ""}: {message}')


def _parse_entry(index: int, entry) -> Archetype:
    if not isinstance(entry, dict):
        raise _entry_error(index, entry, 'is not a mapping')
    unknown = set(entry) - set(FIELDS)
    missing = {'id', 'combination', 'status'} - set(entry)
    if unknown or missing:
        raise _entry_error(index, entry, f'unknown fields {sorted(unknown)}' if unknown else f'missing {sorted(missing)}')
    combination = entry['combination']
    if not isinstance(combination, dict) or set(combination) != set(DIMENSIONS):
        raise _entry_error(index, entry, f'combination needs exactly the keys {list(DIMENSIONS)}')
    for dimension, values in DIMENSIONS.items():
        if combination[dimension] not in values:
            raise _entry_error(index, entry, f'{dimension} {combination[dimension]!r} is not one of {list(values)}')
    if entry['status'] not in STATUSES:
        raise _entry_error(index, entry, f'status {entry["status"]!r} is not one of {list(STATUSES)}')
    archetype = Archetype(
        id=str(entry['id'] or ''),
        combination=tuple(combination[dimension] for dimension in DIMENSIONS),
        name=str(entry.get('name') or ''),
        status=entry['status'],
        play_pattern=str(entry.get('play_pattern') or '').strip(),
        unusable_reason=str(entry.get('unusable_reason') or '').strip(),
        productions=tuple(str(production) for production in entry.get('productions') or ()),
        sheet_lp=entry.get('sheet_lp'),
        examples=tuple(entry.get('examples') or ()),
    )
    if not archetype.id:
        raise _entry_error(index, entry, 'id is empty')
    if archetype.status in ('named', 'proposed'):
        if not archetype.name or not archetype.play_pattern:
            raise _entry_error(index, entry, f'a {archetype.status} entry needs a name and a play pattern')
    elif not archetype.unusable_reason:
        raise _entry_error(index, entry, 'an unusable entry needs an unusable_reason')
    unknown_productions = set(archetype.productions) - set(KNOWN_PRODUCTIONS)
    if unknown_productions:
        raise _entry_error(index, entry, f'unknown productions {sorted(unknown_productions)}')
    return archetype


class Catalogue:
    """Validated archetypes, looked up by id or by combination."""

    def __init__(self, entries: list):
        if not isinstance(entries, list):
            raise ArchetypeError('the archetype file must hold a list of entries')
        archetypes = [_parse_entry(index, entry) for index, entry in enumerate(entries)]
        self.by_combination = {}
        self.by_id = {}
        names = {}
        for archetype in archetypes:
            if archetype.combination in self.by_combination:
                raise ArchetypeError(f'archetypes {self.by_combination[archetype.combination].id} and {archetype.id} '
                                     f'share the combination {describe(archetype.combination)}')
            if archetype.id in self.by_id:
                raise ArchetypeError(f'two archetypes have the id {archetype.id}')
            self.by_combination[archetype.combination] = archetype
            self.by_id[archetype.id] = archetype
            if archetype.name:
                if archetype.name in names:
                    raise ArchetypeError(f'archetypes {names[archetype.name]} and {archetype.id} share the name '
                                         f'{archetype.name!r}')
                names[archetype.name] = archetype.id
        missing = [combination for combination in all_combinations() if combination not in self.by_combination]
        if missing:
            raise ArchetypeError(f'{len(missing)} combinations have no entry, e.g. {describe(missing[0])}')

    def __iter__(self):
        return iter(self.by_combination[combination] for combination in all_combinations())

    def lookup(self, key_usage: str, gate: str, open_mode: str, access: str, base_state: str) -> Archetype:
        """Find the archetype of a combination; REQUIRED and OPTIONAL access count as REQUIRED_OR_OPTIONAL."""
        if access in (AccessMode.REQUIRED.name, AccessMode.OPTIONAL.name):
            access = 'REQUIRED_OR_OPTIONAL'
        return self.by_combination[(key_usage, gate, open_mode, access, base_state)]


def load(path: Path = DEFAULT_PATH) -> Catalogue:
    with Path(path).open(encoding='utf-8') as file:
        return Catalogue(yaml.safe_load(file))


def lock_key_usage(G: nx.DiGraph, lock: str) -> str | None:
    """Key usage of a lock, taken from its primary keys (all its keys when it has no primary key, e.g. a lock
    opened by a clue alone): CONSUMABLE when any of them is consumable.

    None when the lock has no keys or one of them is outside the matrix (DUNGEON).
    """
    keys = G.nodes[lock]['keys']
    primary = {key for key in keys if G.nodes[key]['key_type'] == KeyType.PRIMARY}
    usages = {G.nodes[key]['reusability'] for key in primary or keys}
    if not usages or Reusability.DUNGEON in usages:
        return None
    return Reusability.CONSUMABLE.name if Reusability.CONSUMABLE in usages else Reusability.REUSABLE.name


def lock_archetype(catalogue: Catalogue, G: nx.DiGraph, lock: str) -> Archetype | None:
    """The archetype of a lock node, or None when the lock lies outside the matrix (the DUNGEON entrance)."""
    data = G.nodes[lock]
    key_usage = lock_key_usage(G, lock)
    if key_usage is None or data['open_mode'] == OpenMode.DUNGEON:
        return None
    gate: LogicGate = data['logic_gate']
    state: LockState = data['lock_state']
    return catalogue.lookup(key_usage, gate.name, data['open_mode'].name, data['access_mode'].name, state.name)


def tag_locks(catalogue: Catalogue, G: nx.DiGraph):
    """Set `archetype` (the id) on every lock in the matrix; warn when a lock newly gets an unusable archetype."""
    for lock, data in G.nodes(data=True):
        if data['type'] != 'lock':
            continue
        archetype = lock_archetype(catalogue, G, lock)
        if archetype is None:
            data.pop('archetype', None)
            continue
        if archetype.status == 'unusable' and data.get('archetype') != archetype.id:
            log.warning('lock %s has the unusable combination %s: %s', lock, describe(archetype.combination),
                        archetype.unusable_reason)
        data['archetype'] = archetype.id

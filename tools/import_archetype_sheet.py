"""Seed data/archetypes.yaml from the product sheet's key/lock matrix (CSV export).

Usage: python tools/import_archetype_sheet.py [sheet.csv] [--output data/archetypes.yaml] [--force]

Writes one entry per combination of the 96-cell matrix, in the fixed order of
archetypes.all_combinations(). Named sheet rows become `named` entries; every
other cell becomes a `proposed` entry with no name or play pattern yet, to be
filled in by hand. Examples are copied untranslated. The YAML file is edited
by hand after the import, so the script refuses to overwrite it without --force.
"""
import argparse
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from archetypes import FILE_HEADER, all_combinations, combination_slug  # noqa: E402

DEFAULT_SHEET = ROOT / 'knowledge/.raw/captured/8e3916886ef8870d171881e69a7879f9eb1dad1ae4694d4ad5db266da0b6ebcc.csv'
DEFAULT_OUTPUT = ROOT / 'data/archetypes.yaml'

SHEET_VALUES = {
    'key_usage': {'Reuseable': 'REUSABLE', 'Reusable': 'REUSABLE', 'Consumable': 'CONSUMABLE'},
    'gate': {gate: gate for gate in ('AND', 'OR', 'NAND', 'NOR', 'XOR', 'XNOR')},
    'open_mode': {'Permanent': 'PERMANENT', 'Temporary': 'TEMPORARY'},
    'access': {'Required/Optional': 'REQUIRED_OR_OPTIONAL', 'Failable': 'FAILABLE'},
    'base_state': {'Closed': 'CLOSED', 'Open': 'OPEN'},
}
NAME_FIXES = {'Point of no? return': 'Point of no return'}


def slug(text: str) -> str:
    return '-'.join(''.join(char if char.isalnum() else ' ' for char in text.lower()).split())


def read_sheet(path: Path) -> dict:
    """Return {combination tuple: sheet row} for the sheet's numbered rows."""
    rows = {}
    with path.open(newline='', encoding='utf-8') as file:
        for record in list(csv.reader(file))[1:]:
            production, name, lp, key_usage, gate, open_mode, access, base_state, *examples = record
            if not lp.strip():
                continue
            combination = (SHEET_VALUES['key_usage'][key_usage], SHEET_VALUES['gate'][gate],
                           SHEET_VALUES['open_mode'][open_mode], SHEET_VALUES['access'][access],
                           SHEET_VALUES['base_state'][base_state])
            if combination in rows:
                raise ValueError(f'sheet rows LP {rows[combination]["lp"]} and LP {lp} have the same combination')
            rows[combination] = {
                'lp': int(lp),
                'name': NAME_FIXES.get(name.strip(), name.strip()),
                'production': production.strip(),
                'examples': [example.strip() for example in examples if example.strip()],
            }
    return rows


def build_entries(rows: dict) -> list:
    entries = []
    for combination in all_combinations():
        row = rows.get(combination, {'lp': None, 'name': '', 'production': '', 'examples': []})
        named = bool(row['name'])
        entries.append({
            'id': slug(row['name']) if named else combination_slug(combination),
            'combination': dict(zip(('key_usage', 'gate', 'open_mode', 'access', 'base_state'), combination)),
            'name': row['name'],
            'status': 'named' if named else 'proposed',
            'play_pattern': '',
            'unusable_reason': '',
            'productions': [row['production']] if row['production'] else [],
            'sheet_lp': row['lp'],
            'examples': row['examples'],
        })
    return entries


def main(argv):
    parser = argparse.ArgumentParser(description='Seed data/archetypes.yaml from the product sheet CSV.')
    parser.add_argument('sheet', nargs='?', type=Path, default=DEFAULT_SHEET)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--force', action='store_true', help='overwrite an existing output file')
    args = parser.parse_args(argv)
    if args.output.exists() and not args.force:
        parser.error(f'{args.output} exists and holds hand edits; pass --force to overwrite it')
    entries = build_entries(read_sheet(args.sheet))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', newline='\n', encoding='utf-8') as file:
        file.write(FILE_HEADER)
        yaml.safe_dump(entries, file, sort_keys=False, allow_unicode=True, width=110)
    print(f'wrote {len(entries)} entries to {args.output}')


if __name__ == '__main__':
    main(sys.argv[1:])

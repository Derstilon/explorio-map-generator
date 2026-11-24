import contextlib
import io
import json
import os
import subprocess
import sys
from pathlib import Path

from main import generate

ROOT = Path(__file__).parent.parent


def fingerprint(G):
    """Graph structure and generated attributes as JSON, without the icon images."""
    def plain(value):
        if isinstance(value, set):
            return sorted(value)
        if isinstance(value, list):
            return value
        return str(value) if value is not None else None
    nodes = {node: {key: plain(value) for key, value in sorted(data.items()) if key != 'image'}
             for node, data in G.nodes(data=True)}
    edges = sorted([u, v, data['mode']] for u, v, data in G.edges(data=True))
    return json.dumps({'nodes': dict(sorted(nodes.items())), 'edges': edges}, sort_keys=True)


def quiet_generate(seed, steps=9):
    with contextlib.redirect_stdout(io.StringIO()):
        return generate(seed, steps)


def test_same_seed_gives_the_same_graph():
    assert fingerprint(quiet_generate(42)) == fingerprint(quiet_generate(42))


def test_different_seeds_give_different_graphs():
    assert len({fingerprint(quiet_generate(seed)) for seed in range(5)}) > 1


def test_same_seed_gives_the_same_graph_across_hash_seeds():
    """Set and dict iteration of strings depends on PYTHONHASHSEED; the graph must not."""
    script = (
        'import contextlib, io, sys; sys.path.insert(0, ".")\n'
        'from tests.test_determinism import fingerprint\n'
        'from main import generate\n'
        'with contextlib.redirect_stdout(io.StringIO()):\n'
        '    G = generate(42, 9)\n'
        'print(fingerprint(G))\n'
    )
    outputs = set()
    for hash_seed in ('1', '2', '3'):
        env = {**os.environ, 'PYTHONHASHSEED': hash_seed, 'MPLBACKEND': 'Agg'}
        result = subprocess.run([sys.executable, '-c', script], cwd=ROOT, env=env,
                                capture_output=True, text=True, check=True)
        outputs.add(result.stdout)
    assert len(outputs) == 1

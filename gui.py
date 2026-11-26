"""Local web GUI for the story-graph generator.

Run `python gui.py` and the page opens in the browser. The server only listens
on 127.0.0.1. Endpoints:
- GET /                 the page (web/index.html)
- GET /<file>           static files from web/
- GET /api/productions  production names, sheet numbers, roles and descriptions
- GET /api/derive?seed=42&steps=9&w_P1a=1&w_P2a=0&env=1&enc=1
                        derivation frames and export JSON (see story_export.derive)
"""
import argparse
import json
import math
import mimetypes
import sys
import threading
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from main import PRODUCTIONS
from story_export import derive

WEB_ROOT = (Path(__file__).parent / 'web').resolve()
MAX_STEPS = 200


def derive_params(query: dict) -> dict:
    """Parse /api/derive query parameters; raise ValueError on bad input."""
    def one(name, default):
        return query.get(name, [default])[0]
    seed = int(one('seed', '0'))
    steps = int(one('steps', '9'))
    if not 0 <= steps <= MAX_STEPS:
        raise ValueError(f'steps must be between 0 and {MAX_STEPS}')
    weights = {name: float(one(f'w_{name}', '1')) for name in PRODUCTIONS}
    if any(not math.isfinite(weight) or weight < 0 for weight in weights.values()) or not any(weights.values()):
        raise ValueError('weights must be finite and >= 0, and at least one must be positive')
    return {
        'seed': seed,
        'steps': steps,
        'weights': weights,
        'environment_biomes': one('env', '1') == '1',
        'encounter_biomes': one('enc', '1') == '1',
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def send_body(self, status, body: bytes, content_type: str):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, payload):
        self.send_body(status, json.dumps(payload).encode(), 'application/json')

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == '/api/productions':
            self.send_json(HTTPStatus.OK, [{'name': name, 'number': production.number, 'role': production.role,
                                            'description': production.description}
                                           for name, production in PRODUCTIONS.items()])
            return
        if url.path == '/api/derive':
            try:
                params = derive_params(parse_qs(url.query))
            except ValueError as error:
                self.send_json(HTTPStatus.BAD_REQUEST, {'error': str(error)})
                return
            self.send_json(HTTPStatus.OK, derive(**params))
            return
        relative = 'index.html' if url.path in ('', '/') else url.path.lstrip('/')
        target = (WEB_ROOT / relative).resolve()
        if not target.is_relative_to(WEB_ROOT) or not target.is_file():
            self.send_json(HTTPStatus.NOT_FOUND, {'error': 'not found'})
            return
        content_type = mimetypes.guess_type(target.name)[0] or 'application/octet-stream'
        self.send_body(HTTPStatus.OK, target.read_bytes(), content_type)


def make_server(port: int) -> HTTPServer:
    return HTTPServer(('127.0.0.1', port), Handler)


def main(argv):
    parser = argparse.ArgumentParser(description='Interactive GUI for the Explorio story-graph generator.')
    parser.add_argument('--port', type=int, default=8765, help='port on 127.0.0.1 (default 8765, 0 = any free port)')
    parser.add_argument('--no-browser', action='store_true', help='do not open the browser')
    args = parser.parse_args(argv)
    server = make_server(args.port)
    url = f'http://127.0.0.1:{server.server_address[1]}/'
    print(f'Explorio generator GUI on {url} (Ctrl+C to stop)')
    if not args.no_browser:
        threading.Timer(0.5, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main(sys.argv[1:])

import json
import threading
import urllib.error
import urllib.request

import pytest

from gui import derive_params, make_server


@pytest.fixture(scope='module')
def base_url():
    server = make_server(0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f'http://127.0.0.1:{server.server_address[1]}'
    server.shutdown()
    server.server_close()


def get(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.status, response.headers['Content-Type'], response.read()


def test_derive_params_defaults_and_parsing():
    assert derive_params({}) == {'seed': 0, 'steps': 9, 'weights': {'L1': 1.0, 'L2': 1.0},
                                 'environment_biomes': True, 'encounter_biomes': True}
    params = derive_params({'seed': ['7'], 'steps': ['3'], 'w_L1': ['0'], 'env': ['0']})
    assert params['seed'] == 7 and params['steps'] == 3 and params['weights']['L1'] == 0
    assert params['environment_biomes'] is False


@pytest.mark.parametrize('query', [{'steps': ['-1']}, {'steps': ['999']}, {'w_L1': ['0'], 'w_L2': ['0']},
                                   {'w_L1': ['-2']}, {'seed': ['abc']}, {'w_L1': ['inf']}, {'w_L1': ['nan']},
                                   {'w_L1': ['1e309'], 'w_L2': ['1e309']}])
def test_derive_params_rejects_bad_input(query):
    with pytest.raises(ValueError):
        derive_params(query)


def test_page_and_vendored_scripts_are_served(base_url):
    status, content_type, body = get(f'{base_url}/')
    assert status == 200 and content_type.startswith('text/html') and b'app.js' in body
    for path in ('/app.js', '/style.css', '/vendor/cytoscape-3.30.4.min.js', '/vendor/dagre-0.8.5.min.js'):
        assert get(base_url + path)[0] == 200


def test_paths_outside_web_root_are_refused(base_url):
    with pytest.raises(urllib.error.HTTPError) as error:
        get(f'{base_url}/../main.py')
    assert error.value.code == 404


def test_api_derive_returns_frames(base_url):
    status, content_type, body = get(f'{base_url}/api/derive?seed=42&steps=5')
    payload = json.loads(body)
    assert status == 200 and content_type == 'application/json'
    assert payload['seed'] == 42 and payload['productions_applied'] == 5
    assert payload['frames'][0]['title'] == 'Seed graph'


@pytest.mark.parametrize('query, mentions', [('steps=-3', 'steps'), ('w_L1=inf', 'finite'), ('w_L1=nan', 'finite')])
def test_api_derive_reports_bad_parameters(base_url, query, mentions):
    with pytest.raises(urllib.error.HTTPError) as error:
        get(f'{base_url}/api/derive?{query}')
    assert error.value.code == 400 and mentions in json.loads(error.value.read())['error']


def test_api_productions_lists_names_and_descriptions(base_url):
    productions = json.loads(get(f'{base_url}/api/productions')[2])
    assert [production['name'] for production in productions] == ['L1', 'L2']
    assert all(production['description'] for production in productions)

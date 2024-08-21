import pytest
from src import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_server_is_running(client):
    print(client)
    response = client.get('/v1/healthz')
    print(response)
    assert response.status_code == 200
    json_response = response.json
    assert 'status' in json_response
    assert json_response['status'] == 'healthy'

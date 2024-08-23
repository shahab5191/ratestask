import time
import pytest
from src import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def wait_for_database(client, max_retries=5, delay=5):
    for _ in range(max_retries):
        try:
            response = client.get("/v1/healthz")
            if response.status_code == 200:
                return
        except Exception:
            print(f"Exeption happend trying to connect to database, retrying...")

        print(f"Database not ready, retrying in {delay} seconds...")
        time.sleep(delay)
    raise Exception("Database not ready after waiting")

def test_server_is_running(client):
    wait_for_database(client)
    response = client.get('/v1/healthz')
    assert response.status_code == 200
    json_response = response.json
    assert 'status' in json_response
    assert json_response['status'] == 'healthy'

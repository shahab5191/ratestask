import os
import pytest


def pytest_configure(config):
    os.environ["ENV"] = "TESTING"


@pytest.fixture(scope="module")
def client():
    from src import create_app
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


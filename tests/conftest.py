import os


def pytest_configure(config):
    os.environ["ENV"] = "TESTING"

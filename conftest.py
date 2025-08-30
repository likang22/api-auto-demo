# conftest.py
import pytest, requests

@pytest.fixture(scope="session")
def session():
    sess = requests.Session()
    return sess
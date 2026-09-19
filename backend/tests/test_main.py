import pytest
from fastapi.testclient import TestClient

from main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def client():
    return TestClient(app)


def test_root_status_code(client):
    response = client.get("/")

    assert response.status_code == 200


def test_root_response(client):
    response = client.get("/")

    assert response.json() == {"message": "Backend funcionando!"}


@pytest.mark.parametrize(
    "endpoint",
    ["/", "/?teste=1", "/?teste=abc"]
)
def test_root_with_query_params(client, endpoint):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json()["message"] == "Backend funcionando!"


def test_root_method_not_allowed(client):
    response = client.post("/")

    assert response.status_code == 405


def test_nonexistent_endpoint(client):
    response = client.get("/endpoint-inexistente")

    assert response.status_code == 404
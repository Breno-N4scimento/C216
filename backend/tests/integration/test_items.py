import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services import items as items_service

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_items(monkeypatch):
    monkeypatch.setattr(items_service, "_items", {})
    monkeypatch.setattr(items_service, "_next_id", 1)


def test_list_items():
    response = client.get("/items")

    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    response = client.post(
        "/items",
        json={
            "name": "Notebook",
            "description": "Notebook para estudos",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Notebook",
        "description": "Notebook para estudos",
    }


def test_get_item_by_id():
    created = client.post(
        "/items",
        json={"name": "Mouse", "description": "Mouse sem fio"},
    )

    item_id = created.json()["id"]
    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Mouse"


def test_get_nonexistent_item():
    response = client.get("/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item não encontrado"


def test_create_item_invalid():
    response = client.post(
        "/items",
        json={"name": ""},
    )

    assert response.status_code == 422
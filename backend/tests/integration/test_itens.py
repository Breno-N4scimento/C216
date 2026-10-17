def test_list_items(client):
    response = client.get("/items")

    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client):
    response = client.post(
        "/items",
        json={
            "name": "Notebook",
            "description": "Notebook para estudos",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data["id"], int)
    assert data["name"] == "Notebook"
    assert data["description"] == "Notebook para estudos"


def test_get_item_by_id(client):
    created = client.post(
        "/items",
        json={
            "name": "Mouse",
            "description": "Mouse sem fio",
        },
    )

    assert created.status_code == 201

    item_id = created.json()["id"]

    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["id"] == item_id
    assert response.json()["name"] == "Mouse"
    assert response.json()["description"] == "Mouse sem fio"


def test_get_nonexistent_item(client):
    response = client.get("/items/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item não encontrado"


def test_create_item_invalid(client):
    response = client.post(
        "/items",
        json={"name": ""},
    )

    assert response.status_code == 422

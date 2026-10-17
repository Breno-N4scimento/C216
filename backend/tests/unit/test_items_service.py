import pytest

from app.schemas.items import ItemCreate, ItemUpdate
from app.services import items


@pytest.fixture(autouse=True)
def reset_items(monkeypatch):
    monkeypatch.setattr(items, "_items", {})
    monkeypatch.setattr(items, "_next_id", 1)


def test_create_item():
    item = items.create_item(
        ItemCreate(name="Notebook", description="Para estudos")
    )

    assert item.id == 1
    assert item.name == "Notebook"


def test_get_item_by_id():
    created = items.create_item(ItemCreate(name="Mouse"))

    result = items.get_item_by_id(created.id)

    assert result == created


def test_update_item():
    created = items.create_item(ItemCreate(name="Mouse"))

    updated = items.update_item(
        created.id,
        ItemUpdate(name="Teclado", description="Mecânico"),
    )

    assert updated is not None
    assert updated.name == "Teclado"


def test_patch_item():
    created = items.create_item(
        ItemCreate(name="Mouse", description="Com fio")
    )

    updated = items.patch_item(created.id, {"name": "Mouse sem fio"})

    assert updated is not None
    assert updated.name == "Mouse sem fio"
    assert updated.description == "Com fio"


def test_delete_item():
    created = items.create_item(ItemCreate(name="Mouse"))

    result = items.delete_item(created.id)

    assert result is True
    assert items.get_item_by_id(created.id) is None
from unittest.mock import MagicMock, patch

from app.models.item import Item
from app.schemas.items import ItemCreate, ItemPatch, ItemUpdate
from app.services import items


def create_mock_item(
    item_id: int = 1,
    name: str = "Mouse",
    description: str | None = None,
) -> Item:
    """Cria um item simulado para os testes unitários."""
    return Item(
        id=item_id,
        name=name,
        description=description,
    )


@patch("app.services.items.item_repository.create")
def test_create_item(mock_create):
    mock_create.return_value = create_mock_item(
        name="Notebook",
        description="Para estudos",
    )

    result = items.create_item(
        MagicMock(),
        ItemCreate(name="Notebook", description="Para estudos"),
    )

    assert result.id == 1
    assert result.name == "Notebook"
    mock_create.assert_called_once()


@patch("app.services.items.item_repository.get_by_id")
def test_get_item_by_id(mock_get_by_id):
    mock_get_by_id.return_value = create_mock_item()

    result = items.get_item_by_id(MagicMock(), 1)

    assert result is not None
    assert result.id == 1
    assert result.name == "Mouse"
    mock_get_by_id.assert_called_once()


@patch("app.services.items.item_repository.update")
def test_update_item(mock_update):
    mock_update.return_value = create_mock_item(
        name="Teclado",
        description="Mecânico",
    )

    result = items.update_item(
        MagicMock(),
        1,
        ItemUpdate(name="Teclado", description="Mecânico"),
    )

    assert result is not None
    assert result.name == "Teclado"
    mock_update.assert_called_once()


@patch("app.services.items.item_repository.patch")
def test_patch_item(mock_patch):
    mock_patch.return_value = create_mock_item(
        name="Mouse sem fio",
        description="Com fio",
    )

    result = items.patch_item(
        MagicMock(),
        1,
        ItemPatch(name="Mouse sem fio"),
    )

    assert result is not None
    assert result.name == "Mouse sem fio"
    assert result.description == "Com fio"
    mock_patch.assert_called_once()


@patch("app.services.items.item_repository.get_by_id")
def test_get_item_by_id_not_found(mock_get_by_id):
    mock_get_by_id.return_value = None

    result = items.get_item_by_id(MagicMock(), 999)

    assert result is None


@patch("app.services.items.item_repository.delete")
def test_delete_item(mock_delete):
    mock_delete.return_value = True

    result = items.delete_item(MagicMock(), 1)

    assert result is True
    mock_delete.assert_called_once()


@patch("app.services.items.item_repository.delete")
def test_delete_item_not_found(mock_delete):
    mock_delete.return_value = False

    result = items.delete_item(MagicMock(), 999)

    assert result is False
    mock_delete.assert_called_once()

from sqlalchemy.orm import Session

from app.repositories import item_repository
from app.schemas.items import ItemCreate, ItemPatch, ItemResponse, ItemUpdate


def get_all_items(db: Session) -> list[ItemResponse]:
    items = item_repository.get_all(db)

    return [ItemResponse.model_validate(item) for item in items]


def get_item_by_id(db: Session, item_id: int) -> ItemResponse | None:
    item = item_repository.get_by_id(db, item_id)

    if item is None:
        return None

    return ItemResponse.model_validate(item)


def create_item(db: Session, item_data: ItemCreate) -> ItemResponse:
    item = item_repository.create(db, item_data)

    return ItemResponse.model_validate(item)


def update_item(
    db: Session,
    item_id: int,
    item_data: ItemUpdate,
) -> ItemResponse | None:
    item = item_repository.update(db, item_id, item_data)

    if item is None:
        return None

    return ItemResponse.model_validate(item)


def patch_item(
    db: Session,
    item_id: int,
    item_data: ItemPatch,
) -> ItemResponse | None:
    item = item_repository.patch(db, item_id, item_data)

    if item is None:
        return None

    return ItemResponse.model_validate(item)


def delete_item(db: Session, item_id: int) -> bool:
    return item_repository.delete(db, item_id)

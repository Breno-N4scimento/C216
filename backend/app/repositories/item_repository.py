from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.items import ItemCreate, ItemPatch, ItemUpdate


def get_all(db: Session) -> list[Item]:
    statement = select(Item).order_by(Item.id)
    return list(db.scalars(statement).all())


def get_by_id(db: Session, item_id: int) -> Item | None:
    return db.get(Item, item_id)


def create(db: Session, item_data: ItemCreate) -> Item:
    item = Item(**item_data.model_dump())

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def update(
    db: Session,
    item_id: int,
    item_data: ItemUpdate,
) -> Item | None:
    item = get_by_id(db, item_id)

    if item is None:
        return None

    item.name = item_data.name
    item.description = item_data.description

    db.commit()
    db.refresh(item)

    return item


def patch(
    db: Session,
    item_id: int,
    item_data: ItemPatch,
) -> Item | None:
    item = get_by_id(db, item_id)

    if item is None:
        return None

    changes = item_data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)

    return item


def delete(db: Session, item_id: int) -> bool:
    item = get_by_id(db, item_id)

    if item is None:
        return False

    db.delete(item)
    db.commit()

    return True

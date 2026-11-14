from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.items import (
    ItemCreate,
    ItemPatch,
    ItemResponse,
    ItemUpdate,
)
from app.services.items import (
    create_item,
    delete_item,
    get_all_items,
    get_item_by_id,
    patch_item,
    update_item,
)

router = APIRouter(prefix="/items", tags=["Items"])

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[ItemResponse])
def list_items(db: DatabaseSession):
    return get_all_items(db)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: Annotated[int, Path(gt=0)],
    db: DatabaseSession,
):
    item = get_item_by_id(db, item_id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

    return item


@router.post(
    "",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_item(
    item_data: ItemCreate,
    db: DatabaseSession,
):
    return create_item(db, item_data)


@router.put("/{item_id}", response_model=ItemResponse)
def replace_item(
    item_id: Annotated[int, Path(gt=0)],
    item_data: ItemUpdate,
    db: DatabaseSession,
):
    item = update_item(db, item_id, item_data)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

    return item


@router.patch("/{item_id}", response_model=ItemResponse)
def partially_update_item(
    item_id: Annotated[int, Path(gt=0)],
    item_data: ItemPatch,
    db: DatabaseSession,
):
    item = patch_item(db, item_id, item_data)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

    return item


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_item(
    item_id: Annotated[int, Path(gt=0)],
    db: DatabaseSession,
):
    deleted = delete_item(db, item_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

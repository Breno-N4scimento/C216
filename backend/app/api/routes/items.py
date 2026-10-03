from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

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


@router.get("", response_model=list[ItemResponse])
def list_items():
    return get_all_items()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: Annotated[int, Path(gt=0)]
):
    item = get_item_by_id(item_id)

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
def add_item(item_data: ItemCreate):
    return create_item(item_data)


@router.put("/{item_id}", response_model=ItemResponse)
def replace_item(
    item_id: Annotated[int, Path(gt=0)],
    item_data: ItemUpdate,
):
    item = update_item(item_id, item_data)

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
):
    item = patch_item(
        item_id,
        item_data.model_dump(exclude_unset=True),
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(
    item_id: Annotated[int, Path(gt=0)]
):
    deleted = delete_item(item_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )

    return None
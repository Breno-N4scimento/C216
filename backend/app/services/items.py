from app.schemas.items import ItemCreate, ItemResponse, ItemUpdate

_items: dict[int, ItemResponse] = {}
_next_id = 1


def get_all_items() -> list[ItemResponse]:
    return list(_items.values())


def get_item_by_id(item_id: int) -> ItemResponse | None:
    return _items.get(item_id)


def create_item(item_data: ItemCreate) -> ItemResponse:
    global _next_id

    item = ItemResponse(
        id=_next_id,
        name=item_data.name,
        description=item_data.description,
    )

    _items[_next_id] = item
    _next_id += 1

    return item


def update_item(item_id: int, item_data: ItemUpdate) -> ItemResponse | None:
    if item_id not in _items:
        return None

    item = ItemResponse(
        id=item_id,
        name=item_data.name,
        description=item_data.description,
    )

    _items[item_id] = item
    return item


def patch_item(item_id: int, item_data: dict) -> ItemResponse | None:
    item = _items.get(item_id)

    if item is None:
        return None

    updated_data = item.model_dump()
    updated_data.update(item_data)

    updated_item = ItemResponse(**updated_data)
    _items[item_id] = updated_item

    return updated_item


def delete_item(item_id: int) -> bool:
    if item_id not in _items:
        return False

    del _items[item_id]
    return True
from app.schemas import Item, ItemCreate

_items: dict[int, Item] = {}
_next_id: int = 1


def create(data: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, **data.model_dump())
    _items[_next_id] = item
    _next_id += 1
    return item


def list_all() -> list[Item]:
    return list(_items.values())


def get(item_id: int) -> Item | None:
    return _items.get(item_id)


def update(item_id: int, data: ItemCreate) -> Item | None:
    if item_id not in _items:
        return None
    item = Item(id=item_id, **data.model_dump())
    _items[item_id] = item
    return item


def delete(item_id: int) -> bool:
    if item_id not in _items:
        return False
    del _items[item_id]
    return True

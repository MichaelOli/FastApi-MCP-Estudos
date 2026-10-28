from fastapi import APIRouter, HTTPException

from app.schemas import Item, ItemCreate
from app.services import items as item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", status_code=201, response_model=Item)
async def create_item(data: ItemCreate) -> Item:
    return item_service.create(data)


@router.get("", response_model=list[Item])
async def list_items() -> list[Item]:
    return item_service.list_all()


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    item = item_service.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, data: ItemCreate) -> Item:
    item = item_service.update(item_id, data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    if not item_service.delete(item_id):
        raise HTTPException(status_code=404, detail="Item não encontrado")

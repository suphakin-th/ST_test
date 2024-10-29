from typing import List
from tortoise.exceptions import DoesNotExist
from app.models import Item, ItemCreate, ItemUpdate
from fastapi import HTTPException

async def create_item(item_data: ItemCreate) -> Item:
    item = await Item.create(**item_data.dict())
    return item

async def get_item(item_id: int) -> Item:
    try:
        item = await Item.get(id=item_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

async def get_items() -> List[Item]:
    return await Item.all()

async def update_item(item_id: int, item_data: ItemUpdate) -> Item:
    item = await get_item(item_id)
    await item.update_from_dict(item_data.dict()).save()
    return item

async def delete_item(item_id: int):
    item = await get_item(item_id)
    await item.delete()

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/items", json={"name": "Item 1", "description": "This is item 1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"

@pytest.mark.asyncio
async def test_read_items():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_read_item():
    item_id = 1  # Adjust based on your item creation logic
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(f"/items/{item_id}")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_item():
    item_id = 1  # Adjust based on your item creation logic
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.put(f"/items/{item_id}", json={"name": "Updated Item", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

@pytest.mark.asyncio
async def test_delete_item():
    item_id = 1  # Adjust based on your item creation logic
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/items/{item_id}")
    assert response.status_code == 200

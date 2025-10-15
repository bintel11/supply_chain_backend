# app/tests/unit/test_inventory.py
import pytest

@pytest.mark.asyncio
async def test_create_inventory_item(client):
    response = await client.post("/api/v1/inventory/", json={
        "name": "Widget A",
        "quantity": 100,
        "location_id": 1
    })
    assert response.status_code in [200, 201]
    assert response.json()["data"]["name"] == "Widget A"

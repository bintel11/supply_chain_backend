# app/tests/automation/test_load_stress.py
import pytest
import asyncio

@pytest.mark.asyncio
async def test_load_stress(client):
    tasks = [client.get("/api/v1/orders/") for _ in range(50)]
    responses = await asyncio.gather(*tasks)
    assert all(r.status_code == 200 for r in responses)

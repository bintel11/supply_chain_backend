# app/tests/automation/test_response_time.py
import pytest
import time

@pytest.mark.asyncio
async def test_response_time(client):
    start = time.time()
    await client.get("/api/v1/inventory/")
    assert (time.time() - start) < 1.5  # less than 1.5 seconds

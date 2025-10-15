# app/tests/unit/test_tracking.py
import pytest

@pytest.mark.asyncio
async def test_tracking_event(client):
    response = await client.get("/api/v1/tracking/events")
    assert response.status_code == 200

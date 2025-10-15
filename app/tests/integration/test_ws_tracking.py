# app/tests/integration/test_ws_tracking.py
import pytest

@pytest.mark.asyncio
async def test_websocket_tracking(client):
    async with client.websocket_connect("/api/v1/tracking/ws") as websocket:
        await websocket.send_text("status")
        data = await websocket.receive_text()
        assert "tracking" in data.lower()

# app/tests/unit/test_robotics.py
import pytest

@pytest.mark.asyncio
async def test_robot_command(client):
    response = await client.post("/api/v1/robotics/command", json={"command": "move", "robot_id": 1})
    assert response.status_code in [200, 202]

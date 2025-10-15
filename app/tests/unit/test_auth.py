# app/tests/unit/test_auth.py
import pytest

@pytest.mark.asyncio
async def test_register_and_login(client):
    # Register
    response = await client.post("/api/v1/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "Password1"
    })
    assert response.status_code == 200

    # Login
    response = await client.post("/api/v1/auth/login", data={
        "username": "testuser",
        "password": "Password1"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

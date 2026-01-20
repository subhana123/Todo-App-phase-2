import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_register_user(client):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    
    response = client.post("/api/v1/register", json=user_data)
    assert response.status_code == 200
    
    created_user = response.json()
    assert created_user["username"] == "testuser"
    assert created_user["email"] == "test@example.com"


def test_login_user(client):
    # First register a user
    user_data = {
        "username": "loginuser",
        "email": "login@example.com",
        "password": "testpassword"
    }
    
    client.post("/api/v1/register", json=user_data)
    
    # Then try to login
    login_data = {
        "grant_type": "",
        "username": "loginuser",
        "password": "testpassword",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
    
    response = client.post("/api/v1/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
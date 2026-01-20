import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Todo API"}


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_and_get_todo(client):
    # Test creating a todo
    todo_data = {
        "title": "Test Todo",
        "description": "This is a test todo item",
        "completed": False
    }
    
    response = client.post("/api/v1/", json=todo_data)
    assert response.status_code == 200
    
    created_todo = response.json()
    assert created_todo["title"] == "Test Todo"
    assert created_todo["description"] == "This is a test todo item"
    assert created_todo["completed"] is False
    
    # Get the created todo by ID
    todo_id = created_todo["id"]
    response = client.get(f"/api/v1/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
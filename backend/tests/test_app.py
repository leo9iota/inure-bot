import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root_endpoint():
    """Test that the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Welcome to Inure Bot API"

def test_health_check():
    """Test that the health check endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
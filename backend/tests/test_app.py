from app.main import app
from fastapi.testclient import TestClient
from typing import Dict

client: TestClient = TestClient(app)


def test_root_endpoint() -> None:
    """Test that the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    response_json: Dict[str, str] = response.json()
    assert "message" in response_json
    assert response_json["message"] == "Welcome to Inure Bot API"


def test_health_check() -> None:
    """Test that the health check endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    response_json: Dict[str, str] = response.json()
    assert response_json == {"status": "healthy"}

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_problems():
    response = client.get("/api/problems")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2
    assert data[0]["title"] == "Design a Parking Lot"

def test_submit_solution():
    payload = {
        "problem_id": 1,
        "code": "class ParkingLot:\n    def __init__(self, levels):\n        pass"
    }
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "COMPLETED"
    assert "solid_score" in data
    assert "feedback_notes" in data
    # Store attempt ID for later verification
    attempt_id = data["attempt_id"]
    # Verify that the attempt appears in the attempts list
    attempts_response = client.get("/api/attempts")
    assert attempts_response.status_code == 200
    attempts = attempts_response.json()
    assert any(att["attempt_id"] == attempt_id for att in attempts)

def test_get_attempts_initially_empty():
    # Ensure the attempts list is empty before any submissions in a fresh test client
    fresh_client = TestClient(app)
    response = fresh_client.get("/api/attempts")
    assert response.status_code == 200
    attempts = response.json()
    assert isinstance(attempts, list)
    assert len(attempts) == 0

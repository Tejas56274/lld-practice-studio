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

def test_attempt_history_flow():
    # Submit a new solution to generate an attempt record
    payload = {
        "problem_id": 2,
        "code": "class ElevatorSystem:\n    def __init__(self, floors):\n        pass"
    }
    submit_resp = client.post("/api/submit", json=payload)
    assert submit_resp.status_code == 200
    submit_data = submit_resp.json()
    attempt_id = submit_data["attempt_id"]

    # Retrieve the attempts list and verify the new attempt is present
    attempts_resp = client.get("/api/attempts")
    assert attempts_resp.status_code == 200
    attempts = attempts_resp.json()
    assert any(att["attempt_id"] == attempt_id for att in attempts)

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

def test_attempt_history_after_submission():
    # Submit a solution first
    payload = {
        "problem_id": 2,
        "code": "class ElevatorSystem:\n    def __init__(self):\n        pass"
    }
    submit_resp = client.post("/api/submit", json=payload)
    assert submit_resp.status_code == 200
    submit_data = submit_resp.json()
    attempt_id = submit_data["attempt_id"]

    # Retrieve attempts list
    attempts_resp = client.get("/api/attempts")
    assert attempts_resp.status_code == 200
    attempts = attempts_resp.json()
    # Ensure the newly created attempt is present
    matching = [a for a in attempts if a["attempt_id"] == attempt_id]
    assert matching, "Submitted attempt not found in attempts list"
    attempt = matching[0]
    assert attempt["problem_id"] == 2
    assert attempt["status"] == "COMPLETED"
    assert "solid_score" in attempt
    assert "feedback_notes" in attempt
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
    # Verify that the attempt was recorded
    attempts_resp = client.get("/api/attempts")
    assert attempts_resp.status_code == 200
    attempts = attempts_resp.json()
    assert any(att["attempt_id"] == data["attempt_id"] for att in attempts)
    # Ensure the recorded attempt matches the submitted problem and code
    recorded = next(att for att in attempts if att["attempt_id"] == data["attempt_id"])
    assert recorded["problem_id"] == payload["problem_id"]
    assert recorded["code"] == payload["code"]

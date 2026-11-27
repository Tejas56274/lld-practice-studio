from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_problems():
    response = client.get("/api/problems")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2
    assert data[0]["title"] == "Design a Parking Lot"


def test_submit_solution_and_history():
    payload = {
        "problem_id": 1,
        "code": "class ParkingLot:\n    def __init__(self, levels):\n        pass"
    }
    # Submit a solution
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "COMPLETED"
    assert "solid_score" in data
    assert "feedback_notes" in data

    # Verify that the attempt is recorded in history
    history_resp = client.get("/api/attempts")
    assert history_resp.status_code == 200
    attempts = history_resp.json()
    assert any(att["attempt_id"] == data["attempt_id"] for att in attempts)

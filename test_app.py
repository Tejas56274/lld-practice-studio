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

def test_submit_empty_code_returns_422():
    payload = {"problem_id": 1, "code": "   "}
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 422
    # Ensure the validation error mentions the code field
    assert "code" in response.text

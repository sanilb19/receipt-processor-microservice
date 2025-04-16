import json
import os
import requests
import pytest

EXAMPLES_DIR = "examples"
# Use PORT from environment, with a clear default
PORT = int(os.getenv("PORT", 8000))
API_BASE = f"http://localhost:{PORT}"

# Print the port being used for clarity
print(f"Testing API at {API_BASE}")

EXPECTED_POINTS = {
    "simple-receipt.json": 31,
    "morning-receipt.json": 15,
    "target-receipt-1.json": 28,
    "MGM-receipt.json": 109
}

def load_example_receipt(filename):
    with open(os.path.join(EXAMPLES_DIR, filename), "r") as f:
        return json.load(f)

def test_process_receipt():
    receipt_data = load_example_receipt("simple-receipt.json")
    response = requests.post(f"{API_BASE}/receipts/process", json=receipt_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_receipt_points():
    filename = "simple-receipt.json"
    receipt_data = load_example_receipt(filename)

    post_resp = requests.post(f"{API_BASE}/receipts/process", json=receipt_data)
    assert post_resp.status_code == 200
    receipt_id = post_resp.json()["id"]

    get_resp = requests.get(f"{API_BASE}/receipts/{receipt_id}/points")
    assert get_resp.status_code == 200
    points_data = get_resp.json()
    assert "points" in points_data
    assert isinstance(points_data["points"], int)

    assert points_data["points"] == EXPECTED_POINTS[filename]

@pytest.mark.parametrize("filename", [f for f in os.listdir(EXAMPLES_DIR) if f.endswith(".json")])
def test_all_receipts(filename):
    receipt_data = load_example_receipt(filename)

    post_resp = requests.post(f"{API_BASE}/receipts/process", json=receipt_data)
    assert post_resp.status_code == 200
    receipt_id = post_resp.json()["id"]

    get_resp = requests.get(f"{API_BASE}/receipts/{receipt_id}/points")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert "points" in data
    assert isinstance(data["points"], int)

    if filename in EXPECTED_POINTS:
        assert data["points"] == EXPECTED_POINTS[filename]

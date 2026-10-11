import re
import requests


def test_create_user(base_url):
    url = f"{base_url}/users"

    payload = {
        "name": "Sri Varshini",
        "email": "sri@example.com"
    }

    response = requests.post(url, json=payload)

    # Validate status code
    assert response.status_code == 201

    # Validate response time
    assert response.elapsed.total_seconds() < 5

    # Validate response body
    data = response.json()

    assert isinstance(data, dict)
    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0

    # Validate returned values
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]

    # Validate email format
    assert re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        data["email"]
    )
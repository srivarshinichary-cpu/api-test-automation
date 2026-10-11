import requests

def test_update_user(base_url):
    url = f"{base_url}/users/1"
    payload = {
        "name": "Updated User"
    }
    response = requests.put(url, json=payload, timeout=5)

# Validate status code
    assert response.status_code == 200

# Validate response time
    assert response.elapsed.total_seconds() < 5

# Validate response body
    data = response.json()

    assert isinstance(data, dict)
    assert "id" in data
    assert data["name"] == payload["name"]


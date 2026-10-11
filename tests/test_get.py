import requests


def test_get_users(base_url):
    url = f"{base_url}/users"

    response = requests.get(url, timeout=5)

    # Validate status code
    assert response.status_code == 200

    # Validate response time
    assert response.elapsed.total_seconds() < 5

    # Validate response body
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    # Validate required fields
    user = data[0]

    assert "id" in user
    assert "name" in user
    assert "email" in user

    # Validate data types
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)

    # Validate values are not empty
    assert user["name"].strip() != ""
    assert user["email"].strip() != ""
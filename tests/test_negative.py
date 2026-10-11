import pytest
import requests

@pytest.mark.parametrize("user_id", [9999, 10000, 12345])
def test_invalid_user(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)

# Validate status code
    assert response.status_code == 404

# Validate response time
    assert response.elapsed.total_seconds() < 5

# Validate error response
    data = response.json()

    assert data == {}



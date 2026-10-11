import requests

def test_delete_user(base_url):
    url = f"{base_url}/users/1"
    response = requests.delete(url)

# Validate status code
    assert response.status_code == 200

# Validate response time
    assert response.elapsed.total_seconds() < 5

# Validate response body
    assert response.text == "{}"


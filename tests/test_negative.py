import requests


def test_invalid_user():
    url = "https://jsonplaceholder.typicode.com/users/9999"

    response = requests.get(url)

    # Validate status code
    assert response.status_code == 404

    # Validate response time
    assert response.elapsed.total_seconds() < 5

    # Validate error response
    data = response.json()

    assert data == {}
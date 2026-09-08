import requests


def test_delete_user():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.delete(url)

    # Validate status code
    assert response.status_code == 200

    # Validate response time
    assert response.elapsed.total_seconds() < 5

    # Validate response body
    assert response.text == "{}"
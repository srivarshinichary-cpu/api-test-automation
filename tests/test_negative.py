import requests


def test_invalid_user():
    url = "https://jsonplaceholder.typicode.com/users/9999"

    response = requests.get(url)

    assert response.status_code == 404
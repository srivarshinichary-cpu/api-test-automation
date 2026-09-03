import requests


def test_delete_user():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.delete(url)

    assert response.status_code == 200
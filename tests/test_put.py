import requests


def test_update_user():
    url = "https://jsonplaceholder.typicode.com/users/1"

    payload = {
        "name": "Updated User"
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
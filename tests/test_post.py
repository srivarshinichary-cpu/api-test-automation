import requests


def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Sri Varshini",
        "email": "sri@example.com"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Sri Varshini"
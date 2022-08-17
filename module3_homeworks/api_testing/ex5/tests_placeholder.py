import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"


def test_get_one_posts():
    response = requests.get(base_url + "/posts/1")
    assert response.status_code == 200
    assert response.json()["userId"] == 1
    assert response.json()["id"] == 1


def test_get_all_users():
    response = requests.get(base_url + "/posts/1/comments")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_post():
    response = requests.post(base_url + "/posts")
    assert response.status_code == 201
    assert response.json()["id"] == 101


@pytest.mark.parametrize("by_params", ["posts", "users", "comments"])
def test_get_by_params(by_params):
    response = requests.get(base_url + f"/{by_params}", params=by_params)
    assert response.status_code == 200


@pytest.mark.parametrize("by_params", ["photos", "albums"])
def test_get_by_more_params(by_params):
    response = requests.get(base_url + f"/{by_params}", params=by_params)
    assert response.status_code == 200


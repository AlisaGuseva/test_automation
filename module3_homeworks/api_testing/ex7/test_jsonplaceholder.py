import requests
import pytest


@pytest.mark.parametrize("post_id", [1, 5, 100])
def test_get_post_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id


@pytest.mark.parametrize("post_id", [-1, 0, 101])
def test_get_post_id_negative(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code != 200
    data = response.json()
    assert len(data) == 0


def test_creating_resource():
    headers = {"Content-type": "application/json; charset=UTF-8"}
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, json=body)
    data = response.json()
    for i in body.keys():
        assert body[i] == data[i]


@pytest.mark.parametrize("filter_by, user_id", [
    ("posts", 1),
    ("todos", 5),
    ("albums", 3)
])
def test_filtering_resources(filter_by, user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{filter_by}?userId={user_id}")
    data = response.json()
    for i in data:
        assert i["userId"] == user_id


def test_get_albums_photo():
    albumId = 1
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums/{albumId}/photos/")
    data = response.json()
    for i in data:
        assert i["albumId"] == albumId


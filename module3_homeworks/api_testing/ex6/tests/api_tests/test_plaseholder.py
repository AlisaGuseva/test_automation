import pytest
import requests
from jsonschema import validate


def test_jsonplaceholder_200_get(base_placeholder_url):
    response = requests.get(base_placeholder_url + "posts/1")
    assert response.status_code == 200


def test_jsonplaceholder_200_del(base_placeholder_url):
    response = requests.delete(base_placeholder_url + "posts/1")
    assert response.status_code == 200


def test_jsonplaceholder_all_resourses(base_placeholder_url):
    response = requests.get(base_placeholder_url + "posts")
    assert len(response.json()) == 100


def test_add_data(base_placeholder_url):
    var_data = {"title": "test"}
    response = requests.patch(base_placeholder_url + "posts/1", var_data)
    xjson = response.json()
    assert xjson["title"] == "test"


@pytest.mark.parametrize("id_num", ["1", "5", "10"])
def test_filter(base_placeholder_url, id_num):
    response = requests.get(f"{base_placeholder_url}posts?userId={id_num}")
    j_response = response.json()
    assert (j_response[0])["userId"] == int(id_num)


@pytest.mark.parametrize("var_url", ["posts/1", "users/1", "comments/1", "albums/1", "photos/1", "todos/1"])
def test_id_validate(base_placeholder_url, var_url):
    response = requests.get(base_placeholder_url + var_url)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
        },
        "required": ["id"]
    }
    validate(response.json(), schema)

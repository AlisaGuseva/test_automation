import pytest
import requests

from jsonschema import validate


def check_200(response):
    return response.status_code == 200


url_all = 'https://dog.ceo/api/breeds/list/all'
url_random = 'https://dog.ceo/api/breeds/image/random'
url_list = 'https://dog.ceo/api/breed/{0}/list'
url_rand_img = 'https://dog.ceo/api/breeds/image/random/{0}'

schema_hard = {
    "type": "object",
    "properties": {
        "message": {
            "type": "object",
            "patternProperties": {
                "^[a-z]+$": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        }
    },
    "required": ["message", "status"]
}

schema_norm = {
    "type": "object",
    "properties": {
        "message": {
            "type": "array",
            "breed": {"type": "string"}
        },
        "status": {"type": "string"}
    },
    "required": ["message", "status"]
}

schema_simp = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["message", "status"]
}

breeds = (x for x in requests.get(url_all).json()['message'])
print(requests.get(url_all).json()['message'])


def test_validate_all():
    response = requests.get(url_all)
    assert check_200(response)
    validate(instance=response.json(), schema=schema_hard)


def test_validate_random():
    response = requests.get(url_random)
    assert check_200(response)
    validate(instance=response.json(), schema=schema_simp)


@pytest.mark.parametrize("breed", breeds)
def test_validate_breeds(breed):
    response = requests.get(url_list.format(breed))
    assert check_200(response)
    validate(instance=response.json(), schema=schema_norm)


@pytest.mark.parametrize("count", range(50))
def test_validate_rand_img(count):
    response = requests.get(url_rand_img.format(count))
    assert check_200(response)
    validate(instance=response.json(), schema=schema_norm)


@pytest.mark.parametrize("count", range(51, 1000, 50))
def test_random_max(count):
    response = requests.get(url_rand_img.format(count))
    assert check_200(response)
    assert len(response.json()['message']) == 50


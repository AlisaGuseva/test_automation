import pytest
import requests
import random
from jsonschema import validate


@pytest.mark.parametrize("param",
                         ["breeds/list/all", "breeds/image/random", "breeds/image/random/3",
                          "breed/hound/images", "breed/hound/images/random", "breed/hound/images/random/3",
                          "breed/hound/list", "breed/hound/afghan/images", "breed/hound/afghan/images/random"],
                         ids=["Full list", "Random image", "X_random images", "all the images from a breed,",
                              "dog image from a breed, e.g. hound", "image from a breed, e.g. hound",
                              "sub-breeds from a breed", "images from the sub-breed",
                              " IMAGE FROM A SUB BREED COLLECTION", ])
def test_200_dogs(base_dog_url, param):
    reader = requests.get(base_dog_url + param)
    assert reader.status_code == 200


@pytest.mark.parametrize("param",
                         ["breeds/list/all", "breeds/image/random", "breeds/image/random/3",
                          "breed/hound/images", "breed/hound/images/random", "breed/hound/images/random/3",
                          "breed/hound/list", "breed/hound/afghan/images", "breed/hound/afghan/images/random"],
                         ids=["Full list", "(status)Random image", "(status)X_random images",
                              "(status)all the images from a breed,",
                              "(status)dog image from a breed, e.g. hound", "(status)image from a breed, e.g. hound",
                              "(status)sub-breeds from a breed", "(status)images from the sub-breed",
                              "(status)IMAGE FROM A SUB BREED COLLECTION", ])
def test_status_dogs(base_dog_url, param):
    reader = requests.get(base_dog_url + param)
    j_reader = reader.json()
    assert (j_reader["status"]) == "success"


@pytest.mark.parametrize("param_url", ["breeds/image/random/", "breed/hound/images/random/"])
def test_random_count(base_dog_url, param_url):
    x = random.randint(1, 50)
    reader = requests.get(base_dog_url + param_url + (str(x)))
    j_reader = reader.json()
    assert len(j_reader["message"]) == x


@pytest.mark.parametrize("param_random",
                         ["breeds/image/random", "breed/hound/images/random", "breed/hound/afghan/images/random"])
def test_random_image(base_dog_url, param_random):
    reader1 = requests.get(base_dog_url + param_random)
    reader2 = requests.get(base_dog_url + param_random)
    assert reader1.json()["message"] != reader2.json()["message"]


@pytest.mark.parametrize("param", ["breeds/list/all"])
def test_all_dogs_schem(base_dog_url, param):
    reader = requests.get(base_dog_url + param)
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "object"
            },
            "status": {"type": "string"},
        },
        "required": ["status"]
    }
    validate(reader.json(), schema)


from lesson_6_DDT.api_schemas import DogSchemas as ds
from lesson_6_DDT.helpers import RANDOM_DOGS, RANDOM_DOG_BREED, validatejson
from lesson_6_DDT.scr.dogs.Dogs_api import DogsApi

import pytest


class TestRandomDogsImage:
    @pytest.mark.parametrize("url, number,  schema", [
        (RANDOM_DOGS, 1, ds.schema_dog_request),
        (RANDOM_DOGS, 3, ds.schema_dog_request)
    ])
    def test_random_dog_schemas_validation(self, url, number, schema):
        body = DogsApi(url=url)
        assert body.dog_request(number).status_code == 200
        assert body.dog_request(number).json().get("status") == "success"
        assert validatejson(jsondata=body.dog_request(number).json(), schema=schema), "Схема не валидна"

    @pytest.mark.parametrize("url, number, desirable_dogs", [
        (RANDOM_DOGS, 5, 5),
        (RANDOM_DOGS, 50, 50),
        (RANDOM_DOGS, 1, 1)
    ])
    def test_dogs_count_in_request(self, url, number, desirable_dogs):
        body = DogsApi(url=url)
        exists_dogs = body.dogs_len(count=number)
        assert body.dog_request(number).status_code == 200
        assert body.dog_request(number).json().get("status") == "success"
        assert exists_dogs == desirable_dogs, "Длины не равны"

    def test_check_status(self):
        body = DogsApi(url=RANDOM_DOGS)
        status = body.dog_request(5).json().get("status")
        assert status == "success"

    def test_status_code(self):
        body = DogsApi(url=RANDOM_DOGS + "/").dog_request(1)
        assert body.status_code == 404
        assert body.json().get("status") == "error"


class TestDogsByBreed:
    def test_schema_by_breed_validation(self):
        body = DogsApi(url=RANDOM_DOG_BREED)
        assert body.custom_request().status_code == 200
        assert body.custom_request().json().get("status") == "success"
        assert validatejson(jsondata=body.custom_request().json(),
                            schema=ds.schema_dog_request), "Схема не валидна"


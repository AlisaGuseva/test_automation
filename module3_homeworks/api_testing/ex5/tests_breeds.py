import pytest
import requests

base_url = "https://dog.ceo/api"


@pytest.mark.parametrize('breed', ["hound", "malamute", "corgi"])
def test_get_breeds(breed):
    images_breeds = requests.get(base_url + f"/breed/{breed}/images", params={'breads': breed})
    assert images_breeds.status_code == 200
    assert images_breeds.json()["status"] == "success"


def test_get_all_breeds_list():
    breeds_list = requests.get(base_url + "/breeds/list/all")
    assert breeds_list.status_code == 200
    assert breeds_list.json()["message"]["sheepdog"] == ["english", "shetland"]
    assert breeds_list.json()["status"] == "success"


@pytest.mark.parametrize('sub_breed', ["hound", "retriever", "setter", "spaniel"])
def test_list_all_sub_breeds(sub_breed):
    sub_breed_list = requests.get(base_url + f"/breed/{sub_breed}/list", params={'breads': sub_breed})
    assert sub_breed_list.json()["status"] == "success"
    assert sub_breed_list.status_code == 200


def test_get_sub_breeds_image():
    sub_breeds_image = requests.get(base_url + "/breed/hound/afghan/images")
    assert sub_breeds_image.json()["status"] == "success"
    assert sub_breeds_image.status_code == 200


def test_random_images_from_breed_collections():
    image_collection = requests.get(base_url + "/breed/corgi/cardigan/images/random")
    assert image_collection.json()["status"] == "success"
    assert "https://images.dog.ceo/breeds/corgi-cardigan/" in image_collection.json()["message"]
    assert image_collection.status_code == 200

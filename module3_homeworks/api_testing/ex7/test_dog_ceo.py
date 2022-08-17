import requests
import pytest


def test_get_all_breeds_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    assert response.status_code == 200
    assert not len(data["message"]) == 0


def test_get_single_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert "success" in data["status"]


@pytest.mark.parametrize("n", [1, 7, 50])
def test_get_multiple_random_images(n):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{n}")
    data = response.json()
    assert response.status_code == 200
    assert "success" in data["status"]
    assert len(data["message"]) == n


@pytest.mark.parametrize("n", [2, 49])
@pytest.mark.parametrize("breed", ["terrier", "corgi", "chihuahua"])
def test_get_multiple_random_images_by_breed(n, breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random/{n}")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) == n
    for obj in data["message"]:
        assert ("images" in obj) and (f"{breed}" in obj)


@pytest.mark.parametrize("breed, sub_breed", [
    ("bulldog", "boston"),
    ("bulldog", "english")
])
def test_get_list_all_sub_breed_images(breed, sub_breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images")
    data = response.json()
    assert response.status_code == 200

    assert not len(data["message"]) == 0
    for obj in data["message"]:
        assert "images" in obj and f"{breed}-{sub_breed}" in obj


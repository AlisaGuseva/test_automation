import requests
import pytest


def test_get_all_breweries_list():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    data = response.json()
    assert response.status_code == 200
    assert not len(data) == 0


@pytest.mark.parametrize("filter_by, value", [
    ("by_city", "san_diego"),
    ("by_dist", "38.8977,77.0365"),
    ("by_name", "cooper"),
    ("by_state", "ohio"),
    ("by_postal", "44107")
])
def test_filter_brewery_by(filter_by, value):
    params = {filter_by: value}
    response = requests.get("https://api.openbrewerydb.org/breweries", params=params)
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0


@pytest.mark.parametrize("btype", ["large", "micro", "brewpub"])
def test_filter_by_type_of_brewery(btype):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={btype}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0
    for i in data:
        assert i["brewery_type"] == btype


@pytest.mark.parametrize("brewery_id", ["madtree-brewing-cincinnati"])
def test_get_brewery(brewery_id):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert brewery_id == data["id"]


def test_search_brewery():
    query = "dog"
    response = requests.get(f"https://api.openbrewerydb.org/breweries/search?query={query}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0


import pytest
import requests
from jsonschema import validate


@pytest.mark.parametrize("filtre,city", [
    ("?by_city=san%20diego", "San Diego"),
    ("?by_city=windsor", "Windsor"),
    ("?by_city=oregon%20сity", "Oregon"),
    ("?by_city=boring", "Boring"),
])
def test_filtreses(base_breweries_url, filtre, city):
    response = requests.get(f"https://api.openbrewerydb.org/breweries{filtre}")
    jeson_response = response.json()
    for i in range(len(jeson_response)):
        assert city in (jeson_response[i])["city"]


@pytest.mark.parametrize("page", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_base_count_page(base_breweries_url, page):
    response = requests.get(f"{base_breweries_url}?page={page}")
    assert len(response.json()) == 20


@pytest.mark.parametrize("size_page", [10, 15, 20, 25, 30, 50])
def test_base_count_page(base_breweries_url, size_page):
    response = requests.get(f"{base_breweries_url}?per_page={size_page}")
    assert len(response.json()) == size_page


def test_status_code(base_breweries_url):
    response = requests.get(base_breweries_url)
    assert response.status_code == 200


def test_breweryd_list(base_breweries_url):
    response = requests.get(f"{base_breweries_url}/autocomplete?query = black")
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
        },
        "required": ["name"]
    }
    for i in response.json():
        validate(i, schema)


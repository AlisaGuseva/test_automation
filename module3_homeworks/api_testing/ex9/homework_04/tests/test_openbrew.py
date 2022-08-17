import pytest
import requests

from jsonschema import validate


def check_200(response):
    return response.status_code == 200


main_url = 'https://api.openbrewerydb.org/breweries'

possible_types = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor',
                  'closed', 'taproom']
# в документации не указан тип taproom
# сПаСиБо тЕсТаМ

schema = {
    'type': 'array',
    'properties': {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {"type": "string"},
        "address_3": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }
}


@pytest.mark.parametrize("num", range(1, 10, 2))
def test_per_page(num):
    response = requests.get(f'{main_url}?per_page={num}')
    assert check_200(response)
    assert len(response.json()) == num


def test_check_default_per_page():
    response = requests.get(f'{main_url}')
    assert check_200(response)
    assert len(response.json()) == 20


@pytest.mark.parametrize('page', range(1, 100))
def test_validation(page):
    response = requests.get(f'{main_url}?page={page}&per_page=50')
    assert check_200(response)
    validate(response.json(), schema)


@pytest.mark.parametrize('page', range(1, 100))
def test_types(page):
    num = 50
    response = requests.get(f'{main_url}?page={page}&per_page={num}')
    assert check_200(response)
    for i in range(num):
        if response.json()[i]['brewery_type'] not in possible_types:
            raise AssertionError(f"Incorrect type in {response.json()[i]['id']}")


def test_search():
    num = 50
    response = requests.get(f'{main_url}/search?query=dog&per_page={num}')
    assert check_200(response)
    validate(response.json(), schema)

    
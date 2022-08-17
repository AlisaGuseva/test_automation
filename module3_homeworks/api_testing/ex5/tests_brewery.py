import pytest
import requests

base_url = "https://api.openbrewerydb.org/breweries"


def test_get_all_brewery():
    response = requests.get(base_url)
    assert response.status_code == 200


@pytest.mark.parametrize("city", ["windsor", "pasadena", "manchester", "miami"])
def test_get_brewery_by_city(city):
    response = requests.get(base_url + f"?by_city={city}", params={'brewery': city})
    assert response.status_code == 200
    assert response.json()[0]["city"].lower() == city


@pytest.mark.parametrize("state", ["florida", "ohio", "california", "texas"])
def test_get_brewery_by_state(state):
    response = requests.get(base_url + f"?by_state={state}", params={'brewery': state})
    assert response.status_code == 200
    assert response.json()[0]["state"].lower() == state


@pytest.mark.parametrize("postal_code", ["77356", "53959-1967", "01930-2256"])
def test_get_brewery_postal_code(postal_code):
    response = requests.get(base_url + f"?by_postal={postal_code}", params={'brewery': postal_code})
    assert response.status_code == 200
    assert response.json()[0]["postal_code"] == postal_code


@pytest.mark.parametrize("by_type",
                         ["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprieter",
                          "closed"])
def test_get_brewery_by_type(by_type):
    response = requests.get(base_url + f"?by_type={by_type}", params={'brewery': by_type})
    if response.json() != []:
        assert response.json()[0]["brewery_type"] == by_type
    assert response.status_code == 200


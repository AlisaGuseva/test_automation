import requests


def test_status(url, status):
    assert requests.get(url).status_code == status


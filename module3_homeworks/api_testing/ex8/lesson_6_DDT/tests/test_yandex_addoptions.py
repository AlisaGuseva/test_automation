import requests


def test_url_and_status_code(url: str, status_code: int):
    responce = requests.get(url)
    assert responce.status_code == status_code


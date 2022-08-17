import requests


def test_check_yandex(base_url, status_code):
    response = requests.get(f"{base_url}")
    assert response.status_code == int(status_code)


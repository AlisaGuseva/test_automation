import pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru')
    parser.addoption('--status_code', default=200)


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status(request):
    return int(request.config.getoption('--status_code'))

@pytest.fixture
def request_method(request) -> requests.models.Request():
    return getattr(requests, request.config.getoption('--method'))


@pytest.fixture
def status_code(request) -> int:
    return int(request.config.getoption('--status_code'))
import pytest


@pytest.fixture
def base_dog_url():
    return "https://dog.ceo/api/"


@pytest.fixture
def base_placeholder_url():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture
def base_breweries_url():
    return "https://api.openbrewerydb.org/breweries"


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default='https://ya.ru',
        help='this use tour url'
    )

    parser.addoption(
        "--status_code",
        default=200,
        help='expected status code'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def expected_statuscode(request):
    return int(request.config.getoption('--status_code'))


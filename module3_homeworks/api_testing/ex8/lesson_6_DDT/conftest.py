import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="default url, if no other were given, is: ya.ru"
    )

    parser.addoption(
        "--status_code",
        default="200",
        choices=["200", "201", "204", "304", "400 ", "401", "404", "403", "500", "501", "502", "503", "504"],
        help="status_code params, default==200"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))


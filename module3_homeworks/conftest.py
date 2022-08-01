import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.72.130:8081/")
    parser.addoption("--drivers", default=os.path.expanduser("~/Documents/Developer/drivers"))


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    if browser_name == "chrome":
        print("chrome")
    elif browser_name == "firefox":
        print("chrome")
    else:
        print("Wrong browser")
    return browser
    browser.close()
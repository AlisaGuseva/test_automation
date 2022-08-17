import pytest
import os
import pytest
from selenium import webdriver

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
    browser=None
    if browser_name == "chrome":
        browser = 1
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f"geckodriver")
    else:
        print("Wrong browser")
    return browser
    browser.close()

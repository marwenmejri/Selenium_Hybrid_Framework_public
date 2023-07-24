import pytest

from selenium.webdriver import Firefox, Chrome, Edge


@pytest.fixture()
def setup():
    driver = Firefox()
    driver.implicitly_wait(time_to_wait=10)
    driver.maximize_window()
    return driver

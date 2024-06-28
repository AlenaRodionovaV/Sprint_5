import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

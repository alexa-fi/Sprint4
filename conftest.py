import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get("https://qa-scooter.praktikum-services.ru/order")
    yield browser
    browser.quit()
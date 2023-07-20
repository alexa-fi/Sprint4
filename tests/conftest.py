import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 8])
def question_number(request):
    return request.param

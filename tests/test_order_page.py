import allure
import pytest
from selenium.common import NoSuchWindowException

from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from page_objects.base_page import BasePage

from data import (
    get_first_name, get_second_name, get_first_lastname, get_second_lastname,
    get_first_adress, get_second_adress, get_first_metro_station, get_second_metro_station,
    get_first_number_telephone, get_second_number_telephone, get_first_date, get_second_date,
    get_first_comment, get_second_comment
)


@allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" наверху страницы')
@allure.title('Заказ самоката по кнопке "Заказать" наверху страницы')
@pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, comment", [
    (get_first_name(), get_first_lastname(), get_first_adress(), get_first_metro_station(),
     get_first_number_telephone(), get_first_date(), get_first_comment()),
    (get_second_name(), get_second_lastname(), get_second_adress(), get_second_metro_station(),
     get_second_number_telephone(), get_second_date(), get_second_comment())
])
def test_first_order(browser, first_name, last_name, address, metro_station, phone_number, date, comment):
    try:
        main_page = MainPage(browser)
        main_page.agree_cookie_click()
        main_page.first_order_button_click()
        order_page = OrderPage(browser)

        order_page.fill_order_fields(first_name, last_name, address, metro_station, phone_number, date, comment)

        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

    except NoSuchWindowException:
        # If the browser window is closed or discarded, refresh the page and retry the test.
        browser.refresh()


@allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" внизу страницы')
@allure.title('Заказ самоката по кнопке "Заказать" внизу страницы')
@pytest.mark.parametrize("name, surname, address, metro_station, phone_number, date, comment", [
    (get_first_name(), get_first_lastname(), get_first_adress(), get_first_metro_station(),
     get_first_number_telephone(), get_first_date(), get_first_comment()),
    (get_second_name(), get_second_lastname(), get_second_adress(), get_second_metro_station(),
     get_second_number_telephone(), get_second_date(), get_second_comment())
])
def test_second_order(browser, name, surname, address, metro_station, phone_number, date, comment):
    main_page = MainPage(browser)
    main_page.agree_cookie_click()
    main_page.second_order_button_click()
    order_page = OrderPage(browser)

    order_page.fill_order_fields(name, surname, address, metro_station, phone_number, date, comment)

    order_page.click_order_button()
    order_page.click_yes_button()
    assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

import allure
import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from scr.data import (get_first_name, get_second_name, get_first_lastname, get_second_lastname,
                  get_first_adress, get_second_adress, get_first_metro_station, get_second_metro_station,
                  get_first_number_telephone, get_second_number_telephone, get_first_date, get_second_date,
                  get_first_comment, get_second_comment)


@allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" наверху страницы')
@allure.title('Заказ самоката по кнопке "Заказать" наверху страницы')
# ... (предыдущий код)

@pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, comment", [
    (get_first_name(), get_first_lastname(), get_first_adress(), get_first_metro_station(),
     get_first_number_telephone(), get_first_date(), get_first_comment()),
    (get_second_name(), get_second_lastname(), get_second_adress(), get_second_metro_station(),
     get_second_number_telephone(), get_second_date(), get_second_comment())
])
def test_first_order(browser, first_name, last_name, address, metro_station, phone_number, date, comment):
    browser.get('https://qa-scooter.praktikum-services.ru/')
    main_page = MainPage(browser)
    main_page.agree_cookie_click()
    main_page.first_order_button_click()
    order_page = OrderPage(browser)
    order_page.set_name(first_name)
    order_page.set_surname(last_name)
    order_page.set_address(address)
    order_page.set_metro_station(metro_station)
    order_page.set_phone_number(phone_number)
    order_page.click_next_button()

    order_page.set_date(date)
    order_page.set_rental_period()
    order_page.click_black_checkbox()
    order_page.set_comment(comment)
    order_page.click_order_button()
    order_page.click_yes_button()
    assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

# ... (остальной код)

@allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" внизу страницы')
@allure.title('Заказ самоката по кнопке "Заказать" внизу страницы')
@pytest.mark.parametrize("name, surname, address, metro_station, phone_number, date, comment", [
    (get_first_name(), get_first_lastname(), get_first_adress(), get_first_metro_station(),
     get_first_number_telephone(), get_first_date(), get_first_comment()),
    (get_second_name(), get_second_lastname(), get_second_adress(), get_second_metro_station(),
     get_second_number_telephone(), get_second_date(), get_second_comment())
])
def test_second_order(browser, name, surname, address, metro_station, phone_number, date, comment):
    browser.get('https://qa-scooter.praktikum-services.ru/')
    main_page = MainPage(browser)
    main_page.agree_cookie_click()
    main_page.second_order_button_click()
    order_page = OrderPage(browser)
    order_page.set_name(name)
    order_page.set_surname(surname)
    order_page.set_address(address)
    order_page.set_metro_station(metro_station)
    order_page.set_phone_number(phone_number)
    order_page.click_next_button()

    order_page.set_date(date)
    order_page.set_rental_period()
    order_page.click_grey_checkbox()
    order_page.click_order_button()
    order_page.click_yes_button()
    assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

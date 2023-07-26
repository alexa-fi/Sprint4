import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from data import get_first_name
from data import get_second_lastname
from data import get_second_name
from data import get_first_lastname
from data import get_first_adress
from data import get_second_adress
from data import get_first_number_telephone
from data import get_second_number_telephone
from data import get_first_metro_station
from data import get_second_metro_station
from data import get_first_date
from data import get_second_date
from data import get_first_comment
from data import get_second_comment

first_name = get_first_name()
second_name = get_second_name()
first_last_name = get_first_lastname()
second_last_name = get_second_lastname()
first_adress = get_first_adress()
second_adress = get_second_adress()
first_phone_number = get_first_number_telephone()
second_phone_number = get_second_number_telephone()
first_metro_station = get_first_metro_station()
second_metro_station = get_second_metro_station()
first_date = get_first_date()
second_date = get_second_date()
first_comment = get_first_comment()
second_comment = get_second_comment()

class OrderPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Первый ввод имени')
    def set_name(self, first_name):
        self.browser.find_elements(*OrderPageLocators.inputs)[0].send_keys(first_name)

    @allure.step('Второй ввод имени')
    def set_name_2(self, second_name):
        self.browser.find_elements(*OrderPageLocators.inputs)[0].send_keys(second_name)

    @allure.step('Первый ввод фамилии')
    def set_surname(self, first_last_name):
        self.browser.find_elements(*OrderPageLocators.inputs)[1].send_keys(first_last_name)

    @allure.step('Второй ввод фамилии')
    def set_surname_2(self, second_last_name):
        self.browser.find_elements(*OrderPageLocators.inputs)[1].send_keys(second_last_name)

    @allure.step('Первый ввод адреса')
    def set_address(self, first_adress):
        self.browser.find_elements(*OrderPageLocators.inputs)[2].send_keys(first_adress)

    @allure.step('Второй ввод адреса')
    def set_address_2(self, second_adress):
        self.browser.find_elements(*OrderPageLocators.inputs)[2].send_keys(second_adress)

    @allure.step('Ввести станцию метро')
    def set_metro_station(self, first_metro_station):
        self.browser.find_element(*OrderPageLocators.metro_station_input).send_keys(first_metro_station)
        self.browser.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Ввести вторую станцию метро')
    def set_metro_station_2(self, second_metro_station):
        self.browser.find_element(*OrderPageLocators.metro_station_input).send_keys(second_metro_station)
        self.browser.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Введите номер телефона')
    def set_phone_number(self, first_phone_number):
        self.browser.find_elements(*OrderPageLocators.input_phone_locator).send_keys(first_phone_number)

    @allure.step('Введите второй номер телефона')
    def set_phone_number_2(self, second_phone_number):
        self.browser.find_elements(*OrderPageLocators.input_phone_locator)[3].send_keys(second_phone_number)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.browser.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Введите дату')
    def set_date(self, first_date):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[0].send_keys(first_date)
        self.browser.find_element(*OrderPageLocators.date_picker_selected).click()

    @allure.step('Введите вторую дату')
    def set_date_2(self, second_date):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[0].send_keys(second_date)
        self.browser.find_element(*OrderPageLocators.date_picker_selected).click()

    @allure.step('Выберите срок аренды')
    def set_rental_period(self):
        self.browser.find_element(*OrderPageLocators.dropdown_control).click()
        self.browser.find_elements(*OrderPageLocators.dropdown_option)[0].click()

    @allure.step('Выберите второй срок аренды')
    def set_rental_period_2(self):
        self.browser.find_element(*OrderPageLocators.dropdown_control).click()
        self.browser.find_elements(*OrderPageLocators.dropdown_option)[1].click()

    @allure.step('Кликнуть черный чек-бокс')
    def click_black_checkbox(self):
        self.browser.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step('Кликнуть серый чек-бокс')
    def click_grey_checkbox(self):
        self.browser.find_element(*OrderPageLocators.grey_checkbox).click()

    @allure.step('Написать комментарий')
    def set_comment(self, first_comment):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[1].send_keys(first_comment)

    @allure.step('Написать второй комментарий')
    def set_comment_2(self, second_comment):
        self.browser.find_elements(*OrderPageLocators.inputs_second_page)[1].send_keys(second_comment)

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.browser.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Нажать кнопку Да')
    def click_yes_button(self):
        self.browser.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Получить текст "Заказ оформлен"')
    def order_has_been_placed_text(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.order_has_been_placed)).text
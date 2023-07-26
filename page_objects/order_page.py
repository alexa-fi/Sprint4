import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from data import get_first_name, get_second_lastname, get_second_name, get_first_lastname
from data import get_first_adress, get_second_adress, get_first_number_telephone, get_second_number_telephone
from data import get_first_metro_station, get_second_metro_station, get_first_date, get_second_date
from data import get_first_comment, get_second_comment
from base_page import BasePage

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


class OrderPage(BasePage):

    @allure.step('Ввод значения в поле')
    def set_input_field(self, locator, value):
        input_field = self.browser.find_element(*locator)
        input_field.clear()
        input_field.send_keys(value)

    @allure.step('Ввести имя')
    def set_name(self, name):
        self.set_input_field(OrderPageLocators.locator_order_name_fild, name)

    @allure.step('Ввести фамилию')
    def set_surname(self, surname):
        self.set_input_field(OrderPageLocators.locator_order_last_name_fild, surname)

    @allure.step('Ввести адрес')
    def set_address(self, address):
        self.set_input_field(OrderPageLocators.locator_order_adress_fild, address)

    @allure.step('Ввести станцию метро')
    def set_metro_station(self, metro_station):
        self.set_input_field(OrderPageLocators.metro_station_input, metro_station)
        self.browser.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Ввести номер телефона')
    def set_phone_number(self, phone_number):
        self.set_input_field(OrderPageLocators.locator_order_phone_number_fild, phone_number)

    @allure.step('Ввести дату')
    def set_date(self, date):
        date_picker = self.set_input_field(OrderPageLocators.locator_order_date_fild, date)
        date_picker.send_keys(Keys.ENTER)

    @allure.step('Выбрать срок аренды')
    def set_rental_period(self, index=0):
        self.browser.find_element(*OrderPageLocators.dropdown_control).click()
        self.browser.find_elements(*OrderPageLocators.dropdown_option)[index].click()

    @allure.step('Кликнуть черный чек-бокс')
    def click_black_checkbox(self):
        self.browser.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step('Написать комментарий')
    def set_comment(self, comment):
        self.set_input_field(OrderPageLocators.locator_order_comments_fild, comment)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.browser.find_element(*OrderPageLocators.next_button).click()

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

    @allure.step('Заполнить поля заказа')
    def fill_order_fields(self, name, surname, address, metro_station, phone_number, date, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        self.click_next_button()
        self.set_date(date)
        self.set_rental_period()
        self.click_black_checkbox()
        self.set_comment(comment)

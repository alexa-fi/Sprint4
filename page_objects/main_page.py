import allure
from locators.main_page_locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по логотипу "Яндекс"')
    def yandex_logo_click(self):
        self.browser.find_element(*MainPageLocators.yandex_logo).click()

    @allure.step('Клик по логотипу "Самокат"')
    def scooter_logo_click(self):
        self.browser.find_element(*MainPageLocators.scooter_logo).click()

    @allure.step('Принять cookie')
    def agree_cookie_click(self):
        self.browser.find_element(*MainPageLocators.cookie_button).click()

    @allure.step('Клик по кнопке "Заказать" наверху страницы')
    def first_order_button_click(self):
        self.browser.find_elements(*MainPageLocators.order_button)[0].click()

    @allure.step('Клик по кнопке "Заказать" снизу страницы')
    def second_order_button_click(self):
        self.browser.find_elements(*MainPageLocators.order_button)[2].click()

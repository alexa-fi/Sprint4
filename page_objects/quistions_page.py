import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


class QuestionsPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Клик на первый вопрос")
    def click_first_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(MainPageLocators.first_question))
        element.click()

    @allure.step("Клик на второй вопрос")
    def click_second_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.second_question))
        element.click()

    @allure.step("Клик на третий вопрос")
    def click_third_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.third_question))
        element.click()

    @allure.step("Клик на четвёртый вопрос")
    def click_fourth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.fourth_question))
        element.click()

    @allure.step("Клик на пятый вопрос")
    def click_fifth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.fifth_question))
        element.click()

    @allure.step("Клик на шестой вопрос")
    def click_sixth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.sixth_question))
        element.click()

    @allure.step("Клик на седьмой вопрос")
    def click_seventh_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.seventh_question))
        element.click()

    @allure.step("Клик на восьмой вопрос")
    def click_eighth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.eight_question))
        element.click()

    @allure.step("Ответ на первый вопрос")
    def get_first_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(*MainPageLocators.first_answer)).text

    @allure.step("Ответ на второй вопрос")
    def get_second_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.second_answer)).text

    @allure.step("Ответ на третий вопрос")
    def get_third_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.third_answer)).text

    @allure.step("Ответ на четвертый вопрос")
    def get_fourth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.fourth_answer)).text

    @allure.step("Ответ на пятый вопрос")
    def get_fifth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.fifth_answer)).text

    @allure.step("Ответ на шестой вопрос")
    def get_sixth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.sixth_answer)).text

    @allure.step("Ответ на седьмой вопрос")
    def get_seventh_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.seventh_answer)).text

    @allure.step("Ответ на восьмой вопрос")
    def get_eighth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.eight_answer)).text
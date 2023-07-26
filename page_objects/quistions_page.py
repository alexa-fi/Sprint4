import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from base_page import BasePage


class QuestionsPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_question(self, question_locator):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.scroll_to_element(last_element)
        element = self.wait_for_element_visibility(question_locator)
        element.click()

    @allure.step("Ответ на вопрос")
    def get_answer(self, answer_locator):
        return self.wait_for_element_visibility(answer_locator).text

    @allure.step("Клик на первый вопрос")
    def click_first_question(self):
        self.click_question(MainPageLocators.first_question)

    @allure.step("Клик на второй вопрос")
    def click_second_question(self):
        self.click_question(MainPageLocators.second_question)

    @allure.step("Клик на третий вопрос")
    def click_third_question(self):
        self.click_question(MainPageLocators.third_question)

    @allure.step("Клик на четвёртый вопрос")
    def click_fourth_question(self):
        self.click_question(MainPageLocators.fourth_question)

    @allure.step("Клик на пятый вопрос")
    def click_fifth_question(self):
        self.click_question(MainPageLocators.fifth_question)

    @allure.step("Клик на шестой вопрос")
    def click_sixth_question(self):
        self.click_question(MainPageLocators.sixth_question)

    @allure.step("Клик на седьмой вопрос")
    def click_seventh_question(self):
        self.click_question(MainPageLocators.seventh_question)

    @allure.step("Клик на восьмой вопрос")
    def click_eighth_question(self):
        self.click_question(MainPageLocators.eight_question)

    @allure.step("Ответ на первый вопрос")
    def get_first_answer(self):
        return self.get_answer(MainPageLocators.first_answer)

    @allure.step("Ответ на второй вопрос")
    def get_second_answer(self):
        return self.get_answer(MainPageLocators.second_answer)

    @allure.step("Ответ на третий вопрос")
    def get_third_answer(self):
        return self.get_answer(MainPageLocators.third_answer)

    @allure.step("Ответ на четвертый вопрос")
    def get_fourth_answer(self):
        return self.get_answer(MainPageLocators.fourth_answer)

    @allure.step("Ответ на пятый вопрос")
    def get_fifth_answer(self):
        return self.get_answer(MainPageLocators.fifth_answer)

    @allure.step("Ответ на шестой вопрос")
    def get_sixth_answer(self):
        return self.get_answer(MainPageLocators.sixth_answer)

    @allure.step("Ответ на седьмой вопрос")
    def get_seventh_answer(self):
        return self.get_answer(MainPageLocators.seventh_answer)

    @allure.step("Ответ на восьмой вопрос")
    def get_eighth_answer(self):
        return self.get_answer(MainPageLocators.eight_answer)

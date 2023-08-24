import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class QuestionsPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_question(self, question_number):
        question_locator = (By.XPATH, MainPageLocators.questions.format(question_number))
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.scroll_to_element(last_element)
        element = self.wait_for_element_visibility(question_locator)
        element.click()

    @allure.step("Ответ на вопрос")
    def get_answer(self, answer_locator):
        return self.wait_for_element_visibility(answer_locator).text

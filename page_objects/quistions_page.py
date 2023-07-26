from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


class QuestionsPage:

    def __init__(self, browser):
        self.browser = browser

    def click_question(self, question_number):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        if question_number == 1:
            element = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located(MainPageLocators.first_question))
        elif question_number == 2:
            element = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located(MainPageLocators.second_question))
        elif question_number == 3:
            element = WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located(MainPageLocators.third_question))
        # Добавьте остальные вопросы здесь
        else:
            raise ValueError(f"Вопрос с номером {question_number} не найден.")
        element.click()

    def get_answer(self, question_number):
        last_element = self.browser.find_element(*MainPageLocators.eight_question)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        if question_number == 1:
            element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(MainPageLocators.first_answer))
        elif question_number == 2:
            element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(MainPageLocators.second_answer))
        elif question_number == 3:
            element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(MainPageLocators.third_answer))
        # Добавьте остальные ответы здесь
        else:
            raise ValueError(f"Вопрос с номером {question_number} не найден.")
        return element.text

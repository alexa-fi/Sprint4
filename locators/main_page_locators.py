from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainPageLocators:
    yandex_logo = [By.XPATH, '//*[contains(@class, "Header_LogoYandex")]']
    scooter_logo = [By.XPATH, '//*[contains(@class, "Header_LogoScooter")]']
    order_button = [By.XPATH, '//*[contains(@class, "Button_Button")]']
    cookie_button = [By.ID, 'rcc-confirm-button']

    first_question = [By.ID, 'accordion__heading-0']
    second_question = [By.ID, 'accordion__heading-1']
    third_question = [By.ID, 'accordion__heading-2']
    fourth_question = [By.ID, 'accordion__heading-3']
    fifth_question = [By.ID, 'accordion__heading-4']
    sixth_question = [By.ID, 'accordion__heading-5']
    seventh_question = [By.ID, 'accordion__heading-6']
    eight_question = [By.ID, 'accordion__heading-7']

    first_answer = [[By.ID, 'accordion__panel-0']]
    second_answer = [By.ID, 'accordion__panel-1']
    third_answer = [By.ID, 'accordion__panel-2']
    fourth_answer = [By.ID, 'accordion__panel-3']
    fifth_answer = [By.ID, 'accordion__panel-4']
    sixth_answer = [By.ID, 'accordion__panel-5']
    seventh_answer = [By.ID, 'accordion__panel-6']
    eight_answer = [By.ID, 'accordion__panel-7']
    question_locator = (By.XPATH, "//div[@class='faq-item']")
    answer_locator = (By.XPATH, "//div[@class='faq-item__desc']")

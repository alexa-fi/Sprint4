import allure
import pytest
from page_objects.quistions_page import QuestionsPage
from page_objects.base_page import BasePage


question_data = [
    (1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (2,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (3,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (6,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]


class TestQuestions:

    @allure.description('При клике на вопрос открывается соответствующий текст ответа')
    @allure.title('При клике на вопрос открывается соответствующий текст ответа')
    @pytest.mark.parametrize('question_number, expected_answer', question_data)
    def test_question(self, browser, question_number, expected_answer):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_question(question_number)
        assert questions_page.get_answer() == expected_answer

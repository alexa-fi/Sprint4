import allure
import sys
from page_objects.quistions_page import QuestionsPage


class TestQuestions:

    @allure.description('При клике на первый вопрос открывается текст первого вопроса')
    @allure.title('При клике на вопрос открывается текст первого вопроса')
    def test_first_question(self, browser):
        questions_page = QuestionsPage(browser)
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page.click_first_question()
        assert questions_page.get_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('При клике на второй вопрос открывается текст второго вопроса')
    @allure.title('При клике на вопрос открывается текст второго вопроса')
    def test_second_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_second_question()
        assert questions_page.get_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('При клике на третий вопрос открывается текст третьего вопроса')
    @allure.title('При клике на вопрос открывается текст третьего вопроса')
    def test_third_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_third_question()
        assert questions_page.get_third_answer() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    @allure.description('При клике на четвертый вопрос открывается текст четвертого вопроса')
    @allure.title('При клике на вопрос открывается текст четвертого вопроса')
    def test_fourth_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_fourth_question()
        assert questions_page.get_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


    @allure.description('При клике на пятый вопрос открывается текст пятого вопроса')
    @allure.title('При клике на вопрос открывается текст пятого вопроса')
    def test_fifth_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_fifth_question()
        assert questions_page.get_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('При клике на шестой вопрос открывается текст шестого вопроса')
    @allure.title('При клике на вопрос открывается текст шестого вопроса')
    def test_sixth_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_sixth_question()
        assert questions_page.get_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'


    @allure.description('При клике на седьмой вопрос открывается текст седьмого вопроса')
    @allure.title('При клике на вопрос открывается текст седьмого вопроса')
    def test_seventh_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_seventh_question()
        assert questions_page.get_seventh_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('При клике на восьмой вопрос открывается текст восьмого вопроса')
    @allure.title('При клике на вопрос открывается текст восьмого вопроса')
    def test_eighth_question(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        questions_page.click_eighth_question()
        assert questions_page.get_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
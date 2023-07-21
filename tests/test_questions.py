import allure
from page_objects.quistions_page import QuestionsPage


class TestQuestions:

    @allure.description('При клике на вопрос открывается соответствующий текст ответа')
    @allure.title('При клике на вопрос открывается соответствующий текст ответа')
    def test_question(self, browser, question_number):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        questions_page = QuestionsPage(browser)
        if question_number == 1:
            questions_page.click_first_question()
            assert questions_page.get_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        elif question_number == 2:
            questions_page.click_second_question()
            assert questions_page.get_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        elif question_number == 3:
            questions_page.click_third_question()
            assert questions_page.get_third_answer() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        elif question_number == 4:
            questions_page.click_fourth_question()
            assert questions_page.get_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        elif question_number == 5:
            questions_page.click_fifth_question()
            assert questions_page.get_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        elif question_number == 6:
            questions_page.click_sixth_question()
            assert questions_page.get_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        elif question_number == 7:
            questions_page.click_seventh_question()
            assert questions_page.get_seventh_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        elif question_number == 8:
            questions_page.click_eighth_question()
            assert questions_page.get_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

import allure
from page_objects.main_page import MainPage


class TestMainPage:

    @allure.description('При нажатии на логотип "Яндекс" в новом окне открывается главная Яндекса')
    @allure.title('Клик на логотип "Яндекс"')
    def test_yandex_logo_click(self, browser):
        main_page = MainPage(browser)
        main_page.yandex_logo_click()
        assert len(browser.window_handles) == 2

    @allure.description('При нажатии на лого "Самокат" переброс на главную Самоката')
    @allure.title('Клик на лого "Самокат"')
    def test_click_samokat_logo(self, browser):
        main_page = MainPage(browser)
        main_page.scooter_logo_click()
        assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"
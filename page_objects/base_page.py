import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def scroll_to_element(self, locator):
        element = self.browser.find_element(*locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def wait_for_element_visibility(self, locator, timeout=30):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator))

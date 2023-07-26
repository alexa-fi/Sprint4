from selenium.webdriver.common.by import By


class OrderPageLocators:

    locator_order_name_fild = (By.XPATH, '//*[@placeholder="* Имя"]')
    locator_order_last_name_fild = (By.XPATH, '//*[@placeholder="* Фамилия"]')
    locator_order_adress_fild = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]')
    metro_station_input = [By.CLASS_NAME, 'select-search__input']
    metro_station_row = [By.CLASS_NAME, 'select-search__row']
    locator_order_phone_number_fild = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    locator_order_date_fild = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]')
    inputs_second_page = (By.XPATH, "//div[contains(@class, 'Order_Content__bmtHS')]//input[contains(@class, "
                                    "'Input_Responsible__1jDKN')]")
    date_picker_selected = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    dropdown_control = [By.CLASS_NAME, 'Dropdown-control']
    dropdown_option = [By.CLASS_NAME, 'Dropdown-option']
    black_checkbox = [By.ID, 'black']
    grey_checkbox = [By.ID, 'grey']
    order_button = [By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]"]
    yes_button = [By.XPATH, "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]"]
    order_has_been_placed = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    locator_order_comments_fild = (By.XPATH, '//*[@placeholder="Комментарий для курьера"]')

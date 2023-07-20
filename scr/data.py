from selenium.webdriver.common.by import By
from typing import Dict


def get_first_name() -> Dict[str, str]:
    return {"first_name": "Имя"}


def get_second_name() -> Dict[str, str]:
    return {"second_name": 'Александр'}


def get_first_lastname() -> Dict[str, str]:
    return {'first_lastname': 'Сталин'}


def get_second_lastname() -> Dict[str, str]:
    return {'second_lastname': 'Пушкин'}


def get_first_adress() -> Dict[str, str]:
    return {'first_adress': 'Санкт-Петербург, Каменноостровский пр., д32'}


def get_second_adress() -> Dict[str, str]:
    return {'second_adress': 'Москва, Ленинский проспект, д.15'}


def get_first_metro_station() -> Dict[str, str]:
    return {'first_metro_station': 'Лу'}


def get_second_metro_station() -> Dict[str, str]:
    return {'second_metro_station': 'Динамо'}


def get_first_number_telephone() -> Dict[str, str]:
    return {'first_number_telephone' '+79216789005'}


def get_second_number_telephone() -> Dict[str, str]:
    return {'second_number_telephone': '+79119807645'}


def get_first_date() -> Dict[str, str]:
    return {'first_date': '13.08.2014'}


def get_second_date() -> Dict[str, str]:
    return {'second_date', '05.09.2023'}


def get_first_comment() -> Dict[str, str]:
    return {'first_comment', 'Нужен самокат'}


def get_second_comment() -> Dict[str, str]:
    return {'second_comment', 'Нужен самокат с прицепом'}

from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def testing_data():
    keyboard = KeyBoard('Dark Project KD87A', 9600, 5)
    return keyboard


def test_language_default(testing_data):
    """
    Проверка на то, что при инициализации по умолчанию задана англоязычная раскладка
    """
    assert testing_data.language == "EN"


def test_change_language(testing_data):
    """
    Проверка на корректность смены языка на русский
    """
    testing_data.change_lang()
    assert testing_data.language == "RU"


def test_invalid_language_assignment(testing_data):
    """
    Проверка на смену незапрограммированного языка
    """
    with pytest.raises(AttributeError):
        testing_data.language = 'CH'
        testing_data.language = 'BY'

import pytest
from src.phone import Phone


@pytest.fixture
def testing_data():
    """ Определяем тестовые данные экземпляра класса Phone """
    phone1 = Phone("Honor", 150000, 10, 2)
    return phone1


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Phone """
    assert testing_data.name == "Honor"
    assert testing_data.price == 150000
    assert testing_data.quantity == 10
    assert testing_data.number_of_sim == 2


def test_str(testing_data):
    """
    Тест проверяет корректность вывода метода str
    в формате 'object_name'
    """
    assert str(testing_data) == 'Honor'


def test_repr(testing_data):
    """
        Тест проверяет корректность вывода строки для отладки в формате
        "ClassName('object_name', object_price, object_quantity, object_num_of_sim)"
        """
    assert repr(testing_data) == "Phone('Honor', 150000, 10, 2)"


def test_number_of_sim(testing_data):
    """ Тест на неотрицательное целое число сим-карт в телефоне """
    with pytest.raises(ValueError):
        testing_data.number_of_sim = -1
        testing_data.number_of_sim = 0
        testing_data.number_of_sim = 1.2



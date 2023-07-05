from unittest import result

import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def testing_data():
    item = Item("apple", 1.0, 10)
    return item


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Item """
    assert testing_data.name == "apple"
    assert testing_data.price == 1.0
    assert testing_data.quantity == 10


def test_all_items(testing_data):
    """ Тест на проверку добавления экземпляра класса Item в список all """
    assert testing_data in Item.all


def test_init_error():
    """ Тест на проверку возникновения исключения при передаче
    некорректных типов данных в конструктор """
    with pytest.raises(TypeError):
        Item(123, 'abc', 1.0)


def test_calculate_total_price(testing_data):
    """ Тест на проверку корректности выводимого значения
    при вызове calculate_total_price  """
    assert testing_data.calculate_total_price() == 10.0


def test_apply_discount(testing_data):
    """ Тест на применение скидки при вызове self.price
    после вызова apply_discount """
    Item.pay_rate = 0.8
    testing_data.apply_discount()
    assert testing_data.price == 0.8


def test_name(testing_data):
    """
    Тест на выполнение условий вывода наименования товара
    в зависимости от количества символов
    """
    testing_data.name = 'Планшет'
    assert testing_data.name == 'Планшет'
    testing_data.name = 'Квадрокоптер'
    assert testing_data.name == 'Квадрокопт'


def test_instantiate_from_csv():
    """ Тест на соответствие содержания файла данным из списка"""
    Item.instantiate_from_csv()
    item1 = Item.all[1]
    item2 = Item.all[4]
    assert item1.name == 'Ноутбук'
    assert item2.price == 75
    assert item1.quantity == 3
    assert len(Item.all) == 5


@pytest.mark.parametrize('testing_str, results', [
    ('1', 1),
    ('3.2', 3),
    ('105.8', 105),
    ('abc', None),
    ('apple', None)
])
def test_string_to_number(testing_str, results):
    """ Тест на проверку корректности перевода строки в целое число """
    if results is not None:
        assert Item.string_to_number(testing_str) == results
    else:
        with pytest.raises(ValueError):
            Item.string_to_number(testing_str)


def test_repr(testing_data):
    """
    Тест проверяет корректность вывода строки для отладки в формате
    "ClassName('object_name', object_price, object_quantity)"
    """
    assert repr(testing_data) == "Item('apple', 1.0, 10)"


def test_str(testing_data):
    """
    Тест проверяет корректность вывода метода str
    в формате 'object_name'
    """
    assert str(testing_data) == 'apple'

@pytest.mark.parametrize('quantity1, quantity2, result', [
    (1, 4, 5),
    (100, 66, 166),
    (0, 5, 5),
])
def test_add(quantity1, quantity2, result):
    """ Тест проверяет возможность складывать количество товаров разных классов """
    class Test:
        """ Тестовый класс, который не наследуется от класса Item """
        def __init__(self, quantity):
            self.quantity = quantity

    test1 = Test(quantity2)
    item1 = Item('apple', 100, quantity1)
    phone1 = Phone('Samsung', 200, quantity2, 6)

    assert item1 + phone1 == result
    assert item1 + item1 == quantity1 * 2
    assert phone1 + phone1 == quantity2 * 2
    with pytest.raises(ValueError):
        phone1 + test1
        item1 + test1
        item1 + 10000
        phone1 + 123

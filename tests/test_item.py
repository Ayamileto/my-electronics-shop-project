import pytest
from src.item import Item


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
    """ Тест на проверку возникновения исключения при передаче некорректных типов данных в конструктор """
    with pytest.raises(TypeError):
        Item(123, 'abc', 1.0)


def test_calculate_total_price(testing_data):
    """ Тест на проверку корректности выводимого значения при вызове calculate_total_price  """
    assert testing_data.calculate_total_price() == 10.0


def test_apply_discount(testing_data):
    """ Тест на применение скидки при вызове self.price после вызова apply_discount """
    Item.pay_rate = 0.8
    testing_data.apply_discount()
    assert testing_data.price == 0.8
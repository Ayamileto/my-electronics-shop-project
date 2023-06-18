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
        Item(123, "abc", 1.0)

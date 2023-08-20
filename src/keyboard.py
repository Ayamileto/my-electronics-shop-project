from src.item import Item


class LanguageMixin:
    pass


class KeyBoard(Item, LanguageMixin):
    """ Класс для товара 'клавиатура' """
    def __init__(self, name, price, quantity):
        """
        Инициализация класса наследуется от класса Item и LanguageMixin
        """
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)



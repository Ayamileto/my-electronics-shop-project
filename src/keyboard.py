from src.item import Item


class LanguageMixin:
    """
    Класс, добавляющий метод смены языка к другим классам
    """
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """
        Метод для смены языка
        """
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class KeyBoard(Item, LanguageMixin):
    """ Класс для товара 'клавиатура' """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

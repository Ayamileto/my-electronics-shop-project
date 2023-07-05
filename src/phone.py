from src.item import Item


class Phone(Item):
    """ Класс товара категории Телефон """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = None  # Инициализируем атрибут без присваивания ему значения
        self.number_of_sim = number_of_sim  # Вызываем сеттер для проверки и установки значения


    @property
    def number_of_sim(self):
        return self._number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Проверяет переданное значения атрибуту на неотрицательное целое число иначе возвращает ValueError
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value


    def __repr__(self):
        """
                Возвращает строку для отладки в формате
                ClassName(object_name, object_price, object_quantity, number_of_sim)
                """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


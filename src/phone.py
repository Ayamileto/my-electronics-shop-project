from src.item import Item


class Phone(Item):
    """ Класс товара категории Телефон """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
                Возвращает строку для отладки в формате
                ClassName(object_name, object_price, object_quantity, number_of_sim)
                """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой')
        elif not isinstance(price, (int, float)):
            raise TypeError('Значение стоимости должно быть числом')
        elif not isinstance(quantity, int):
            raise TypeError('Количество товара должно быть целым числом')
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, value):
        """ Метод проверяет, что длина наименования товара не больше 10 символов.
        В противном случае обрезает строку (оставит первые 10 символов)."""
        if len(value) > 10:
            self.__name = value[:10]
            #raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        src_path = os.path.dirname(__file__)
        src_filename = "items.csv"
        file_path = os.path.join(src_path, src_filename)
        cls.all.clear()

        with open(file_path, newline='', encoding='windows-1251') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for item in csv_reader:
                name = item['name']
                price = cls.string_to_number(item['price'])
                quantity = cls.string_to_number(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """ Статический метод, возвращающий целое число из числа-строки """
        if '.' in string:
            number = float(string)
            return int(number)
        elif string.isdigit():
            return int(string)
        else:
            raise ValueError('Невозможно преобразовать строку в число.')


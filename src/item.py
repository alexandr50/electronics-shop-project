import csv
import os

from errors.errors import InstantiateCSVError

# from src.phone import Phone
path = os.path.dirname(__file__) + '/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @staticmethod
    def validate(value):
        """
        Проверка на длину имени
        """
        if len(value) > 10:
            raise ValueError('Длинна имени не может превышать десяти символов')

    @staticmethod
    def string_to_number(value):
        """
        Возвращает целочисленное значение из строки
        """
        res = int(float(value))
        return res

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """Добавил коментарии"""
        self.validate(value)
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Читает данные из файла и создает объекты на основе этих данных
        """
        try:
            with open(filename) as file:
                res = csv.DictReader(file)
                for i in res:
                    if list(i.keys()) == ['name', 'price', 'quantity']:
                        cls(i['name'], i['price'], i['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        # except InstantiateCSVError:
        #     raise InstantiateCSVError('Файл item.csv поврежден')

    def __str__(self):
        res = f"{self.name}"
        return res

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

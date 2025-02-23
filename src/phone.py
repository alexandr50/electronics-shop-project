from src.item import Item


class Phone(Item):
    """
    Создание экземпляра класса item.

    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
    :param number_of_sim: Количество сим карт
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.check_number_of_sim(number_of_sim)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        '''Сеттер атрибута number_of_sim'''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        '''Геттер атрибута number_of_sim'''
        self.check_number_of_sim(value)
        self.__number_of_sim = value

    @staticmethod
    def check_number_of_sim(value):
        '''Проверка количества сим на меньше 1'''
        if value <= 0:
            raise ValueError('Количество сим должно быть больше 0')
        return value

    def __repr__(self):
        class_name = str(self.__class__).split('.')[-1][:-2]
        return f"{class_name}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """Метод сложения по количеству товара"""
        if type(other) not in (Item, Phone):
            raise TypeError('arguments must be class Item or Phone')
        return self.quantity + other.quantity

    def __radd__(self, other):
        """Метод правостороннего сложения по количеству товара"""
        if type(other) not in (Item, Phone):
            raise TypeError('arguments must be class Item or Phone')
        return self.quantity + other.quantity

from src.item import Item
from src.mixins import MixinChangeLanguage


class KeyBoard(Item, MixinChangeLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)








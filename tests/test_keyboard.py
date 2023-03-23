import pytest

from src.keyboard import KeyBoard
from src.item import Item
from src.mixins import MixinChangeLanguage

@pytest.fixture
def keyboard():
    return KeyBoard('Asus', 1000, 7)

def test_init(keyboard):
    assert keyboard.name == 'Asus'
    assert keyboard.price == 1000
    assert keyboard.quantity == 7
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    with pytest.raises(AttributeError):
        keyboard.language = 'something'


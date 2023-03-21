import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('honor', 10000, 4, 2)


def test_repr(phone):
    assert repr(phone) == "Phone('honor', 10000, 4, 2)"


def test_add(phone):
    item: Item = Item('phone', 10000, 4)
    with pytest.raises(TypeError):
        phone + 1
        1 + phone
        item + 1
        1 + item

import pathlib
from pathlib import Path

import pytest

from errors.errors import InstantiateCSVError
from src.item import Item
from src.phone import Phone

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'test_file.csv')


@pytest.fixture
def item():
    return Item('phone', 10000, 4)


def test_item_init(item):
    """Тестирование класса Item"""
    assert type(item.name) == str
    assert type(item.price) == int
    assert type(item.quantity) == int
    assert item.name == 'phone'
    assert item.price == 10000
    assert item.quantity == 4


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 40000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 11000.0


def test_set_name(item):
    item.name = 'monitor'
    assert item.name == 'monitor'


def test_string_to_number(item):
    assert item.string_to_number('5') == 5


def test_validate(item):
    with pytest.raises(ValueError):
        item.name = 'abracadabdaabracadabra'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 9
    assert Item.all[-1].name == 'console'
    assert Item.all[-1].price == '10000'
    assert Item.all[-1].quantity == '2'


def test_str(item):
    assert str(item) == 'phone'


def test_repr(item):
    assert repr(item) == "Item('phone', 10000, 4)"


def test_add(item):
    phone = Phone('Honor', 1000, 5, 2)
    assert item + phone == 9
    assert phone + item == 9
    with pytest.raises(TypeError):
        item + 10


def test_FileNotFoundError_errors():
    file = ''
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file)


def test_InstantiateCSVError_errors():
    path_uncorrect_file = Path(dir_path, 'uncorrect_items.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_uncorrect_file)

import csv
import os
import pathlib
from pathlib import Path

import pytest
from src.item import Item

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
    with open(path) as file:
        res = csv.DictReader(file)
        for i in res:
            Item(i['name'], i['price'], i['quantity'])
    assert len(Item.all) == 9
    assert Item.all[-1].name == 'console'
    assert Item.all[-1].price == '10000'
    assert Item.all[-1].quantity == '2'

def test_str(item):
    assert str(item) == 'phone'

def test_repr(item):
    assert repr(item) == "Item('phone', 10000, 4)"



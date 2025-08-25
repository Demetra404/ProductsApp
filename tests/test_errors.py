import pytest

from src.order import Order
from src.products import Product
from src.category import Category
from src.exceptions import Quantity,QuantityError

@pytest.fixture()
def first_error_product():
    return Product("Газонная трава", "Элитная трава для газона", 500.0, 50)

@pytest.fixture()
def first_error_category():
    return Category('Смартфоны', 'Всё равно разобьются', [])

@pytest.fixture()
def first_nice_category():
    return Category('Смартфоны', 'Всё равно разобьются', [Product('Xiaomi POCO', 'Да нормальный', 15000, 100), Product('Iphone 16', 'ГигаКамера',100000, 13)])

@pytest.fixture()
def first_error_order():
    return Order('Xiaomi POCO', 100, 0)

def test_error_product(first_error_product):
    with pytest.raises(ValueError):
        zero_quantity = Product("Газонная трава", "Элитная трава для газона", 500.0, 0)

def test_average_price(first_error_category):
    empty_list = first_error_category.average_price
    assert empty_list == 0


def test__error_average_price():
    with pytest.raises(QuantityError):
        Quantity(0)


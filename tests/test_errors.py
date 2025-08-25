
import pytest
from src.products import Product
from src.category import Category


@pytest.fixture()
def first_error_product():
    return Product("Газонная трава", "Элитная трава для газона", 500.0, 20)

@pytest.fixture()
def first_error_category():
    return Category('Смартфоны', 'Всё равно разобьются', [])

@pytest.fixture()
def first_nice_category():
    return Category('Смартфоны', 'Всё равно разобьются', [Product('Xiaomi POCO', 'Да нормальный', 15000, 100), Product('Iphone 16', 'ГигаКамера',100000, 13)])

def test_average_price(first_error_category):
    print(first_error_category.average_price)

def test__error_average_price(first_error_category):
    print(first_error_category.average_price)


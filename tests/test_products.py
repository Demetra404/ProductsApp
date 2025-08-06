from src.products import Product
import pytest

@pytest.fixture()
def first_product():
    return Product('Iphone 16', 'ГигаКамера',100000, 13)

@pytest.fixture()
def second_product():
    return Product('Xiaomi POCO', 'Да нормальный', 15000, 100)

def test_product(first_product):
    assert first_product.name == 'Iphone 16'
    assert first_product.description == 'ГигаКамера'
    assert first_product.price == 100000
    assert first_product.quantity == 13

def test_product_new(second_product):
    assert second_product.name == 'Xiaomi POCO'
    assert second_product.description == 'Да нормальный'
    assert second_product.price == 15000
    assert second_product.quantity == 100
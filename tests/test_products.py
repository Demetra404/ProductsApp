from pyexpat.errors import messages

from src.products import Product
import pytest

@pytest.fixture()
def first_product():
    return Product('Iphone 16', 'ГигаКамера',100000, 13)

@pytest.fixture()
def second_product():
    return Product('Xiaomi POCO', 'Да нормальный', 15000, 100)

@pytest.fixture()
def product_dict():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}

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

def test_new_product(product_dict):
    new_product = Product.new_product(
        product_dict)
    assert new_product.name == 'Samsung Galaxy S23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product_one = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Черный цвет, 200MP камера", "price": 170000.0,
         "quantity": 7})
    assert new_product_one.name == 'Samsung Galaxy S23 Ultra'
    assert new_product_one.description == '256GB, Черный цвет, 200MP камера'
    assert new_product_one.price == 180000.0
    assert new_product_one.quantity == 12
    new_product_two = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Черный цвет, 200MP камера", "price": 170000.0,
         "quantity": 7})
    assert new_product_two.name == 'Samsung Galaxy S23 Ultra'
    assert new_product_two.description == '256GB, Черный цвет, 200MP камера'
    assert new_product_two.price == 180000.0
    assert new_product_two.quantity == 19

def test_price(capsys, second_product):
    product_for_test_price = second_product
    assert product_for_test_price.price == 15000
    product_for_test_price.price = -100
    message = capsys.readouterr()
    assert  message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    assert product_for_test_price.price == 15000
    product_for_test_price.price = 0
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    assert product_for_test_price.price == 15000


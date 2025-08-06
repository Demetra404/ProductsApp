import pytest
from src.category import Category
from src.products import Product



@pytest.fixture()
def first_category():
    return Category('Телевизоры','Было и было')

@pytest.fixture()
def second_category():
    return Category('Смартфоны', 'Всё равно разобьются', [Product('Xiaomi POCO', 'Да нормальный', 15000, 100), Product('Iphone 16', 'ГигаКамера',100000, 13)])

def test_category(first_category):
    assert first_category.name == 'Телевизоры'
    assert first_category.description == 'Было и было'
    assert first_category.products == []
    assert first_category.product_count == 0
    assert first_category.category_count == 1

def test_new_category(second_category):
    assert second_category.name == 'Смартфоны'
    assert second_category.description == 'Всё равно разобьются'
    assert second_category.product_count == 2
    assert second_category.category_count == 2
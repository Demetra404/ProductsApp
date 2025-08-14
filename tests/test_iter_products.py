import pytest
from src.products import Product
from src.category import Category
from src.iter_products import IterProduct

@pytest.fixture()
def object_category():
    return Category('Смартфоны', 'Всё равно разобьются', [Product('Xiaomi POCO', 'Да нормальный', 15000, 100), Product('Iphone 16', 'ГигаКамера',100000, 13)])

def test_iter_product(object_category):
    test_list = []
    for product in object_category.products_list:
        assert product.name == 'Xiaomi' or 'Iphone 16'
        test_list.append(product)
    assert len(test_list) == len(object_category.products_list)

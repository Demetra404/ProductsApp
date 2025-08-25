from pyexpat.errors import messages

from src.products import Product, Smartphone, LawnGrass
import pytest

@pytest.fixture()
def first_product():
    return Product('Iphone 16', 'ГигаКамера',100000, 13)

@pytest.fixture()
def first_product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
@pytest.fixture()
def first_product_grass_one():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

@pytest.fixture()
def first_product_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
@pytest.fixture()
def first_product_smartphone_one():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture()
def first_product_smartphone_two():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture()
def second_product():
    return Product('Xiaomi POCO', 'Да нормальный', 15000, 100)

@pytest.fixture()
def third_product():
    return Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 170000.0, 8)

@pytest.fixture()
def product_dict():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Черный цвет, 200MP камера", "price": 180000.0,
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

def test_new_product(product_dict, first_product, second_product, third_product):
    new_product = Product.new_product(
        product_dict)
    assert new_product.name == 'Samsung Galaxy S23 Ultra'
    assert new_product.description == '256GB, Черный цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product_one = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Черный цвет, 200MP камера", "price": 170000.0,
         "quantity": 7})
    assert new_product_one.name == 'Samsung Galaxy S23 Ultra'
    assert new_product_one.description == '256GB, Черный цвет, 200MP камера'
    assert new_product_one.price == 170000.0
    assert new_product_one.quantity == 7
    new_product_two = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 170000.0,
         "quantity": 7}, [first_product, second_product, third_product])
    assert new_product_two.name == 'Samsung Galaxy S23 Ultra'
    assert new_product_two.description == '256GB, Серый цвет, 200MP камера'
    assert new_product_two.price == 170000.0
    assert new_product_two.quantity == 15


def test_price(capsys, second_product):
    product_for_test_price = second_product
    assert product_for_test_price.price == 15000
    product_for_test_price.price = -100
    message = capsys.readouterr()
    assert  message.out.strip() == 'Xiaomi POCO, Да нормальный, 15000, 100\nЦена не должна быть нулевая или отрицательная'
    assert product_for_test_price.price == 15000
    product_for_test_price.price = 0
    assert message.out.strip() == 'Xiaomi POCO, Да нормальный, 15000, 100\nЦена не должна быть нулевая или отрицательная'
    assert product_for_test_price.price == 15000

def test_str_product(first_product, second_product):
    assert str(first_product) == 'Iphone 16, 100000 руб. Остаток: 13 шт.\n'
    assert str(second_product) == 'Xiaomi POCO, 15000 руб. Остаток: 100 шт.\n'

def test_add_product(first_product, second_product):
    assert first_product + second_product == 100000 * 13 + 15000 * 100

def test_smartphone(first_product_smartphone, first_product_smartphone_one, first_product_smartphone_two):
    assert first_product_smartphone.name == 'Samsung Galaxy S23 Ultra'
    assert first_product_smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert first_product_smartphone.price == 180000.0
    assert first_product_smartphone.quantity == 5
    assert first_product_smartphone.efficiency == 95.5
    assert first_product_smartphone.model == "S23 Ultra"
    assert first_product_smartphone.memory == 256
    assert first_product_smartphone.color == "Серый"

def test_add(first_product_smartphone, first_product_smartphone_one, first_product_grass, first_product_grass_one):
    assert first_product_smartphone + first_product_smartphone_one == 2580000.0
    with pytest.raises(TypeError):
        first_product_smartphone + first_product_grass
import pytest
from src.order import Order

@pytest.fixture()
def first_order():
    return Order('Iphone 16', 2,100000)

def test_order(first_order):
    assert first_order.name == 'Iphone 16'
    assert first_order.quantity == 2
    assert first_order.full_price == 100000
    assert str(first_order) == 'Iphone 16, 2, 100000.'
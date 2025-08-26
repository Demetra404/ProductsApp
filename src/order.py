from src.category import BaseFunc
from src.exceptions import Quantity, QuantityError


class Order(BaseFunc):
    name: str
    quantity: int
    full_price: float

    def __init__(self, name: str, quantity: int, full_price: float):
        self.name = name
        try:
            Quantity(quantity)
            self.quantity = quantity
        except QuantityError:
            print('Измените количество товара')
        else:
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена')
        self.full_price = full_price

    def __str__(self) -> str:
        return f'{self.name}, {self.quantity}, {self.full_price}.'

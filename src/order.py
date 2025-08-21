from src.category import BaseFunc


class Order(BaseFunc):
    name: str
    quantity: int
    full_price: float

    def __init__(self, name: str, quantity: int, full_price: float):
        self.name = name
        self.quantity = quantity
        self.full_price = full_price
        print(repr(self))

    def __str__(self) -> str:
        return f'{self.name}, {self.quantity}, {self.full_price}.'

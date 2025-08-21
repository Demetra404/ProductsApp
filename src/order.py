from src.category import BaseFunc

class Order(BaseFunc):
    name: str
    quantity: int
    full_price: float
    def __init__(self, name, quantity, full_price):
        self.name = name
        self.quantity = quantity
        self.full_price = full_price
        print(repr(self))

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.full_price}.'



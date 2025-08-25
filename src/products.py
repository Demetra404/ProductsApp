from abc import ABC, abstractmethod
from typing import Any, Self


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any):
        pass


class MixinProduct:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.quantity}'


class Product(BaseProduct, MixinProduct):
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if not quantity:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n'

    def __add__(self, other: Self) -> float:
        if isinstance(self, type(other)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, dict_products: dict, product_list: list[Any] | None = None) -> Self:
        name = dict_products['name']
        description = dict_products['description']
        price = dict_products['price']
        quantity = dict_products['quantity']
        new_product = cls(name, description, price, quantity)
        if product_list:
            for product in product_list:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product
            product_list.append(new_product)
        return new_product

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        elif new_price < self.__price:
            user_answer = input()
            if user_answer == 'y':
                self.__price = new_price
            elif user_answer == 'n':
                return


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

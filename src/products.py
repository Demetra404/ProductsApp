from typing import Self


class Product:
    name: str
    description: str
    quantity: int
    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        """Доп к заданию 3 (кривовато)))"""
        if Product.products is []:
            Product.products.append([self.name, self.description, self.__price, self.quantity])
        else:
            for product in Product.products:
                if product[0] == self.name:
                    product[3] += quantity
                    self.quantity = product[3]
                    if price > product[2]:
                        product[2] = price
                        self.__price = product[2]
                    else:
                        self.__price = product[2]
                    return
            Product.products.append([self.name, self.description, self.__price, self.quantity])

    @classmethod
    def new_product(cls, dict_products: dict) -> Self:
        name = dict_products['name']
        description = dict_products['description']
        price = dict_products['price']
        quantity = dict_products['quantity']
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        elif new_price < self.__price:
            user_answer = input()
            if user_answer == 'y':
                self.__price = new_price
            elif user_answer == 'n':
                return

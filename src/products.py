from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int
    products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if Product.products is []:
            Product.products.append([self.name, self.description, self.__price, self.quantity])
        else:
            for product in Product.products:
                if product[0] == name:
                    product[3] = quantity
                    return
            Product.products.append([self.name, self.description, self.__price, self.quantity])





    @classmethod
    def new_product(cls, dict_products: dict):
        name = dict_products['name']
        description = dict_products['description']
        price = dict_products['price']
        quantity = dict_products['quantity']
        for product_new in Product.products:
            if product_new[0] == name:
                product_new[3] += quantity
                if price > product_new[2]:
                     product_new[2] = price
            return cls(product_new[0], product_new[1], product_new[2], product_new[3])
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
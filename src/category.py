from abc import ABC, abstractmethod
from sys import prefix
from typing import Any, Union

from src.products import Product
from src.exceptions import QuantityError, Quantity


class BaseFunc(ABC):

    @abstractmethod
    def __str__(self):
        pass


class Category(ABC):
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Union[list[Any], None] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        quantity_category = 0
        for product in self.__products:
            quantity_category += product.quantity
        return f'{self.name}, количество продуктов: {quantity_category} шт.\n'

    def add_product(self, product: "Product") -> None:
        if isinstance(product, Product):
            quantity = product.quantity
            try:
                test = Quantity(quantity)
                self.__products.append(product)
                Category.product_count += 1
            except QuantityError:
                print('Измените количество товара')
            else:
                print('Товар добавлен')
            finally:
                print('Обработка добавления товара завершена')

        else:
            raise TypeError

    @property
    def average_price(self):
        price = 0
        try:
            for product in self.__products:
                price += product.price
            ave_price = price // len(self.__products)
            return ave_price
        except ZeroDivisionError:
            return 0


    @property
    def products(self) -> str:
        product_str = ''
        for product in self.__products:
            product_str += f'{str(product)}'
        return product_str

    @property
    def products_list(self) -> list:
        return self.__products

first_category = Category('Смартфоны', 'Всё равно разобьются', [Product('Xiaomi POCO', 'Да нормальный', 15000, 100), Product('Iphone 16', 'ГигаКамера',100000, 13)])
first_product = Product('samsung 16', 'Да да деньги', 65000, 0)
first_category.add_product(first_product)
for product in first_category.products_list:
    print(product.quantity)

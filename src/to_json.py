import json
import os
from typing import Any, List

from src.category import Category
from src.products import Product

path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'data', 'products.json')


def open_file_products(path: str) -> List[Any]:
    with open(path, 'r', encoding='utf-8') as file:
        data_products = json.load(file)
    return data_products if isinstance(data_products, list) else []


def create_object_from_data(data: List[Any]) -> List[Any]:
    if data is []:
        return []
    categories = []
    for object_data in data:
        products = []
        for product in object_data['products']:
            products.append(Product(product['name'], product['description'],
                                    product['price'], product['quantity']))
        categories.append(Category(object_data['name'],
                                   object_data['description'],
                                   products))
    return categories


if __name__ == '__main__':
    raw_data = open_file_products(path_to_file)
    print(type(raw_data))
    categories_data = create_object_from_data(raw_data)
    print(categories_data)
    print(categories_data[0].name)
    print(categories_data[0].products[0].name)
    print(categories_data[1].name)
    print(categories_data[1].products[0].name)

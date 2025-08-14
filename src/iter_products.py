from src.category import Category
from src.products import Product

class IterProduct:

    def __init__(self, category_obj):
        self.category = category_obj


    def __iter__(self):
        self.index_category = 0
        return self

    def __next__(self):
        if self.index_category < len(self.category.products_list):
            product_ = self.category.products_list[self.index_category]
            self.index_category += 1
            return product_
        else:
            raise StopIteration

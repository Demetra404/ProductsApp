class QuantityError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нельзя добавить товар с нулевым количеством'
    def __str__(self):
        return self.message

class Quantity:

    def __init__(self, product):
        if not product:
            raise QuantityError
        else:
            self.product = product
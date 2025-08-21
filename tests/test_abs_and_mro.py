from src.products import Product

def test_product_mixin(capsys):
    Product('Iphone 16', 'ГигаКамера',100000, 13)
    print_mixin = capsys.readouterr()
    assert print_mixin.out.strip() == "Iphone 16, ГигаКамера, 100000, 13"

    Product('Xiaomi POCO', 'Да нормальный', 15000, 100)
    print_mixin = capsys.readouterr()
    assert print_mixin.out.strip() == "Xiaomi POCO, Да нормальный, 15000, 100"

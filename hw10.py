from datetime import datetime, date


class Shop:
    def __init__(self):
        self.delivery_of_products = []

    def is_fresh_product(self, new_product):
        if new_product.best_before_date < datetime.now().date():
            return False
        else:
            return True

    def add_product(self, new_product):
        if not self.is_fresh_product(new_product):
            # error_msg = 'У продукта {} закончился срок годности!'.format(new_product)
            print(f'У продукта', new_product, 'закончился срок годности!')
        else:
            print(f'Продукт {new_product} добавлен в магазин')
            self.delivery_of_products.append(new_product)


class Products:
    def __init__(self, id_product: int, name_product: str, price: float, amount: int):
        self.id_product = id_product
        self.name_product = name_product
        self.price = price
        self.amount = amount


class FruitProduct(Products):
    def __init__(self, id_product: int, name_product: str, price: float, amount: int,
                 manufacturing_country: str, best_before_date: date):

        super().__init__(id_product, name_product, price, amount)
        self.manufacturing_country = manufacturing_country
        self.best_before_date = best_before_date

    def __str__(self):
        return self.name_product


if __name__ == '__main__':
    market = Shop()
    product1 = FruitProduct(12, 'apple', 25.3, 10, 'Russia', date(2021, 12, 12))
    product2 = FruitProduct(10, 'kiwi', 35, 30, 'Indonesia', date(2021, 2, 10))
    product3 = FruitProduct(18, 'banana', 15, 100, 'Africa', date(2021, 1, 10))

    market.add_product(product1)
    market.add_product(product2)
    market.add_product(product3)
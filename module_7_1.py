# from pprint import pprint
class Product:

    def __init__(self, name, weight, category):
        self.name = name  # название продукта (строка)
        self.weight = weight  # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category  # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'  # список товаров, имеющихся в магазине

    def get_products(self):  # для обработки файла products.txt
        product = open(self.__file_name, 'r')
        all_products = product.read()
        product.close()
        return all_products

    def add(self, *products):
        product = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in Shop.get_products(self):
                product.write(f'{i}\n')
            else:
                print(f'Продукт {str(i)} уже есть в магазине')
        product.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

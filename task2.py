from ean import ean_country_codes


class Product:
    """
    This class represents a product identified by its barcode.

    Attributes
    -----------
    - __barcode: str, The unique identifier code for the product.
    - __value: float, The value or price of the product.
    - __country: str, The country code associated with the product's barcode.

    Methods
    --------
    - get_barcode(): Returns the barcode of the product.
    - get_country(): Returns the country associated with the product's barcode.
    - get_value(): Returns the value or price of the product.
    - __eq__(other): Checks if two products are equal based on their barcode and value.

    Note
    ----
    This class relies on an external dictionary `ean_country_codes` to retrieve the country code based on the first three digits of the barcode.
    """

    def __init__(self, barcode, value):
        self.__barcode = barcode
        self.__value = value
        self.__country = ean_country_codes[self.__barcode[:3]]

    def get_barcode(self):
        """
        Returns the barcode of the product.
        """
        return self.__barcode

    def get_country(self):
        """
        get_country(): Returns the country associated with the product's barcode.
        """
        return self.__country

    def get_value(self):
        """
        Returns the value or price of the product.
        """
        return self.__value

    def __eq__(self, other):
        """
        Checks if two products are equal based on their barcode and value.
        """
        return self.__barcode == other.get_barcode() and self.__value == other.get_value()


class ShoppingCart:
    """
        It is a class representing a shopping cart for an online store.

        Attributes
        -----------
        - items: list, A list of available products.
        - cart: list, A list of products added to the shopping cart.
        - total_cost: float, Total cost of all products in the shopping cart.

        Methods
        --------
        - load_products(file_name): Loads product data from a file into the available items list.
        - add_product(product): Adds a product to the shopping cart and updates the total cost.
        - remove_product(product): Removes a product from the shopping cart and updates the total cost.
        - show_cart_content(): Displays the content of the shopping cart including product details and total cost.
        - __eq__(other): Checks if two products are equal based on their barcode and value.
        """

    def __init__(self, items=[], cart=[], cost=0):
        self.__items = items
        self.__cart = cart
        self.__total_cost = cost

    def load_products(self, file_name):
        """
        Loads product data from a file into the available items list.
        """
        with open(file_name, 'r') as file:
            for line in file:
                barcode, value = line.strip().split(' ')
                product = Product(barcode, float(value))
                self.__items.append(product)
        i = 1
        print('Товары в наличии:')
        for item in self.__items:
            print(f' {str(i).center(2)}: Штрих-код:{item.get_barcode().center(16)}| Страна: '
                  f'{item.get_country().center(14)}| Цена:{str(item.get_value()).center(8)}руб.|')
            print("---------------------------------------------------------------------------")
            i += 1

    def add_product(self, product):
        """
        Adds a product to the shopping cart and updates the total cost.
        """
        self.__cart.append(product)
        self.__total_cost += float(product.get_value())

    def remove_product(self, product):
        """
        Removes a product from the shopping cart and updates the total cost.
        """
        if product in self.__cart:
            self.__cart.remove(product)
            self.__total_cost -= float(product.get_value())

    def show_cart_content(self):
        """
        Displays the content of the shopping cart including product details and total cost.
        """
        i = 1
        print('Товары в корзине:')
        for item in self.__cart:
            print(f' {str(i).center(2)}: Штрих-код:{item.get_barcode().center(16)}| Страна: '
                  f'{item.get_country().center(14)}| Цена:{str(item.get_value()).center(8)}руб.|')
            print("---------------------------------------------------------------------------")
            i += 1
        print("Total cost:", self.__total_cost)


def menu(cart):
    print('')
    print('1. Загружать данные о товарах из файла.\n'
          '2. Добавлять товар в корзину.\n'
          '3. Удалить товар из корзины.\n'
          '4. Посмотреть содержание корзины.\n')
    choose = int(input('Выберите необходимое действие:'))
    print(choose == 1)
    if choose == 1:
        cart.load_products('products.txt')
    elif choose == 2:
        barcode = input('Введите штрихкод товара:')
        value = input('Введите цену товара:')
        product = Product(barcode, float(value))
        cart.add_product(product)
    elif choose == 3:
        barcode = input('Введите штрихкод товара:')
        value = input('Введите цену товара:')
        product = Product(barcode, float(value))
        cart.remove_product(product)
    elif choose == 4:
        cart.show_cart_content()
    menu(cart)


cart = ShoppingCart()
menu(cart)

from product import Product

class Store:
    """
    Represents a store that can order and sell products, apply price markups,
    and manage its stock and money.
    """
    def __init__(self, name, money):
        """
        Initializes the Store with a name, starting balance,
        and an empty list of products.

        :param name: Name of the store.
        :param money: Starting amount of money the store holds.
        """
        self.__name = name
        self.__money = money
        self.__products = []

    def find_product(self, id):
        """
        Searches the store's product list and returns the product matching the given ID.

        :param id: The unique ID of the product to find.
        :return: The matching Product object, or None if not found.
        """
        for product in self.__products:
            if product.get_id() == id:
                return product
        return None

    def order_product(self, product, quantity):
        """
        Orders a product by adding it to the store's inventory.
        If the product already exists, its quantity is increased.
        The store does not lose money when ordering.

        :param product: A Product object to be added or updated in stock.
        :param quantity: Number of units to add.
        :return: None
        """
        for existing_product in self.__products:
            if existing_product.get_id() == product.get_id():
                existing_product.increase_quantity(quantity)
                return
        product.increase_quantity(quantity)
        self.__products.append(product)

    def sell_product(self, id, amount):
        """
        Sells a specified amount of a product by its ID.
        If the product exists and has enough stock, quantity is reduced
        and store’s money is increased.

        :param id: Unique product ID to find the product.
        :param amount: Number of units to sell.
        :return: None
        """
        product = self.find_product(id)
        if product is None:
            print(f"Product with ID {id} not found.")
            return

        current_quantity = product.get_quantity()

        if current_quantity == 0:
            return

        if amount > current_quantity:
            print()
            print(f"This quantity ({amount}) cannot be sold as there are only ({current_quantity}) {product.get_name()}(s) remaining in stock.")
            print(f"The item: {product.get_name()} is sold out.\n")
            return

        product.decrease_quantity(amount)
        total_price = round(product.get_price() * amount, 2)
        self.__money += total_price


    def markup_prices(self, multiplier):
        """
        Increases the price of all products by a given multiplier.

        :param multiplier: Float multiplier to apply to all prices (e.g., 1.2 for +20%).
        :return: None
        """
        for product in self.__products:
            current_price = product.get_price()
            new_price = round(current_price * multiplier, 2)
            product.set_price(new_price)

    def __str__(self):
        """
        Returns a formatted string representation of the store,
        including its name, current holdings, and inventory.
        :return: A multi-line formatted string.
        """
        output = []
        output.append(f"{self.__name.upper()}")
        rounded_money = round(self.__money, 2)
        if rounded_money == int(rounded_money):
            output.append(f"Current Holdings: ${rounded_money:.1f}")
        else:
            output.append(f"Current Holdings: ${rounded_money:.2f}")

        if not self.__products:
            output.append("This store is out of stock... of everything. *shrug*")
        else:
            output.append("Current Stock:")
            for product in self.__products:
                output.append("===========")
                output.extend(str(product).splitlines())
                output.append("===========")

        if self.__products:
            output.append("")
        return "\n".join(output)


class Product:
    """
    Represents a product in a store with a name, price, quantity, and description.
    """
    def __init__(self, id, name, description, price, quantity=2):
        """
        Initializes a Product object with the given details.

        :param id: Unique identifier for the product (str or int).
        :param name: Name of the product.
        :param description: Brief info about the product.
        :param price: Unit price of the product.
        :param quantity: Available stock (defaults to 2).
        """
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity


    def increase_quantity(self, amount):
        """
        Increases the current quantity by the given amount.

        :param amount: Number of units to add to stock.
        """
        if type(amount) != int:
            print("\nInvalid input: Amount must be a number.\n")
        elif amount <= 0:
            print("\nInvalid input: Amount must be greater than zero.\n")
        else:
            self.__quantity += amount


    def decrease_quantity(self, amount):
        """
        Decreases the quantity by the given amount (if available).
        Prevents quantity from going below zero.

        :param amount: Number of units to remove from stock.
        """
        if type(amount) != int:
            print("\nAmount must be a whole number.\n")
        elif amount <= 0:
            print("\nAmount must be greater than zero.\n")
        elif amount > self.__quantity:
            print(f"Cannot remove {amount}. The remaining {self.__quantity} in stock is removed.")
            self.__quantity = 0
        else:
            self.__quantity -= amount

    def __str__(self):
        """
        Returns a formatted string with product details.

        :return: Multi-line string with name, description, quantity, and price.
        """
        output = []
        output.append(f"Product: {self.__name}")
        output.append(f"Description: {self.__description}")
        output.append(f"Quantity: {self.__quantity}")
        output.append(f"Price: ${self.__price} each")
        return "\n".join(output)

# Create a product
pillow = Product(1, "Pillow Set", "Set of two bamboo material pillows.", 45.99)

pillow.increase_quantity(200)
print(pillow)

pillow.decrease_quantity(-1)
pillow.increase_quantity(0)

pillow.decrease_quantity(50)
print(pillow)

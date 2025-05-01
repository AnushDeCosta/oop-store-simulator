# Store Simulator – OOP Project

![Image](https://github.com/user-attachments/assets/afde902e-3b34-483d-9a78-d4b018be87fa)

## Summary
Store Simulator is a Python-based object-oriented program that models a real-world retail system. This project demonstrates the use of two core classes (`Product` and `Store`) to simulate common business operations like ordering stock, selling items, adjusting prices, and managing inventory. It showcases clean, modular design principles and prepares students for test-driven, real-world development.

## Introduction
This OOP project was built to reinforce foundational concepts of object-oriented design in Python. It covers:
- Encapsulated attributes with private variables
- Getter/setter logic where appropriate
- Condition-based validation before executing operations
- Modular methods supporting clear class responsibilities

All output formatting is designed to match automated tests line-for-line.

> **Note**: This project was created as part of the Object-Oriented Programming Workshops (Week 4) for the Bachelor of Data Analytics (XBDA) degree at the University of South Australia (UniSA).

## Project Features
The system allows users to:
- **Create Product objects** with id, name, description, price, and quantity
- **Add or order products** in the Store's inventory
- **Sell products**, ensuring that:
  - The product exists
  - There is enough stock
- **Apply markup multipliers** to all product prices
- **Display the full inventory and current store balance** with clean, test-aligned output

### Core Mechanics
- Inventory is managed using a list of `Product` objects inside the `Store`.
- Selling logic prevents overselling and prints a formatted warning message if stock is insufficient.
- The Store prints money with `.1f` or `.2f` formatting based on whole vs fractional values.
- Quantity changes and price updates are dynamically handled with basic input validation.

### Output Formatting
- Each product is printed in a formatted block using `__str__()`.
- Products are separated with `"==========="` as per testing spec.
- Final printout includes whitespace for spacing between events and states.

## Tools
- Python 3.10+
- VSCode or PyCharm
- GitHub for version control

## Files
- `product.py` – Defines the `Product` class and handles product-related logic
- `store.py` – Defines the `Store` class with methods to manage sales, inventory, and pricing
- `README.md` – Project documentation

## Usage
To use the classes, run or import the files and interact with the store:

```python
from product import Product
from store import Store

store = Store("Sleep Token", 1000.0)
pillow = Product(1, "Pillow Set", "Set of two bamboo material pillows.", 45.99)
candle = Product(2, "Scented Candle", "Sandalwood, dual-wick candle.", 39.99)

print(store)  # Initial empty store

store.order_product(pillow, 2)
store.order_product(candle, 4)

store.sell_product(1, 3)  # Will trigger "not enough in stock" warning
store.sell_product(1, 2)
store.sell_product(1, 2)  # Will be silently ignored if stock is 0

print(store)

store.markup_prices(1.5)  # Apply 50% price increase
store.sell_product(2, 2)

print(store)
```

## Future Enhancements
- Add input validation for float vs int values
- Support product removal or price changes by ID
- Implement persistent storage (file or database)
- Add a menu-based CLI interface for user interaction
- Track sales history or transactions for reporting

## License
This project is intended for educational purposes only as part of coursework for the University of South Australia (UniSA) Bachelor of Data Analytics (XBDA) degree.
© 2025 Anush De Costa.

## Acknowledgements
This project was developed as part of the Week 4 Object-Oriented Programming (OOP) Workshops for the Bachelor of Data Analytics (XBDA) degree at UniSA.

Special thanks to the UniSA teaching team for guidance on modular design, method construction, and formatted output testing in Python.

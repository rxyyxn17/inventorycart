class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"{self.name}: ${self.price}, Quantity: {self.quantity}")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def display_inventory(self):
        for product in self.products:
            product.display_product()

# Example Usage
inventory = Inventory()
inventory.add_product(Product("Laptop", 1200, 10))
inventory.add_product(Product("Mouse", 20, 50))
inventory.display_inventory()
inventory.remove_product("Mouse")
print("\nInventory after removing mouse:")
inventory.display_inventory()
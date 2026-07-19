class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(ID={self.product_id}, Name='{self.name}', Price=₹{self.price}, Qty={self.quantity})"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to inventory.")

    def display_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            print("\nInventory List:")
            for product in self.products:
                print(f"ID: {product.product_id}, Name: {product.name}, Price: ₹{product.price}, Quantity: {product.quantity}")
            print("-" * 40)

    def search_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                print(f"Product Found → ID: {product.product_id}, Name: {product.name}, Price: ₹{product.price}, Quantity: {product.quantity}")
                return
        print(f"Product '{name}' not found in inventory.")

inventory = Inventory()

p1 = Product(101, "Laptop", 55000, 10)
p2 = Product(102, "Smartphone", 25000, 25)
p3 = Product(103, "Headphones", 2000, 50)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

inventory.display_products()

inventory.search_product("Smartphone")
inventory.search_product("Tablet")
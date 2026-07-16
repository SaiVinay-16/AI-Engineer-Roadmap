inventory = {
    "Product1": {"Quantity": 10, "Price": 250},
    "Product2": {"Quantity": 5, "Price": 120},
    "Product3": {"Quantity": 20, "Price": 75}
}

print("\n--- Inventory Details ---")
for product, details in inventory.items():
    print(f"Product Name : {product}")
    print(f"Quantity     : {details['Quantity']}")
    print(f"Price        : {details['Price']}")
    print("---------------------------")
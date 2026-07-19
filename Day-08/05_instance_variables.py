class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("Car Details:")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : ₹{self.price}")
        print("-" * 25)

car1 = Car("Toyota", "Innova", 2000000)
car2 = Car("Tesla", "Model 3", 3500000)
car1.display_details()
car2.display_details()
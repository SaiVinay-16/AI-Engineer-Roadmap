class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __repr__(self):
        return f"Product(Name : {self.name},Price : {self.price})"
class Cart:
    def __init__(self):
        self.products=[]
    def add_product(self,prod):
        self.products.append(prod)
        print(f"Product : {prod.name} added to cart")
    def remove_product(self,prod):
        for product in self.products:
            if prod.lower() ==  product.name.lower():
                self.products.remove(product)
                print(f"{product.name} removed successfully")
                return 
        return f"{prod} not found"
    def display_product(self):
        if not self.products:
            print("No Products are there")
        else:
            for product in self.products:
                print(f"Name : {product.name}\nPrice : {product.price}")
    def calculate_price(self):
        total_price=0
        if not self.products:
            print("No Products are there")
        else:
            for product in self.products:
                total_price+=product.price
            print(f"Total price is : {total_price}")

def main():
    obj=Cart()
    while True:
        print("==============================================")
        print("1.Add product")
        print("2.Remove product")
        print("3.Display products")
        print("4.Calculate total price of all products")
        print("5.Exit")
        print("==============================================")
        choice=int(input("Enter your choice:"))
        if 0<choice<6:
            if choice==1:
                name=input("Enter the product name:")
                price=int(input("Enter its price:"))
                obj.add_product(Product(name,price))
            elif choice==2:
                name=input("Enter the product name:")
                obj.remove_product(name)
            elif choice==3:
                obj.display_product()
            elif choice==4:
                obj.calculate_price()
            elif choice==5:
                print("Exit successfully")
                break

main()
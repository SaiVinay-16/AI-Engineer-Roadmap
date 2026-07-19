class Mobile:
    def __init__(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def get_details(self):
        print(f"Brand : {self.brand}\nRAM : {self.ram}GB\nStorage : {self.storage}GB")
m=Mobile("IQOO",8,64)
m.get_details()
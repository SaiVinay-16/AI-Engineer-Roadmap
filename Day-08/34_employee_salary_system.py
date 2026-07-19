class Employee:
    hra=3.5
    da=20
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        final_salary=self.salary+self.hra+self.da
        print(f"Name : {self.name}\nSalary : {final_salary}")
obj=Employee("Saivinay",10000)
obj.display()
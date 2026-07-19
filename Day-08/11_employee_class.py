class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def employee_details(self):
        print(f"Id : {self.id}\nName : {self.name}\nSalary : {self.salary}")
emp=Employee(16,"Saivinay",20000)
emp.employee_details()
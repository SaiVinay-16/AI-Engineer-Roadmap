class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return (f"Employee Information:\n"
                f"ID         : {self.emp_id}\n"
                f"Name       : {self.name}\n"
                f"Department : {self.department}\n"
                f"Salary     : ₹{self.salary}")

emp1 = Employee(101, "Sai", "IT", 50000)
emp2 = Employee(102, "Anita", "HR", 45000)

print(emp1)
print("-" * 30)
print(emp2)
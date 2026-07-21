from .employee_details import Employee

class EmployeeSalary(Employee):
    def __init__(self, emp_id, name, department, salary):
        super().__init__(emp_id, name, department)
        self.salary = salary

    def display_salary(self):
        """Display employee salary details."""
        self.display_details()
        print(f"Salary: ₹{self.salary}")
class Employee:
    def __init__(self, emp_id, name, department, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.__basic_salary = basic_salary   # private variable

    def get_basic_salary(self):
        return self.__basic_salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Basic Salary: ₹{self.__basic_salary}")


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added to payroll.")

    def calculate_net_salary(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                basic = emp.get_basic_salary()
                # Example: HRA = 20%, DA = 10%, Tax = 5%
                hra = 0.20 * basic
                da = 0.10 * basic
                tax = 0.05 * basic
                net_salary = basic + hra + da - tax
                print(f"Net Salary for {emp.name} (ID: {emp.emp_id}) = ₹{net_salary}")
                return net_salary
        print(f"Employee with ID {emp_id} not found.")
        return None

    def display_report(self):
        print("\n--- Payroll Report ---")
        if not self.employees:
            print("No employees in payroll.")
        else:
            for emp in self.employees:
                emp.display_info()
        print("-" * 40)

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee Found:")
                emp.display_info()
                return emp
        print(f"Employee with ID {emp_id} not found.")
        return None

    # Optional bonus: operator overloading
    def __len__(self):
        return len(self.employees)


# Example usage
payroll = Payroll()

e1 = Employee(101, "Sai", "IT", 50000)
e2 = Employee(102, "Anita", "HR", 45000)
e3 = Employee(103, "Ravi", "Finance", 60000)

payroll.add_employee(e1)
payroll.add_employee(e2)
payroll.add_employee(e3)

payroll.display_report()

payroll.calculate_net_salary(101)
payroll.calculate_net_salary(103)

payroll.search_employee(102)
payroll.search_employee(200)

print(f"Total Employees in Payroll: {len(payroll)}")  # uses operator overloading
# from employee import employee_details,employee_salary

# emp = employee_details.Employee(16, "Sai Vinay", "Artificial Intelligence and Data Science")
# emp.display_details()
# obj=employee_salary.EmployeeSalary(16, "Sai Vinay", "Artificial Intelligence and Data Science",40000)
# obj.display_salary()

from employee import employee_details
from employee import employee_salary

emp = employee_details.Employee(16, "Sai Vinay", "Artificial Intelligence and Data Science")
emp.display_details()

obj = employee_salary.EmployeeSalary(16, "Sai Vinay", "Artificial Intelligence and Data Science", 40000)
obj.display_salary()
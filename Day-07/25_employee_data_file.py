def store_employee_data(filename):
    try:
        with open(filename, "w") as f:
            n = int(input("Enter number of employees: "))
            for i in range(n):
                print(f"\nEnter details for Employee {i+1}:")
                emp_id = input("Employee ID: ")
                name = input("Name: ")
                dept = input("Department: ")
                salary = input("Salary: ")

                f.write(f"{emp_id},{name},{dept},{salary}\n")

        print("\nEmployee records stored successfully.\n")

        with open(filename, "r") as f:
            print("Employee Records:")
            for line in f:
                emp_id, name, dept, salary = line.strip().split(",")
                print(f"ID: {emp_id}, Name: {name}, Department: {dept}, Salary: {salary}")

    except Exception as e:
        print(f"An error occurred: {e}")

store_employee_data("employees.txt")
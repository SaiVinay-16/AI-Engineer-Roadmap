def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def main():
    while True:
        print("\n===== Calculator Menu =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Exiting Calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select between 1 and 5.")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid number input. Please enter numeric values.")
                continue

            if choice == 1:
                print(f"Result: {add(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply(num1, num2)}")
            elif choice == 4:
                result = divide(num1, num2)
                if result is not None:
                    print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter a valid menu choice (1-5).")

main()
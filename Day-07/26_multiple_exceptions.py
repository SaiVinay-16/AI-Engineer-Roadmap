def multiple_exceptions_demo():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))

        result = num1 / num2
        print(f"Result: {result}")

        sample_list = [10, 20, 30]
        index = int(input("Enter index to access (0-2): "))
        print(f"Value at index {index}: {sample_list[index]}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except IndexError:
        print("Error: Index out of range. Valid indices are 0, 1, or 2.")
    except Exception as e:
        print(f"Unexpected error: {e}")

multiple_exceptions_demo()
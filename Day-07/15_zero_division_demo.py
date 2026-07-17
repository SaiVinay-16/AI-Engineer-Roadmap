def safe_division():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))

        result = numerator / denominator
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")

safe_division()
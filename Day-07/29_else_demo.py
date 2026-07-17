def demo_division():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))

        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integers.")
    else:
        print(f"Division successful! Result = {result}")
    finally:
        print("Program execution completed. (finally block)")
        

demo_division()
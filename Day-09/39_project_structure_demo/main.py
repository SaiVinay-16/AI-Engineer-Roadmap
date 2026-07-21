from utils import calculator, validator

def main():
    print("--- Simple Calculator ---")
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not (validator.is_number(a) and validator.is_number(b)):
        print("❌ Invalid input. Please enter numbers only.")
        return

    a, b = float(a), float(b)

    print(f"Addition: {calculator.add(a, b)}")
    print(f"Subtraction: {calculator.subtract(a, b)}")
    print(f"Multiplication: {calculator.multiply(a, b)}")
    print(f"Division: {calculator.divide(a, b)}")

if __name__ == "__main__":
    main()
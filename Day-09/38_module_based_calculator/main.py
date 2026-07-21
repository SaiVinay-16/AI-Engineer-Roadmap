from operations import addition,subtraction,multiplication,division
def main():
    print("--- Simple Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {addition.add(a, b)}")
    print(f"Subtraction: {subtraction.subtract(a, b)}")
    print(f"Multiplication: {multiplication.multiply(a, b)}")
    print(f"Division: {division.divide(a, b)}")

if __name__ == "__main__":
    main()
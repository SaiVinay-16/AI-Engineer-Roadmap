from utility import calculator
from utility import string_utilities
from utility import datetime_utilities

def menu():
    while True:
        print("\n--- Utility Toolbox ---")
        print("1. Calculator")
        print("2. String Utilities")
        print("3. Date & Time Utilities")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Add:", calculator.add(a, b))
            print("Subtract:", calculator.subtract(a, b))
            print("Multiply:", calculator.multiply(a, b))
            print("Divide:", calculator.divide(a, b))

        elif choice == "2":
            text = input("Enter text: ")
            print("Uppercase:", string_utils.to_uppercase(text))
            print("Lowercase:", string_utils.to_lowercase(text))
            print("Reversed:", string_utils.reverse_string(text))
            print("Vowel Count:", string_utils.count_vowels(text))

        elif choice == "3":
            print("Current DateTime:", datetime_utils.current_datetime())
            print("Current Date:", datetime_utils.current_date())
            print("Current Time:", datetime_utils.current_time())

        elif choice == "4":
            print("Exiting Toolbox. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
def add_expense(filename):
    try:
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        with open(filename, "a") as f:
            f.write(f"{date},{category},{amount}\n")
        print("=== Expense Added Successfully ===\n")
    except ValueError:
        print("Error: Amount must be a number.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")


def view_expenses(filename):
    try:
        with open(filename, "r") as f:
            data = f.readlines()
            if data:
                print("\n--- All Expenses ---")
                for line in data:
                    date, category, amount = line.strip().split(",")
                    print(f"Date: {date}, Category: {category}, Amount: {amount}")
                print("--------------------\n")
            else:
                print("No expenses recorded yet.\n")
    except FileNotFoundError:
        print("No expense file found yet.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")


def calculate_total(filename):
    try:
        total = 0
        with open(filename, "r") as f:
            for line in f:
                _, _, amount = line.strip().split(",")
                total += float(amount)
        print(f"\nTotal Expense = {total}\n")
    except FileNotFoundError:
        print("No expense file found yet.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")


def main():
    filename = "expenses.txt"
    while True:
        print("============== Expense Tracker ==============")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expense")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                add_expense(filename)
            elif choice == 2:
                view_expenses(filename)
            elif choice == 3:
                calculate_total(filename)
            elif choice == 4:
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 4.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")


main()
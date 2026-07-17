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


def search_by_category(filename):
    try:
        category_search = input("Enter category to search: ")
        found = False
        with open(filename, "r") as f:
            for line in f:
                date, category, amount = line.strip().split(",")
                if category.lower() == category_search.lower():
                    print(f"Date: {date}, Category: {category}, Amount: {amount}")
                    found = True
        if not found:
            print("No expenses found in this category.\n")
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


def highest_expense(filename):
    try:
        max_expense = 0
        max_record = None
        with open(filename, "r") as f:
            for line in f:
                date, category, amount = line.strip().split(",")
                amount = float(amount)
                if amount > max_expense:
                    max_expense = amount
                    max_record = (date, category, amount)
        if max_record:
            print(f"\nHighest Expense → Date: {max_record[0]}, Category: {max_record[1]}, Amount: {max_record[2]}\n")
        else:
            print("No expenses recorded yet.\n")
    except FileNotFoundError:
        print("No expense file found yet.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")


def main():
    filename = "personal_expenses.txt"
    while True:
        print("============== Personal Expense Tracker ==============")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Calculate Total Expense")
        print("5. Display Highest Expense")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                add_expense(filename)
            elif choice == 2:
                view_expenses(filename)
            elif choice == 3:
                search_by_category(filename)
            elif choice == 4:
                calculate_total(filename)
            elif choice == 5:
                highest_expense(filename)
            elif choice == 6:
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 6.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.\n")

main()
import calendar

def show_month_calendar():
    year = int(input("Enter year (e.g., 2026): "))
    month = int(input("Enter month (1-12): "))

    print("\nHere is your calendar:\n")
    print(calendar.month(year, month))

if __name__ == "__main__":
    show_month_calendar()
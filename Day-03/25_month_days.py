def month_days(month_num):
    months = {
        1: ("January", 31),
        2: ("February", 28),  # ignoring leap years
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31)
    }
    
    if month_num in months:
        name, days = months[month_num]
        print(f"Month: {name}\nDays: {days}")
    else:
        print("Invalid month number! Please enter a number between 1 and 12.")


month_num = int(input("Enter month number (1–12): "))
month_days(month_num)

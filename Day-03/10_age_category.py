age=int(input("Enter the age for the category:"))
if age<=12:
    print("child")
elif 13<=age<=19:
    print("Teenager")
elif 20<=age<=59:
    print("Adult")
elif age>=60:
    print("Senior Citizen")
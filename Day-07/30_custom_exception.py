try:
    age=int(input("Enter the age:"))
    if age<18:
        raise ValueError("You are not eligible.")
except ValueError as e:
    print(e)
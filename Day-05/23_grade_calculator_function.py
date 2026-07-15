def get_grade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks <= 89:
        return "A"
    elif 70 <= marks <= 79:
        return "B"
    elif 60 <= marks <= 69:
        return "C"
    elif 35 <= marks <= 59:
        return "D"
    else:
        return "Fail"
marks=int(input("Enter the marks:"))
print(get_grade(marks))
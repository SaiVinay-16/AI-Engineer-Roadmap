def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 35:
        return "D"
    else:
        return "Fail"

def result(marks):
    if any(m < 35 for m in marks):
        return "Fail"
    else:
        return "Pass"

def student_report():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks for Subject {i}: "))
        marks.append(m)

    tot = total(marks)
    avg = average(marks)
    grd = grade(avg)
    res = result(marks)

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print("Total Marks:", tot)
    print("Average Marks:", avg)
    print("Grade:", grd)
    print("Result:", res)

student_report()
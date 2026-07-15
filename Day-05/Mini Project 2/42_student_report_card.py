def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
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
        return "F"

def determine_result(marks):
    if any(m < 35 for m in marks):
        return "Fail"
    else:
        return "Pass"

def display_report_card(name, roll, marks, total, avg, grade, result):
    print("\n--- Student Report Card ---")
    print("Name       :", name)
    print("Roll Number:", roll)
    print("Marks      :", marks)
    print("Total      :", total)
    print("Average    :", round(avg, 2))
    print("Grade      :", grade)
    print("Result     :", result)


def student_report_card():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks for Subject {i}: "))
        marks.append(m)

    total = calculate_total(marks)
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    result = determine_result(marks)

    display_report_card(name, roll, marks, total, avg, grade, result)

student_report_card()
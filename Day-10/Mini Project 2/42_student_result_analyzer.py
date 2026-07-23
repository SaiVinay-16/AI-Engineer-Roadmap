from functools import reduce
students = [("Alice", 85), ("Bob", 42), ("Charlie", 73), ("David", 55), ("Eva", 91)]
data = [{"name": name, "marks": marks} for name, marks in students]
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

graded_data = list(map(lambda s: {**s, "grade": assign_grade(s["marks"])}, data))
passed_students = list(filter(lambda s: s["marks"] >= 50, graded_data))
total_marks = reduce(lambda acc, s: acc + s["marks"], graded_data, 0)
average_marks = total_marks / len(graded_data)
print("📊 Student Result Report")
print("-" * 40)
for s in graded_data:
    print(f"Name: {s['name']:<10} Marks: {s['marks']:<3} Grade: {s['grade']}")
print("-" * 40)
print(f"Total Marks: {total_marks}")
print(f"Class Average: {average_marks:.2f}")
print("Passed Students:", ", ".join([s["name"] for s in passed_students]))
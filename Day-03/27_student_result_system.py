marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
average = total / 5

if all(m >= 35 for m in marks):
    result = "Pass"
else:
    result = "Fail"

if result == "Pass":
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"
else:
    grade = "No Grade"

print("\n--- Student Result ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)
print("Grade:", grade)

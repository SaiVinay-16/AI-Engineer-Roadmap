name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

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

print("\n========== Student Report Card ==========")
print(f"Name       : {name}")
print(f"Roll Number: {roll}")
print("-----------------------------------------")
for i, m in enumerate(marks, start=1):
    print(f"Subject {i} Marks: {m}")
print("-----------------------------------------")
print(f"Total Marks: {total}")
print(f"Average    : {average:.2f}")
print(f"Result     : {result}")
print(f"Grade      : {grade}")
print("=========================================")
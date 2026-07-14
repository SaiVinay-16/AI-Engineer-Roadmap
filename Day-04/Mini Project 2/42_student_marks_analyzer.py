n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

passed = sum(1 for m in marks if m >= 35)
failed = n - passed

print("\n--- Student Marks Report ---")
print("Total Students:", n)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Marks:", round(average, 2))
print("Number of Passed Students:", passed)
print("Number of Failed Students:", failed)
marks = [
    [85, 90, 78], 
    [70, 65, 80], 
    [95, 88, 92]  
]

print("\n--- Student Marks Report ---")

for i, student in enumerate(marks, start=1):
    print(f"\nStudent {i} Marks: {student}")
    total = sum(student)
    avg = total / len(student)
    print(f"Total Marks   : {total}")
    print(f"Average Marks : {round(avg, 2)}")
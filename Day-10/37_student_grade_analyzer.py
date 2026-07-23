from functools import reduce
marks = [35, 67, 80, 45, 90, 25, 55]
grades = list(map(lambda m: 
                  ('A' if m >= 75 else 
                   'B' if m >= 60 else 
                   'C' if m >= 50 else 
                   'D' if m >= 35 else 'F'), marks))
passed = list(filter(lambda m: m >= 35, marks))
total_marks = reduce(lambda a, b: a + b, marks)
print("Original marks:", marks)
print("Grades assigned:", grades)
print("Students who passed (marks >= 35):", passed)
print("Total marks of all students:", total_marks)
class Student:
    def __init__(self,name,roll_no,branch,cgpa):
        self.name=name
        self.roll_no=roll_no
        self.branch=branch
        self.cgpa=cgpa
    def get_details(self):
        print(f"Name : {self.name}\nRoll_no : {self.roll_no}\nBranch : {self.branch}\nCGPA : {self.cgpa}")
s=Student("vinay",16,"AI&DS",8.5)
s.get_details()
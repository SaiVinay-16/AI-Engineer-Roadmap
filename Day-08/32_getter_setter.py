class Student:
    __cgpa=8.5
    def set_cgpa(self,cgpa):
        self.__cgpa=cgpa
    def get_cgpa(self):
        print(f"CGPA : {self.__cgpa}")
s=Student()
s.set_cgpa(8.6)
s.get_cgpa()
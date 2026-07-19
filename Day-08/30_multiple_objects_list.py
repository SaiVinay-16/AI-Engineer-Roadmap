class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_details(self):
        print(f"Name : {self.name}\nAge : {self.age}")
s1=Students("vinay",21)
s2=Students("vivek",18)
s3=Students("mouni",24)
s4=Students("sandeep",27)
li=[s1,s2,s3,s4]
for obj in li:
    obj.get_details()
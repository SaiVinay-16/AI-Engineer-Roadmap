from datetime import datetime
x=datetime.now()
print("Current Date :",x.strftime("%d-%m-%Y"))
print("Current Time :",x.strftime("%I:%M:%S"))
print("Current Year :",x.strftime("%Y"))
print("Current Month Name :",x.strftime("%B"))
print("Current Day Name :",x.strftime("%A"))
print("Week Number :",x.strftime("%U"))
print("Day Number of the Year :",x.strftime("%j"))
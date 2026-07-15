def bmi_category(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
a=int(input("Enter the weight:"))
b=int(input("Enter the height:"))
print(bmi_category(a,b))
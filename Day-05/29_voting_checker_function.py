def voting_checker(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
age=int(input("Enter your age:"))
print(voting_checker(age))
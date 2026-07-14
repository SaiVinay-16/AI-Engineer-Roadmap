import re
character=input("Enter the character:")
if re.search(r"[A-Z]",character):
    print("Upper case alphabet")
elif re.search(r"[a-z]",character):
    print("lower case alphabet")
elif re.search(r"[0-9]",character):
    print("Digit")
elif re.search(r"[!@#$%^&*(),.?\":{}|<>]", character):
    print("Special Character")
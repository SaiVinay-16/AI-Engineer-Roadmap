import re
def check_password(password):
    if len(password)<8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Weak"
    if not re.search(r"[a-z]", password):
        return "Weak"
    if not re.search(r"[0-9]", password):
        return "Weak"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak"
    return "Strong"
password=input("Enter the password to check whether the password is strong or weak:")
res=check_password(password)
if res=="Strong":
    print("The password is strong")
else:
    print("The passwrod is weak")
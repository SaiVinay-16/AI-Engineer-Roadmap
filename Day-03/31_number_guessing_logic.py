secret_number=66
while True:
    guess_num=int(input("Enter the number to guess it:"))
    if guess_num<secret_number:
        print("Low")
    elif guess_num>secret_number:
        print("High")
    else:
        print("Correct")
        break
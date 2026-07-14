secret_num=56
count=0
while True:
    guess=int(input("Enter the guessing number:"))
    if guess<secret_num:
        print("Your number is low:")
        count+=1
    elif guess>secret_num:
        print("Your number is high:")
        count+=1
    else:
        count+=1
        print("Your entered is correct")
        print("The total number of counts is :",count)
        break
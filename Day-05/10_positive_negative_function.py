def pos_or_neg_or_zero(x):
    if x<0:
        return "Negative"
    elif x>0:
        return "Postitive"
    else:
        return "Zero"
a=int(input("Enter the number:"))
print(pos_or_neg_or_zero(a))
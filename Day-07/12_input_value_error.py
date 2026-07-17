try:
    num=int(input("Enter the value:"))
except ValueError:
    print("Enter value not text")
else:
    print(num)
finally:
    print("==========================")
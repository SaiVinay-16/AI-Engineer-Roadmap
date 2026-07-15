def table_upto_ten_steps(x):
    for i in range(1,11):
        print(f"{x} * {i} = {x*i}")
a=int(input("Enter the number:"))
table_upto_ten_steps(a)
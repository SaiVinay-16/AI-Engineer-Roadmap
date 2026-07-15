def sum_numbers(*args):
    add=0
    for i in range(len(args)):
        add+=args[i]        
    print(add)
sum_numbers(10,20,30,40)
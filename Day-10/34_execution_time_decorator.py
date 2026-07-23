import time
def decorate_greet(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        print("Function Started")
        func(*args,**kwargs)
        print("Function Finished")
        end=time.time()
        print("Execution time :",end-start)
    return wrapper

@decorate_greet
def greet():
    time.sleep(2)
    print("Hello!Welcome to Peddi's world")
greet()
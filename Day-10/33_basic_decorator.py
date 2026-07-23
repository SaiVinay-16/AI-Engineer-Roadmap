def decorate_greet(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Finished")
    return wrapper

@decorate_greet
def greet():
    print("Hello!Welcome to Peddi's world")
greet()
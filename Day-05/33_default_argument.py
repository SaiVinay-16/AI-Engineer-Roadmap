def greet(*args):
    if len(args) > 0:
        name = args[0]
    else:
        name = "Guest"
    print("Hello", name)

greet()            
greet("Sai")     
greet("Anu")     
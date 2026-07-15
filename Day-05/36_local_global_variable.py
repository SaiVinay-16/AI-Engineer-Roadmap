x = 10

def demo_function():
    y = 5
    print("Inside function:")
    print("Global variable x =", x)   
    print("Local variable y =", y) 

demo_function()

print("\nOutside function:")
print("Global variable x =", x) 
# 20_generator_fibonacci.py

# Generator function for Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
        
n_terms = 10
print(f"Fibonacci sequence up to {n_terms} terms:")

for num in fibonacci_generator(n_terms):
    print(num)
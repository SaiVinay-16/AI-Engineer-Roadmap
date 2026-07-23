def fibonacci_return(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence   # returns the entire list at once

# Function using yield
def fibonacci_yield(n):
    a, b = 0, 1
    for _ in range(n):
        yield a       # yields one value at a time
        a, b = b, a + b

# Example usage
n_terms = 10

print("Using return:")
print(fibonacci_return(n_terms))   # prints full list immediately

print("\nUsing yield:")
for num in fibonacci_yield(n_terms):
    print(num)   # prints values one by one

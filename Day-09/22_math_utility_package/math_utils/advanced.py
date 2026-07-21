import math

def factorial(n):
    """Return the factorial of a number using math.factorial."""
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    return math.factorial(n)

def square_root(x):
    """Return the square root of a number using math.sqrt."""
    if x < 0:
        return "Error: Square root not defined for negative numbers"
    return math.sqrt(x)

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return math.pow(base, exponent)
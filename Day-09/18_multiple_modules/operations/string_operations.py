def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]

def to_uppercase(s):
    """Convert string to uppercase."""
    return s.upper()

def to_lowercase(s):
    """Convert string to lowercase."""
    return s.lower()

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
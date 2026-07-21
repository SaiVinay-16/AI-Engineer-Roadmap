def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def capitalize_words(s):
    """Capitalize the first letter of each word in the string."""
    return s.title()
def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
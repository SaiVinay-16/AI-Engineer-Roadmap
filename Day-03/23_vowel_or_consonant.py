def check_vowel_or_consonant(ch):
    vowels = "aeiouAEIOU"
    if ch in vowels:
        return "Vowel"
    else:
        return "Consonant"


alphabet = input("Enter a single alphabet: ")

if len(alphabet) != 1 or not alphabet.isalpha():
    print("Invalid input! Please enter a single alphabet (A–Z).")
else:
    result = check_vowel_or_consonant(alphabet)
    print(f"{alphabet} is a {result}.")
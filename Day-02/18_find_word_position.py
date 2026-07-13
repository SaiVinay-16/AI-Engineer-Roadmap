sentence = input("Enter a sentence: ")
word = input("Enter the word to find: ")

position = sentence.find(word)

if position != -1:
    print(f"'{word}' found at position {position}")
else:
    print(f"'{word}' not found in the sentence.")
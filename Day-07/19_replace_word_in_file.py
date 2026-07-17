def replace_word_in_file(filename, old_word, new_word):
    try:
        with open(filename, "r") as f:
            data = f.read()

        updated_data = data.replace(old_word, new_word)

        with open(filename, "w") as f:
            f.write(updated_data)

        print(f"All occurrences of '{old_word}' replaced with '{new_word}' in {filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

replace_word_in_file("example.txt", "vinay", "mouni")
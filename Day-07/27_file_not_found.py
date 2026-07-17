def open_file():
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r") as f:
            data = f.read()
            print("\nFile Content:\n")
            print(data)
    except FileNotFoundError:
        print("Error: File Not Found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

open_file()
def read_file_with_finally():
    f = None
    try:
        filename = input("Enter the filename: ")
        f = open(filename, "r")
        data = f.read()
        print("\nFile Content:\n")
        print(data)
    except FileNotFoundError:
        print("Error: File Not Found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if f:
            f.close()
            print("\nFile has been closed (inside finally block).")

read_file_with_finally()
def password_checker(filename):
    try:
        with open(filename, "r") as f:
            stored_password = f.read().strip()

        entered_password = input("Enter password: ")

        if entered_password == stored_password:
            print("Access Granted ✅")
        else:
            print("Access Denied ❌")

    except FileNotFoundError:
        print("Error: Password file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

password_checker("password.txt")
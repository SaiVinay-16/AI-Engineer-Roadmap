def register_user(filename):
    try:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        with open(filename, "a") as f:
            f.write(f"{username},{password}\n")
        print("=== User Registered Successfully ===\n")
    except Exception as e:
        print(f"Error while registering user: {e}\n")


def login_user(filename):
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        found = False
        with open(filename, "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    print("Access Granted ✅\n")
                    found = True
                    break
        if not found:
            print("Access Denied ❌\n")
    except FileNotFoundError:
        print("No users registered yet. Please register first.\n")
    except Exception as e:
        print(f"Error while logging in: {e}\n")


def main():
    filename = "users.txt"
    while True:
        print("============== Login System ==============")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                register_user(filename)
            elif choice == 2:
                login_user(filename)
            elif choice == 3:
                print("Exiting Login System. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 3.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")

main()
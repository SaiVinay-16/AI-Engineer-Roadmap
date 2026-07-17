import os

def check_file():
    filename = input("Enter the filename: ")

    if os.path.isfile(filename):
        print("File Found")
    else:
        print("File Not Found")

check_file()
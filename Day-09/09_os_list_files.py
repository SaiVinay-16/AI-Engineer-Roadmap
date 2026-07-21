import os

current_directory = os.getcwd()

items = os.listdir(current_directory)

print("Current Directory:", current_directory)
print("Files and Folders:")
for item in items:
    print("-", item)
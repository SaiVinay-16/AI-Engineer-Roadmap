import os

def directory_info():
    # Get current working directory
    current_dir = os.getcwd()
    print(f"📂 Current Directory: {current_dir}")

    # List all items in the directory
    items = os.listdir(current_dir)

    # Count files and folders
    file_count = sum(1 for item in items if os.path.isfile(os.path.join(current_dir, item)))
    folder_count = sum(1 for item in items if os.path.isdir(os.path.join(current_dir, item)))

    print(f"📄 Number of Files: {file_count}")
    print(f"📁 Number of Folders: {folder_count}")

# Run the function
if __name__ == "__main__":
    directory_info()
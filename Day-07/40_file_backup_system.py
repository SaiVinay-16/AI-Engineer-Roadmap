import os
import shutil

def create_backup():
    try:
        filename = input("Enter the filename to back up: ")

        if not os.path.exists(filename):
            print("Error: File does not exist.")
            return

        backup_filename = filename.replace(".txt", "_backup.txt")

        shutil.copy(filename, backup_filename)
        print(f"Backup created successfully → {backup_filename}")

    except Exception as e:
        print(f"Unexpected error: {e}")

create_backup()
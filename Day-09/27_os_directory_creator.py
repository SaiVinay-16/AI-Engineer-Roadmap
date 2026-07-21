import os
file_name="rough.py"
if not os.path.exists(file_name):
    os.mkdir(file_name)
    print(file_name," created successful")
else:
    print(f"{file_name} already exists")
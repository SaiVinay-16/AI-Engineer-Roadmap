# move the terminal path to this folder
import os
if os.path.isfile('sample.txt'):
    print("Exists")
else:
    print("Not exists")
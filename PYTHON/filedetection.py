# Python file detection
# There are 2 types of file paths
# 1. Relative file path
#       folder/test.txt
# 2. Absolute file path
#       C:/Users/BroCode/Desktop/test.txt

import os

file_path = "PYTHON/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
    
else:
    print("That location doesn't exist")
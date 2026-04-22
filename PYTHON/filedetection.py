# Python file detection
# There are 2 types of file paths
# 1. Relative file path
#       folder/test.txt
# 2. Absolute file path
#       C:/Users/BroCode/Desktop/test.txt

# import os

# file_path = "PYTHON/test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
    
# else:
#     print("That location doesn't exist")


# 1. Document Checker
# A company's document management system needs to verify files before processing.
# Write a program that checks if a file called "invoice.txt" exists in a folder called "documents".
# If it exists print whether it is a file or directory.
# If it doesn't exist print "invoice.txt not found".
# Create the file/folder manually on your system to test both cases.

# import os

# file_path = "documents/invoice.txt"

# if os.path.exists(file_path):
#     print(f"That location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     if os.path.isdir(file_path):
#         print("That is a directory")
# print(f"That location {file_path} doesn't exist")
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

# 2. Spot the Bug
# The following file detection code has a bug —
# it always prints "That is a file" even for directories.
# Identify and fix it:

# import os

# path = "PYTHON/files"

# if os.path.exists(path):
#     if os.path.isfile(path):
#         print("That is a file")
#     if os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("Path doesn't exist")

# 3. File Extension Checker
# A media platform only accepts certain file types.
# Write a program that takes a filename like "video.mp4" and checks if it exists.
# If it does, use os.path.splitext() to extract the extension
# and print whether it is a ".mp4", ".jpg", or ".pdf" — printing "Unsupported file type" for anything else.
# This introduces os.path.splitext() — look it up and figure out what it returns.

# import os

# file_name = "PYTHON/video.mp3"

# if os.path.exists(file_name):
#     print(f"The file {file_name} exists")
#     root, ext = os.path.splitext(file_name)
#     print(f"It as a {ext} file")
# else:
#     print(f"The file {file_name} doesn't exist")

# 4. Backup System
# A backup system checks if files exist before copying them.
# Write a program that checks a list of 5 filenames —
# ["report.txt", "data.csv", "image.jpg", "notes.txt", "archive.zip"] —
# and separates them into two lists: files_found and files_missing.
# Print both lists at the end. Create at least 2 of the files on your system to test it.

# import os

# file_names = ["PYTHON/report.txt", "PYHTON/data.csv", "PYTHON/image.jpg", "PYTHON/notes.txt", "PYTHON/archive.zip"]
# files_found = []
# files_missing = []

# for file_name in file_names:
#     if os.path.exists(file_name):
#         print(f"That file {file_name} exists")
#         files_found.append(file_name)
#     else:
#         print(f"That file {file_name} doesn't exist")
#         files_missing.append(file_name)

# for file_name in files_found:
#     print(file_name)
# print(" ")

# for file_name in files_missing:
#     print(file_name)

# 5. Directory Scanner
# A file management tool scans a directory and categorizes its contents.
# Write a program that uses os.listdir() to list everything inside a folder,
# then separates the contents into two lists — files and subdirectories.
# Print the count of each.
# This introduces os.listdir() — figure out what it returns
# and how to use it with os.path.isfile() and os.path.isdir().

import os

directory_files = []
directory_subdirectories = []

directory_contents = os.listdir("PYTHON")
# print(directory_contents)
for directory_content in directory_contents:
    if os.path.isfile(directory_content):
        directory_files.append(directory_content)
    if os.path.isdir(directory_content):
        directory_subdirectories.append(directory_subdirectories)

print("------PYTHON FILES-----")
for i, directory_file in directory_files:
    print(f"{i}. {directory_file}")
    print(" ")

print(" ")
print("-----PYTHON SUBDIRECTORIES-----")
for i, directory_subdirectory in directory_subdirectories:
    print(f"{i}. {directory_subdirectory}")






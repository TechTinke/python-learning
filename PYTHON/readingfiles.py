#Python reading files(.txt, .json, .csv)

import json #importing the json module
import csv #importing the csv module

# file_path = "PYTHON/output.txt"
# file_path = "PYTHON/output.json"
file_path = "PYTHON/output.csv"

#with statement is used to wrap a block of code within a context manager
try:
    with open(file=file_path, mode="r") as file:
        # content = file.read() #.txt file
        # content = json.load(file) # .json file
        content = csv.reader(file) # .csv file but this returns a memory address
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read this file")



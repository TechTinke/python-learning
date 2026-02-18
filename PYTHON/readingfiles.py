#Python reading files(.txt, .json, .csv)

import json #importing the json module
import csv #importing the csv module

# file_path = "PYTHON/output.tx"
    
file_path = "PYTHON/output.json"
#with statement is used to wrap a block of code within a context manager

try:
    with open(file=file_path, mode="r") as file:
        # content = file.read() #.txt file
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read this file")



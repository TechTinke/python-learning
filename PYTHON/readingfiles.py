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



# WORK TO BE DONE 
# 1. Simple Log Writer
# Write a function log_message(filename: str, message: str) that:
# Opens file in append mode ("a")
# Writes message + timestamp (use datetime.datetime.now())
# Uses with statement
# Handles PermissionError with friendly message
# Call it 3 times with different messages and check the file.


# 2. Read First Line of File
# Write read_first_line(filename: str) -> str that:
# Opens file in read mode
# Returns first line (stripped)
# Returns "File empty" if no lines
# Handles FileNotFoundError
# Test with existing and non-existing files.


# 4. CSV Employee Report Generator (partial code)
# Finish this script:

# Pythonimport csv
# from datetime import datetime

# def write_employee_report(filename: str, employees: list[list]):
#     # employees = [["Name", "Age", "Salary"], ["Oscar", 25, 80000], ...]
#     try:
#         with open(filename, mode="w", newline="") as file:
#             writer = csv.writer(file)
#             # Finish: write header + all rows
#             # Add timestamp comment at top: "# Generated on {datetime.now()}"
#         print(f"Report saved to {filename}")
#     except PermissionError:
#         print("Permission denied")
#     except Exception as e:
#         print(f"Error: {e}")

# # Demo data
# data = [
#     ["Name", "Age", "Salary"],
#     ["Oscar", 25, 80000],
#     ["Arry", 24, 65000],
#     ["Eugene", 30, 95000]
# ]

# # Finish: call the function + read back and print the file content


# 4. JSON Config File Manager
# Create functions:
# save_config(filename: str, config: dict) → write dict as JSON with indent=4
# load_config(filename: str) -> dict → read JSON, return dict or empty dict on error
# update_config(filename: str, key: str, value) → load → update → save
# Demo: save config, update one key, load and print.


# 5. Append-Only Log System with Rotation
# Write a script that:
# Appends messages to app.log
# If file > 1MB, rename to app.log.1, create new app.log
# Use os.path.getsize() to check size
# Handle file not found on first write
# Run a loop that appends 100 messages → show rotation.


# 6. CSV Reader & Analyzer
# Read a CSV file with columns: Name, Age, Salary
# Functions:
# load_employees(filename) → return list of dicts
# average_salary(employees) → compute average
# highest_paid(employees) → return name + salary
# Print average salary and highest paid person.


# 7. Backup File Copier
# Create backup_files(source_dir: str, backup_dir: str) that:
# Lists all .txt files in source_dir
# Copies each to backup_dir with timestamp prefix (e.g. 2026-03-02_report.txt)
# Use shutil.copy()
# Handle missing source dir or permission errors
# Test with a small folder.


# 8. JSON User Database (mini-project)
# Build functions for a simple "database":
# add_user(filename: str, user: dict) → append user to list in JSON file
# get_user(filename: str, name: str) -> dict → find by name
# delete_user(filename: str, name: str) → remove from list, rewrite file
# Use json.load/dump with indent=2
# Demo adding 3 users, getting one, deleting one.


# 9. CSV to JSON Converter
# Read a CSV file (Name, Age, City)
# Convert each row to dict
# Save as JSON array of objects
# Handle missing columns or bad data gracefullyExample input CSV → output JSON file.


# 10. Multi-File Logger with Thread Safety (longer)
# Create a logger that writes to different files based on category (error.log, info.log).
# Use threading.Lock() to make it thread-safe
# Functions:
# log(category: str, message: str) → append to correct file
# Use with lock: around write
# Start 5 threads that log random messages to random categories
# Show no data corruption even with concurrent writes.
# Python writing files (.txt, .json, .csv)
#csv - comma seperated values - common with spreadsheet data
import json #help with the json module
import csv #help with csv module

# txt_data = "I like pizza"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]


# Absolute file path - gives the full complete location of the file
# Relative file path - described relatively to your working directory

file_path = "PYTHON/output.csv"  #Relative file path
# file_path = "C:\Users\HP\Desktop\output.txt" #Absolute file path

try:
    with open(file=file_path, mode="w", newline="") as file:  # with is used to wrap a block of code to execute # with will close the file the same way it opens it #"w" is for writing the file #as keyword is used to give it a name
        # file.write("\n" + employees) #write() is used for a string and not a list
        # for employee in employees:
        #     file.write("\n" + employee)
        # json.dump(employee, file, indent=4)#convert our dictionary to a json string
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file '{file_path}' was created")

except FileExistsError:
    print("That file already exists")

# There are different modes
# "w" - writing a file / overwriting the file
# "x" - writing a file if it doesn't exist
# "r" - reading a file
# "a" - appending / updating the data in the file

# txt_data = "I love my girlfriend"

# file_path = "PYTHON/girlfriend.txt"

# with open(file=file_path, mode= "w") as file:
#     file.write(txt_data)

# .json is made of key value pairs like in a dictionary

            # {
            #     "firstName": "Joe",
            #     "lastName": "Jackson",
            #     "gender": "male",
            #     "address": {
            #         "streetAddress: "101",
            #         "city": "San Diego",
            #         "state": "CA"
            #     },
            #     "phoneNumbers": [
            #         {"type": "home", "number": "7349282382"}
            #     ]
            # }
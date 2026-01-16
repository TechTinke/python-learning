#Membership Operators - used to test whether a value or variable is found in a sequence which include but not limited to
#                       (list, tuple, string, set or ditionary)
#                       1. in
#                       2. not in

#1. String
word = "Apple"

letter = input("Guess a letter in the secret word: ")

if letter not in word: #in is the membership operator used to check whether the value/variable is found within the sequence
    print(f"Your letter {letter} was not found")
else:
    print(f"Your letter {letter} is in the secret word")

#2. Set
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")

#3. Dictionary
grades = {"Sandy": "A",
         "Squidward": "B",
         "Spongebob": "C",
         "Patrick": "D"
}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")

order = {"Morris": "Pilau",
         "Oscar": "Biryani Chicken",
         "Natash": "Fish Chips",
         "Deborah": "Ugali Matoke"
}

order_for = input("Please enter your name: ")

if order_for not in order:
    print("Your order was not found")
else:
    print(f"The order for {order_for} is {order[order_for]}")

email = "maingioscar2@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Email is invalid")
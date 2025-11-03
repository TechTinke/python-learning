#while loop = execute some code WHILE some condition remains TRUE until the condition is no longer true
#preferred for execution for an infinite number of times

#EXAMPLE 1
name = input("Please enter your name: ")

while name == "":
    print("You did not enter your name")
#take care of INFINITE LOOPS which might cause the program to crash when executed when there is no exit for the loop
    name = input("Please enter your name: ")
print(f"Hello, {name}")

#EXAMPLE 2
age = int(input("Enter your age: "))

while age <0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

#EXAMPLE 3
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("Bye")

#EXAMPLE 4

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 9:
    print(f"Please enter a number within the given range. {num} is not within the range")
    num = int(input("Enter a number between 1-10: "))
print(f"Your number is {num}")

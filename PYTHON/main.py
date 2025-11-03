#tThis is my first Python program
print("I like chicken")
print("It's really fantastic") 
#Variable = A re-usable container for storing values (string, integer, float, boolean)

#Strings - series of characters(text)
first_name = "Anne"
food = "Chicken"
email = "maingioscar2@gmail.com"

#to  use formatted string literals, begin with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a python expression between {and} characters that can refer to variables or literal values.
print(f"Hello {first_name}")
print(f"Yula loves {food}")
print(f"Your email is {email}")

#Integer - whole numbers
age = 25
quantity = 3
num_of_students = 36

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f" Your class has {num_of_students}")

#Float - cNumbers that contain a decimal portion 
price = 10.99
gpa = 4.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} miles")

#Boolean - true/false
is_student = True
for_sale = False
is_online = False
if is_student:
    print("You are a student")

else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")
if is_online:
    print("The user is online")
else:
    print("The user is offline")


#typecasting - the process of converting a value of one data type to another
#You can do this EXPLICITLY or IMPLICITLY

#EXPLICIT TYPECASTING- manual conversion using cast words like bool, str, int or float
name = "Yula"
age = 0
gpa = 4.2
student = True

age = float(age)
gpa = int(gpa)
student = str(student)
age = bool(age)
name = bool(name)

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
print(age)
print(gpa)
print(student)
print(name)

#IMPLICIT TYPECASTING - a value or variable is converted into a different data type automatically 
#This happens when certain arithmetic operations are performed such as division
x = 2
y = 2.0

x = x/y

print(x)
print(type(x))


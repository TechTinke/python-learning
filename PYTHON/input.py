name = input("Enter your name:")
#User input is always a string. You can convert it to any other data type that you want like in the example below
age = int(input("Enter your age:"))
age = age + 1
print(f"Hello {name}. I missed you")
print(f"You are {age} years old")
print(type(name))
print(type(age))

#if = Do some code only IF some condition is True
     #ELSE something else is done

#age = int(input("Please enter your age: "))


#if age >= 100:
   # print("You are too old to be signed up")
#elif age <0:
#    print("You haven't been born yet")
#elif age <18:
   # print("You must be 18+ to sign up")
#else:
   # print("You are now signed up")

#response = (input("Would you like some food?(Y/N): "))

#if response == "Y":
    #print("Have some food")
#elif not response == "N":
    #print("Please enter a valid answer")

#else:
   # print("You  will NOT have some food")

#name = input("Enter your name: ")

#if name == "":
    #print("You did not type in your name")
#else:
    #print(f"Hello, {name}")

#online = False

#if online:
   # print("This user is online")
#else:
   # print("The user is offline")

#PYTHON CALCULATOR

operator = input("Please enter an operator:(+ * / -): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Your result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Your result is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Your result is {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Your result is {result}")
elif not operator == "+" or operator == "-" or operator == "*" or operator == "/":
    print("Please enter a valid operator.") 
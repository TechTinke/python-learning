# exception =   An event that interrupts the flow of a program
#               (ZeroDivisionError, TypeError, ValueError)
# - ValueError triggers when you pass the right type but wrong value like int("pizza").
# - TypeError triggers when you pass the wrong type entirely like "Hoes" / 90.

#               1. try, 2. except, 3. finally

# ZeroDivisionError - occurs when you divide a number by 0
# 1 / 0

#TypeError - when we attempt to perform an operation on value of wrong data type
# 1 + "pizza"

#ValueError - typecast a value of the wrong data type
# int("pizza")

# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You can't divide by 0")
# except ValueError:
#     print("Enter only numbers please")
# except Exception:
#     print("Something went wrong")
# finally:
#     print("Do some cleanup here")

# 1. ATM Withdrawal
# A bank ATM needs to handle errors gracefully.
# Write a function withdraw(balance, amount) that divides the balance by the amount.
# Handle a ZeroDivisionError if amount is 0, a ValueError if a non-number is passed,
# and use finally to always print "Transaction complete."
# Test with three cases — a valid withdrawal, a zero amount, and a string amount.

# def withdraw(balance, amount):
#     try:
#         balance_amount = balance / amount
#         print(f"{balance} / {amount} = {balance_amount}")
#         print("Transaction complete")
#     except ZeroDivisionError:
#         print("Amount can't be zero")
#     except TypeError:
#         print("Please enter a number")
       

# withdraw(56000, 0)
# print(" ")
# withdraw("Hoes", 90)
# print(" ")
# withdraw(56000, 6890)
# print(" ")

# 2. Spot the Bug
# The following exception handling code has a bug —
# it never reaches the specific error handlers.
# Identify and fix it:
# try:
#     age = int(input("Enter your year of birth: "))
#     print(f"Your age is {2026 - age}")
# except ValueError:
#     print("Please enter a valid number")
# except Exception: #Exception is the parent class of all exceptions. IT ALWAYS COMES LAST!
#     print("Something went wrong")

# 3. Custom Exception
# A voting system needs to reject underage voters.
# Create a custom exception class UnderageVoterError that inherits from Exception.
# Write a function register_voter(name, age) that raises UnderageVoterError
# if age is below 18 with the message "{name} is too young to vote".
# Handle it with a try/except block and test with both a valid and invalid age.

class UnderageVoterError(Exception):
    pass
def register_voter(name, age):
            if age < 18:
                  raise UnderageVoterError(f"{name} is too young to vote")
            else:
                  print(f"{name} is eligible to vote")
try:
    register_voter("Oscar", 14)

except UnderageVoterError as e:
      print(e)
    
            


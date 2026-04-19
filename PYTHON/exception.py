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

def withdraw(balance, amount):
    try:
        balance_amount = balance / amount
        print(f"{balance} / {amount} = {balance_amount}")
        print("Transaction complete")
    except ZeroDivisionError:
        print("Amount can't be zero")
    except TypeError:
        print("Please enter a number")
       

withdraw(56000, 0)
print(" ")
withdraw("Hoes", 90)
print(" ")
withdraw(56000, 6890)
print(" ")
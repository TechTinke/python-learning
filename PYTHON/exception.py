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

# class UnderageVoterError(Exception):
#     pass
# def register_voter(name, age):
#             if age < 18:
#                   raise UnderageVoterError(f"{name} is too young to vote")
#             else:
#                   print(f"{name} is eligible to vote")
# try:
#     register_voter("Oscar", 14)

# except UnderageVoterError as e:
#       print(e)


# 4. File Reader
# A document processing system reads files.
# Write a function read_file(filename) that opens and reads a file.
# Handle FileNotFoundError if the file doesn't exist, PermissionError if the file can't be accessed,
# and use finally to print "File operation attempted."
# Test by passing a filename that doesn't exist on your system.

# def read_file(filename):
#     file = open(filename, "r") #raises FileNotFoundError
#     content = file.read()
#     print(content)
#     file.close()
# try:
#     read_file("oscar")
# except FileNotFoundError:
#     print("File doesn't exist!")
# except PermissionError:
#     print("You don't have the permission to access the file")
# finally:
#     print("File operation attempted")

# 5. Multiple Custom Exceptions
# An e-commerce checkout system needs specific error handling.
# Create three custom exceptions — OutOfStockError, InvalidQuantityError (quantity must be positive),
# and PaymentFailedError. Write a function place_order(item, quantity, payment_valid)
# that raises the appropriate exception based on the situation. Handle each separately and test all three error cases.

# class OutOfStockError(Exception):
#     pass
# class InvalidQuantityError(Exception):
#     pass
# class PaymentFailedError(Exception):
#     pass

# def place_order(item, quantity, payment_valid):
#     if not payment_valid:                        
#         raise PaymentFailedError("Payment is invalid")
#     if quantity == 0:
#         raise OutOfStockError(f"{item} is out of stock")
#     elif quantity < 0:                           
#         raise InvalidQuantityError("Quantity must be greater than 0")
#     print(f"Order placed for {quantity}x {item} successfully!")

# try:
#     place_order("Cedar", 9, False)
# except OutOfStockError as e:
#     print(e)
# except InvalidQuantityError as e:
#     print(e)
# except PaymentFailedError as e:
#     print(e)

# print(" ")

# try:
#     place_order("Yoghurt", 0, True)
# except OutOfStockError as e:
#     print(e)
# except InvalidQuantityError as e:
#     print(e)
# except PaymentFailedError as e:
#     print(e)

# print(" ")

# try:
#     place_order("Apple", -9, True)
# except OutOfStockError as e:
#     print(e)
# except InvalidQuantityError as e:
#     print(e)
# except PaymentFailedError as e:
#     print(e)

# 6. Exception Chaining
# A user authentication system logs errors with context.
# Write a function authenticate(username, password) that tries to look up a user from a dictionary.
# If the user doesn't exist, catch the KeyError and raise a new AuthenticationError
# using raise AuthenticationError("Login failed") from original_error.
# This is called exception chaining — explain what the from keyword adds and
# why it is useful in production systems.

# system_users = {"Oscar": "oskrr4567",
#                 "Mlewa": "mlewa1234"}

#NB: indexing a key from a dictionary gives back the value
# class AuthenticationError(Exception):
#     pass
# def authenticate(username, password):
#     try:
#         username_password = system_users[username]
#     except KeyError as e:
#         raise AuthenticationError("Login failed - User not found") from e # Exception Chaining # from keyword attaches the original KeyError as the cause
    
#     if username_password != password:
#         raise AuthenticationError("Login failed - Wrong password")
#     print("Successful login")
# try:
#     authenticate("Oscar", "oskrr4567")
# except AuthenticationError as e:
#     print(e)

# print(" ")

# try:
#     authenticate("Oscr", "oskrr467")
# except AuthenticationError as e:
#     print(e)

# print(" ")

# try:
#     authenticate("Oscar", "yiw7")
# except AuthenticationError as e:
#     print(e)

# 7. Retry with Custom Exceptions
# A flight booking system retries failed API calls.
# Create a custom APITimeoutError exception.
# Write a function book_flight(destination) that randomly raises APITimeoutError 60% of the time.
# Write a retry(func, max_attempts) function that retries the function up to max_attempts times,
# catching APITimeoutError each time and printing "Timeout, retrying...".
# If all attempts fail raise a final APITimeoutError with the message "Booking service unavailable
#   after {max_attempts} attempts".

# import random

# class APITimeoutError(Exception):
#     pass

# def book_flight(destination):
#     if random.random() < 0.6:
#         raise APITimeoutError("Connection timeout")
#     print(f"Flight to {destination} booked successfully")

# def retry(func, max_attempts):
#     for attempt in range(max_attempts):
#         try:
#             func()
#             break
#         except APITimeoutError:
#             print(f"Attempt {attempt + 1} failed, retrying...")
#     else:
#         raise APITimeoutError(f"Booking service unavailable after {max_attempts} attempts")

# retry(lambda:book_flight("Nairobi"), 3) # lambda lets you pass book_flight WITH its argument as a function

# 8. Context Manager with Exceptions
# A database system needs to ensure connections are always closed even when errors occur.
# Write a class DatabaseConnection with __enter__ and __exit__ methods — __enter__ prints "Connection opened"
# and returns the connection, __exit__ prints "Connection closed"
# and handles any exceptions that occur inside the with block.
# Use it with a with statement and deliberately raise an exception inside the block
# to show the connection still closes.

# class DatabaseConnection():
#     def __enter__(self):
#         print("Connection opened")
#         return self
#     def __exit__(self, exc_type, exc_val, tb): #exc_type - exception type(TypeError, ValueError, KeyError)
#         #exc_val - exception message
#         #tb - traceback
#         print("Connection closed")
#         if exc_type:
#             print(f"Error handled: {exc_val}")
#         return True # Suppresses the exception and thus the program continues
#         # return False # Re-raises the exception and thus the program crashes
# with DatabaseConnection() as db:
#     print("Doing some database work")
#     raise Exception("Something went wrong")
#     print("This never works")

# 9. Exception Hierarchy
# A payment processing system has a hierarchy of exceptions.
# Create a base PaymentError exception,
# then create child exceptions InsufficientFundsError, CardExpiredError, and NetworkError —
# all inheriting from PaymentError.
# Write a function process_payment(amount, card) that raises different exceptions based on conditions.
# Write TWO exception handlers — one that catches specific child exceptions
# and one that catches the parent PaymentError — and demonstrate that catching the parent catches all children 
# but loses specificity.

# class PaymentError(Exception):
#     pass
# class InsufficentFundsError(PaymentError):
#     pass
# class CardExpiredError(PaymentError):
#     pass
# class NetworkError(PaymentError):
#     pass

# def process_payment(amount, card):
#     if card == None:
#         raise NetworkError("No card has been detected - Network Error")
#     if amount < 1000:
#         raise InsufficentFundsError("Insufficient funds - Please top up your account")
#     if card == "expired":
#         raise CardExpiredError("Your card has expired, please try another card")
#     print(f"Payment of {amount} has been processed successfully!")

# try:
#     process_payment(6970, None)
# except NetworkError as e:
#     print(e)
# except InsufficentFundsError as e:
#     print(e)
# except CardExpiredError as e:
#     print(e)

# print(" ")

# try:
#     process_payment(8900, None)
# except PaymentError as e:
#     print(f"Payment failed: {e}")


# 10. Global Exception Handler — Production Logger
# A production web server needs to handle all unexpected errors gracefully without crashing.
# Write a decorator handle_exceptions(func) that wraps any function in a try/except block,
# catches all exceptions, logs the error with the function name, exception type, and
# message to a list called error_log, and returns None instead of crashing.
# Apply it to three different functions that raise different exceptions.
# After running all three print the full error_log.
# This pattern is used in every production web framework —
# explain why returning None instead of crashing is critical in a live server.

import traceback

error_log = []

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_log.append({
                "function": func.__name__,        # ✅ Function name
                "exception_type": type(e).__name__, # ✅ Exception type
                "message": str(e)                  # ✅ Exception message
            })
            return None                            # ✅ Returns None instead of crashing
    return wrapper

@handle_exceptions
def process_order(order_id):
    raise ValueError(f"Invalid order ID: {order_id}")

@handle_exceptions
def send_email(recipient):
    raise ConnectionError(f"Could not connect to mail server for {recipient}")

@handle_exceptions
def calculate_discount(price):
    raise ZeroDivisionError("Cannot divide discount by zero!")

# Run all three — none of them crash the program
print("-----RUNNING FUNCTIONS-----")
process_order(999)
send_email("oscar@gmail.com")
calculate_discount(5000)
print("All functions ran without crashing!")

# Print the full error log
print(" ")
print("-----ERROR LOG-----")
for error in error_log:
    print(f"Function : {error['function']}")
    print(f"Exception: {error['exception_type']}")
    print(f"Message  : {error['message']}")
    print(" ")
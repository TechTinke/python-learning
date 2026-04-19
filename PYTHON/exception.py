# exception =   An event that interrupts the flow of a program
#               (ZeroDivisionError, TypeError, ValueError)
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
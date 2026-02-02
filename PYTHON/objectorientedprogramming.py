#object = A "bundle" of related attributes(variables) and methods(functions) 
#         Ex. A phone, A cup, A book
#         You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object
#methods are actions that an object can perform

from classcar import *

car1 = Car("Mustang", 2026, "Red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car2.drive()
car1.stop()
car1.describe()

#WORK TO BE DONE
# 1. Library Management System
# Build a Library class that manages books and members.
# Attributes: name (str), books (list of Book objects), members (list of Member objects)
# Methods to implement:
# add_book(title, author, isbn) → creates a Book and adds it
# register_member(name, member_id) → creates a Member and adds it
# lend_book(isbn, member_id) → marks book as checked out to that member (only if available)
# return_book(isbn) → marks book as available again
# list_overdue_books(current_date) → prints books that are overdue (assume each Book has due_date)

# Then write example code that: creates a library, adds 3 books, registers 2 members, lends/returns some books, and shows overdue ones.
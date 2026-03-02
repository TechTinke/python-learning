# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behaviour of objects

class Book():

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self): #Creating a string representation of the object
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other): # Compare of two objects are equal
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

        

book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
book2 = Book("Harry Porter and The Philosopher Stone", "J.K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkein", 310)

print(book1)  #returns a memory address when __str__ is not defined
print(book2)
print(book3)
print(book1 == book4)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print("Lion" in book3)
print(book3['audio'])

# WORK TO BE DONE
# 1. Custom Vector Class
# Create a Vector2D class with:
# __init__(self, x, y)
# __str__(self) → returns "(x, y)"
# __add__(self, other) → returns new Vector2D with summed components
# __eq__(self, other) → True if both x and y match
# Show: create two vectors, add them, compare equality, print them.

#2. Temperature with Unit Conversion
# Create Temperature class:
# __init__(self, value, unit="C")
# __str__(self) → "25.0°C" or "77.0°F"
# __eq__(self, other) → compares after converting both to Celsius
# __lt__(self, other) → compares after conversion
# Demonstrate comparing Celsius and Fahrenheit objects.

# 3. Shopping Cart with Magic Methods (partial code)
# Finish/extend this class:

# Pythonclass ShoppingCart:
#     def __init__(self):
#         self.items = {}  # item_name: quantity

#     def add_item(self, item_name, quantity=1):
#         self.items[item_name] = self.items.get(item_name, 0) + quantity

#     # Finish: __str__ → "Cart: Apple x2, Banana x1 (Total items: 3)"
#     def __str__(self):
#         pass

#     # Finish: __len__ → total quantity of all items
#     def __len__(self):
#         pass

#     # Finish: __contains__ → check if item_name in cart
#     def __contains__(self, item_name):
#         pass

#     # Finish: __getitem__ → return quantity of item_name or 0
#     def __getitem__(self, item_name):
#         pass

#     # Finish: __iadd__ → allow cart1 += cart2 (merge items)
#     def __iadd__(self, other):
#         pass
# Then show usage: create two carts, add items, merge them, check length/contains/getitem, print cart.

# 4. Fraction Class (mathematical object)
# Create Fraction:
# __init__(self, numerator, denominator)
# __str__(self) → "3/4"
# __repr__(self) → "Fraction(3, 4)" (for debugging)
# __add__(self, other) → return new Fraction (sum)
# __eq__(self, other) → compare value (not just numerator/denominator)
# __lt__(self, other) → compare value
# __float__(self) → return float value
# Show adding fractions, comparing them, converting to floatFraction Class (mathematical object)

# 5. Custom Dictionary with Case-Insensitive Keys
# Create CaseInsensitiveDict:
# Inherits from dict
# Override __setitem__, __getitem__, __contains__, __delitem__ to treat keys case-insensitively
# __str__ → pretty print like normal dict
# Show: add keys "Name" and "name", they overwrite each other, "NAME" in dict returns True.

# 6. Game Inventory System
# Create Inventory:
# __init__(self) → self.slots = {}
# __str__(self) → "Inventory: Sword x1, Potion x5"
# __len__(self) → total item count
# __contains__(self, item_name) → check if item exists
# __getitem__(self, item_name) → return quantity or raise KeyError
# __setitem__(self, item_name, quantity) → set quantity (allow 0 to remove)
# __add__(self, other) → merge two inventories
# Build a player inventory, add/remove items, merge with another player's loot.

# 7. Money / Currency Class
# Create Money:
# __init__(self, amount: float, currency="KES")
# __str__(self) → "KES 1,250.50"
# __repr__(self) → "Money(1250.50, 'KES')"
# __add__(self, other) → same currency only, return new Money
# __eq__(self, other) → same amount and currency
# __lt__(self, other) → compare amounts (same currency)
# __float__(self) → return amount as float
# Show adding money, comparing, converting to float.

# 8. Task Scheduler with Priority Queue
# Create Task:
# __init__(self, description, priority=1)
# __lt__(self, other) → higher priority (lower number) comes first
# __str__(self) → "Task: Fix bug (Priority: 1)"
# Create Scheduler:
# Uses heapq internally
# __len__, __contains__, __iter__
# Add tasks, pop highest priority
# Show scheduling tasks, printing queue.

# 9. Custom List with Statistics
# Create SmartList:
# Inherits from list
# __init__(self, *args)
# __str__(self) → list + " (avg: X, min: Y, max: Z)"
# __add__ → concatenate and return new SmartList
# __iadd__ → extend in place
# Add property or method for average/min/max
# Show creating, adding, printing with stats.

# 10. Coordinate Point in 3D Space (longer design)
# Create Point3D:
# __init__(self, x, y, z)
# __str__(self) → "(x, y, z)"
# __repr__(self)
# __eq__(self, other) → exact match
# __add__(self, other) → vector addition
# __sub__(self, other) → vector subtraction
# __mul__(self, scalar) → scalar multiplication
# __len__(self) → Euclidean distance from origin
# __getitem__(self, index) → x=0, y=1, z=2
# Show vector math, distance calculation, indexing.

#@property = Decorator used to define a method(function) as a property(it can be accessed like an attribute/variable)
#            Benefit: Add additional logic when read, write or delete attributes
#            Gives you getter to read, setter to write and deleter to delete method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # width and height are internal/protected members of the class Rectangle
        # They are only meant to be used inside of the class
        # If we need to get the width and height, we use the getter methods below provided by @property decorator
        # @property decorator helps us add additional logic when reading a method
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 10

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)

# WORK TO BE DONE
# 1. Temperature Class with Conversion
# Create a Temperature class:
# Internal: self._celsius
# @property def celsius(self) → return formatted "25.0°C"
# @property def fahrenheit(self) → computed: (celsius × 9/5) + 32
# @celsius.setter → validate > -273.15, convert input if needed
# @fahrenheit.setter → convert back to celsius
# Show: set in Fahrenheit, read in Celsius (and vice versa).

# 2. User Age with Validation
# Create User with:
# self._birth_year
# @property def age(self) → compute current age (use datetime)
# @age.setter → not allowed (raise AttributeError: "Age is read-only")
# @property def is_adult(self) → age >= 18
# Demonstrate read-only computed age + adult check.

# 3. Bank Account with Balance Control (partial code)
# Finish this:

# Pythonclass BankAccount:
#     def __init__(self, holder, initial_balance=0.0):
#         self._balance = initial_balance
#         self.holder = holder

#     @property
#     def balance(self):
#         # Finish: return formatted "KES 1,250.50"
#         pass

#     @balance.setter
#     def balance(self, new_balance):
#         # Finish: only allow increase (deposit), reject decrease
#         # Print message if invalid
#         pass

#     @property
#     def can_withdraw(self):
#         # Finish: True if balance >= 100
#         pass

#     def withdraw(self, amount):
#         if self.can_withdraw and amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew KES {amount:,.2f}")
#         else:
#             print("Insufficient funds or below minimum")
# Then: create account, try invalid set, withdraw, check can_withdraw.

# 4. Product Price with Discount Rules
# Create Product:
# Internal: self._price, self._discount_percent = 0
# @property def price(self) → return discounted price (price × (1 - discount/100)) formatted
# @price.setter → validate price > 0
# @property def discount(self) → return current %
# @discount.setter → 0–75%, else raise ValueError
# @property def original_price(self) → raw price
# Show: set price, apply discount, read final price vs original.

# 5. Game Player Stats with Level-Up
# Create Player:
# Internal: self._level = 1, self._xp = 0
# @property def level(self) → return current level
# @property def xp(self) → return current xp
# @xp.setter → add xp, auto level-up if >= 100 × level
# @property def max_health(self) → 100 + level × 20
# @property def is_max_level(self) → level >= 50
# Show gaining xp, auto-leveling, reading health.

# 6. Employee Salary with Tax Bracket
# Create Employee:
# Internal: self._salary
# @property def salary(self) → formatted monthly salary
# @salary.setter → validate > 0, apply company rules
# @property def annual_salary(self) → salary × 12
# @property def tax_rate(self) → computed: 10% if < 50k, 25% if < 200k, 30% above
# @property def net_salary(self) → salary - (salary × tax_rate)
# Create employees, set salary, read net pay.

# 7. Configuration with Read-Only & Computed Settings
# Create AppConfig:
# Internal dict self._config = {}
# @property def theme(self) → return self._config.get("theme", "light")
# @theme.setter → only allow "light", "dark", "auto"
# @property def debug_mode(self) → bool from config
# @debug_mode.setter → log change (print "Debug mode changed")
# @property def version(self) → always "v2.1.0" (read-only)
# @version.setter → raise AttributeError("Version is read-only")
# Show setting theme, toggling debug, trying to change version.

# 8. Rectangle Area & Perimeter (your example expanded)
# Extend your Rectangle:
# @property def area(self) → width × height
# @property def perimeter(self) → 2 × (width + height)
# @property def diagonal(self) → sqrt(width² + height²)
# @property def is_square(self) → width == height
# @width.setter & @height.setter → update and print "Dimensions updated"
# Show creating rectangle, changing size, reading computed properties.

# 9. Shopping Cart Total with Tax
# Create Cart:
# Internal: self._items = {} (name: (price, qty))
# @property def subtotal(self) → sum(price × qty)
# @property def tax(self) → 16% of subtotal
# @property def total(self) → subtotal + tax
# @property def item_count(self) → sum quantities
# @property def is_empty(self) → item_count == 0
# Method add_item(self, name, price, qty=1)
# Show adding items, reading total/tax, checking empty.

# 10. User Profile with Lazy-Computed Fields
# Create UserProfile:
# Internal: self._birth_date, self._full_name
# @property def age(self) → computed from birth_date (use datetime)
# @property def initials(self) → first letters of full_name
# @property def email_domain(self) → extract from email if set
# @full_name.setter → split and store first/last name separately
# @birth_date.setter → validate date format, update age cache if needed
# Show setting name/birth, reading age/initials.

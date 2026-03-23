# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
#                 Best for class level data or require access to the class itself

# Class Methods deal with class level data such as class variables or behaviour
# Instance  Methods deal with individual instances(objects) belonging to a class

# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1 #Increase count by 1 for every student that is created
#         Student.total_gpa += gpa
    
#     #Instance Method
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     #Class Method 1
#     @classmethod
#     def get_count(cls):
#         return f"Total no of students: {cls.count}"
    
#     #Class Method 2
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
    
# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())

# WORK TO BE DONE
# 1. Library Book Tracker
# Create a Book class with:
# Class variables: total_books = 0, borrowed_count = 0
# __init__(self, title, author) → increment total_books
# Instance method borrow(self) → increment borrowed_count if not already borrowed
# Class method @classmethod def get_availability(cls) -> str → returns f"{cls.total_books - cls.borrowed_count} books available"

# class Book():

#     total_books = 0
#     borrowed_count = 0

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#         Book.total_books += 1
    
#     def borrow(self):
#         if self.is_borrowed:
#             print("This book is already borrowed")
#         else:
#             self.is_borrowed = True
#             Book.borrowed_count += 1
#             print(f"You borrowed '{self.title}' by {self.author}")
    
#     @classmethod
#     def get_availability(cls):
#         available_books = cls.total_books - cls.borrowed_count
#         return f"{available_books} books available (Total: {cls.total_books}, Borrowed: {cls.borrowed_count})"

# book1 = Book("The Alchemist", "Paulo Coelho")
# book2 = Book("Atomic Habits", "James Clear")
# book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")

# print(Book.get_availability())

# book1.borrow()
# book2.borrow()
# book2.borrow()
# print(Book.get_availability())

# 2. Bank Account Tracker
# A bank needs to track how many accounts have been opened. 
# Write a BankAccount class with a class variable account_count. 
# Add a class method get_account_count() that returns the total number of accounts created. 
# Create 3 accounts and call the method.

# class BankAccount():
#     total_accounts_created = 0

#     def __init__(self, name:str, opening_deposit:float):
#         self.name = name
#         self.opening_deposit = opening_deposit
#         BankAccount.total_accounts_created += 1
    
#     @classmethod
#     def get_account_count(cls):
#         return f"The total accounts opened are {cls.total_accounts_created}"

# bank_account1 = BankAccount("Maraya", 3000)
# bank_account2 = BankAccount("Shirley", 5600)
# bank_account3 = BankAccount("Gunna", 56000)
# print(BankAccount.get_account_count())

# 3. App Config
# A mobile app stores a global theme setting (e.g., "dark" or "light"). 
# Write a AppSettings class with a class variable theme = "light" 
# and a class method set_theme(cls, new_theme) that updates the theme for the entire app. 
# Why is a class method more appropriate here than an instance method?

# class AppSettings():
#     theme = "light"

#     @classmethod
#     def set_theme(cls, new_theme):
#         cls.theme = new_theme

# print(AppSettings.theme)
# AppSettings.set_theme("dark")
# print(AppSettings.theme)

# 4. Spot the Bug
# The following code is meant to track how many orders have been placed in an e-commerce system, 
# but it has a bug. Identify and fix it:

# class Order():
#     order_count = 0

#     def __init__(self, item:str):
#         self.item = item
#         Order.order_count += 1  # Bug here

#     @classmethod
#     def get_order_count(cls):
#         print(f"Total orders: {cls.order_count}")

# order1 = Order("Pants")
# order2 = Order("Thermal")
# order3 = Order("Sneakers")
# order4 = Order("Jordans")
# order5 = Order("T-shirts")

# Order.get_order_count()

# 5. Employee Department Roster
# A company HR system needs to know how many employees belong to each department. 
# Write an Employee class that tracks a class-level dictionary department_counts (e.g., {"Engineering": 3, "HR": 2}).
# Add a class method get_department_summary() that returns the dictionary.
# Create at least 4 employees across 2 departments.

# class Employee():
#     department_summary = {}

#     def __init__(self, name, department):
#         self.name = name
#         self.department = department

#         if self.department in Employee.department_summary:
#             Employee.department_summary[self.department] += 1
#         else:
#             Employee.department_summary[self.department] = 1
    
#     @classmethod
#     def get_department_summary(cls):
#         return cls.department_summary

# employee1 = Employee("Oscar", "Engineering")
# employee2 = Employee("Erick", "HR")
# employee3 = Employee("Diana", "Engineering")
# employee4 = Employee("James", "HR")
# employee5 = Employee("Brenda", "Engineering")

# print(Employee.get_department_summary())

# class Employee():
#     department_summary = {}

#     def __init__(self, name, department):
#         self.name = name
#         self.department = department

#         if self.department in Employee.department_summary:
#             Employee.department_summary[self.department] += 1
#         else:
#             Employee.department_summary[self.department] = 1
        
#     @classmethod
#     def get_department_summary(cls):
#         return cls.department_summary
        
# employee1 = Employee("Morris", "Finance")
# employee2 = Employee("Oscar", "IT")
# employee3 = Employee("Anne", "Content Creation")
# employee4 = Employee("Abel", "Finance")
# employee5 = Employee("Ian", "IT")
# employee6 = Employee("Wahinya", "Content Creation")
# employee7 = Employee("Erick", "Finance")

# print(Employee.get_department_summary())

# 6. Alternative Constructors — CSV Import
# A logistics company receives shipment data as comma-separated strings(CSV) like "PKG-001,Cairo,15.5".
# Write a Shipment class with a regular __init__(self, tracking_id, destination, weight)
# and a class method from_csv(cls, csv_string) that parses the string and returns a new Shipment instance. 
# This is one of the most common real-world uses of class methods — explain why @classmethod is used instead of a static method here.

# class Shipment():
#     def __init__(self, tracking_id, destination, weight):
#         self.tracking_id = tracking_id
#         self.destination = destination
#         self.weight = weight

#     def get_info(self):
#         print(f"Tracking Id: {self.tracking_id}")
#         print(f"Destination: {self.destination}")
#         print(f"Weight: {self.weight}kgs")
        
#     @classmethod
#     def from_csv(cls, csv_string):
#         shipment_data = csv_string.split(",")
#         tracking_id = shipment_data[0]
#         destination = shipment_data[1]
#         weight = float(shipment_data[2])
#         return cls(tracking_id, destination, weight)

# print("-----SHIPMENT DETAILS-----") 
# shipment1 = Shipment.from_csv("PKG-001,Cairo,7890.76")
# shipment2 = Shipment.from_csv("PKG-002,Kenya,157.8")
# shipment3 = Shipment.from_csv("DKG-001,Egypt,673.4")
# shipment4 = Shipment.from_csv("DKG-002,South Africa,829.87")
# shipment5 = Shipment.from_csv("SKG-001,Texas,433")
# shipment1.get_info()
# print()
# shipment2.get_info()
# print()
# shipment3.get_info()
# print()
# shipment4.get_info()
# print()
# shipment5.get_info()
# print()

# 7. Session Manager
# A web app needs to enforce that no more than 5 active user sessions exist at once.
# Write a Session class that tracks active sessions using a class variable.
# Add a class method can_create_session(cls) that returns True or False,
# and modify __init__ to raise a ValueError with a meaningful message if the limit is exceeded.
# Test it by trying to create 6 sessions.

# class Session():
#     active_sessions = 0
#     limit = 5
#     def __init__(self, user_id:int, username:str):
#         self.user_id = user_id
#         self.username = username
#         if Session.can_create_session():
#             Session.active_sessions += 1
#         else:
#             raise ValueError(f"Session Limit of {Session.limit} exceeded, can't create a new session")
    
#     @classmethod
#     def can_create_session(cls):
#         return Session.active_sessions < Session.limit

# try:
#     session1 = Session(1, "Oscar")
#     session2 = Session(2, "Rachael")
#     session3 = Session(3, "Yula")
#     session4 = Session(4, "Ashley")
#     session5 = Session(5, "Claire")
#     session6 = Session(6, "Brienna")
# except ValueError as e:
#     print(e)


# 8. Inventory System with Low Stock Alerts
# A retail store tracks products.
# Write a Product class that stores name, price, and stock.
# Use class variables to track total_products and total_inventory_value.
# Add class methods:
# get_total_products() — returns the count
# get_inventory_value() — returns the total value (sum of price × stock for all products)
# low_stock_alert(cls, threshold) — but wait, this method needs access to all instances, not just class variables. What problem do you run into, and how would you redesign the class to solve it?

# class Product():
#     total_products = 0
#     total_inventory_value = 0
#     products = []

#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
#         Product.total_products += 1
#         Product.total_inventory_value += price * stock
#         Product.products.append(self)
    
#     @classmethod
#     def get_total_products(cls):
#         print(f"Total Products: {cls.total_products}")
    
#     @classmethod
#     def get_inventory_value(cls):
#         print(f"Inventory Value: {cls.total_inventory_value}")
#     @classmethod
#     def low_stock_alert(cls, threshold):
#         for each_product in Product.products:
#             if each_product.stock < threshold:
#                 print(f"{each_product.name}s are low on stock! Current Stock: {each_product.stock}")

# product1 = Product("iPhone", 56000, 48)
# product2 = Product("Samsung", 44500, 76)
# product3 = Product("Google Pixel", 99690, 45)

# print("-----INVENTORY SYSTEM-----")
# Product.get_total_products()
# Product.get_inventory_value()
# Product.low_stock_alert(90)

# 9. Singleton Pattern — Database Connection
# In production systems, you never want more than one database connection open at a time (this is called the Singleton pattern).
# Implement a DatabaseConnection class where:
# A class variable _instance holds the single connection
# A class method get_connection(cls) returns the existing instance if one exists, or creates a new one if not
# Each instance has a connection_id (use uuid or a simple counter)

class DatabaseConnection():
    _instance = None
    connection_count = 0

    def __init__(self):
        DatabaseConnection.connection_count += 1
        self.connection_id = DatabaseConnection.connection_count
    
    @classmethod
    def get_connection(cls):
        if cls._instance == None:
            cls._instance = cls()
            return cls._instance
        else:
            return cls._instance
    def get_connection(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

conn1 = DatabaseConnection.get_connection()
conn2 = DatabaseConnection.get_connection()
conn3 = DatabaseConnection.get_connection()

DatabaseConnection.get_connection()
DatabaseConnection.get_connection()
DatabaseConnection.get_connection()
# Test it by calling get_connection() 3 times and confirm all 3 return the same instance.

# 10. Polymorphism with Class Methods — Multi-Format Report
# A data analytics platform exports reports in different formats. You have a base class Report with a class method generate(cls, data). Create two subclasses: PDFReport and CSVReport, each overriding generate() to return a string simulating that format. Then write a function export_report(report_class, data) that accepts any report class and calls its generate() method. This demonstrates how class methods enable polymorphic behavior — explain what would break if generate() were a static method instead.

# 11. Factory + Registry Pattern — Plugin System
# You're building a notification system that supports multiple channels: Email, SMS, and Push. Design a Notification base class with:

# A class variable _registry = {} — a dictionary mapping channel names to classes
# A class method register(cls, channel_name) used as a decorator to register subclasses
# A class method create(cls, channel_name, message) that looks up the registry and instantiates the right subclass


# 2. Configuration Manager
# Create AppConfig with:
# Class variable settings = {} (dict)
# Class method @classmethod def set_setting(cls, key: str, value) -> None → sets cls.settings[key] = value
# Class method @classmethod def get_setting(cls, key: str, default=None) → returns value or default
# No __init__ needed (pure class usage)
# Demonstrate setting/getting values using only class methods (no instances).

# class AppConfig:
#     # Class variable: shared across all "usage" of the class (no instances needed)
#     settings = {}

#     @classmethod
#     def set_setting(cls, key: str, value) -> None:
#         """
#         Sets a configuration value in the shared settings dictionary.
#         """
#         cls.settings[key] = value
#         print(f"Set '{key}' = {value!r}")

#     @classmethod
#     def get_setting(cls, key: str, default=None):
#         """
#         Retrieves a configuration value.
#         Returns the value if key exists, otherwise returns default.
#         """
#         value = cls.settings.get(key, default)
#         print(f"Getting '{key}' → {value!r}")
#         return value


# # Demonstration: pure class usage (no instances created)
# if __name__ == "__main__":
#     # Set some settings
#     AppConfig.set_setting("theme", "dark")
#     AppConfig.set_setting("api_key", "sk-abc123xyz")
#     AppConfig.set_setting("debug_mode", True)
#     AppConfig.set_setting("max_retries", 5)

#     # # Get existing values
#     # theme = AppConfig.get_setting("theme")              # → "dark"
#     # api_key = AppConfig.get_setting("api_key")          # → "sk-abc123xyz"
#     # debug = AppConfig.get_setting("debug_mode")         # → True

#     # # Get non-existing value with default
#     # timeout = AppConfig.get_setting("timeout", 30)      # → 30 (default)
#     # language = AppConfig.get_setting("language", "en")  # → "en" (default)

#     # # Show current full settings
#     # print("\nCurrent configuration:")
#     # for k, v in AppConfig.settings.items():
#     #     print(f"  {k:12} : {v!r}")

#     # # Update an existing setting
#     # AppConfig.set_setting("theme", "light")
#     # print(f"New theme: {AppConfig.get_setting('theme')}")

# 3. Employee Database (partial code)
# Finish this class:

# class Employee:
#     all_employees = []           # class-level list
#     total_salary = 0.0           # class-level sum

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         # Finish: append self to all_employees
#         # Finish: add salary to total_salary

#     def get_info(self):
#         return f"{self.name}: KES {self.salary:,.2f}"

#     @classmethod
#     def add_employee(cls, name, salary):
#         # Finish: create and add new Employee using cls
#         pass

#     @classmethod
#     def get_average_salary(cls):
#         # Finish: return average if employees exist, else 0
#         pass

#     @classmethod
#     def get_employee_count(cls):
#         return len(cls.all_employees)
# Then: use class method to add 4 employees, print count + average salary.

# 4. Inventory Stock Manager
# Create Product:
# Class variables: inventory = {} (name → quantity), low_stock_threshold = 10
# __init__(self, name, price, initial_stock) → add/update cls.inventory[name]
# Instance method sell(self, quantity) → reduce stock, print warning if low
# Class method @classmethod def restock(cls, name, amount) → increase stock
# Class method @classmethod def get_low_stock_items(cls) → return list of names where stock < threshold
# Class method @classmethod def total_products(cls) → sum of all quantities
# Show: create products, sell/restock, get low-stock report using class method.

# class Product():
    
#     inventory = {} # dictionary shared by all Product objects(name, quantity)
#     {"Laptop": 35}
#     low_stock_threshold = 10

#     def __init__(self, name, price, initial_stock):
#     # def __init__(self, name: str, price: float, initial_stock: int) #You can declare the data types of your parameters
#         self.name = name
#         self.price = price
#         Product.inventory[name]
#         self.initial_stock = initial_stock
    
#     def sell(self, quantity):
#         if quantity < Product.low_stock_threshold:
#             print("Product stock is Low")
#         Product.quantity -= quantity

#     @classmethod
#     def restock(cls, name, amount):
#         Product.quantity += amount

#     @classmethod
#     def get_low_stock_items(cls):
#         if Product.quantity < Product.low_stock_threshold:
#             return f""

#     @classmethod
#     def total_products(cls):
#         pass



# 5. Bank Branch Statistics
# Create BankAccount:
# Class variables: branch_total = 0.0, branch_accounts = 0
# __init__(self, holder, initial_balance) → update class totals
# Instance method deposit(self, amount)
# Instance method withdraw(self, amount)
# Class method @classmethod def get_branch_balance(cls) → return total
# Class method @classmethod def get_average_balance(cls) → return average
# Class method @classmethod def reset_branch(cls) → clear totals (for new day)
# Create multiple accounts, do transactions, print branch stats.

# 6. Game High Score Tracker
# Create Player:
# Class variables: high_scores = [] (list of dicts {name, score}), max_players = 10
# __init__(self, name)
# Instance method submit_score(self, score) → add to high_scores, sort descending, keep only top max_players
# Class method @classmethod def get_leaderboard(cls) → return formatted top 5
# Class method @classmethod def clear_scores(cls) → reset list
# Show submitting scores from different players, printing leaderboard via class method.

# 7. Order ID Generator & Statistics
# Create Order:
# Class variable order_counter = 0
# Class method @classmethod def generate_id(cls) -> str → return f"ORD-{cls.order_counter:04d}" and increment counter
# Instance attributes: order_id, customer, total
# __init__(self, customer, total) → self.order_id = cls.generate_id()
# Class variable total_revenue = 0.0
# Instance method complete_order(self) → add total to cls.total_revenue
# Class method @classmethod def get_total_revenue(cls) → formatted string
# Create 5 orders, complete them, print total revenue and last order ID.

# 8. Student Grade Analyzer (mini-project)
# Create StudentGrade:
# Class variables: all_grades = [], subject_count = {} (subject → count)
# __init__(self, name, subject, grade) → append grade to all_grades, update subject_count
# Instance method get_letter_grade(self) → A/B/C/D/F based on grade
# Class method @classmethod def get_average_grade(cls) → overall average
# Class method @classmethod def get_subject_average(cls, subject) → average for one subject
# Class method @classmethod def get_highest_grade(cls) → max grade + student name
# Create multiple students with different subjects/grades, print stats.

# 9. Subscription Plan Manager
# Create Subscription:
# Class variables: plans = {"Basic": 499, "Pro": 999, "Enterprise": 4999}
# Class method @classmethod def add_plan(cls, name, price) → add to plans
# Class method @classmethod def get_all_plans(cls) → return formatted list
# Instance attributes: user_name, plan_name
# Instance method get_monthly_cost(self) → return cls.plans[self.plan_name]
# Show adding a new plan via class method, creating users, calculating costs.

# 10. Task Priority Queue (longer design)
# Create Task:
# Class variable priority_levels = {1: "Low", 2: "Medium", 3: "High"}
# Class method @classmethod def get_priority_name(cls, level: int) → return label
# Instance attributes: description, priority (1–3)
# Instance method get_display(self) → f"{self.description} ({cls.get_priority_name(self.priority)})"
# Class variable all_tasks = []
# Class method @classmethod def add_task(cls, desc, prio) → create and append
# Class method @classmethod def get_high_priority(cls) → list tasks with priority 3
# Build a small task manager: add tasks, print high-priority ones using class method.
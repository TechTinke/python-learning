# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
#                 Best for class level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 #Increase count by 1 for every student that is created
        Student.total_gpa += gpa
    
    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    #Class Method 1
    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"
    
    #Class Method 2
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())

# WORK TO BE DONE
# 1. Library Book Tracker
# Create a Book class with:
# Class variables: total_books = 0, borrowed_count = 0
# __init__(self, title, author) → increment total_books
# Instance method borrow(self) → increment borrowed_count if not already borrowed
# Class method @classmethod def get_availability(cls) -> str → returns f"{cls.total_books - cls.borrowed_count} books available"

class Book():

    total_books = 0
    borrowed_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.total_books += 1
    
    def borrow(self):
        if self.is_borrowed:
            print("This book is already borrowed")
        else:
            self.is_borrowed = True
            Book.borrowed_count += 1
            print(f"You borrowed '{self.title}' by {self.author}")
    
    @classmethod
    def get_availability(cls):
        available_books = cls.total_books - cls.borrowed_count
        return f"{available_books} books available (Total: {cls.total_books}, Borrowed: {cls.borrowed_count})"

book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")

# print(Book.get_availability())

# book1.borrow()
# book2.borrow()
# book2.borrow()
# print(Book.get_availability())

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

class Employee:
    all_employees = []           # class-level list
    total_salary = 0.0           # class-level sum

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Finish: append self to all_employees
        # Finish: add salary to total_salary

    def get_info(self):
        return f"{self.name}: KES {self.salary:,.2f}"

    @classmethod
    def add_employee(cls, name, salary):
        # Finish: create and add new Employee using cls
        pass

    @classmethod
    def get_average_salary(cls):
        # Finish: return average if employees exist, else 0
        pass

    @classmethod
    def get_employee_count(cls):
        return len(cls.all_employees)
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

class Product():
    
    inventory = {} # dictionary shared by all Product objects(name, quantity)
    {"Laptop": 35}
    low_stock_threshold = 10

    def __init__(self, name, price, initial_stock):
    # def __init__(self, name: str, price: float, initial_stock: int) #You can declare the data types of your parameters
        self.name = name
        self.price = price
        Product.inventory[name]
        self.initial_stock = initial_stock
    
    def sell(self, quantity):
        if quantity < Product.low_stock_threshold:
            print("Product stock is Low")
        Product.quantity -= quantity

    @classmethod
    def restock(cls, name, amount):
        Product.quantity += amount

    @classmethod
    def get_low_stock_items(cls):
        if Product.quantity < Product.low_stock_threshold:
            return f""

    @classmethod
    def total_products(cls):
        pass



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
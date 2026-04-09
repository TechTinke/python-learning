# Decorator = A function(method) that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator
#             We are adding sth to the base function without changing it

#             @add_sprinkles
#             get_ice_cream("vanilla")
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("You add sprinkles")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("You add fudge")
#         func(*args, **kwargs)
#     return wrapper 

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream")

# get_ice_cream("chocolate")

# 1. Logging Decorator
# A company wants to track every time a function is called.
# Write a decorator log_call that prints "Function {function_name} was called" before the function runs.
# Apply it to a function process_order(order_id) that prints "Processing order {order_id}".
# Call the function and observe the output.
# Then answer: what would happen if you removed the decorator?

# def log_call(func):
#     def log(*args, **kwargs):
#         print(f"Function {func.__name__} was called")
#         func(*args, **kwargs)
#     return log

# @log_call
# def process_order(order_id):
#     print(f"Processing order {order_id}")

# process_order(9)

# 2. Spot the Bug
# The following decorator is meant to print "Starting timer..." before a function runs and "Done!" after,
# but it has a bug.
# Identify and fix it:

# def timer(func):
#     def wrapper(*args, **kwargs):
#         print("Starting timer...")
#         func(*args, **kwargs)
#         print("Done!")
#     return wrapper

# @timer
# def run_report():
#     print("Generating report...")

# run_report()

# 3. Repeat Decorator
# A notification system needs to send certain alerts multiple times.
# Write a decorator repeat(n) that runs the decorated function n times.
# Apply it to a function send_alert(message) that prints "ALERT: {message}".
# Call it with n=3 and a message of your choice. This introduces decorators with arguments —
# notice the extra layer of nesting required.

# Nesting refers to placing one programming construct inside another

# def repeat(n):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner

# @repeat(4)
# def send_alert(message):
#     print(f"ALERT: {message}")

# send_alert("Oscar is a hero!")


# 4. Authentication Decorator
# A web app needs to protect certain routes.
# Write a decorator require_login(func) that checks a global variable is_logged_in.
# If True → run the function. If False → print "Access denied. Please log in first."
# Apply it to a function view_dashboard(). Test it with both is_logged_in = True and is_logged_in = False.

# def require_login(is_logged_in):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             if is_logged_in == True:
#                 func(*args, **kwargs)
#             else:
#                 print("Access denied. Please log in first")
#         return wrapper
#     return inner

# @require_login(True)
# def view_dashboard():
#     print("Access Approved!")

# view_dashboard()

# def require_login(func):
#     def wrapper(*args, **kwargs):
#         if is_logged_in == True:
#             func(*args, **kwargs)
#         else:
#             print("Access denied. Please log in first")
#     return wrapper

# @require_login
# def view_dashboard(name):
#     print(f"Access Approved, Welcome back, {name}!")

# is_logged_in = False
# view_dashboard("Abel")

# print(" ")

# is_logged_in = True
# view_dashboard("Oscar")

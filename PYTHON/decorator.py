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

# Timing Decorator
# A developer wants to measure how long certain functions take to run.
# Write a decorator measure_time that records the time before
# and after the function runs using Python's time module and prints "Function took {time} seconds".
# Apply it to a function fetch_data() that simulates a delay using time.sleep(2).
# This is a very common real world use case — you'll see this pattern in almost every production codebase.

# import time
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         time_taken = end - start
#         print(f"Function took {time_taken:.2f} seconds")
#     return wrapper

# @measure_time
# def fetch_data():
#     time.sleep(4)
#     print("Function completed")

# fetch_data()


# 6. Stacking Decorators
# A food delivery app applies multiple checks before processing an order.
# Write three decorators — check_restaurant_open (prints "✅ Restaurant is open"),
# check_items_available (prints "✅ Items are available"), and check_delivery_zone (prints "✅ Delivery zone confirmed").
# Stack all three on a function place_order(order_id).
# Then answer: in what order do the decorators run and why?

# def check_restaurant_open(func):
#     def wrapper(*args, **kwargs):
#         if restaurant_open:
#             print("Restaurant is open")
#             func(*args, **kwargs)
#         else:
#             print("Restaurant is closed, can't place order!")
#     return wrapper

# def check_items_available(func):
#     def wrapper(*args, **kwargs):
#         if items_available:
#             print("Items are available")
#             func(*args, **kwargs)
#         else:
#             print("Items aren't available, can't place order!")
#     return wrapper

# def check_delivery_zone(func):
#     def wrapper(*args, **kwargs):
#         if delivery_zone:
#             print("Delivery Zone is confirmed")
#             func(*args, **kwargs)
#         else:
#             print("Delivery Zone unavailable, can't place order!")
#     return wrapper

# @check_restaurant_open
# @check_items_available
# @check_delivery_zone
# def place_order(order_id):
#     print(f"Order {order_id} confirmed!")

# restaurant_open = True
# print(" ")
# items_available = True
# print(" ")
# delivery_zone = False
# place_order(9)

# 7. Cache Decorator
# A weather app makes expensive API calls.
# Write a decorator cache that stores the result of a function call in a dictionary using the function's arguments as the key.
# If the same arguments are passed again, return the cached result instead of running the function again
# and print "Returning cached result".
# Apply it to a function get_weather(city) that simulates an API call
# by printing "Fetching weather for {city}..." and returning a fake temperature.
# Call it twice with the same city and once with a different city.

# NB:append() is used for lists ONLY and not dictionaries

# def cache(func):
#     function_results = {} #needs to be outside wrapper so that when wrapper is called, it doesn't return to empty

#     def wrapper(*args, **kwargs):
#         if args in function_results:
#             print("Returning cached result")
#             print(function_results[args])
#         else:
#             result = func(*args, **kwargs)
#             function_results[args] = result
#             # return result
#     return wrapper 

# @cache
# def get_weather(city):
#     print(f"Fetching weather for {city}...")
#     print(f"{city}: 28°C")

# get_weather("Nairobi")
# print(" ")
# get_weather("Nairobi")
# print(" ")
# get_weather("Kisumu")
# print(" ")
# get_weather("Kisumu")
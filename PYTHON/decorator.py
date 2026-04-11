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

# 8. Retry Decorator
# A payment system sometimes fails due to network issues.
# Write a decorator retry(max_attempts)
# that runs the decorated function up to max_attempts times if it raises an exception.
# After each failed attempt print "Attempt {n} failed, retrying...".
# If all attempts fail print "All attempts failed".
# Apply it to a function charge_card() that randomly raises a ConnectionError using Python's random module.
# Test it with max_attempts=3.

# import random

# def retry(max_attempts):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_attempts): # max_attempts is a variable and hence cannot be iterated over.
#                 try:
#                     func(*args, **kwargs)
#                     break
#                 except ConnectionError:
#                     print(f"Attempt {attempt + 1} failed, retrying...")
#             else:
#                 print("All attempts failed")
#         return wrapper
#     return inner

# @retry(4)
# def charge_card():
#     if random.random() < 0.7:
#         raise ConnectionError("Network failure")
#     else:
#         print("Payment Successful")
# charge_card()


# 9. Rate Limiter Decorator
# An API endpoint should not be called more than 5 times per minute.
# Write a decorator rate_limit(max_calls) that tracks how many times a function has been called using a list of timestamps.
# If the limit is exceeded within 60 seconds print "Rate limit exceeded.
# Try again later." and block the call.
# Apply it to a function search_products(query).
# Test it by calling the function 7 times rapidly and observe which calls get blocked.

# def rate_limit(max_calls):
#     call_count = 0
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             nonlocal call_count
#             call_count += 1
#             if call_count <= max_calls:
#                 func(*args, **kwargs)
#             else:
#                 print("Rate limit exceeded. Please try again later")
#         return wrapper
#     return inner

# @rate_limit(5)
# def search_products(query):
#     print(f"Searching for {query}...")

# search_products("TV")
# search_products("Boots")
# search_products("Books")
# search_products("Water bottles")
# search_products("Shoes")
# search_products("Bags of chips")
# search_products("Samosas")


# 10. Class Based Decorator
# Most decorators are functions but Python also allows classes as decorators.
# Write a class based decorator CallCounter that tracks how many times a decorated function has been called
# and prints "This function has been called {n} times" before each call.
# Apply it to a function generate_report().
# Then compare it to a function based decorator doing the same thing —
# explain what __init__ and __call__ do in a class based decorator and why you would choose one over the other.

# class CallCounter():
#     call_count = 0

#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         self.call_count += 1
#         print(f"This function has been called {self.call_count} times")
#         self.func(*args, **kwargs)

# @CallCounter
# def generate_report():
#     print("Generating report...")

# generate_report()
# generate_report()
# generate_report()

# class Count():
#     call_count = 0

#     def __init__(self, func):
#         self.func = func
    
#     def __call__(self, *args, **kwargs):
#         self.call_count += 1
#         print(f"Function call no.{self.call_count}")
#         self.func(*args, **kwargs)

# @Count
# def generate_report():
#     print("Generating report...")

# generate_report()
# print(" ")
# generate_report()
# print(" ")
# generate_report()
# print(" ")
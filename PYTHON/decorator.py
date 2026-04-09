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

def log_call(func):
    def log(*args, **kwargs):
        print(f"Function {func.__name__} was called")
        func(*args, **kwargs)
    return log

@log_call
def process_order(order_id):
    print(f"Processing order {order_id}")

process_order(9)
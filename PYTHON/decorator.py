# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator
#             We are adding sth to the base function without changing it

#             @add_sprinkles
#             get_ice_cream("vanilla")
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper 

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("chocolate")

#   WORK TO BE DONE
# 1. Simple Logging Decorator
# Create a decorator log_call that prints:
# "Calling {func_name} with args={args}, kwargs={kwargs}"
# "Finished {func_name}"
# Apply it to a function add(a, b) that returns a + b.
# Show stacked with another decorator that prints the result.

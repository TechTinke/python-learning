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


# WORK TO BE DONE
# 1. Simple Logging Decorator
# Create a decorator log_call that prints:
# "Calling {func_name} with args={args}, kwargs={kwargs}"
# "Finished {func_name}"
# Apply it to a function add(a, b) that returns a + b.
# Show stacked with another decorator that prints the result.

# 2. Timing Decorator
# Create @timer decorator that:
# Measures how long the function takes (use time.time())
# Prints "Function {name} took {seconds:.4f} seconds"
# Apply to a slow function (e.g. loop 1 million times).
# Demonstrate with and without arguments.
    

# 3. Authentication Decorator (partial code)
# Finish this role-based access control decorator:

# Pythondef require_role(required_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # Assume there's a global or passed user
#             user_role = kwargs.get('user_role', 'guest')  # for simplicity
#             if user_role != required_role:
#                 raise PermissionError(f"Role {required_role} required")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @require_role("admin")
# def delete_user(user_id):
#     print(f"User {user_id} deleted")

# # Finish: create @require_role("user") for read_user(user_id)
# # Show: call both with different user_roles
# Then: add a class-based version using @classmethod or a class decorator.


# 4. Rate Limiting Decorator (mini-project)
# Create @rate_limit(max_calls=5, period_seconds=60) decorator that:
# Uses a class variable or nonlocal dict to track calls per function
# Raises TooManyRequests if limit exceeded in time window
# Resets after period
# Apply to a function send_email(to, message).
# Show calling it 6 times quickly → last one fails.


# 5. Caching Decorator with Expiration
# Create @cache(expire_seconds=300) decorator that:
# Stores results in a dict (key = args + kwargs tuple)
# Checks if cached and not expired
# Calls original function if miss/expired
# Stores result with timestamp
# Apply to an expensive function (e.g. fetch_weather(city)).
# Call twice quickly → second is cached; wait >5 min → recomputed.


# 6. Input Validation Decorator
# Create @validate_args(**validators) decorator where validators is dict of arg_name → validator function.
# Example: @validate_args(age=lambda x: isinstance(x, int) and x > 0)Raise ValueError if any check fails.
# Apply to create_user(name, age, email).
# Show valid + invalid calls.


# 7. Logging + Timing + Exception Handling (combined decorators)
# Create three decorators:
# @log → print function name + args before/after
# @timer → print execution time
# @catch_errors → catch exceptions, print "Error in {func}: {err}", return None
# Stack them on a function divide(a, b) that can raise ZeroDivisionError.
# Show different stacking orders and behavior.


# 8. Class Method & Static Method Decorator
# Create a class Calculator:
# @staticmethod + your own decorator @uppercase_result that converts string results to uppercase
# @classmethod + @log_class_call that prints "Class method called on {cls.name}"
# Show decorating both types of methods.


# 9. Retry Decorator with Backoff
# Create @retry(max_attempts=3, backoff_factor=2) decorator that:
# Catches exceptions, waits (backoff_factor ** attempt) seconds, retries
# Raises original exception after max attempts
# Apply to fetch_api(url) that simulates flaky network (raise random exceptions).
# Show retrying until success or failure.


# 10. Permission System for API Endpoints (longer project)
# Create a Flask-like simulation with decorators:
# @login_required → check if user kwarg is not None
# @admin_required → check if user.role == 'admin'
# @rate_limit_api(calls_per_minute=10) → track calls
# Define fake endpoint functions:
# @login_required @admin_required def delete_post(post_id)
# @login_required @rate_limit_api def get_comments()
# Simulate calls with different users/roles, show access denied or rate limit errors.
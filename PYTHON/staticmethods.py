# Static Methods = A method(function) belonging to a class rather than any object from that class(instance)
#                  Used for general utility function
# Instance methods = Best for operations of the class(objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod #Best for utility functions that do not need access to data that is in a class
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Roxket"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# WORK TO BE DONE
# 1. User Authentication Utility
# Create a User class with:
# Instance method login(self, password) → prints f"{self.username} logged in successfully"
# Static method is_valid_email(email: str) -> bool → checks if email contains "@" and "."
# Show: create a user, call instance method on the object, call static method on the class.
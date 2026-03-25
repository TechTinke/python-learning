#super() = Function used in a child class(subclass) to call methods from a parent class(super class).
#          Allows you to extend the functionality of the inherited methods
# import math
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
    
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     # METHOD OVERWRITING
#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius *self.radius}squarecm")
#         super().describe()

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width
    

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

# circle = Circle("Red", True, 5)
# square = Square("Blue", False, 6)
# triangle = Triangle("Yellow", True, 7, 8)

# print(circle.color)
# print(circle.is_filled)
# print(f"{circle.radius}cm")

# print(" ")

# print(square.color)
# print(square.is_filled)
# print(f"{square.width}cm")

# print(" ")

# print(triangle.color)
# print(triangle.is_filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")

# circle.describe()
# square.describe()
# triangle.describe()

# PRACTICE
# 1. Online Store Product
# An online store has a Product parent class with __init__ taking name and price,
# and a get_info() method that prints both.
# Create a child class DigitalProduct with an additional file_size attribute (in MB).
# Use super().__init__() to avoid rewriting the parent's logic.
# Create an instance and call get_info().
# Then answer: what would break if you removed super().__init__()?

# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"Price: Kshs.{self.price:.2f}")

# class DigitalProduct(Product):
#     def __init__(self, name, price, file_size):
#         super().__init__(name, price)
#         self.file_size = file_size
    
#     def get_info(self):
#         super().get_info()
#         print(f"File Size: {self.file_size} GB")
# SamsungTv = DigitalProduct("Samsung LED TV", 890000, 56)
# SamsungTv.get_info()

# 2. Spot the Bug
# The following code models a hospital system but throws an error. Identify and fix it:
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
    
    def get_info(self):
        return f"Dr. {self.name}, Age: {self.age}, Specialization: {self.specialization}"

doctor = Doctor("Ahmed", 45, "Cardiology")
print(doctor.get_info())
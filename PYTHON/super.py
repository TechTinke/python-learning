#super() = Function used in a child class(subclass) to call methods from a parent class(super class).
#          Allows you to extend the functionality of the inherited methods
import math
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    # METHOD OVERWRITING
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius *self.radius}squarecm")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("Red", True, 5)
square = Square("Blue", False, 6)
triangle = Triangle("Yellow", True, 7, 8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(" ")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print(" ")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

circle.describe()
square.describe()
triangle.describe()


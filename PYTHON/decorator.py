#@property = Decorator used to define a method(function) as a property(it can be accessed like an attribute/variable)
#            Benefit: Add additional logic when read, write or delete attributes
#            Gives you getter to read, setter to write and deleter to delete method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # width and height are internal/protected members of the class Rectangle
        # They are only meant to be used inside of the class
        # If we need to get the width and height, we use the getter methods below provided by @property decorator
        # @property decorator helps us add additional logic when reading a method
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 10

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)

# WORK TO BE DONE
# 1. Temperature Class with Conversion
# Create a Temperature class:
# Internal: self._celsius
# @property def celsius(self) → return formatted "25.0°C"
# @property def fahrenheit(self) → computed: (celsius × 9/5) + 32
# @celsius.setter → validate > -273.15, convert input if needed
# @fahrenheit.setter → convert back to celsius
# Show: set in Fahrenheit, read in Celsius (and vice versa).



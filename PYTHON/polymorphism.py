#Polymorphism = Greek word that means to "have many forms or faces"
#               Poly = Many
#               Morphe = Form

#There are TWO ways to achieve POLYMORPHISM
# 1. Inheritance = An object could be treated as of the same type as the parent class
# 2. "Duck typing" = Object must have necessary attributes(variables) and methods(functions)

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 *self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle): #A pizza is considered a Pizza, a Shape and a Circle(Polymorphism)
    def __init__(self, topping, radius):
       super().__init__(radius)
       self.topping = topping

# circle = Circle() #The circle is a circle and also a shape but not a Square or a Triangle
# square = Square() #circle is a Circle and also a shape but not a Triangle or a circle
# triangle = Triangle() #triangle is a Triangle and also a Shape but not a Sqaure or a Circle

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} square centimetres")


#WORK TO BE DONE
# 1. Payment Processor (inheritance + overriding)
# Create an abstract base class PaymentMethod with:
# @abstractmethod def process(amount: float) -> str
# Create three child classes:
# Mpesa(PaymentMethod) → returns f"M-Pesa payment of KES {amount} successful"
# Card(PaymentMethod) → returns f"Card payment of KES {amount} processed (Visa/Mastercard)"
# PayPal(PaymentMethod) → returns f"PayPal payment of USD {amount} completed"
# Then create a list of different payment objects and loop through them calling process(1500.50) on each — demonstrate polymorphism.
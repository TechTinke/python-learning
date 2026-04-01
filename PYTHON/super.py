#super() = Function used in a child class(subclass) to call methods from a parent class(super class).
#          Allows you to extend the functionality of the inherited methods
# super() automatically finds the parent
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
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Doctor(Person):
#     def __init__(self, name, age, specialization):
#         super().__init__(name, age)
#         self.specialization = specialization
    
#     def get_info(self):
#         return f"Dr. {self.name}, Age: {self.age}, Specialization: {self.specialization}"

# doctor = Doctor("Ahmed", 45, "Cardiology")
# print(doctor.get_info())

# 3. Method Extension with super()
# A logistics company has a Package parent class with
# a get_label() method that returns "Package: {tracking_id}".
# Create a child class FragilePackage that extends get_label() using super()
# to include "⚠️ FRAGILE — Handle with care" at the end — without rewriting the parent's logic.
# This is the difference between overriding (replacing) and extending (adding to) a method.

# class Package():
#     def __init__(self, tracking_id:int):
#         self.tracking_id = tracking_id
    
#     def get_label(self):
#         print(f"Package: {self.tracking_id}")

# class FragilePackage(Package):

#     # EXTENDING — builds on top of the parent method
#     def get_label(self):
#         super().get_label()
#         print("⚠️FRAGILE — Handle with care")
    
#     # OVERRIDING — replaces the parent method entirely
#     # def get_label(self):
#         # print("⚠️FRAGILE — Handle with care")  # Parent output is GONE

# refrigerator = FragilePackage(9)
# refrigerator.get_label()

# 4. Hotel Booking System
# A hotel manages different room types.
# Write a Room parent class with room_number, price_per_night, and a get_booking_info() method.
# Create two child classes — StandardRoom with a has_breakfast boolean,
# and SuiteRoom with a butler_service boolean and a floor attribute.
# Both should use super().__init__() and override get_booking_info() using super()
# to extend the parent's output.
# Book one of each and print their info.

# class Room():
#     def __init__(self, room_number, price_per_night):
#         self.room_number = room_number
#         self.price_per_night = price_per_night
    
#     def booking_info(self):
#         print(f"Room Number: {self.room_number}")
#         print(f"Price Per Night: {self.price_per_night}")

# class StandardRoom(Room):
#     def __init__(self, room_number, price_per_night, has_breakfast=True):
#         super().__init__(room_number, price_per_night)
#         self.has_breakfast = has_breakfast
    
#     def booking_info(self):
#         super().booking_info()
#         print(f"Has Breakfast: {self.has_breakfast}")

# class SuiteRoom(Room):
#     def __init__(self, room_number, price_per_night, floor, butler_service=True):
#         super().__init__(room_number, price_per_night)
#         self.floor = floor
#         self.butler_service = butler_service
    
#     def booking_info(self):
#         super().booking_info()
#         print(f"Floor: {self.floor}")
#         print(f"Butler Service: {self.butler_service}")

# standardroom = StandardRoom(9, 9560, True)
# suiteroom = SuiteRoom(8, 15600, 2, True)


# print("-----StandardRoom Booking Info-----")
# standardroom.booking_info()
# print(" ")
# print("-----SuiteRoom Booking Info-----")
# suiteroom.booking_info()

# 5. super() in Multiple Method Types
# A fitness app tracks different workout types.
# Write a Workout parent class with __init__ taking duration and calories_burned,
# an instance method get_summary(), and a class method get_type() returning "General Workout".
# Create a child class HIITWorkout that:
# Uses super().__init__() in __init__ and adds rounds
# Extends get_summary() using super() to add round info
# Overrides the class method get_type() using super() to return "HIIT — " + super().get_type()
# This shows super() works across all method types, not just __init__.


# class Workout():
#     def __init__(self, duration, calories_burned):
#         self.duration = duration
#         self.calories_burned = calories_burned
    
#     def get_summary(self):
#         print(f"Duration: {self.duration} mins")
#         print(f"Calories Burned: {self.calories_burned} kcal")

#     @classmethod
#     def get_type(cls):
#         return "General Workout"

# class HIITWorkout(Workout):
#     def __init__(self, duration, calories_burned, rounds):
#         super().__init__(duration, calories_burned)
#         self.rounds = rounds

#     def get_summary(self):
#         super().get_summary()
#         print(f"Rounds: {self.rounds}")

#     @classmethod
#     def get_type(cls):
#         return "HIIT — " + super(HIITWorkout, cls).get_type()

# workout1 = Workout(67, 147)
# workout2 = Workout(89, 286)
# hiitworkout1 = HIITWorkout(90, 300, 2)
# hiitworkout2 = HIITWorkout(78, 245, 1)
# print("-----GENERAL WORKOUTS-----")
# print(workout1.get_type())
# workout1.get_summary()
# print(" ")
# print(workout2.get_type())
# workout2.get_summary()
# print(" ")
# print("-----HIIT WORKOUTS-----")
# print(hiitworkout1.get_type())
# hiitworkout1.get_summary()
# print(" ")
# print(hiitworkout2.get_type())
# hiitworkout2.get_summary()


# 6. Multilevel super() Chain
# A game has a character progression system.
# Write three classes — Character with name and health, Warrior(Character)
# adding weapon and extending get_stats(), and EliteWarrior(Warrior) adding armor and
# extending get_stats() further. Each level should use super().__init__() 
# and super().get_stats() so the final output builds on every level.
# Trace through exactly what happens when EliteWarrior.get_stats() is called
# — which get_stats() runs first?

# class Character():
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def get_stats(self):
#         print(f"Name: {self.name}")
#         print(f"Health: {self.health}")

# class Warrior(Character):
#     def __init__(self, name, health, weapon):
#         super().__init__(name, health)
#         self.weapon = weapon
#     def get_stats(self):
#         super().get_stats()
#         print(f"Weapon: {self.weapon}")
# class EliteWarrior(Warrior):
#     def __init__(self, name, health, weapon, armor):
#         super().__init__(name, health, weapon)
#         self.armor = armor
#     def get_stats(self):
#         super().get_stats()
#         print(f"Armor: {self.armor}")

# rapunzo = Character("Rapunzo", 62)
# realto = Warrior("Realto", 78, "Butcher's Knife")
# salto = EliteWarrior("Salto", 99, "Malet", "Body Armor")
# rapunzo.get_stats()
# print(" ")
# realto.get_stats()
# print(" ")
# salto.get_stats()

# 7. E-Commerce Discount System
# An e-commerce platform applies different discount rules.
# Write a BasePrice class with price and a get_final_price() returning the price as it is.
# Create a chain of discount classes — MemberDiscount(BasePrice) applying 10% off using super().get_final_price()
# and FlashSaleDiscount(MemberDiscount) applying an additional 20% off on top.
# Show that the discounts stack by calling get_final_price() on a FlashSaleDiscount instance
# and tracing exactly how super() chains through each level to produce the final price.

# class BasePrice():
#     def __init__(self, price):
#         self.price = price
    
#     def get_final_price(self):
#         return self.price

# class MemberDiscount(BasePrice):
#     def __init__(self, price):
#         super().__init__(price)
#     def get_final_price(self):
#         discounted = super().get_final_price() * 0.90
#         print(f"After Member Discount(10%): {discounted:.2f}")
#         return discounted
# class FlashSaleDiscount(MemberDiscount):
#     def __init__(self, price):
#         super().__init__(price)
    
#     def get_final_price(self):
        # discounted = super().get_final_price() * 0.80
#         print(f"After FlashSale Discount(20%): {discounted:.2f}")

# flashsalediscount = FlashSaleDiscount(67900)
# print("-----PRICE BREAKDOWN-----")
# print(f"Original Price: {flashsalediscount.price}")
# flashsalediscount.get_final_price()


# 8. School Management System
# A school manages different types of staff.
# Write a StaffMember parent class with name, employee_id, and salary,
# and methods get_info() and apply_raise(percentage).
# Create child classes Teacher (adds subject and grade_level) and
# Administrator (adds department and office_number).
# Both should extend get_info() with super() and override apply_raise() — 
# Teacher gets an additional 5% bonus on top of the standard raise,
# Administrator gets an additional 3%.
# Use super().apply_raise() to avoid rewriting the raise logic.
# Test with a 10% raise for both.

# class StaffMember():
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Salary: {self.salary}")
#     def apply_raise(self, percentage):
#         rise = self.salary * percentage/100
#         new_salary = self.salary + rise
#         print(f"New Salary(After Raise): {new_salary}")
#         return new_salary
# class Teacher(StaffMember):
#     def __init__(self, name, employee_id, salary, subject, grade_level):
#         super().__init__(name, employee_id, salary)
#         self.subject = subject
#         self.grade_level = grade_level
#     def get_info(self):
#         super().get_info()
#         print(f"Subject: {self.subject}")
#         print(f"Grade Level: {self.grade_level}")
#     def apply_raise(self, percentage):
#         new_base_salary = super().apply_raise(percentage)
#         bonus =  new_base_salary * 0.05
#         new_salary = new_base_salary + bonus
#         print(f"New Salary(After Bonus): {new_salary:.2f}")

# class Administrator(StaffMember):
#     def __init__(self, name, employee_id, salary, department, office_number):
#         super().__init__(name, employee_id, salary)
#         self.department = department
#         self.office_number = office_number
#     def get_info(self):
#         super().get_info()
#         print(f"Department: {self.department}")
#         print(f"Office No.: {self.office_number}")
#     def apply_raise(self, percentage):
#         new_base_salary = super().apply_raise(percentage)
#         new_salary = new_base_salary * 0.03
#         print(f"New Salary(After Bonus): {new_salary:.2f}")

# rachael = Teacher("Rachael", 373, 167000, "Physiology", "A2")
# print("-----EMPLOYEE DETAILS-----")
# rachael.get_info()
# print(" ")
# print("---SALARY RAISES---")
# rachael.apply_raise(50)

# 9. super() vs Direct Parent Call
# A delivery system has three classes — Delivery, ExpressDelivery(Delivery), and SameDayDelivery(ExpressDelivery).
# Implement the same system twice — once using super()
# and once calling the parent class directly by name (e.g. Delivery.__init__(self, ...)).
# Then change ExpressDelivery to inherit from a different class and observe what breaks in each version.
# This demonstrates why super() is always preferred over hardcoding the parent class name — explain the difference in your own words.

class Delivery():
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
    def get_info(self):
        print(f"Tracking Id: {self.tracking_id}")

class ExpressDelivery(Delivery):
    def __init__(self, tracking_id, speed):
        super().__init__(tracking_id)
        self.speed = speed
    def get_info(self):
        super().get_info()
        print(f"Speed: {self.speed}")

class SameDayDelivery(ExpressDelivery):
    def __init__(self, tracking_id, speed, cutoff_time):
        super().__init__(tracking_id, speed)
        self.cutoff_time = cutoff_time
    def get_info(self):
        super().get_info()
        print(f"Cutoff Time: {self.cutoff_time}")

class Delivery2():
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
    def get_info(self):
        print(f"Tracking Id: {self.tracking_id}")

class ExpressDelivery2(Delivery):
    def __init__(self, tracking_id, speed):
        Delivery2.__init__(self, tracking_id)
        self.speed = speed
    def get_info(self):
        Delivery2.get_info(self)
        print(f"Speed: {self.speed}")

class SameDayDelivery2(ExpressDelivery2):
    def __init__(self, tracking_id, speed, cutoff_time):
        ExpressDelivery2.__init__(self, tracking_id, speed)
        self.cutoff_time = cutoff_time
    def get_info(self):
        SameDayDelivery2.get_info(self)
        print(f"Cutoff time: {self.cutoff_time}")

# package1 = SameDayDelivery(1, 40, 23)
# package2 = ExpressDelivery(2, 67)
package3 = SameDayDelivery2(3, 45, 12)
package4 = ExpressDelivery2(4, 98)
print("-----PACKAGES-----")
# package1.get_info()
# print(" ")
# package2.get_info()
# print(" ")
package3.get_info()
print(" ")
package4.get_info()

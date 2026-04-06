#Inheritance = Allows a class to inherit attributess(variables) and methods(functions) from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)
#              You write code once and then you re-use it rather than make that change MANUALLY multiple times

#The child classes can have different attributes(variables) 
# and methods(functions) from the parent class 

# class Animal():
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True #Since it is set to True, it doesn't need to be set as a parameter
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} is barking: Woof!Woof!")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} is meowing!")

# class Mouse(Animal):
#     def speak(self):
#         print(f"{self.name} is squeaking!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(cat.name)
# print(mouse.name)
# dog.eat()
# dog.sleep()
# cat.eat()
# cat.sleep()
# mouse.eat()
# mouse.sleep()
# dog.speak()
# cat.speak()
# mouse.speak()

# PRACTICE
# 1. Vehicle Fleet
# A transport company manages different types of vehicles.
# Write a Vehicle parent class with attributes make, model, and year,
# and a method get_info() that returns the vehicle details.
# Create two child classes Car and Truck 
# Car has an additional method play_music() 
# and Truck has an additional method load_cargo().
# Create an instance of each and call all their methods.

# class Vehicle():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self):
#         print(f"Year: {self.year}")
#         print(f"Model: {self.model}")
#         print(f"Make: {self.make}")

# class Car(Vehicle):
#     def play_music(self):
#         print("The Car is playing some music")

# class Truck(Vehicle):
#     def load_cargo(self):
#         print("The Truck is loading some cargo")

# car = Car("Lamborghini", "Urus", 2024)
# truck = Truck("Volvo", "GTS", 2027)
# print("------CAR INFO-----")
# car.get_info()
# car.play_music()
# print(" ")
# print("-----TRUCK INFO-----")
# truck.get_info()
# truck.load_cargo()    

# 2. Spot the Bug - Banking System
# The following code is meant to model a banking system but throws an error.
# Identify and fix it:

# class Account():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     def get_info(self):
#         return f"{self.owner}: {self.balance}"

# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
    
#     def get_interest(self):
#         interest = self.balance * self.interest_rate
#         return interest

# savings = SavingsAccount("Oscar", 5000, 0.05)
# print(savings.get_interest())

# 3. Method Overriding
# A company has different types of employees.
# Write an Employee parent class with a method get_role() that returns "Employee".
# Create two child classes Manager and Intern that override get_role()
# to return "Manager" and "Intern" respectively.
# Create an instance of each and call get_role() — explain what method overriding is and why it is useful.

# class Employeee():
#     def get_role(self):
#         return "Employee"

# class Manager(Employeee):
#     def get_role(self):
#         return "Manager"
# class Intern(Employeee):
#     def get_role(self):
#         return "Intern"

# oscar = Employeee()
# rachel = Manager()
# morris = Intern()

# print(morris.get_role())
# print(rachel.get_role())
# print(oscar.get_role())

#Over-riding means changing the logic of the child class in relation to the parent class

# 4. E-Commerce Product Catalog
# An online store sells different types of products.
# Write a Product parent class with name, price, and a get_info() method.
# Create three child classes — Electronics with a warranty_years attribute,
# Clothing with a size attribute, and Food with an expiry_date attribute.
# Each child class should override get_info() to include their unique attribute using super().
# Create one instance of each and print their info.

# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"Price: Kshs. {self.price:.2f}")

# class Electronics(Product):
#     def __init__(self, name, price, warranty_years):
#         super().__init__(name, price)
#         self.warranty_years = warranty_years
#     def get_info(self):
#         super().get_info()
#         print(f"Warranty Years: {self.warranty_years}")
# class Clothing(Product):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self.size = size
#     def get_info(self):
#         super().get_info()
#         print(f"Size: {self.size}")

# class Food(Product):
#     def __init__(self, name, price, expiry_date):
#         super().__init__(name, price)
#         self.expiry_date = expiry_date
#     def get_info(self):
#         super().get_info()
#         print(f"Expiry Date: {self.expiry_date}")

# chicken_wings = Food("Chicken Wings", 560, "30.04.26")
# pants = Clothing("Sweatpants", 2500, "XL")
# smart_tv = Electronics("Samsung Smart TV", 118000, 2)

# chicken_wings.get_info()
# print(" ")
# pants.get_info()
# print(" ")
# smart_tv.get_info()
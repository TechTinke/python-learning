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

# 5. Multilevel Inheritance
# A game has different character types.
# Write a Character base class with name and health.
# Create a child class Warrior(Character) that adds a weapon attribute and an attack() method
# that prints "{name} attacks with {weapon}!".
# Then create a grandchild class EliteWarrior(Warrior) that adds an armor attribute
# and overrides attack() to deal double damage by printing "{name} attacks with {weapon} for DOUBLE DAMAGE!"
# and also prints "{name} is protected by {armor}".
# Create an instance of EliteWarrior and show it has access to attributes from all three levels.

# class Character():
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
# class Warrior(Character):
#     def __init__(self, name, health, weapon):
#         super().__init__(name, health)
#         self.weapon = weapon
#     def attack(self):
#         print(f"{self.name} attacks with {self.weapon}!")

# class EliteWarrior(Warrior):
#     def __init__(self, name, health, weapon, armor):
#         super().__init__(name, health, weapon)
#         self.armor = armor
#     def attack(self):
#         print(f"{self.name} attacks with {self.weapon} for DOUBLE DAMAGE!")
#         print(f"{self.name} is protected by {self.armor}")

# elite_warrior = EliteWarrior("Javlin", 98, "Karate Swords", "Shield")
# elite_warrior.attack()

# 6. Polymorphism Through Inheritance
# A zoo management system tracks different animals.
# Write an Animal parent class with name and a method make_sound() that prints "Some generic sound".
# Create four child classes — Lion, Elephant, Parrot, and Snake — each overriding make_sound() with their own sound.
# Then write a function zoo_sounds(animals) that takes a list of mixed animal objects
# and calls make_sound() on each.
# This demonstrates polymorphism — explain in your own words how Python knows which make_sound() to call
# for each animal.
# Since the animals that we've created are child classes from the base parent Animal class and each animal created is automatically appended to the class variable animals, then the loop in the function zoo_sounds loops over each animal in animals and calls the function make_sound which is inherited by all animals

# class Animal():
#     animals = []
#     def __init__(self, name):
#         self.name = name
#         Animal.animals.append(self)
    
#     def make_sound(self):
#         return "Some generic sound!"

# class Lion(Animal):
#     def make_sound(self):
#         return "ROOOARR!"

# class Elephant(Animal):
#     def make_sound(self):
#         return "GROWWWLLL!"

# class Parrot(Animal):
#     def make_sound(self):
#         return "TRIIILL!"
    
# class Snake(Animal):
#     def make_sound(self):
#         return "HIIIISS!"

# lion = Lion("Simba")
# elephant = Elephant("Elephante")
# parrot = Parrot("Hennery")
# snake = Snake("Nyoka")

# def zoo_sounds(animals):
#     for animal in animals:
#         print(" ")
#         print(animal.make_sound())
# zoo_sounds(Animal.animals)

# 7. Restaurant Order System
# A restaurant has a menu with different item categories.
# Write a MenuItem parent class with name, price,
# and a get_receipt_line() method that returns "{name} .... {price}".
# Create child classes MainCourse, Drink, and Dessert — Drink has a size attribute ("small", "medium", "large")
# that affects the price (+20% for medium, +40% for large),
# and Dessert has an is_vegan boolean. Each child overrides get_receipt_line() using super().
# Then create an Order class (not inheriting from MenuItem) that holds a list of MenuItem objects,
# has a get_total() method, and a print_receipt() method that calls get_receipt_line() on each item.
# Create a full order and print the receipt.

class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_receipt_line(self):
        return f"{self.name} - {self.price}"
class MainCourse(MenuItem):
    pass
class Drink(MenuItem):
    pass
class Dessert(MenuItem):
    pass

# 8. Notification System
# A company sends notifications through different channels.
# Write a Notification parent class with recipient and message attributes
# and a send() method that prints "Sending notification to {recipient}...".
# Create three child classes — EmailNotification (adds email_address),
# SMSNotification (adds phone_number), and PushNotification (adds device_id) —
# each overriding send() using super() to extend the parent output with channel-specific details.
# Then write a function send_all(notifications) that takes a list of mixed notification objects
# and calls send() on each. Create at least 5 mixed notifications and call send_all().

# class Notification():
#     notifications = []
#     def __init__(self, recipient, message):
#         self.recipient = recipient
#         self.message = message
#         Notification.notifications.append(self)
#     def send(self):
#         print(f"Sending notification to {self.recipient}...")
# class EmailNotification(Notification):
#     def __init__(self, recipient, message, email_address):
#         super().__init__(recipient, message)
#         self.email_address = email_address
#     def send(self):
#         super().send()
#         print(f"{self.email_address}")
# class SMSNotification(Notification):
#     def __init__(self, recipient, message, phone_number):
#         super().__init__(recipient, message)
#         self.phone_number = phone_number
#     def send(self):
#         super().send()
#         print(f"{self.phone_number}")
# class PushNotification(Notification):
#     def __init__(self, recipient, message, device_id):
#         super().__init__(recipient, message)
#         self.device_id = device_id
#     def send(self):
#         super().send()
#         print(f"{self.device_id}")

# email_notification1 = EmailNotification("Oscar Maingi", "You are amazing!", "somba@gmail.com")
# sms_notification2 = SMSNotification("Mlewa Morris", "I am a doctor", 789345672)
# push_notification1 = PushNotification("Abel Patrick", "You are Oscar's roomate", 8)
# sms_notification2 = SMSNotification("Ashley Emmanuelah", "I live in Donholm", 776268723)
# push_notification2 = PushNotification("Myke Kyma", "I am a star", 9)
# sms_notification3 = SMSNotification("Anne Yula", "I am a dentist", 782098734)
# email_notification2 = EmailNotification("Rachael Mailo", "Mehhhn, you are nonchalant", "rachael@gmail.com")

# def send_all(notifications):
#     for notification in notifications:
#         print(" ")
#         notification.send()
# send_all(Notification.notifications)

# 9. Abstract Base Classes
# A payment processing system handles multiple payment methods.
# Write an abstract Payment base class using Python's abc module with an abstract method process_payment().
# Create three concrete child classes — CreditCardPayment, MpesaPayment, and PayPalPayment —
# each implementing process_payment() differently.
# Then try to instantiate the abstract Payment class directly and observe what happens.
# Explain why abstract base classes are useful in real systems — what problem do they solve that regular inheritance doesn't?

#They are useful in real systems because once a new class is created it must implement the methods in the parent class reminding the developer that the methods from the parent class must be used lest Python will throw an error
#When a parent class has an abstract method, every child class must implement it or Python throws an error

# from abc import ABC, abstractmethod

# class Payment(ABC): #importing from ABC makes it abstract
#     def __init__(self, amount):
#         self.amount = amount

#     @abstractmethod
#     def process_payment(self):
#         pass
    
# class CreditCardPayment(Payment):
#     def __init__(self, amount, card_number):
#         super().__init__(amount)
#         self.card_number = card_number
#     def process_payment(self):
#         print(f"Processing Payment of {self.amount} under credit card number {self.card_number}...")

# class MpesaPayment(Payment):
#     def __init__(self, amount, phone_number):
#         super().__init__(amount)
#         self.phone_number = phone_number
#     def process_payment(self):
#         print(f"Processing payment of {self.amount} to {self.phone_number}...")
# class PayPalPayment(Payment):
#     def __init__(self, amount, email_address):
#         super().__init__(amount)
#         self.email_address = email_address
#     def process_payment(self):
#         print(f"Processing payment of {self.amount}; Paypal email address: {self.email_address}")

# #INSTANTIATE - create an object from a class
# #payment = Payment(400)  #Can't instantiate abstract class Payment with abstract methods process_payment
# mpesa_payment = MpesaPayment(7800, 768789830)
# paypal_payment = PayPalPayment(90000, "rachael1234@gmail.com")
# credit_card_payment = CreditCardPayment(78900, 5674234576434567)

# mpesa_payment.process_payment()
# print(" ")
# paypal_payment.process_payment()
# print(" ")
# credit_card_payment.process_payment()


# Mixin Pattern
# A large e-commerce platform needs logging, serialization, and validation across many unrelated classes.
# Create three mixin classes — LogMixin with a log(message) method that prints "[LOG]: {message}",
# SerializeMixin with a to_dict() method that returns the object's attributes as a dictionary,
# and ValidateMixin with a validate() method that checks required fields are not empty and returns True or False.
# Then create a CustomerOrder class that inherits from all three mixins plus a base Order class with order_id, product, and quantity.
# Demonstrate all mixin methods working on a CustomerOrder instance.
# Explain what a mixin is and why it is preferred over putting all this logic in one giant parent class.


class Order():
    object_attributes = {}
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        Order.object_attributes.append()

class LogMixin():
    def log(message):
        print(f"[LOG]: {message}")

class SerializeMixin():
    def to_dict():
        return Order.object_attributes

class ValidateMixin():
    def validate():
        pass


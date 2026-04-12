# "Duck Typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"
#Polymorphism - allowing objects to achieve different behaviours


# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Car:
#     alive = False
#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()] #Car meets the minimum requirements to be called an Animal(has speak attribute, alive attribute)
# #                               even though it doesn't inherit from the class Animal                                

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# PRACTICE QUESTIONS
# 1. Payment Processor
# A checkout system processes payments.
# Write three classes — CreditCard, Mpesa, and PayPal — none of which inherit from each other.
# Each has a process(amount) method that prints how it processes the payment.
# Write a function checkout(payment_method, amount) that calls process() on whatever object is passed.
# Test it with all three. Then answer: why does this work even though the classes share no parent?

# class CreditCard():
#     #All instance methods require self
#     # Instance method - a regular method that belongs to an object 
#     def process(self, amount):
#         return f"Processing Kshs.{amount} via Credit Card"

# class Mpesa():
#     def process(self, amount):
#         return f"Processing Kshs.{amount} via Mpesa"

# class PayPal():
#     def process(self, amount):
#         return f"Processing Kshs.{amount} via Paypal"
    
# def checkout(payment_method, amount):
#     print(payment_method.process(amount))

# checkout(PayPal(), 3500)
# checkout(Mpesa(), 7800)
# checkout(CreditCard(), 8900)

# 2. Spot the Bug
# The following duck typing code throws an error. Identify and fix it:
# class Keyboard:
#     def type(self):
#         print("Clack clack clack!")

# class Typewriter:
#     def type(self):
#         print("Clack ding!")

# class VoiceAssistant:
#     def speak(self):
#         print("How can I help you?")

# devices = [Keyboard(), Typewriter(), VoiceAssistant()]

# for device in devices:
#     if hasattr(device, 'type'):
#         device.type()
#     else:
#         print(f"{device.__class__.__name__} doesn't support typing")

# 3. Renderable UI Components
# A UI framework renders different components on screen. Write three classes — Button, Image, and TextBox — each with a render() method that prints what it renders. Write a function render_all(components) that loops through a list and calls render() on each. Create a mixed list and call render_all(). This is exactly how real UI frameworks like React work internally.
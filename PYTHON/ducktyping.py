# "Duck Typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"
#Polymorphism - allowing objects to achieve different behaviours

# Duck Typing        → No parent class, no rules — just needs log() to exist
                    #  - Flexible as there is No enforcement

# Inheritance        → Parent Logger class with log() — child can override or use parent's
                    #  shared behavior and Child can forget to override, no crash

# Abstract Classes   → Parent Logger with @abstractmethod log()
                    #   Enforced  : More code, more rigid

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
# A UI framework renders different components on screen.
# Write three classes — Button, Image, and TextBox — each with a render() method that prints what it renders.
# Write a function render_all(components) that loops through a list and calls render() on each.
# Create a mixed list and call render_all().
# This is exactly how real UI frameworks like React work internally.

# Rendering - calling your components

# class Button():
#     def render(self):
#         print("Rendering button!")
# class Image():
#     def render(self):
#         print("Rendering image!")
# class TextBox():
#     def render(self):
#         print("Rendering a text box!")
# components = [Button(), Image(), TextBox()]
# def render_all(components):
#     for component in components:
#         component.render()
# render_all(components)

# 4. File Exporter
# A data platform exports reports in different formats.
# Write three classes — PDFExporter, CSVExporter, and ExcelExporter — each with an export(data) method.
# None inherit from each other.
# Write a function run_export(exporter, data) that calls export() on whatever exporter is passed.
# Then add a fourth class XMLExporter without an export() method and try passing it to run_export() —
# observe what happens and explain why.

# class PDFExporter():
#     def export(self, data):
#         print(f"Exporting {data} in PDF format")
# class CSVExporter():
#     def export(self, data):
#         print(f"Exporting {data} in CSV format")
# class ExcelExporter():
#     def export(dself, data):
#         print(f"Exporting {data} in excel format")
# class XMLExporter():
#     def move(self, data):
#         print(f"Exporting {data} in XML format")


# def run_export(exporter, data):
#     exporter.export(data)
# run_export(PDFExporter(), "Oscar is a hero")
# run_export(CSVExporter(), "Oscar, 17, CEO")
# run_export(ExcelExporter(), "Morris, 179000")
# run_export(XMLExporter(), "WTH, WTF") # returns AttributeError: 'XMLExporter' object has no attribute 'export' because it doesn't have export method

# 5. Logger System
# A backend system logs events in different ways.
# Write three classes — FileLogger, DatabaseLogger, and CloudLogger — each with a log(message) method
# that prints where the message is being logged.
# Write a function log_event(logger, message) that works with any logger.
# Then explain: how is this different from achieving the same thing with inheritance or abstract classes?
# With Inheritance, there would be a parent class like a Logger class with sub classes now like FileLogger that would be inheriting from the parent class and they would all have a log method and would not crash even if a particular class would not be overriding the fucntion from the parent class. Using abstract methods there would be enforcement
# class FileLogger():
#     def log(self, message):
#         print(f"{message} is being logged to a file")
# class DatabaseLogger():
#     def log(self, message):
#         print(f"{message} is being logged to a database")
# class CloudLogger():
#     def log(self, message):
#         print(f"{message} is being logged to the cloud")

# def log_event(logger, message):
#     logger.log(message)
# log_event(CloudLogger(), "Kiseuni employee data")
# log_event(DatabaseLogger(), "Student info")
# log_event(FileLogger(), "Invoice data")

# 6. Serializer

# Serialization - process of converting complex data objects or data structures into a format
# such as bytes, JSON, or XML—that can be easily stored (in memory, files, or databases) or transmitted across a network


# A web API needs to serialize objects into different formats.
# Write three classes — JSONSerializer, XMLSerializer, and CSVSerializer — each with a serialize(data) method
# that returns a string representation of the data in that format.
# Write a function send_response(serializer, data) that calls serialize() and prints the result.
# Pass a simple dictionary as data and test all three.

class JSONSerializer():
    def serialize(self, data):
        result = str(data).replace("'", "'")
        print(f"JSON: {result}")
        # return data.json()
class XMLSerializer():
    def serialize(self, data):
        result = "".join(f"<{k}>{v}</{k}>" for k, v in data.items())
        print(f"XML: <root>{result}</root>")
        # return data.xml()
class CSVSerializer():
    def serialize(self, data):
        result = ", ".join(f"{k}: {v}" for k, v in data.items())
        print(f"CSV: {result}") 
        # return data.csv()

def send_response(serializer, data):
    serializer.serialize(data)

data = {"Oscar": "CEO",
        "Morris": "Surgeon"}
send_response(JSONSerializer(), data)
send_response(XMLSerializer(), data)
send_response(CSVSerializer(), data)



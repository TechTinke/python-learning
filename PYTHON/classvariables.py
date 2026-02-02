#Class Variables = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allows you to share data among all objects created from that class
#Instance Variables are the one defined inside the constuctor

class Student:
    class_year = 2025 #This is the class variable
    num_students = 0

    def __init__(self, name, age ):#self refers to the object that is being created(Student)
        self.name = name #these are instance Variables
        self.age = age
        Student.num_students += 1 #Modifying a class variable

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.class_year)#Improved readability that class_year is a class variable not instance
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

#WORK TO BE DONE
# Configuration Manager for a Web App
# Many web applications share the same global settings (e.g., API version, default timeout).
# Create a AppConfig class with:
# Class variable: api_version = "v2.0"
# Class variable: default_timeout_seconds = 30
# Instance variables in __init__: user_id (str)
# Add a method get_full_config() that returns a dictionary with the user_id + the two class variables.
# Show usage: create two instances with different user_ids, change the class variable default_timeout_seconds to 60 via the class name, then print both configs to show the change affects everyone.
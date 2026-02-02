#Class Variables = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allows you to share data among all objects created from that class
#Instance Variables are the one defined inside the constuctor

class Student:

    def __init__(self, name, age ):#self refers to the object that is being created(Student)
        self.name = name
        self.age = age

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
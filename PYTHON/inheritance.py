#Inheritance = Allows a class to inherit attributess(variables) and methods(functions) from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)
#              You write code once and then you re-use it rather than make that change MANUALLY multiple times

#The child classes can have different attributes(variables) 
# and methods(functions) from the parent class 

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True #Since it is set to True, it doesn't need to be set as a parameter
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking: Woof!Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(cat.name)
print(mouse.name)
dog.eat()
dog.sleep()
cat.eat()
cat.sleep()
mouse.eat()
mouse.sleep()
dog.speak()
cat.speak()
mouse.speak()
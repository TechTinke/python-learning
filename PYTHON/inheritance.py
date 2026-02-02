#Inheritance = Allows a class to inherit attributess(variables) and methods(functions) from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True #Since it is set to True, it doesn't need to be set as a parameter
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

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
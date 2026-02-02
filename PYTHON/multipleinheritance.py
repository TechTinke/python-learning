#multiple inheritamce = a child class inherits from more than one parent Class
#                       C(A, B)
#multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A
#                         A parent can inherit from another parent

class Animal:
    def __init__(self, name):
        self.name = name
        pass
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): #Parent Class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal): #Parent Class
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #Child class can inherit from more than on parent class
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

print(" ")

rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()
hawk.eat()
hawk.sleep()

#WORK TO BE DONE

# 1. GUI Widget System (inspired by Tkinter or PyQt)
# Create two parent classes:
# Clickable: method on_click() → prints "Element clicked!"
# Draggable: method on_drag() → prints "Element dragged to new position"
# Create a child class Button(Clickable, Draggable) that inherits both.
# Add its own method render() → prints "Rendering button".
# Show: create a Button, call on_click(), on_drag(), render().
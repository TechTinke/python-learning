#For better organization as Class can take up a lot of space,
#The class defition should be placed in a different file for better organisation
#then imported to where the objects are being declared

#Attributes are variables that an object has
#Methods are actions that an object can perform

class Car:
    def __init__(self, model, year, color, for_sale): #Constructor method
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self): #Methods(fuctions) are actions that objects can perform
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")





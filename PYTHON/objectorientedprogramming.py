#object = A "bundle" of related attributes(variables) and methods(functions) 
#         Ex. A phone, A cup, A book
#         You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object
#methods are actions that an object can perform

from classcar import *

car1 = Car("Mustang", 2026, "Red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)
# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

car2.drive()
car1.stop()
car1.describe()
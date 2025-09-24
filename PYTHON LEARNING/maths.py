friends = 4
friends = friends + 1
friends += 2#argumented operator
friends = friends - 2
friends -= 2#argumented operator
friends = friends * 3
friends *= 3#argumented operator
friends =  friends / 2
friends /= 2 #argumented operator
friends = friends **2
friends **= 2 #argumented operator
rem_friends = friends % 3
friends %= 2 #argumented operator

x = 78.98
y = 5
z = 2

result = round(x) #used for truncation
result = abs(y) # returns the absolute value of a number(returns the positive value of a number)
result = pow(y, 3) #same as exponention
result = max(x,y,z) #returns the maximum value from a set of values
result = min(x,y,z) #returns the minimum value from a set of values

# USEFUL CONSTANTS AND FUNCTIONS 
import math

x = 2560
math.pi #returns the value of pi
math.sqrt(x) #returns the square root of a number
math.ceil(x) #rounded up(with decimal places)
math.floor(x) #rounded down(with decimal places)

# EXERCISES
#CIRCUMFRENCE OF A CIRCLE 
radius = float(input("Enter the radius of a circle: "))
circumfrence = 2 * round(math.pi, 2) * radius
print(f"The circumfrence of your circle is {round(circumfrence, 1)}cm")

#AREA OF A CIRCLE
radius = float(input("Please enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of your circle is {round(area, 2)}square centimetres")

#HYPOTENUSE OF A RIGHT ANGLED TRIANGLE
a = float(input("Please input the height of the triangle: "))
b = float(input("Please input the base of the triangle: "))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse of your right angled triangle is {round(c, 2)} cm")
print(type(c))
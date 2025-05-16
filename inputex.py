#mad libs
noun = input("Enter a noun:")
verb1 = input("Enter the first verb")
adjective = input("Enter an adjective")
verb2 = input("Enter the second verb")
pronoun = input("Enter a pronoun")

print(f"I have a pretty girlfriend and her name is {noun}")
print(f"My pretty girlfriend {noun} loves to {verb1}")
print(f"My girlfriend {noun} who loves to {verb1} is so {adjective}")
print(f"My girlfriend {noun} also loves to {verb2} {pronoun} me")

#Area/Volume of  a Rectangle 
length = int(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
height = int(input("Enter the height of the rectangle"))
area = length * width
volume = length * width * height
print(f"The area of the rectangle is {volume} square centimetres")
print(f"The area of the rectangle is {round(area, 2)}")

#SHOPPING CART
item = input("What item would you like to buy?:")
price = float(input("What is the price of the item?:"))
quantity = int(input(f"How many {item}s would you like to buy?:"))

total = price * quantity
print(f"You have bought {quantity} {item}s")
print(f"The total of your items is {round(total, 2)}")#Round function is used for truncation(You can also set the number of decimal places)


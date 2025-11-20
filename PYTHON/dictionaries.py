# dictionary = a collection of {key:value} pairs that are ordered and changeable. There are No duplicates
                            #    id : name
                            #    item : price 
                            #    country : capital

capitals = {"USA": "Washington DC",
            "Kenya": "Nairobi",
             "China": "Beijing",
              "India": "Indiana" }

# print(dir(capitals)) #used to see all the attributes and methods of a dictionary
# print(help(capitals))#in depth description of these attributes and methods of the dictionary

#Some of these methods include get, update, pop, popitem(), keys(), clear(), values(), items()

#1. GET 
# print(capitals.get("USA"))#the value associated with the key USA is Wahington DC so that is what will be printed
# print(capitals.get("India"))#the value associated with the key India is Indiana
# print(capitals.get("China"))#the value associated with the key China is Beijing
# print(capitals.get("Kenya"))#the value associated with the key Kenya is Nairobi

# print(capitals.get("Indi"))#if there is no value associated to the input key then the value returns None

#Checking whether a key is within the dictionary
# if capitals.get("India"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

#2.update - used to insert a new key value pair or update an existing value pair
# capitals.update({"Germany": "Berlin"}) #this adds a new key value pair
# capitals.update({"Germany": "Berinadina"})#this updates an existing key value pair
# capitals.update({"Kenya": "Hawkins"})#this updates an existing key value pair
capitals.update({"New York": "Laviiinski"})
#3.pop - used to remove a key value pair
capitals.pop("Kenya") #removes the key value pair associated with the id Kenya

#4. popitem() - removing the latest key value pair that was inserted within a dictionary
#capitals.popitem()

#5. clear() - clearing all the items from the dictionary
# capitals.clear() 
#after this an empty string is returned

#6. keys() - used to list all the keys within the dictinary
#print(capitals.keys())

# for key in capitals.keys():
#     print(key)
# - Iterate and print every key in the dictionary

#7. values() - used to list all the associated values of the keys in the dictionary
# print(capitals.values())

# for value in capitals.values():
#     print(value)
# - Iterate and print every value in the dictionary

#8. items() - used to list all the key value pairs within the dictionary in form of an object
# print(capitals.items()) - prints out the key value pairs in a list without any iteration
# print(capitals) # this only lists the keys

# for key, value in capitals.items():
#     print(f"{key} - {value}")
#iterates over every key value pair

#CONCESSION STAND PROGRAM
#Program to be used to help us grt more useed to dictionaries
# menu = {"pizza": 300.00,
#         "nachos": 400.50,
#         "popcorns": 600.00,
#         "fries": 200.50,
#         "chips": 100.00,
#         "pretzel": 300.50,
#         "soda": 300.00,
#         "lemonade": 400.25}

# cart = []
# total = 0

# print("----------MENU----------")
# for key, value in menu.items():
#     print(f"{key:15}: Kshs {value:.2f}")
# print("----------END----------")
# while True:
#     food = input("Please select an item from the menu(q to quit): ").lower() #.lower() method takes the user input and converts it to lowercase
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)#append is used to add the valid items from food(which is the input) to the cart

# print("-----YOUR ORDER-----")
# for food in cart:
#     total += menu.get(food)
#     print(food, end = " ")

# print()
# print(f"Total is : Kshs {total:.2f}")

menu = {"Chapati" : 20,
        "Rice" : 60,
        "Ugali": 30,
        "Beans": 60,
        "Cabbage": 50,
        "Pojo": 30}

plate = []
total = 0

print("--------KISII UNI MLO WA HARAKA--------")
for key, value in menu.items():
    print(f"{key:10} - Kshs {value:.2f}")
print("--------END OF MENU--------")

while True:
    order = input("Please select item to order menu(q to quit): ").lower()
    if order == "q":
        break
    elif menu.get(order) is not None:
        plate.append(order)

print("----ORDER YAKO COMRADE----")
for order in plate:
    total += menu.get(order)
    print(order, end =" ")

print()
print(f"The total price for your food is {total:.2f}")

 





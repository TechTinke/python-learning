#Iterable - any object/collection that can return its elements one at a time
#           allowing it to be iterated over in a loop.

#1. List - []
numbers = [1, 2, 3, 4, 5] 

for item in numbers:
    print(item)
print()
#reversed() functios is used to iterate backwards
for item in reversed(numbers):
    print(item)
#If we do not want each item to start we can use end
for item in reversed(numbers):
    print(item, end=" ")#since print() is a function
print() 


#2. Tuple - ()
items = (1, 2, 3, 4, 5)

for number in items:
    print(number, end=" ")
print() 

#3. Set - {}
#      A set cannot be reversed
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

#4. String
name = "Bro Code"
for character in name:
    print(character, end="")
print()


#5.Dictionaries - {}
#               - Almost similar to a set only that it has key value pairs
my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}
for key in my_dictionary:
    print(key) #if you iterate over a dictionary it only returns the keys
for value in my_dictionary.values():#.values() is used to return the values of the keys in the dictionary
    print(value)
for key, value in my_dictionary.items():#.items() is used to return the key value pairs of the dictionary
    #print(f"{key} = {value}")
    print(key, value)
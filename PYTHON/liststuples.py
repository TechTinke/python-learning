# #collection = single "varibale" used to store multiple values
# #List = [] ordered and changeable. Duplicates OK
# #Set = {} uordered and immutable, but Add/Remove OK. NO duplicates
# #Tuple = () ordered and changeable. Duplicates OK. FASTER

# #List #Can store multiple variables separated with a comma # Sorrounded with square bracket []
# #The naming convention should be in plural just as it is a list(multiple values)
# fruits = ["Apple", "Orange", "Banana", "Coconut", "Pineapple"] 
# #print(help(fruits))# What you can get to do with a list
# # print(fruits[2]) #accesing the element at index number 2 in the list
# # print(fruits[0:3]) #accesing the elements in the list from index 0 to 3 but 3 is exclusive
# #print(len(fruits)) #prints out the number of items in the list

# #in OPERATOR is used to find for an item within a list
# #returns a TRUE/FALSE(BOOLEAN) whether the item specified is in the list
# # print("Coconut" in fruits) #returns TRUE
# # print("Pineapple" in fruits) #returns TRUE
# # print("Oscar" in fruits) #returns FALSE
# # print("apple" in fruits) #returns FALSE as apple in the list starts with cap A
# # print("Banana" in fruits) #returns TRUE as Banana is in  the list
# # print("Orange" in fruits) #returns TRUE as Orange is in the list

# #RE-ASSIGNING - You can re-assign an element in a list using the index operator
# fruits[0] = "Watermelon"  
# fruits[1] = "Fenesi"
# fruits[1] = "Apple"
# #append method is used to add an item at the end of a list
# fruits.append("Berris") # Adds the item Berris at the end of the list
# fruits.append("Guava") #If you want to append more than one item, add an extra empty append 
# fruits.append(" ")

# #remove method is  used to remove an element from the list(SPECIFIED/ INDEX operator)
# fruits.remove("Coconut") #Removes the item Coconut from the list
# #fruits.remove("Oscar") #returns an error the item Oscar is not in the list
# fruits.remove(fruits[-1]) # removes the last element in the list
# fruits.remove("Berris") #removes the item Berris from the list
# fruits.remove(fruits[0]) #removes the element at index 0 from the list
# #fruits.remove("Fenesi") #removes the item Fenesi fro  the list

# #insert method is used to insert an element at a particular index  in the list
# fruits.insert(0, "Berris")# inserts Berris at index 0
# fruits.insert(1, "Cocomelon")#inserts Cocomelon at index 1 and pushes the item at index 1 to index 2
# fruits.insert(2, "Watermelon") #inserts Watermelon at index 2 and pushes the item at index 2 to index 3
# fruits.insert(2, "Guava") #inserts Guava at index 2 and pushes the item at index 2 to index 3
# fruits.insert(2, "Guava") #inserts Guava at index 2 and pushes the item at index 2 to index 3

# fruits.sort() #Places the items in the list in ALPHABETICAL order
# fruits.reverse() #reverses the order of items in the list based on their POSITIONS in the list and not Alphabetical Order
#     #If you want the list reversed in alphabetical order  you sort first
# #fruits.clear() #Clears all the items in the list

# #Getting the index of an item in the list
# ##print(fruits.index("Banana")) #returns 5
# #print(fruits.index("Guava")) # returns 2
# #print(fruits.index("Berris")) # returns 4
# #print(fruits.index("Oscar")) # ValueError(Oscar is not in the list) 

# print(fruits.count("Guava"))
# print(len(fruits))
# for fruit in fruits:
#     print(fruit)


#SET
#1. Does not include any Duplicates
#2. You can add/ remove elements from a set
#3. Unordered and immutable
#To set a variable in set you enclose the variable in {}

fruits = {"apple", "orange", "banana", "coconut", "watermelon"}

#Finding whether a value is within the set using in method - returns a TRUE/FALSE
# print("apple" in fruits) #returns TRUE because apple is in the fruits set
# print("orange" in fruits) #returns TRUE because orange is in the fruits set
# print("Coconut" in fruits) #returns FALSE because coconut is in the fruits set

#print(fruits[0]) #One cannot use indexing for a set because a set is UNORDERED 

#Adding an item in a set using add method
fruits.add("berries")
fruits.add("pawpaw")
fruits.add("fenesi")

#Removing an item using remove method
fruits.remove("berries")
fruits.remove("pawpaw")
fruits.remove("apple")

fruits.pop() #changing the order of the items in a set
#fruits.clear() #clear(delete) all the items in a list
print(fruits)
print(len(fruits))

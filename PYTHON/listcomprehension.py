#List Comprehension - a concise way to create lists in Python
#                      Compact and easier to read than traditional lists
#                      [expression for value in iterable if condition]

# Traditional way of doing it
doubles = []
for x in range(1, 11):#In range the second number is exclusive(1-10)
    doubles.append(x*2)#append() is for creating new values

print(doubles)

#List Comprehension
doubles = []
triples = [] 
squares = []

doubles = [num*2 for num in range(1, 11)]#List Comprension - concise way to create lists in Python
triples = [value * 3 for value in range(1, 11)]
squares = [x * x for x in range(1, 10)]

print(doubles)
print(triples)
print(squares)

#List Comprehension with String lists
fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits] #Re-assigning fruits list instead of creating a new list
fruit_chars = [fruit[0] for fruit in fruits] #Prints out the first character(index of 0) in each fruit

print(fruits)
print(fruit_chars)

#List Comprehension - Condition
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num <0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(odd_nums)



grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
failing_grades = [grade for grade in grades if grade <60]
print(passing_grades)
print(failing_grades)
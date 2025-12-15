# Function - block of reusable code(code that can be reused)


def happy_birthday(age, name):#name is a parameter(a temporary variable that is used within a variable)
    #You can set multiple parameters if you want to use more than one argument while calling an argument
    print(f"Happy birthday to {name}")#you instance is replaced with the parameter name
    print(f"You are {age} years old!")
    print("We shall always celebrate your birthday")
    print()

#happy_birthday() #this is invoking a function or simply calling a function that has already been defined
happy_birthday(20, "Bro")#Any data you send a function are known as arguments
                         #You also need a matching set of parameters while defining the function
                         #The order in which they follow each other also matters 
happy_birthday(28, "Oscar")
happy_birthday(30, "Steve")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of Kshs {amount:.2f} is due on {due_date}")

display_invoice("Amanda", 7800, "07/08/2025")

def order(name, food, total):
    print(f"Hello {name}")
    print(f"You ordered {food} and the bill for your order is Kshs {total:.2f}")

order("Oscar", "Chapati", 90 )
order("Abel", "Samosa", 30)
order("Ian", "Indomie", 45)


#return - statement useed to end a fucntion and send  the rseult back to the caller 

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(6, 5))
print(subtract(6, 5))
print(multiply(6, 5))
print(divide(6, 5))

def create_name(first, last):#parameters set up
    first = first.capitalize()#Capitalize the first letter of the variable first
    last = last.capitalize()#Capitalize the first letter of the variable last
    return first + " " + last #Concatenate the first and the last name together
                            #returning some data back to the place in which you invoke(call) a function

full_name = create_name("spongebob", "squarepants")
print(full_name)#sending our function some arguments


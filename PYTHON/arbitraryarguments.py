#Arbitrary- a varying amount of arguments(we do not know the number of arguments that the user is going to pass in when invoking a function)
# * - unpacking operator
# *args - allows you to pass multiple arguments(tuple)
# *kwargs - allows you to pass multiple keyword arguments(dictionary)

def add(a, b):
    return a + b
print(add(5, 7))
#print(add(4, 5, 6))#Since the arguments are now 3 the first function becomes invalid
#Modifying the function it becomes, 
#1. *args
def add(*args):#the parameter name can change, arg is a naming convention, the unpacking operator(*) is what's important.
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3, 4))

def display_name(*args):
    #print(type(args))
    for arg in args:
        print(arg, end=" ")
display_name("Dr.", "John", "Morris", "Davis", "III")

#2. **kwargs

def print_address(**kwargs):
    #print(type(kwargs))
    #iterating over values
    for value in kwargs.values():
        print(value)
    #iterating over keys
    for key in kwargs.keys():
        print(key)
    #iterating over both the keys and the values(key value pairs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.",
              apart="100",
              city="Detroit",
              state="Michigan", 
              zip="54321",
              )

#3. *args and **kwargs
def shipping_label(*args, **kwargs):#args first followed by kwargs
    for arg in args:
        print(arg, end=" ")
    print()
    #for value in kwargs.values():
      #  print(value, end=" ")
    #If you want each on a single line
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="Michigan",
               zip="54321")
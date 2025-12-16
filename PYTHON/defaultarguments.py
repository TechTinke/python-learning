#default arguments = a default value for certain parameters
   # Makes functions more flexible and reduces the number of arguments
   # - The default is used when the argument is omitted when calling/invoking a function
# - There are four types of arguments;
#1. positional arguments
#2. default arguments
#3. keyword arguments
#4. arbitrary arguments

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))#Automatically uses the arguments set at the parameters for dicount and tax
print(net_price(500, 0.1))#You can still set a different argument from the one that is set on the parameter
print(net_price(500, 0.1, 0))#You can still set a different argument from the one that is set on the parameter

#Count up timer Exercise
import time

def count(end, start=0):#end is exclusive(not included)#default argument should follow non default argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
count(30, 15)

def count(end, start=0):
    for x in range(start, end +1):
        print(x)
        time.sleep(1)
    print("The count is done")

count(30, 20)

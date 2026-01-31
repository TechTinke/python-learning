# #Variable scope  = where a variable is visible and accessible
# #scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# Local Variables are used first then if not there, the Enclosed ones then Global then Built In
# #Note: Functions can't see inside of other functions

#1. LOCAL VERSION
def func1():
    x = 1  #local version of x found within function 1
    print(x)

def func2():
    x = 2  #local version of x found within function 2
    print(x)

def func3():
    a = 1  #local version of a found within function 3
    print(a)

def func4():
    b = 2  #local version of b found within function 4
    print(b)


func1()
func2()

#2. ENCLOSED VERSION
def func1():
    x = 1
    def func2():
        # x = 2 #this is the variable that will be available
        #If it were to be eliminated, then the enclosed variable 1 would be used since x
        #that is to be printed within the local scope was not found
        print(x)
    func2()

func1()

#3. GLOBAL VERSION
def func1():
    print(x)

def func2():
    print(x)

x = 3 #declaring a global version of x
func1()
func2()
# The results if func1() and func2() will be 3 since 3 is the global variable of x
# and there are neither local nor enclosed variables of x

#4. BUILT-IN VERSION
from math import e #e is an exponential constant

def func1():
    print(e)

#if a global version of e is declared, it would be the one to be printed
# e = 3
func1()





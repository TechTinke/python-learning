#module = a file containing code you want to include  in your program
#         use 'import' to include a module  (built-in or your own)
#         useful to break up a large program into reusable separate files
#print(help("math")) #Functions under the math module
#print(help("modules"))#Listing the different types of modules

#You can import a module by calling its name
import math
print(math.pi)

#You can also declare a name(alias) for the module that you are importing
import math as m
print(m.pi)

#You can also use from to import a certain function in a module
#However, this can cause naming conflicts
from math import pi
print(pi)




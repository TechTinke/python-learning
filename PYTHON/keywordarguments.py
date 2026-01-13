#keyword arguments = an argument preceded by an identifier
                     # - Helps with readability
                     # - Order of arguments does not matter
# The 4 types of arguments still are;
           # 1. positional arguments
           # 2. default arguments
           # 3. keyword arguments
           # 4. arbitrary arguments

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    greeting = greeting.capitalize()
    title = title.capitalize()
    first = title.capitalize()
    last = last.capitalize()
    return greeting + " " + title + " " + first + " " + last


greeting = hello("morning", "mrs", "annah", "somba")#Positional argument should come before any keyword argument
print(greeting)
#keyword arguments are used to improve readability

#NB: Some of the built in functions such as print have keyword arguments for example
for x in range(1,11):
    print (x, end=" ")#end is a keyword argument found within the built in print statement
print(" ")
print("1", "2", "3", "4", "5", sep="-")#sep is a keyword argument found within the built in print statement


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=254, area=7, first=9049, last=9672)
print(phone_num)

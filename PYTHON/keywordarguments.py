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


greeting = hello("morning", "mrs", "annah", "somba")
print(greeting)
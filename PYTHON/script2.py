from script1  import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script 2")
    favorite_food("Sushi")
    favorite_drink("Coffee")
    print("Goodbye")

if __name__ == '__main__':
    main()
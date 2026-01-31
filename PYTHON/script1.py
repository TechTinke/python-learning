# print(__name__)

#Structure of __name__ = '__main__':
# if __name__ == '__main__':
#     main()

# from script2 import * # * means everything
# print(__name__)


def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script 1")
    favorite_food("pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()

# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# print("This is script 1")
# favorite_food("pizza")
# print("Goodbye")


import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
# number = random.randint(1, 20) #prints out different integers through the range of 1 and 6 each time it is executed e.g roller dice program
number = random.randint(low, high) #prints out different integers through the range of the variables low and high
number = random.random() # prints out floating point between 0 and 1
#.random() takes no arguments like .randint which can take 2 arguments
option = random.choice(cards) #great for picking a random element
random.shuffle(cards) #shuffling(changing in between the values)
#works with objects only 
# print(cards)
# print(option)

#PYTHON NUMBER GUESSING GAME 
lowest_num = 1
highest_num = 100
#Setting the range in terms of variables
answer = random.randint(lowest_num, highest_num)#lowest_num and highest_num are the arguments
guesses = 0
is_running = True
print("----Welcome to Oscar Python Number Guessing Game-----")
print(f"Select a number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer is {guess}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}: ")

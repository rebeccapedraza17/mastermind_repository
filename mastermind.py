# Rebecca Pedraza
# Nov 5
# Mastermind

# The computer will create a 4 digit random number without repeats
print("The computer will create a 4 digit random number")

# Imports
import random

# Variables
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
random.shuffle(numbers)
secret = numbers[:4]
print(secret)

# Ask user to guess the random number 
user_guess = [int(input("Guess the random number: "))]

# The loop will continue until is the correct guess or user runs out of chances
while user_guess is secret:
    if guess[0] == secret[0]:
        print("green")
    elif guess[0] == secret[0]:
        print("yellow")
    else:
        print("red")
    user_guess = print("Guess again: ")


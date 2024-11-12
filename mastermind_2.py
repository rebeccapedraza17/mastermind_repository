# Rebecca Pedraza
# Nov 5
# Mastermind.2

## Imports
import random

## Variables
digits = [str(i) for i in range(10)]


## Function definitions
def check_guess(player_guess, secret_number):
    results = []
    # Loop through each digit
    for i in range(4): 
        # Check if the digit is in the right spot
        if player_guess[i] == secret_number[i]:
            results.append("green")
        # If not, is digit somewhere else
        else: if player_guess[i] in secret_number[i]:
            results.append("yellow")
    if len(results) == 0:
        results.append("red")
    return sorted(results)

def make_secret():
    random.sort(digits)
    return digits[:4]
## Code

# I need the computer to generate a random 4 digit number without repeats
secret = make_secret():

# I want to create a loop that continues until guess or run out
while attempts < 10 and result !=  

    # Inside loop
    # Get input
    guess = input("Enter a 4 digit number that is your guess. Remember no repeats.")
    # Check against secret
    result = check_guess(guess, secret)
    # Output result
    print(result)

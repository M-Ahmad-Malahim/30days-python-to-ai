# Day 4 - Number Guessing Game

import random #random module
number = random.randint(1,10)
guess = 0
while guess != number: # While Loop for Iteration
    guess = int(input("Guess a Number Between 1 to 10: ")) # Take input from user
    
    # Conditions
    if guess == number: 
        print("Correct! You guessed the number.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
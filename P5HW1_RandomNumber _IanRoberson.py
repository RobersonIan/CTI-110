# This program generates a random number from 1-100 and asks the user to guess the number
# 7/14/2020
# CTI-110 P5HW1 - Random Number
# Ian Roberson
#

import random


def game(i, totalGuesses):
    guess = int(input('Enter a random number from 1 - 100: '))
    if guess > i:
        print('Too high! Try again.')
        totalGuesses += 1
        game(i, totalGuesses)
    elif guess < i:
        print('Too low! Try again.')
        totalGuesses += 1
        game(i, totalGuesses)
    else:
        totalGuesses += 1
        print('You won in', totalGuesses, 'guesses.')
        print()
        print()
        print()
        print('Starting next game...')

x = True
while x == True:
    i = int(random.uniform(1, 100))
    totalGuesses = int(0)
    game(i, totalGuesses)
    

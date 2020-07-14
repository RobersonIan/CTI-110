# Asks the user to add 2 random numbers and can recognize correct and incorrect answers.
# 7/14/2020
# CTI-110 P5HW2 - Math Quiz
# Ian Roberson
#

import random

def game(x, y):
    print('What is', x, '+', y)
    z = x + y
    guess = int(input('Enter your answer: '))
    if guess == z:
        print('Correct')
    else:
        print('Incorrect. The answer was', z)


i = True
while i == True:
    x = int(random.uniform(0, 1000))
    y = int(random.uniform(0, 1000))
    game(x, y)

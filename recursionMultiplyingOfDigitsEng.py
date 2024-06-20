# Python 3.8
# os - library for working with the console
# random - library for working with random data

import os
import random

# Setting the font color of the console
os.system('COLOR B')


# get_multiplied_digits - a function for the product of digits of a number
def get_multiplied_digits(number):
    str_number = str(number)  # converting a number to a string
    first = int(str_number[0])  # the first digit of the number

    # The production process
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


LEFT = 0  # LEFT - the left border
RIGHT = 100000  # RIGHT - the right border

number = random.randint(LEFT, RIGHT)
# number - a random integer
result = get_multiplied_digits(number)
# result - the product of the digits of the number

# Output of the result of the product of digits result of the number
print(f'\nThe product of the digits of a number {number}: {result}.\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen

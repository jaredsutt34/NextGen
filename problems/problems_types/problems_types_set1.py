import random
import time
from random import randint, choice  # call a function directly from a mod
from time import sleep

FirstVariable = int(2.9)
print(FirstVariable)
SecondVariable = int(-2.5)
print(SecondVariable)
ThirdVariable = input('How are you?')
print(ThirdVariable)
print(2018 - float(ThirdVariable))
#
a = 3
b = 5
c = 7
# Print true if a < b and b < c
# Also print true if a > b and b > c

all_three = all((a < b, b < c))or (a > b and b > c)
print(all_three)
print(( a < b and b < c) or (a > b and b > c))
# the other way


year = random.randint(2018)  # uses a range of ONLY numbers
print('was', year, 'a leap year?', end='\n')
print((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0))

letter = random.choice((5, 6, 19))  # pick from your choices
print(letter)

timeMod = time.sleep(5)
print('wait for it', timeMod)

print('wait for it...')
time.sleep(5)
print('done!')

print('challenge...', end= ' ', flush=True)
# flush just tells computer to just let all the held strings and stuff to be dropped
time.sleep(3)
print('accepted.')

import random
import time
from random import randint, choice  # call a function directly from a mod
from time import sleep

a = random. randint(0,10)

print(a)

year = random.randint(1000, 2018)  # uses a range of ONLY numbers
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


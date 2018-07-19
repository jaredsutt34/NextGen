import random

secretNumber = random.randint (1,10)
guessNumber = int(input("Guess a number..."))

# runs until its false

while guessNumber != secretNumber:
    guessNumber = int(input("WRONG. Guess another number..."))

print('You won.. the number was..', secretNumber)


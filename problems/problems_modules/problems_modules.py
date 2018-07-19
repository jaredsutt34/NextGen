from random import randint
from statistics import mode, mean

guessNumber = input('Pick a number from 1-10...')  # inclusive
randomNumber = randint(1, 10)

equalOrNot = int(guessNumber) == randomNumber
print('Are you a winner?', equalOrNot)
print('The corret number was...', randomNumber)

meanAge = mean((18, 20, 21, 17, 20, 15, 16, 20, 18, 21, 17, 22, 14))  # reason for the double parentesis
modeAge = mode((18, 20, 20, 21, 17, 15, 16, 20, 18, 21, 17, 22, 14))
# cant have a tie for the most frequent, bc then wouldn't work so added 20
print(meanAge)
print(modeAge)

# This is using conditionals

guessNumber = input('Pick a number from 1-10...')  # inclusive
randomNumber = randint(1, 10)

if guessNumber == randomNumber:
    print("correct")
else:
    print("wrong")

# or with an additional conditional

if int(guessNumber) == randomNumber:
    print('correct')
elif int(guessNumber) > randomNumber:
    print('too high')
else:
    print('too low')

#or

if int(guessNumber) == randomNumber:
    print('correct')
else:
    print("You lost. Why? you are off by...", abs(int(guessNumber) - randomNumber))
    if int(guessNumber) > randomNumber:
        print('too high of a guess')
    else:
        print('too low of a guess')

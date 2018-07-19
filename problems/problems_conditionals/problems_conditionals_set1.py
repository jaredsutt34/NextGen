from random import randint

winningNumber = randint(1, 10)
Message = 'You have won'
guessNumber = input('type a number...')
guessNumber = int(guessNumber)

if guessNumber > winningNumber: # if not true everything within is just completely ignored, even chnaged variables
    Message = 'too high'

elif guessNumber < winningNumber:
    Message = 'too low'

print(Message)


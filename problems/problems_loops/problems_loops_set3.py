from random import randint

firstNumber = 0
secondNumber = 1

while firstNumber != secondNumber:
    firstNumber = randint(1, 10)
    secondNumber = randint(1, 10)

print("The first number is...", firstNumber, 'and the other number is...', secondNumber)



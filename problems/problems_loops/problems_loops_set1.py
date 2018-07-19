from random import randint

myNumber = input('put a number between 1 and 10...')
computerNumber = randint(1,10)
print('is it ', computerNumber, '?')

answer = input()
oldguess = (0,)

while answer != 'yes':
    oldguess = oldguess + (computerNumber,)
    computerNumber = randint(1, 10)
    while computerNumber in oldguess:
        computerNumber = randint(1, 10)
    print('is it', computerNumber, '?') #can jump back to first while
    print(oldguess)
    answer = input()

print('you won')



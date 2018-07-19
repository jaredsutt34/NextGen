userWord = (input('PLease type in a word...'))
firstSet = 'x', 's'
secondSet = 'th', 'sh', 'ch'

if userWord[-1:] in(firstSet): #just until the end with the colon then nothing
    print(userWord + 'es')

elif userWord[-2:] in(secondSet): #just until the end with the colon then nothing
    print(userWord + 'es')

else:
    print(userWord + 's')

print()
totalNumber = 0

for x in range(20):
    totalNumber = totalNumber + (2 ** x) # totalNumber is carrying number from the previous loop

print(totalNumber)
print()

totalNumber2 = 0
for x in range(256): #what is that range really going up to?
    totalNumber2 = totalNumber2 + (2 ** x)
    print(totalNumber2)

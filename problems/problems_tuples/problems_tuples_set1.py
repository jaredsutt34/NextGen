from random import randint
from random import choice

myText = 'How are you today, dude'
print(len(myText))

myText = myText.replace(',', ' ')
myTextTuple = tuple(myText.split())
print(myTextTuple)
print('there are',len(myTextTuple), 'words')

name = ('kathy', 'benjy', 'alexander')

for i in name:
    print(len(i))

randomNames = ('jared', 'joey', 'james', 'john', 'jessie', 'jen')
randomNames2 = ('sutton', 'balm', 'setton', 'rosen', 'cohen', 'dweck')


numberWanted = int(input('how many names do you want...'))
totalNames = 0

while totalNames < numberWanted:
    random1 = choice(randomNames)
    random2 = choice(randomNames2)
    print(random1, random2)
    totalNames +=1

#longer way, could have just done a for loop


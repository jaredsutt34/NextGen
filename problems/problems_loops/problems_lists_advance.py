animal_list = ['hat', 'cat', 'book']

for i in range(len(animal_list)):
    animal_list[i] = animal_list[i].capitalize()

print(animal_list)

number_list = [1, 2, 3, 4, 5, 6]

for i in range(len(number_list)):
    number_list[i] = number_list[i] ** 2

print(number_list)

animalWeight_list = [
    ['dog', 30],
    ['mug', 2],
    ['book', 4]
]

print('a', animalWeight_list[1][0], 'weighs', animalWeight_list[1][1], 'pounds')

animalWeight_list.append(['truck', 5000])

print(animalWeight_list)

for animalweight in animalWeight_list:
        print ('a', animalweight[0], 'weighs', animalweight[1], 'pounds')


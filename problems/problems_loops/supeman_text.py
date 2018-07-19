from random import choice


file_handler = open('/Users/jaredsutton/Desktop/superman_jared.rtf', mode='r')
text_file = file_handler.read()
text_file = text_file.replace(',', '').replace('.', '').replace('?', '').replace(';','')
text_file_list = text_file.split()
text_file_set = list(set(text_file_list))
total = 0

for x in text_file_list:
    total = total + 1
print(total)

print(len(text_file_set))


# new problem
random_word = choice(text_file_set).lower()

turn = 0
all_guesses = ()
correct_guesses = []
player_letter = ''

while (len(set(correct_guesses)) != len(set(random_word))) and turn < 10:

    all_guesses = all_guesses + (player_letter,)
    turn = turn + 1
    player_letter = input('guess a letter...')

    while  player_letter in all_guesses:
        player_letter = input('guess a letter...')

    for w in random_word:
        if w in all_guesses:
            print(w, end='')
            correct_guesses.append(w)
        else:
            print('_', end=' ')

if turn >= 10:
    print('you lost')
else:
    print('you won')
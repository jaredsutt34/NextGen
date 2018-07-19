from random import randint

# #set 2
# listOf_targets = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',]
#
# prize_spot = randint(0, 9)
#
# player_guess = -1
# turn = 0
#
# while player_guess != prize_spot and turn < 6:
#     turn = turn + 1
#     player_guess = int(input('guess the spot I hid the prize: '))
#     if player_guess != prize_spot:
#         listOf_targets[player_guess] = 'x'
#         for i in listOf_targets:
#             print(i, end='  ')
#     elif player_guess == prize_spot:
#         listOf_targets[player_guess] = '!!@!!'
#         for i in listOf_targets:
#             print(i, end='  ')
#     print()
#
# if player_guess == prize_spot:
#     print('/n''you found the prize')
# else:
#     print('you lost')

#more complicated

listOf_targets = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',]

prize_spot = randint(0, 10)
prize_spot2 = randint(0, 10)
while prize_spot == prize_spot2:
    prize_spot2 = randint(0, 10)
total_prize_spots = [prize_spot, prize_spot2]
turn = 0

while total_prize_spots != [] and turn < 20:
    turn = turn + 1
    for i in listOf_targets:
        print(i, end='  ')
    print()
    player_guess = int(input('guess the spot I hid the prize: '))
    if player_guess not in total_prize_spots:
        listOf_targets[player_guess] = 'x'

    elif player_guess in total_prize_spots:
        total_prize_spots.remove(player_guess)
        listOf_targets[player_guess] = '!!@!!'

    print()

if len(total_prize_spots) == 0:
    print('\n''you found the prize(s)')
else:
    print('you lost')

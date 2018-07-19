from random import randint

# set 3
# light-brite

light_bright = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

board = []
for i in range(0, 10):
    board.append(light_bright.copy()) # save each row to another piece of memory

prizes = [
    [randint(0, 9), randint(0, 9)],
    [randint(0, 9), randint(0, 9)]
]

turns = 10
while prizes != 0 and turns > 0:
    turns = turns - 1
    x, y = map(int, input('pick a row and collum ').strip().split(' '))
    if [x,y] in prizes:
        print('you got it')
        board[x][y] = 'X'
        prizes.remove([x, y])
    else:
        board[x][y] = 'O'
    for row in board:
        for placement in row:
            print(placement, end= ' ')
        print('\n')

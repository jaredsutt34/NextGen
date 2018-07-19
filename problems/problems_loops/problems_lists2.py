# inputget_numbers = input('please put in some numbers...')
# get_numbers = get_numbers.replace(',', '')
# get_numbers = get_numbers.split(' ')
#
# total = 0
#
# for x in get_numbers:
#     total = total + int(x)
#
# print(total)
#
# get_numbers = input('please put in some numbers...')
# get_numbers = get_numbers.replace(',', '')
# get_numbers = get_numbers.split(' ')
#
# total = 1
#
# for x in get_numbers:
#     total = total * int(x)
#
# print(total)
#
# total = 0
# get_numbers = input('please put in some numbers...')
# max_num = 0
#
# for x in get_numbers:
#     if x > max_num:
#         max_num = x
#
# get_numbers = (3, 5, 6, 4, 1, 100, 9)
# min_num = get_numbers[0]
#
# for x in get_numbers:
#     if x < min_num:
#         min_num = x
#
# print(min_num)

scores = [
    [97, 89, 91],
    [80, 85, 88],
    [100, 59, 70]
]

for i in range(len(scores)):
    for x in range(len(scores[i])):
        scores[i][x] = scores[i][x] + 3

print(scores)

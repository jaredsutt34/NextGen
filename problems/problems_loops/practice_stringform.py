# things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
# prices = [50, 100, 5, 5, 1, 25]
#
# total = 0
# for i in things:
#     print('{:>12}: ${:>5.2f}'.format(i, (prices[total])))
#     total = total + 1
#
# print('JaredSutton'.rjust(20,'.'))

things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
prices = [50, 100, 5, 5, 1, 25]

total = 0
for i in things:
    print(i.rjust(12), ': $', str(prices[total]).ljust(10)) #why is it spacing all weird and stuff
    total = total + 1



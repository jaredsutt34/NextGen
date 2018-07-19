# was all my code with Brians end help... and i dont understand

word = 'dog'  # for simplistic reasons we are doing random

# would have ints or strings within the touple... touple of strings or touple of ints
# so then a string or int in a touple can equal another variable that is just one string or just one variable

# word = 'tooth'
# correct_guess = ()
# amt_guess = 0
# all_letters = ()
#
# while len(word) != len(correct_guess) and amt_guess < 6: #both need to be true to keep going, if one is flase it kicks out
#     amt_guess = amt_guess + 1
#     user_guess = input('Guess a letter:').lower()
#     print('\n', 'you guessed ', amt_guess, ' time(s)', sep='')
#
#     while user_guess in all_letters:
#         # user_guess = input('Guess a letter:').lower()
#         user_guess = input('You guessed this already. Try again:').lower()
#
#     all_letters = all_letters + tuple(user_guess)
#     print('\nthese are your guessed letters:', all_letters)
#
#     if user_guess in word:
#         print('correct guess')
#         correct_guess = correct_guess + tuple(user_guess)
#
#     for i in word:
#         if i in correct_guess:
#             print(i, end=' ')
#         else:
#             print('_ ', end=' ')
#
# if len(word) == len(correct_guess):
#     print('good game, you won')
# elif amt_guess == 6:
#     print('you lost, bye')

# still never made it work id the word has a letter more than one

all_numbers = (1, 2, 3, 4, 5)
for i in all_numbers:
    print(i)

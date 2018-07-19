# challenge

gradeGotten = input('Enter you test grade...')
gradeGotten = int(gradeGotten)
# a = [93, 94, 95, 96, 97, 98, 99, 100]
#
# # if a.index(int(gradeGotten)):
# #     print("A")

if gradeGotten >= 93:
    print('A')
elif gradeGotten >= 90:
    print('A-')
elif gradeGotten >= 87:
    print('B+')
elif gradeGotten >= 85:
    print('B')
elif gradeGotten >= 83:
    print('B-')
elif gradeGotten >= 78:
    print('C+')
elif gradeGotten >= 76:
    print('C')
elif gradeGotten >= 72:
    print('C-')
elif gradeGotten >= 69:
    print('D+')
elif gradeGotten >= 66:
    print('D')
elif gradeGotten >= 63:
    print('D-')
else:
    print('F')

# ## do other one as well - . Make a simple calculator that adds or subtracts. Ask the user for the first number. Ask them for a ‘+’ or ‘-‘. Ask the user for a second number. If the user entered ‘+’, add the two numbers. If the user entered ‘-‘, subtract the two numbers.
# 3. BONUS: Extend your calculator in #2 with multiplication, division, exponents.
# 4. BONUS-BONUS: Make up your own operator and use it in your calculator. Eg. If you user enters “weird”, divide the number by 10 thousand.

firstNumber = int(input('Put in number'))
operationRequired = input('+ or -')
secondNumber = int(input('Put in another number'))

if operationRequired == '+':
    print(firstNumber + secondNumber)

elif operationRequired == '-':
    print(firstNumber - secondNumber)

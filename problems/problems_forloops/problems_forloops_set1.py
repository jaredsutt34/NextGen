for number in range(0, 99):

    if number % 3 == 0:
        print(number)

count = 0

# problem 2

for countMultiples in range(0, 200):
    if countMultiples % 7 == 0:
        count = count + 1

print(count)

# problem 3

for x in range(8, 0, -1): # done backwards
    print(pow(2, x))

#problem 4

whatName = input('Please put in your name')

for i in whatName:
    print(i, end= ' ')

whatName = input('\nPlease put in your name')

#problem 5

for i in whatName:
    if i == 'a' or i == 'o' or i == 'u' or i == 'e' or i == 'i':
        print(i)

#problem 6

whatName = input('Please put in your name')

for i in whatName:
    a = ord(i)
    aa = str(bin(a))
    print(aa)
    aaa = aa[2:]
    print(aaa)



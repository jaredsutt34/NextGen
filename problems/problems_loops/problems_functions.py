# don't use a print statement in a function
# don't do fancy, or the finishing touch work
# only do the calculations

def max_number(num1, num2, num3):  # variables dire after, only alive when the function is called in that line
    return max((num1, num2, num3))


def sum_number(num4, num5, num6):
    return num4 + num5 + num6


def mult_numbers(num7, num8,
                 num9):  # mine can only take that exact amount other way, use tuple and loops, can take more
    return num7 * num8 * num9


def reverse_string(str1):
    return str1[::-1]


def create_factorial(numbers_input):
    calc_number = range(numbers_input)
    total = 1
    for x in calc_number:
        total = total * x
    return total


def check_number(num10, range, range2):
    if num10 > range and num10 < range2:
        return True
    else:
        return False


def evaluate_string(str1):
    total = 0
    total1 = 0
    for x in str1:
        if x not in '0123456789':  # dont count numbers
            if x in str1.lower():
                total = total + 1
            else:
                total1 = total1 + 1

    return (total, total1)


def make_unique(user_contents):
    user_contents_unique = set(user_contents)
    return user_contents_unique


# continue on... we are up to question number 9

def makeEven(a):
    evenNumbers = ()
    for i in a:
        if i % 2 == 0:
            evenNumbers = evenNumbers + (i,)
    return evenNumbers


def getWeight(a, b='Earth'):
    if b.lower() == 'mercury':
        return a * .38
    elif b.lower() == 'venus':
        return a * .91
    elif b.lower() == 'mars':
        return a * .38
    elif b.lower() == 'jupiter':
        return a * 2.38
    elif b.lower() == 'saturn':
        return a * 1.06
    elif b.lower() == 'uranus':
        return a * .92
    elif b.lower() == 'neptune':
        return a * 1.19
    elif b.lower() == 'pluto':
        return a * .06
    else:
        return a

    # do return not the print function
    # cant even take anything insdie, just a rule to have thsoe parentesis for methods

if __name__ == '__main__':
    print(getWeight(130, 'marS'))

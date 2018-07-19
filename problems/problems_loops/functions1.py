def make_double(b):
    double = b * 2
    return double


def make_half(a):
    half = a / 2
    return half


num_tester = make_half(10)
print(num_tester)


def make_plural(word):  # python just able to assume what you want(like int or string)...
    # most other languages you'd have to say
    add_word = word + 's'
    return add_word


wrd_tester = make_plural('dog')
print(wrd_tester)

def get_power(base, exponent):
    calc_done = base **  exponent
    return calc_done


num_tester2 = get_power(8, 2)
print(num_tester2)

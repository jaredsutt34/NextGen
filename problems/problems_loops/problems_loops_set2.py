
createPassword = input('Make a password:')

while len(createPassword) < 8 or createPassword == createPassword.lower():
    print('invalid')
    createPassword = input('Make a password:')

print('password successfully made')


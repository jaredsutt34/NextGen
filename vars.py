t = 5
animal = 'monkey'
location = 'candy store'

d = vars().copy()  # all the variables in the program and save as a variable

for k, v in d.items():
    if '_' not in k:
        print(k, v)

for k in d:  # cant understand to give one to the value so must do d.items
    if '_' not in k:  # which is the tag
        print(k, d[k])

print(__name__)
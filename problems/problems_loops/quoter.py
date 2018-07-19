import re
from sys import exc_info

try:
    file_handler = open('/Users/jaredsutton/Desktop/harrypotter.txtfvwfv', mode='r')
    text_file = file_handler.read()
except:

    print('You have a mistake...fix out')
    print(exc_info()[0])

def get_quotes_by(name_person, text_to_search):

    counter = re.findall('".*".*' + name_person + '.*',text_to_search) # got to understand regular expressions better
    for i in counter:
        if 'told '+ name_person in i or 'to '+ name_person in i or 'about '+ name_person in i:
            counter.remove(i)
    return counter

# set 2
#
# file_handler = open('/Users/jaredsutton/Desktop/harrypotter.txt', mode='r')
# text_file = file_handler.read()
#
#
#
#     harry_speaks = re.findall('".*".*Harry.*', text_file)  # got to understand regular expressions better
#     for i in harry_speaks:
#         print(i)
#
#     for i in harry_speaks:
#         if 'told Harry' in i or 'to Harry' in i or 'about Harry' in i:
#             harry_speaks.remove(i)
#
#     hermione_speaks = re.findall('".*".*Hermione.*', text_file)  # got to understand regular expressions better
#     for i in hermione_speaks:
#         print(i)
#
#     for i in hermione_speaks:
#         if 'told Hermione' in i or 'to Hermione' in i or 'about Hermione' in i:
#             hermione_speaks.remove(i)
#
#     ron_speaks = re.findall('".*".*Ron.*', text_file)  # got to understand regular expressions better
#     for i in ron_speaks:
#         print(i)
#
#     for i in ron_speaks:
#         if 'told ron' in i or 'to ron' in i or 'about ron' in i:
#             ron_speaks.remove(i)

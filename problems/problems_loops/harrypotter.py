import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter

file_open = open(file='/Users/jaredsutton/Desktop/harrypotter.txt', mode='r')
text = file_open.read()  # .read gets all the contents of the file and converts it to a string
# print(len(text))
# print(len(text))

text = text.lower()
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace(':', '')
text = text.replace('"', '')
text = text.replace('/', '')
text = text.replace('?', '')
text = text.replace('!', '')

text_list = text.split()
text_unique = list(set(text_list))
# print(text_list.count('harry'))
print(len(text_list), len(text_unique), sep='\n')
# print(text_list)
# print(text_unique)

# for x in text_unique:
#     print(x, 'appears', text.count(x), file = new_file)
#
# adverbs = [x for x in text_unique if x.endswith('ly')]
# print(adverbs)
#
# hyphen_finder = [x for x in text_unique if '-' in x]
# print(hyphen_finder)
#
# s_finder = [x for x in text_unique if 's' in x[0:1]]
# print(s_finder)
#
# one_time_used = [x for x in text_list if text_list.count(x) == 1]
# print('\n', one_time_used)
#
# get_capitalized = [x.capitalize() for x in text_list if x in ('harry', 'potter', 'ron')]
# print(get_capitalized)

plt.scatter(['Total words', 'Unique words'], [len(text_list), len(text_unique)])
plt.show()

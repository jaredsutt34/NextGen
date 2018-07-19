# residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
#
# menu = {}
# menu['Sunday'] = 16.78
# menu['Mmonday'] = 3.76
# menu['Tuesday'] = 6.71
#
# for x in menu:  # runs and python knows to take the tags not the values
#     print(x, ': ', menu[x])
#
# zoo_animal_locations = {
#       'Unicorn' : 'Cotton Candy House',
#       'Sloth' : 'Rainforest Exhibit','Bengal Tiger' : 'Jungle House',
#       'Atlantic Puffin' : 'Arctic Exhibit',
#       'Rockhopper Penguin' : 'Arctic Exhibit'
# }
#
# del zoo_animal_locations['Sloth']
# del zoo_animal_locations['Bengal Tiger']
# print(zoo_animal_locations)
#
# zoo_animal_locations['Rockhopper Penguin'] = 'Amazon Forest'
# print(zoo_animal_locations)
#
# webster = {
#       "Aardvark": "A star of a popular children's cartoon show.",
#       "Baa": "The sound a goat makes.",
#       "Carpet": "Goes on the floor.",
#       "Dab": "A small amount."
# }
#
# for i in webster: # because it calls the tags
#     print(webster[i])


my_dict= {
    'title': 'Stranger Things',
    'is_show': True,
    'seasons': 2
}

print(my_dict.items()) # returns a list of tuples
print(my_dict.keys())
print(my_dict.values())

for k, v in my_dict.items(): # this is toooooo smart, knows to assign first V to key and second V to values
    print(k, ':', v)

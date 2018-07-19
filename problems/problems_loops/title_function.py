def title_fixer(title_name):
    word_bank = ['of', 'in', 'the', 'and', 'or']
    title_name = title_name.lower()
    title_name = title_name.split()
    for i in range(len(title_name)):
        if title_name[i] not in word_bank:
            title_name[i] = title_name[i].capitalize()
    title_name[0] = title_name[0].capitalize() # thought this was Not supposed to work
    title_name = ' '.join(title_name) # why doesnt this return it with the parenthesis and wrapped in quotes

    return title_name


my_title = 'of catcher IN the rYE'
print(title_fixer(my_title))

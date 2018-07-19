from random import choice

main_course = ['salmon', 'rice', 'steak']
main_course.insert(0, 'stew')
print(main_course)

user_maincourse = input('please type in 3 main courses...')
user_maincourse = user_maincourse.split()
main_course.extend(user_maincourse)
print(main_course)

side_courses = ['carrots', 'fries', 'salad']
style_courses = ['seared', 'boiled', 'baked']

randomized_meal = choice((main_course, side_courses, style_courses))
print(randomized_meal)

enterProblem = input('enter a problem...')
enterProblem = enterProblem.split()
first_part = int(enterProblem[0])
third_part = int(enterProblem[2])
second_part = enterProblem[1]
answer = 0

if second_part == '+':
    answer = first_part + third_part
elif second_part == '-':
    answer = first_part - third_part
elif second_part == '*':
    answer = first_part * third_part
elif second_part == '/':
    answer = first_part / third_part

print(answer)


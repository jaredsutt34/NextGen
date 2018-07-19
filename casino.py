from dice import Dice

dice = Dice()
print(dice.current_side_up)

dice.roll()

print(dice.current_side_up)

dice_two = Dice()
dice_two.num_sides = 12
dice_two.current_side_up = 1
dice_two.range_of_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
dice_two.roll()
print(dice_two)

dice_three = Dice()
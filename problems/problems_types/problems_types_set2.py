NumberOne = input('Please enter a numbers...')
NumberTwo = input('PLease enter another number...')
NumberThree = input('Please enter last number...')
FirstCalculation = int(NumberOne) * int(NumberTwo)
FinalCalculationResult = FirstCalculation / int(NumberThree)
print (FinalCalculationResult)

CheckEven = FinalCalculationResult % 2 == 0
# 1 dollar = .86 euro

HolidayMoney = input('How much money will you take on the holidays?')
EuroEquivalent = int(HolidayMoney) * .84
print(EuroEquivalent)

# addition, multiplication, greater than or less than

UserName = input('what is your name?')
UserNameFixed = UserName[0:1] #start and then up to but NOT including
UserNameConverted = ord(UserNameFixed)
print(UserNameConverted)


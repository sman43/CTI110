# Kenneth Annan
 # 2/11/25
 # P1HW2
 # Travel Budget calculator

#start
print("-"*2,"This Program calculates and displays travel expenses","-"*2)
#values
budget=int(input("Enter your Budget: "))
loc=input('Where are you going?:')
gas=int(input('How much do you plan on spending on gas?:'))
acc=int(input('How much do you plan on spending on accomodations/Hotels?:'))
eat=int(input('Finally, How much do you plan on spending on food?:'))
final=budget - gas - acc - eat
print('\n')

print('-----Travel Expenses-----')
print('Location:',loc)
print('Initial Budget:',budget)
print('\n')

print('Fuel:',gas)
print('Accomodations:',acc)
print('Food:',eat)
print('\n')

print('-----Spending money-----')
print('$',final)

input('press any key to continue.')

#end
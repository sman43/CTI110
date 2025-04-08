# Kenneth Annan
 # 2/25/25
 # P2HW1
 # Travel Budget calculator Revision

#start
print("-"*2,"This Program calculates and displays travel expenses","-"*2)

#values

budget=float(input("Enter your Budget: "))
print()
loc=input('Where are you going?:')
print()
gas=float(input('How much do you plan on spending on gas?:'))
print()
acc=float(input('How much do you plan on spending on accomodations/Hotels?:'))
print()
eat=float(input('Finally, How much do you plan on spending on food?:'))
total=gas + acc + eat
final=budget - gas - acc - eat
print('\n')

print('-----Travel Expenses-----')
print(f'{'Location:':<20} {loc}')
print(f'{'Initial Budget':<20} ${budget:.2f}')
print(f'{'Fuel':<20} ${gas:.2f}')
print(f'{'Accomodations':<20} ${acc:.2f}')
print(f'{'Food':<20} ${eat:.2f}')
print('\n')

print('-----Spending money-----\n')
print(f'{'You spent:':<20} ${total:.2f}')
print(f'{'You have:':<20} ${final:.2f} left')

input('press any key to continue.')

#end
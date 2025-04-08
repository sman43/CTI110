#P3LAB
#3/6/25
#Kenneth Annan
#Introduction to branching



#inputs
money=float(input('Enter the amount of money as a float: $'))
money=int(money*100)

#calculations
num_dollars=(money // 100)
money= money- (num_dollars * 100)
quarters=money //25

remainder= money%25

dimes=remainder//10

remainder=remainder%10

nickels=remainder//5

remainder=remainder%5

pennies=remainder//1




#I did have to look up how to print without skipping the line,
# hence the end='' function for when there isn't any currency.

#printing
if money==0:
    print('No change due!')


if quarters>=2:
    print(quarters, 'Quarters')
elif quarters==0:
    print(end='')
else:
    print('One Quarter')
if dimes>=2:
    print(dimes, 'Dimes')
elif dimes==0:
    print(end='')
else:
    print('One Dime')
if nickels>=2:
    print(nickels, 'Nickels')
elif nickels==0:
     print(end='')
else:
    print('One Nickel')
if quarters>=2:
    print(pennies, 'Pennies')
elif pennies==0:
    print(end='')
else:
    print('One Penny')


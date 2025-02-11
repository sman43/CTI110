 # Kenneth Annan
 # 2/11/25
 # P1HW1
 # Coding an exponent calculator, as well as an addition and subtraction calculator.

#start
print("-"*5,"Exponent Calculator","-"*5)

exp1=int(input("Pick an integer as the base value: "))
exp2=int(input("Pick integer as the exponent: "))

exp3=exp1**exp2
print('\n')
print(exp1,"to the power of",exp2,"is",exp3,"!!")
print('\n')

input('press any key to continue.')
print('\n')

print('-----Addition and Subtraction-----')

addsub1=int(input("Pick a base number: "))
addsub2=int(input("Pick number to add: "))
addsub3=int(input('Pick a number to subtract: '))
print('\n')

addsub4=addsub1+addsub2-addsub3
print(addsub1,"+",addsub2,"-",addsub3,"=",addsub4)
print("-"*34)
input('press any key to continue.')

#end
#P4LAB2
#Kenneth Annan
#3/23/25
#For and While loops Resubmission
import math
keep_going='yes'

while keep_going=='yes':
    number=int(input('Enter an integer: '))
    if number>0:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
            print('\n')
    else:
        print('This program only handles positive integers.')
    keep_going=input('Do you want to run the program again? ')
    
if keep_going.lower()!='yes':
     print('\n')
     print('Exiting Program...')
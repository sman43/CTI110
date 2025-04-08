#Kenneth Annan
#3/1/25
#P2HW2
#Grade Averaging
import math
mod1=float(input('Enter grade for module 1:'))
mod2=float(input('Enter grade for module 2:'))
mod3=float(input('Enter grade for module 3:'))
mod4=float(input('Enter grade for module 4:'))
mod5=float(input('Enter input for module 5:'))
mod6=float(input('Enter grade for module 6:'))
grades=[mod1,mod2,mod3,mod4,mod5,mod6]
low=min(grades)
high=max(grades)
tot=sum(grades)
av=float(tot/len(grades))

print('-----------results-----------')
print(f'{'Lowest Grade:':<20} {low:.2f}')
print(f'{'Highest Grade:':<20} {high:.2f}')
print(f'{'Sum of Grades:':<20} {tot:.2f}')
print(f'{'Average:':<20} {av:.2f}')

print('-----------'*4)
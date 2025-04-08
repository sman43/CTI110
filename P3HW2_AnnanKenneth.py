#P3HW2
#Kenneth Annan
#3/7/25
# Employee hours program with overtime calculations


name=input('Enter Employee Name: ')
hours=float(input('Enter Hours worked:'))
rate=float(input('Enter Wage: '))
pay= rate*hours
ot=hours-40
otrate=rate*1.5
otpay=ot*otrate

print('Employee:', name)
print(f'{'You made: '} ${pay:.2f} {'For working'} {hours:.2f} hours this week.')
if hours > 40:
    print(f'{'Plus '} ${otpay:.2f} in overtime pay this week.')
elif hours ==0:
    print('You did not work this week.')
else:
    print('')
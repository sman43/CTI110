#P4HW2
#Kenneth Annan
#3/27/25
# Employee hours program with overtime calculations and while loop
keep_going='yes'
emp_entered=0
ovrot=0
ovreg=0
ovrpay=0
while keep_going=='yes':
    
    name=input("Enter Employee's name or 'Done' to terminate: ").lower()
    if name!='done':
        hours=float(input('Enter Hours worked:'))
        rate=float(input('Enter Wage: '))
        pay= rate*hours
        ot=hours-40
        otrate=rate*1.5
        otpay=ot*otrate
        totpay=otpay+pay
        print('Employee:', name)
        print(f'{'Hours Worked'} {'Pay Rate':>10} {'Overtime':>15} {'Overtime Pay':>15} {'Regular Pay':>15} {'Gross Pay':>10}')
        print('--'*40)
        print(f'{hours:.1f} {rate:>15.2f} {ot:>15.2f} {otpay:>15.2f} {pay:>15.2f} {totpay:>10.2f}')
        print('--'*40)
        print('\n')
        emp_entered+=1
        ovrot+=otpay
        ovreg+=pay
        ovrpay+=totpay
        print(f'{'Total Number of employees entered: '} {emp_entered}')
        print(f'{'Total amount paid for overtime: '} {ovrot}')
        print(f'{'Total amount paid for regular hours: '} {ovreg}')
        print(f'{'Total amount paid in gross: '} {ovrpay}')
        
    else:
        break
    
    



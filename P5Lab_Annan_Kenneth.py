#P5LAB
#4/2/25
#Kenneth Annan
#Self Checkout

 #Mr. Norris helped me with getting it to properly display the dollars and the correct change.


import random

def get():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f'You Owe: ${owed:.2f}')
    
    while True:
            try:
                money = float(input('How much are you going to pay? $'))
                if money < owed:
                    print("You must pay at least the amount owed.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    
    change=((money-owed))
    change=round(change, 2)
                                     #debugging print('owed amount', owed)
                                        #print('paid amount', money)
                                        #print('change amount', change)
    return change




def calculations(change):
    money=change
    money = int(money*100)   #convert to pennies
                                  #print('money after mult', money)
    dollars=(money // 100)
    remainder=(money % 100)
                              #debug print('rma100', remainder)
    quarters=remainder //25
   
    remainder=remainder%25
                              # remainder after for debugging print('rma25', remainder)
    dimes=remainder//10
    
    remainder=remainder%10
                                     #print('rma10', remainder)
    nickels=remainder//5

    remainder=remainder%5
                             #print('rma5', remainder)
    pennies=remainder
    
    return int(dollars), int(quarters), int(dimes), int(nickels), int(pennies)


def main():
    change = get()
    dollars, quarters, dimes, nickels, pennies =calculations(change)
    dollars=round(dollars)
    money_returned= change
    print(f'{'Your Change is: $'} {money_returned:.2f}') 
    if money_returned==0:
        print('No change due!')
    else:
        if dollars:
            print(dollars, 'Dollars')
        if quarters:
            print(quarters, 'Quarters')
        if dimes:
            print(dimes, 'Dimes')
        if nickels:
            print(nickels, 'Nickels')
        if pennies:
            print(pennies, 'Pennies')
    return  quarters, dimes, nickels, pennies, money_returned, change


main()

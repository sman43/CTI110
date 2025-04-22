#P5HW1
#4/8/25
#Kenneth Annan
#Game where you play as a hero and fight bosses.


import random


def create():
    cc='yes'
    cw='yes'
    while cc=='yes':
        Hname = input('Name your Hero!: ')
        if Hname!='':
            print(f'{'Welcome!, '} {Hname}')
            cc='no'
            continue
        else:
            print("Invalid input. Please enter a valid name.")
    while cw=='yes':
        wp = input('Pick a Weapon (Enter "Sword" or "Bow".) ')
        wp=wp.lower()
        if wp== 'sword':
            print('You chose the Sword!')
            cw='no'
            continue
        elif wp== 'bow':
            print('You chose the Bow!')
            cw='no'
            continue
        else:
            print("Choose a valid weapon.")
    hero_stats= {'Name': Hname, 'Weapon': wp}
    return hero_stats



def path():
    pathselected='no'
    while pathselected=='no':
        pathchoice=input("You've come across a path! Will you go Left or Right? ")
        pathchoice=pathchoice.lower()
        if pathchoice=='left':
            print('You went left and found a spell for double damage and Double Health!!')
            pathselected='yes'
            continue
        elif pathchoice=='right':
            print('You went right and found a spell for 2x damage!')
            pathselected='yes'
            continue
        else:
            print('Pick a Direction.')
    return pathchoice

def pathresult(pathchoice):
    bow_damage = [5, 10, 15, 20, 25]
    sdmg= 15
    if pathchoice=='left':
        multiplier=2
        bwdmg= [x * multiplier for x in bow_damage]
        sdmg=30
    else:
        multiplier=4
        bwdmg= [x * multiplier for x in bow_damage]
        sdmg=30
    return bwdmg, sdmg

def main():
    hero_stats=create()
    wp = hero_stats['Weapon']
    hname= hero_stats['Name']
    pathchoice=path()
    bwdmg, sdmg=pathresult(pathchoice)
    is_angry= ['yes', 'no']
    angry=random.choice(is_angry)
    if pathchoice== 'left':
        player_health=200
    else:
        player_health=100
        
    boss_damage= [5, 10, 15]
    boss_health=100
    if angry=='yes':
        boss_health=200
        boss_damage= [x * 1.5 for x in boss_damage]
    print(f'{'Time to Fight the Boss! He has:' } {boss_health} {'HP'}')
    
    if angry=='yes':
        print('The boss seems especially angry today...')
    print('')
    input('Press any button to continue. ')
    turn=1
    if wp=='bow':
        while boss_health>=0 and player_health>0:
            print(f'{'Turn: '} {turn} ')
            while turn== 1:
                print(f'{'Welcome, '} {hname}{', I have been waiting for you.'}')
                break
            random_damage=random.choice(bwdmg)
            print(f'{'You hit the boss for: '} {random_damage} {'HP!'}')
            boss_health-=random_damage
            random_bossdamage=random.choice(boss_damage)
            player_health-=random_bossdamage
            print(f'{'The boss hit you for: '} {random_bossdamage} {'HP!'}')
            if boss_health<= 0:
                boss_health=0
            print(f'{'You have: '} {player_health} {'HP Remaining.'}')
            print(f'{'The boss has: '} {boss_health} {'HP Remaining.'}')
            if boss_health==0:
                break
            input('Press any button to continue.')  
            turn+=1
    else:
        while boss_health>=0 and player_health>=0:
            print(f'{'Turn: '} {turn} ')
            while turn== 1:
                print(f'{'Welcome, '} {hname}{', I have been waiting for you.'}')
                break
            print(f'{'You hit the boss for: '} {sdmg} {'HP!'}')
            boss_health-=sdmg
            random_bossdamage=random.choice(boss_damage)
            player_health-=random_bossdamage
            print(f'{'The boss hit you for: '} {random_bossdamage} {'HP!'}')
            if boss_health<= 0:
                boss_health=0
            print(f'{'You have: '} {player_health} {'Remaining.'}')
            print(f'{'The boss has: '} {boss_health} {'Remaining.'}')
            if boss_health==0:
                break
            input('Press any button to continue.')
            turn+=1
    if boss_health<=0 and player_health>0:
        print(f'{'You beat the boss in: '} {turn} {'turns!'}')
    else:
        print('You Lost. :(')
             

main()

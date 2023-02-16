import random
# As a developer, I want to make at least five commits
    #  on GitHub with descriptive messages.  


# As a user, I want an engaging story to be told using print() statements.  


# As a user, I want Hercules (and each enemy) to have health,
    #  attack power, and a List of attack names saved in a Dictionary. 


# As a user, I want the ability to select Hercules’ attack using
    #  a menu prompt. 


# As a user, I want the foe’s attack to be chosen at random. 


# As a user, I want the results of each attack to be logged in the terminal.  


# As a developer, I want to use an Attack() function 
    # that will terminate when Hercules or an enemy’s health reaches zero.  


# As a developer, I want my RunGame() function to call my other functions
    #  in a logical order that will determine game flow. 


# As a developer, I want all of my functions to have a Single Responsibility.
    #  Remember, each function should do just one thing!  
from fighter_classes import Worrior
#next step is to replace the random ai with the ai worrior build created in the class
def run_Game():
    #the hud
    #player_level=1
    ugly_green_dude_level=1
    ugly_green_dude_health=40
    your_health=25
    fight_is_over=False
    crit_damage=10
    crit_chance=10
    block_chance=20
    dodge_chance=10
    attack_after_dodge=5
    story()
    attack(fight_is_over,your_health,ugly_green_dude_health,crit_chance,block_chance,dodge_chance,attack_after_dodge,crit_damage)
    
def story():
    print("It was a dark day that saw Our Great kingdom brought to it's knees. Nature itself was revolting, \ncreatures out of nightmares began to appear upon our sacred land. \nI remember that day well, though thoughts of our great kingdom's demise never once crossed my mind. \nFor me The Fall all began one early summer morning, the sun was just cresting the nearby hills \nwhen I woke to find a dagger attached to an ugly green arm, desending down upon me. \n(I must say this, impending death does wonders to get you out of bed in the morning). \nI quickly twisted the dagger out of the ugly arm's grip, and the fight of my life began... ")

def norm_attack(num,crit_chance,block_chance,dodge_chance,attack_after_dodge):
    norm=False
    starting_num=attack_after_dodge+dodge_chance+block_chance
    ending_num=101-crit_chance
    if starting_num<num and num<ending_num:
        norm=True
        return norm
    return norm

def crit(crit_chance,num):
    crit_hit=False
    crit_chance=100-crit_chance
    if num>crit_chance:
        crit_hit=True
        return crit_hit
    return crit_hit

def block(block_chance,num,dodge_chance,attack_after_dodge):
    block=False
    starting_num=attack_after_dodge+dodge_chance
    ending_num=starting_num+block_chance+1
    if starting_num<num and num<ending_num:
        block=True
        return block
    return block

def dodge(dodge_chance,num,attack_after_dodge):
    dodge=False
    starting_num=attack_after_dodge
    ending_num=starting_num+dodge_chance+1
    if starting_num<num and num<ending_num:
        dodge=True
        return dodge
    return dodge

#when implementing the attack after dodge need to add additional code in the attack function 
# to let the user choose an attack


def dodge_attack(attack_after_dodge,num):
    attack=False
    if num<attack_after_dodge+1:
        attack=True
        return attack
    return attack

    

def attack(fight_is_over,your_health,ugly_green_dude_health,crit_chance,block_chance,dodge_chance,attack_after_dodge,crit_damage):
    attacks={'slash':5,'stab':15,'punch':1,'kick':2}
    list_of_attacks=attacks.keys()
    while fight_is_over==False:
        ugly_green_dude_attack=random.randrange(15)
        player_attack=input(f'choose attack option: {attacks}')
        num=random.randrange(100)
        num2=random.randrange(100)
        for item in list_of_attacks:
            if item==player_attack:
                if crit(crit_chance,num)==True:
                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]-crit_damage
                    print('crit')
                elif norm_attack(num,crit_chance,block_chance,dodge_chance,attack_after_dodge)==True:
                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                elif block(block_chance,num,dodge_chance,attack_after_dodge)==True:
                    print('blocked')
                elif num<11:
                    your_health=your_health-ugly_green_dude_attack
                    print('missed and took a hit')
                print(f'ugly health:{ugly_green_dude_health}')                
                if num2>80:
                    your_health=your_health-ugly_green_dude_attack-10
                    print('took a crit')
                elif 30<num2 and num2<81:
                    your_health=your_health-ugly_green_dude_attack
                elif 10<num2 and num2<31:
                    print('got blocked')
                elif dodge(dodge_chance,num,attack_after_dodge)==True:
                    ran_num=random.randrange(100)
                    print('you dodged attack!')
                    if ran_num<26:
                        print('you have a chance to hit back!')
                        player_attack=input(f'choose attack option: {attacks}')
                        rand=random.randrange(100)
                        for item in list_of_attacks:
                            if item ==player_attack:
                                if rand <51:
                                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                print(f'my health: {your_health}')          
                # ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                if your_health<1:
                    print("I saw it coming but I was helpless to stop it. And so I watched on in horror as the creature's claws tore into my chest, \nspilling the last of my life blood out onto the cold unforgiving floor. \nAnd thus my story ends, for I do not wish to speak of the horror that I have become.")
                    fight_is_over=True
                elif ugly_green_dude_health<1:
                    your_name=input('What is your name? ')
                    print(f"At last there it was! An opening in uglie's gaurd. Without any hesitaion I plunged that dagger into it's throat, \nand watched on as life left it's eyes. After the thrill of the fight left me, \nI stood there for who knows how long, looking down upon the pool of blood that had gathered at my feet, \nwith only one thing in my mind; a thought that still haunts me to this day, \n'What have I become; what will I become!'. For I had enjoyed it.\nI am {your_name} and this is my Tale of the Dark Days.\nAm I Infamous or Legendary maybe both or just another casulty, who knows?\n but come back to the tale I digress. ")
                    fight_is_over=True

# def actual_attack(your_health,ugly_green_dude_health):
#     num=range(100)
#     if num >80:


run_Game()





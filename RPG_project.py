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

def run_Game():
    ugly_green_dude_health=40
    your_health=25
    fight_is_over=False
    story()
    attack(fight_is_over,your_health,ugly_green_dude_health)
    
def story():
    print("It was a dark day that saw Our Great kingdom brought to it's knees. Nature itself was revolting, creatures out of nightmares began to appear upon our sacred land. I remember that day well, though thoughts of our great kingdom's demise never once crossed my mind. For me The Fall all began one early summer morning,the sun was just cresting the nearby hill's when I woke to find a dagger attached to an ugly green arm, desending down upon me. (I must say this, impending death does wonders to get you out of bed in the morning). I quickly twisted the dagger out of the ugly arm's grip, and the fight of my life began... ")

def attack(fight_is_over,your_health,ugly_green_dude_health):
    attacks={'slash':5,'stab':15,'punch':1,'kick':2}
    list_of_attacks=attacks.keys()
    while fight_is_over==False:
        ugly_green_dude_attack=random.randrange(15)
        player_attack=input(f'choose attack option: {attacks}')
        num=random.randrange(100)
        num2=random.randrange(100)
        for item in list_of_attacks:
            if item==player_attack:
                if num>80:
                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]-10
                    print('crit')
                elif 30<num and num<81:
                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                elif 10<num and num<31:
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
                elif num2<11:
                    ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                    print('it missed and you got in a hit')
                print(f'my health: {your_health}')          
                # ugly_green_dude_health=ugly_green_dude_health-attacks[item]
                if your_health<1:
                    print("I saw it coming but I was helpless to stop it. And so I watched on in horror as the creature's claws tore into my chest, spilling the last of my life blood out onto the cold unforgiving floor. And thus my story ends, for I do not wish to speak of the horror that I have become.")
                    fight_is_over=True
                elif ugly_green_dude_health<1:
                    print("At last there it was! An opening in uglie's gaurd. Without any hesitaion I plunged that dagger into it's throat, and watched on as life left it's eyes. After the thrill of the fight left me, I stood there for who knows how long, looking down upon the pool of blood that had gathered at my feet, with only one thing in my mind; a thought that still haunts me to this day, 'What have I become'. For I had enjoyed it. ")
                    fight_is_over=True

# def actual_attack(your_health,ugly_green_dude_health):
#     num=range(100)
#     if num >80:


run_Game()





import random
from fighter_classes import Warrior
from player import Player
#next step is to replace the random ai with the ai worrior build created in the class
class Game:
    def __init__(self):
        self.player=Player()
        self.warrior=Warrior()
    def run_Game(self):
        self.story()
        self.attack()
        
    def story(self):
        print("It was a dark day that saw Our Great kingdom brought to it's knees. Nature itself was revolting, \ncreatures out of nightmares began to appear upon our sacred land. \nI remember that day well, though thoughts of our great kingdom's demise never once crossed my mind. \nFor me The Fall all began one early summer morning, the sun was just cresting the nearby hills \nwhen I woke to find a dagger attached to an ugly green arm, desending down upon me. \n(I must say this, impending death does wonders to get you out of bed in the morning). \nI quickly twisted the dagger out of the ugly arm's grip, and the fight of my life began... ")

    # def norm_attack(num,crit_chance,block_chance,dodge_chance,attack_after_dodge):
    #     norm=False
    #     starting_num=attack_after_dodge+dodge_chance+block_chance
    #     ending_num=101-crit_chance
    #     if starting_num<num and num<ending_num:
    #         norm=True
    #         return norm
    #     return norm

    # def crit(crit_chance,num):
    #     crit_hit=False
    #     crit_chance=100-crit_chance
    #     if num>crit_chance:
    #         crit_hit=True
    #         return crit_hit
    #     return crit_hit

    # def block(block_chance,num,dodge_chance,attack_after_dodge):
    #     block=False
    #     starting_num=attack_after_dodge+dodge_chance
    #     ending_num=starting_num+block_chance+1
    #     if starting_num<num and num<ending_num:
    #         block=True
    #         return block
    #     return block

    # def dodge(dodge_chance,num,attack_after_dodge):
    #     dodge=False
    #     starting_num=attack_after_dodge
    #     ending_num=starting_num+dodge_chance+1
    #     if starting_num<num and num<ending_num:
    #         dodge=True
    #         return dodge
    #     return dodge

    #when implementing the attack after dodge need to add additional code in the attack function 
    # to let the user choose an attack


    # def dodge_attack(attack_after_dodge,num):
    #     attack=False
    #     if num<attack_after_dodge+1:
    #         attack=True
    #         return attack
    #     return attack

        

    def attack(self):
        fight_is_over=False
        attacks={'slash':5,'stab':15,'punch':1,'kick':2}
        list_of_attacks=attacks.keys()
        warrior_health=self.warrior.health
        while fight_is_over==False:
            warrior=self.warrior.normal_attack
            player_attack=input(f'choose attack option: {attacks}')
            num=random.randrange(100)
            num2=random.randrange(100)
            for item in list_of_attacks:
                if item==player_attack:
                    if self.player.crit(num)==True:
                        warrior_health=warrior_health-attacks[item]-self.player.crit_damage
                        print('crit')
                    elif self.player.attack(num)==True:
                        warrior_health=warrior_health-attacks[item]
                    elif self.player.block(num)==True:
                        print('blocked')
                    elif self.player.attack_dodge(num)==True:
                        warrior_health=warrior_health-attacks[item]
                        print('dodged and returned attack!')
                    print(f'ugly health:{warrior_health}')                
                    if self.warrior.crit(num2)==True:
                        self.player.health=self.player.health-warrior-self.warrior.crit_damage
                        print('took a crit')
                    elif self.warrior.attack(num2)==True:
                        self.player.health=self.player.health-warrior
                    elif self.warrior.block(num2)==True:
                        print('got blocked')
                    elif self.warrior.attack_dodge(num2)==True:
                        self.player.health=self.player.health-warrior
                        print('you missed and took a hit')
                    print(f'my health: {self.player.health}')          
                    
                    if self.player.health<1:
                        print("I saw it coming but I was helpless to stop it. And so I watched on in horror as the creature's claws tore into my chest, \nspilling the last of my life blood out onto the cold unforgiving floor. \nAnd thus my story ends, for I do not wish to speak of the horror that I have become.")
                        fight_is_over=True
                    elif warrior_health<1:
                        self.player.name=input('What is your name? ')
                        print(f"At last there it was! An opening in uglie's gaurd. Without any hesitaion I plunged that dagger into it's throat, \nand watched on as life left it's eyes. After the thrill of the fight left me, \nI stood there for who knows how long, looking down upon the pool of blood that had gathered at my feet, \nwith only one thing in my mind; a thought that still haunts me to this day, \n'What have I become; what will I become!'. For I had enjoyed it.\nI am {self.player.name} and this is my Tale of the Dark Days.\nAm I Infamous or Legendary maybe both or just another casulty, who knows?\n but come back to the tale I digress. ")
                        fight_is_over=True

    # def actual_attack(your_health,ugly_green_dude_health):
    #     num=range(100)
    #     if num >80:





